# Woowha
2021 Silicon Valley Online Internship Team D

정지원, 조광식, 최병도, 김하윤

# How to use a docker and composer
## Docker Prerequisites:
- Windows
https://docs.docker.com/docker-for-windows/install/
- Mac
https://docs.docker.com/docker-for-mac/install/


### 1. git clone
```
git clone git@github.com:shpark76/docker-demo.git
```

### 2. docker compose build and up 
```
$ docker-compose build
$ docker-compose up --build
```

# Let’s run the API using docker
## Let’s build the docker image
```
$ docker-compose build
```

## Docker compose up with all associated docker compose services
```
$ docker-compose up
```
#### Note:
If you prefer to use a daemon mode, Let’s run the above command in the background:
```
$ docker-compose up -d
```

### 1. webserver (Flask)
```
http://localhost:5000
```

### 2. client (React)
```
http://localhost:3000
```  


#### If you want to build/run a specific application
> ```
> docker-compose build <custom service>
> docker-compose run <custom service>
> 
> i.e. 
> docker-compose build webserver
> docker-compose run client
> ```

---
## How to use Redis and Postgres
### 1. Redis
https://redis.io/topics/rediscli
```
$ redis-cli -h localhost -p 6379
localhost:6379> exit
$ redis-cli ping
PONG
```

### 2. Postgres
https://www.pgadmin.org/download/
```
psql --host=localhost --username=user --password --dbname=app
Password for user postgres: 1234
```
---

## Development
```shell
./local-set-install.sh
```