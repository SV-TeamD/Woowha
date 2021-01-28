import os

import torch
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
from PIL import Image

from network.transformer import Transformer

ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS").split(",")
STYLES = os.getenv("STYLES").split(",")


class Runner:
    @classmethod
    def __init__(
        cls,
        model_dir="./pretrained_model",
        input_dir="/data/image_input",
        output_dir="/data/image_output",
    ):
        filepath_this = os.path.dirname(os.path.abspath(__file__))
        cls.input_dir = os.path.join(filepath_this, input_dir)
        cls.output_dir = os.path.join(filepath_this, output_dir)
        cls.model_dir = os.path.join(filepath_this, model_dir)
        cls.prev_style = None

    @classmethod
    def run(cls, imagefile_name, style, load_size=450):
        input_image_path = os.path.join(cls.input_dir, imagefile_name)
        try:
            cls.is_file(input_image_path)
            cls.validate_style(style)
            cls.validate_ext(imagefile_name)
            cls.load_weights(style, cls.model_dir)
            input_image = cls.preprocess_image(input_image_path, load_size)
            output_image = cls.output_image(input_image)

            cls.exist_dir(cls.output_dir)
            cls.save_image(output_image, imagefile_name, style)
            print("create {} style image : {}".format(style, imagefile_name))
        except FileExistsError as file_exist_error:
            print(file_exist_error)
        except RuntimeError as e:
            print(e)

    @classmethod
    def exist_dir(cls, dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    @classmethod
    def is_file(cls, input_image_path):
        if not os.path.isfile(input_image_path):
            raise Exception("{}: 파일이 존재하지 않습니다.".format(input_image_path))

    @classmethod
    def load_weights(cls, style, model_dir="./pretrained_model"):
        if cls.prev_style and cls.prev_style == style:
            return
        cls.prev_style = style
        model_path = os.path.join(model_dir, style)
        try:
            cls.model = Transformer()
            cls.model.load_state_dict(torch.load(model_path))
            cls.model.eval()
            cls.model.float()
        except FileNotFoundError as file_not_founr_err:
            raise FileNotFoundError(
                "{} 모델을 불러오는데 오류가 발생하였습니다.".format(style)
            ) from file_not_founr_err
        except FileExistsError as file_exists_err:
            raise FileExistsError("{} 모델을 불러오는데 오류가 발생하였습니다.".format(style)) from file_exists_err
        except Exception as e:
            raise Exception("{} 예외가 발생하였습니다.".format(e)) from e

    @classmethod
    def validate_ext(cls, imagefile_name):
        ext = imagefile_name.split(".")[1]
        if ext not in ALLOWED_EXTENSIONS:
            raise Exception("지원하지 않는 확장자입니다.")

    @classmethod
    def validate_style(cls, style: str):
        if style not in STYLES:
            raise Exception("지원하지 않는 모델입니다.")

    @classmethod
    def preprocess_image(cls, input_image_path, load_size):
        # load image
        input_image = Image.open(input_image_path).convert("RGB")
        # resize image, keep aspect ratio
        _h = input_image.size[0]
        _w = input_image.size[1]
        ratio = _h * 1.0 / _w
        if ratio > 1:
            _h = load_size
            _w = int(_h * 1.0 / ratio)
        else:
            _w = load_size
            _h = int(_w * ratio)
        input_image = input_image.resize((_h, _w), Image.BICUBIC)
        input_image = np.asarray(input_image)
        # RGB -> BGR
        input_image = input_image[:, :, [2, 1, 0]]
        input_image = transforms.ToTensor()(input_image).unsqueeze(0)
        # preprocess, (-1, 1)
        input_image = -1 + 2 * input_image
        input_image = torch.Tensor(input_image)
        return input_image

    @classmethod
    def output_image(cls, input_image):
        # forward
        output_image = cls.model(input_image)
        output_image = output_image[0]
        # BGR -> RGB
        output_image = output_image[[2, 1, 0], :, :]
        # deprocess, (0, 1)
        output_image = output_image.data.cpu().float() * 0.5 + 0.5
        return output_image

    @classmethod
    def output_image_filename(cls, imagefile_name: str, style: str):
        imagefile_name_parts = imagefile_name.split(".")
        imagefile_name_parts[0] += "_{}".format(style)
        return ".".join(imagefile_name_parts)

    @classmethod
    def save_image(cls, output_image, imagefile_name: str, style: str):
        # save
        _output_image_filename = cls.output_image_filename(imagefile_name, style)
        output_image_path = os.path.join(cls.output_dir, _output_image_filename)
        vutils.save_image(output_image, output_image_path)
