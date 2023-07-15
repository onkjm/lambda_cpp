# lambda_cpp
create and run c/c++ apps on aws lambda example

## create c/c++ apps

For example, [vs/testapp](vs/testapp) is a kind of "Hello world" app written in c/c++, using cmake project of Visual Studio.

## compile it on Ubuntu on Docker

create docker container and build c/c++ on it.

```
cd vs
docker build -t u-vs -f Dockerfile.ubuntu .
docker run -p 10022:22 -i -t u-vs /bin/bash
```

the user "master" with password "pass" is automatically added.

in docker container,run ssh.
```
service ssh start
```

then, launch Visual Studio, add localhost as a remote.

ssh setting is like this.
```
host: localhost
port: 10022
user: master
pass: pass
```

cmake project is rsync to Ubuntu on docker container, and built.

### reference

(Build C++ Applications in a Linux Docker Container with Visual Studio)[https://devblogs.microsoft.com/cppblog/build-c-applications-in-a-linux-docker-container-with-visual-studio/]

compiled exec file can be copied to the host computer.
```
docker ps -a
docker cp [ID]:[docker path] [host path]
# example: docker cp d35dfb9a9b76:/home/master/.vs/cmaketest/out/build/linux-release/main/main C:\Users\winuser\Downloads\
```

## create lambda container

move to [lambda](lambda) folder, put exec file in [lambda](lambda) folder, and create docker container.

```
cd lambda
docker build -t testapp -f Dockerfile.ubuntu.lambda .

```

push it to aws ecr.

### reference

[lambda_cvxpy](https://github.com/onkjm/lambda_cvxpy)

## create aws lambda function

create aws lambda function on aws, and test run.

you can see the app running on aws lambda.












