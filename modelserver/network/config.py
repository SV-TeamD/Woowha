import torch


class Config:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # dataloader.py
    batch_size = 8
    num_workers = 4
    photo_image_dir = "dataset/photo/"
    cartoon_image_dir = "dataset/cartoon/"
    edge_smoothed_image_dir = "dataset/cartoon_edge_smoothed/"
    test_photo_image_dir = "dataset/test/"

    # train.py
    adam_beta1 = 0.5  # dcgan
    lr = 0.0002
    num_epochs = 100
    initialization_epochs = 10
    content_loss_weight = 10
    print_every = 100
