### What I learned

* Running a container with `docker run`
* Creating a Dockerfile
* Building a Dockerfile with `docker build`
* Running a container with `docker run`
* Running a Python script in a Docker container

## Basic commands to learn

1. For creating an image from a Dockerfile:

    ```bash
    docker build -t <image_name:tag> <path_to_Dockerfile>
    ```

    Example: `docker build -t test:pandas .`
    
    - `test` is the image name.
    - `pandas` is the tag name.
    - `-t` is for tagging.
    - `.` specifies the current directory.

2. For running a container from an image:

    ```bash
    docker run -it <image_name:tag>
    ```

    Example: `docker run -it test:pandas`
    
    - `test:pandas` is the image name and tag.

3. Running a container with a command line argument:

    ```bash
    docker run -it <image_name:tag> <command>
    ```

    Example: `docker run -it test:pandas python3 test.py`
    
    - `python3 test.py` is the command to run the Python script in the container named `test:pandas`.

4. Some useful commands:

    ```bash
    docker ps -a # List all containers
    docker images # List all images
    docker rm <container_id> # Remove a container
    docker rmi <image_id> # Remove an image
    ```

5. For running a container in detached mode:

    ```bash
    docker run -d <image_name:tag>
    ```

Explanation:
- `-t` is used for tagging an image with a name and an optional tag.
- `-it` is used for interactive mode, allowing you to interact with the container's terminal.
- `<image_name:tag>` specifies the image and its tag.
- `<path_to_Dockerfile>` is the path to the directory containing the Dockerfile.
- `docker ps -a` lists all containers, including stopped ones.
- `docker images` lists all images on your system.
- `docker rm` removes a container.
- `docker rmi` removes an image.
- `-d` runs the container in detached mode, allowing it to run in the background.
