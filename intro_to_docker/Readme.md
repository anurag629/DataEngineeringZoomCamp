### What I learned

* running a container with docker run
* Creating a Dockerfile
* Building a Dockerfile with docker build
* Running a container with docker run
* running python script in docker container

## Basic commands to learn

1. For creating a image from a Dockerfile

```
docker build -t <image_name> <path_to_Dockerfile>
```

ex: `docker build -t test:pandas .`

> here test is the image name and pandas is the tag name, `-t` is for tagging, `.` is for current directory

2. For running a container from a image

```
docker run -it <image_name>
```

ex: `docker run -it test:pandas`

> here `test:pandas` is the image name and tag name

3. Running a container with a command line argument

```
docker run -it <image_name> <command>
```

ex: `docker run -it test:pandas python3 test.py`

> here `python3 test.py` is the command to run the python script in the container named `test:pandas` which is created from the image `test` with tag `pandas`


4. Some useful commands

```
docker ps -a # for listing all the containers
docker images # for listing all the images
docker rm <container_id> # for removing a container
docker rmi <image_id> # for removing a image
```

5. For running a container in detached mode

```
docker run -d <image_name>
```