# Cartoonizer using GAN

### Reference
**[CartoonGAN-Test-Pytorch-Torch](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch)**

> Pytorch and Torch testing code of [CartoonGAN](http://openaccess.thecvf.com/content_cvpr_2018/CameraReady/2205.pdf) `[Chen et al., CVPR18]`. With the released pretrained [models](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/Yongjin.htm) by the authors, I made these simple scripts for a quick test.

<p>
    <img src='https://user-images.githubusercontent.com/25628507/105346214-a0bb2a80-5c28-11eb-974a-b4bf4bd4ad8e.png' width=300 />
    <img src='https://user-images.githubusercontent.com/25628507/105346204-9c8f0d00-5c28-11eb-809c-48c68dcd41a1.png' width=300 />
</p>

## Architecture

![3주차](https://user-images.githubusercontent.com/25628507/105339511-166ec880-5c20-11eb-80c6-69b4e058b047.png)
~~Not the final version yet~~

## Getting started
### Docker
```
docker-compose up --build
```
If you want to run services individually, you should check environment variables. (**`app.env`**, **`Dockerfile`**)

### Client
```
cd client
npm install
npm start
```
### API Server
```
cd webserver
pip install -r requirements.txt
```

### Model Server
```shell
cd modelserver
pip install -r requirements.txt
./load-models.sh # you should download pre-trained models
```
you can **scale up** Model Server using below command
```
docker-compose up --scale modelserver=3
```

## Development
```shell
./local-set-install.sh
```

## Author
- 2021 Silicon Valley Online Internship - Team D
- [Jivvon](https://github.com/Jivvon),
[ByeongdoChoi](https://github.com/ByeongdoChoi),
[genius-jo](https://github.com/genius-jo),
[iSuddenly](https://github.com/iSuddenly)
