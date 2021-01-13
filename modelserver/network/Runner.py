import torch
import os
import sys

import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.utils as vutils

from network.Transformer import Transformer


class Runner:
    def __init__(
        self,
        model_dir="./pretrained_model",
        input_dir="../image_input",
        output_dir="../image_output",
    ):
        filepath_this = os.path.dirname(os.path.abspath(__file__))
        self.input_dir = os.path.join(filepath_this, input_dir)
        self.output_dir = os.path.join(filepath_this, output_dir)
        self.model_dir = os.path.join(filepath_this, model_dir)
        self.prev_style = None

    def run(self, imagefile_name="01.jpg", load_size=450, style="Hayao"):
        input_image_path = os.path.join(self.input_dir, imagefile_name)
        try:
            self.is_file(input_image_path)
            self.load_weights(style, self.model_dir)
            self.validate_ext(imagefile_name)
            input_image = self.preprocess_image(input_image_path, load_size)
            output_image = self.output_image(input_image)
        except Exception as e:
            print("{}: Runner Exception".format(imagefile_name))
            print(e)
            return

        self.check_exist_dir(self.output_dir)
        self.save_image(output_image, input_image_path, style, self.output_dir)
        print("create {} style image : {}".format(style, imagefile_name))

    def check_exist_dir(self, dir_path):
        try:
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
        except:
            os.mkdir(dir_path)

    def is_file(self, input_image_path):
        if not os.path.isfile(input_image_path):
            raise Exception("{}: 파일이 존재하지 않습니다.".format(input_image_path))

    def load_weights(self, style, model_dir="./pretrained_model"):
        if self.prev_style and self.prev_style == style:
            return
        self.prev_style = style
        model_path = os.path.join(model_dir, style + "_net_G_float.pth")
        try:
            self.model = Transformer()
            self.model.load_state_dict(torch.load(model_path))
            self.model.eval()
            self.model.float()
        except:
            raise Exception("{} 모델을 불러오는데 오류가 발생하였습니다.".format(style))

    def validate_ext(self, imagefile_name):
        ext = imagefile_name.split(".")[1]
        valid_ext = ["jpg", "png"]
        if ext not in valid_ext:
            raise Exception("지원하지 않는 확장자입니다.")

    def preprocess_image(self, input_image_path, load_size):
        # load image
        input_image = Image.open(input_image_path).convert("RGB")
        # resize image, keep aspect ratio
        h = input_image.size[0]
        w = input_image.size[1]
        ratio = h * 1.0 / w
        if ratio > 1:
            h = load_size
            w = int(h * 1.0 / ratio)
        else:
            w = load_size
            h = int(w * ratio)
        input_image = input_image.resize((h, w), Image.BICUBIC)
        input_image = np.asarray(input_image)
        # RGB -> BGR
        input_image = input_image[:, :, [2, 1, 0]]
        input_image = transforms.ToTensor()(input_image).unsqueeze(0)
        # preprocess, (-1, 1)
        input_image = -1 + 2 * input_image
        input_image = torch.Tensor(input_image)
        return input_image

    def output_image(self, input_image):
        # forward
        output_image = self.model(input_image)
        output_image = output_image[0]
        # BGR -> RGB
        output_image = output_image[[2, 1, 0], :, :]
        # deprocess, (0, 1)
        output_image = output_image.data.cpu().float() * 0.5 + 0.5
        return output_image

    def save_image(self, output_image, input_image_path, style, output_dir):
        # save
        filename = input_image_path.split("/")[-1].split(".")[0] + "_" + style + ".jpg"
        output_path = os.path.join(output_dir, filename)
        vutils.save_image(output_image, output_path)


if __name__ == "__main__":
    input_img_name = "01.jpg"
    r = Runner()
    r.run(imagefile_name=input_img_name, style="Hayaho")
    r.run(imagefile_name=input_img_name, style="Hayao")
    r.run(imagefile_name=input_img_name, style="Hosoda")
    r.run(imagefile_name=input_img_name, style="Hello")
    r.run(imagefile_name=input_img_name, style="Shinkai")
    print("Done!!")
