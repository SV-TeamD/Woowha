# Cartoonizer using GAN

### Reference
**[CartoonGAN-Test-Pytorch-Torch](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch)**

> Pytorch and Torch testing code of [CartoonGAN](http://openaccess.thecvf.com/content_cvpr_2018/CameraReady/2205.pdf) `[Chen et al., CVPR18]`. With the released pretrained [models](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/Yongjin.htm) by the authors, I made these simple scripts for a quick test.

<p>
    <img src='https://user-images.githubusercontent.com/25628507/105346214-a0bb2a80-5c28-11eb-974a-b4bf4bd4ad8e.png' width=300 />
    <img src='https://user-images.githubusercontent.com/25628507/105346204-9c8f0d00-5c28-11eb-809c-48c68dcd41a1.png' width=300 />
</p>

## Architecture

![architecture](https://user-images.githubusercontent.com/57690870/106702452-ba4a7200-662b-11eb-97e4-de0ca46d5299.PNG)

## Getting started
### Docker
```
$ docker-compose build
$ docker-compose up
```
If you want to run services individually, you should check environment variables. (**`app.env`**, **`Dockerfile`**)

### Client
```
$ cd client
$ npm install
$ npm start
```
### API Server
```
$ cd webserver
$ pip install -r requirements.txt
```

### Model Server
```shell
$ cd modelserver
$ pip install -r requirements.txt
$ ./load-models.sh # you should download pre-trained models
```
you can **scale up** Model Server using below command
```
$ docker-compose up --scale modelserver=3
```

## Monitoring

### Prometheus
http://localhost:9090/targets
![image](https://user-images.githubusercontent.com/25628507/106257240-9cfa5a00-625f-11eb-830c-b251602dcb73.png)

### Grafana
http://localhost:3001  
Login with id: admin pw: 1234

#### Docker container dashboard
![image](https://user-images.githubusercontent.com/25628507/106257481-f2366b80-625f-11eb-8959-8441805185c9.png)

#### Redis dashboard
![image](https://user-images.githubusercontent.com/25628507/106257655-31fd5300-6260-11eb-823d-2649cb38203a.png)


## Development
```shell
$ ./local-set-install.sh
```

## Author
- 2021 Silicon Valley Online Internship - Team D
- [Jivvon](https://github.com/Jivvon),
[ByeongdoChoi](https://github.com/ByeongdoChoi),
[genius-jo](https://github.com/genius-jo),
[iSuddenly](https://github.com/iSuddenly)
