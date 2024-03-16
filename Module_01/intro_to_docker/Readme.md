## All commands with explanations

In the video "DE Zoomcamp 1.2.1 - Introduction to Docker," several commands related to Docker and its functionalities are used. Below is a list of these commands along with explanations for each:

1. **`docker run hello-world`**
   - This command runs the `hello-world` Docker image. If the image is not available locally, Docker fetches it from Docker Hub, a cloud-based registry service. The `hello-world` image is a simple application that demonstrates the Docker installation is functioning correctly by outputting a message.

2. **`docker run -it ubuntu bash`**
   - Breakdown of the command:
     - `docker run`: Command to run a Docker container.
     - `-it`: Option that allows you to interact with the container via a terminal. `-i` stands for interactive, and `-t` assigns a pseudo-tty or terminal inside the new container.
     - `ubuntu`: Specifies the Docker image to use. In this case, it's the official Ubuntu image.
     - `bash`: Specifies the command to run inside the new container. Here, it opens the Bash shell inside the Ubuntu container.
   - This command runs a new Ubuntu container and attaches an interactive terminal to it, allowing you to run Bash commands inside the container.

3. **`docker run -it python:3.9 bash`**
   - Similar to the previous command but specifies the `python:3.9` image, which is a Docker image with Python 3.9 installed. This allows you to run Python 3.9 inside the container. The `bash` command at the end opens a Bash shell for interaction.

4. **`pip install pandas`** (used within a Python container)
   - This command uses Python's package manager, pip, to install the pandas library inside the current container. Pandas is a powerful data analysis and manipulation library for Python.

5. **`docker build -t test .`**
   - Breakdown of the command:
     - `docker build`: Command to build a Docker image from a Dockerfile.
     - `-t test`: Specifies the tag name for the newly created image. In this case, the image is tagged as `test`.
     - `.`: Specifies the build context to the current directory. Docker looks for a Dockerfile in this directory to build the image.
   - This command builds a Docker image named `test` using the Dockerfile in the current directory.

6. **`docker run -e POSTGRES_PASSWORD=mysecretpassword -d postgres`**
   - This command is not explicitly mentioned in the video's provided text but is common in Docker tutorials related to PostgreSQL. It illustrates how to run a PostgreSQL container with Docker.
   - Breakdown of the command:
     - `docker run`: Command to run a Docker container.
     - `-e POSTGRES_PASSWORD=mysecretpassword`: Sets an environment variable inside the container (`POSTGRES_PASSWORD`) with a value (`mysecretpassword`). This is used to set the default password for PostgreSQL.
     - `-d`: Runs the container in detached mode, meaning it runs in the background.
     - `postgres`: Specifies the Docker image to use, which is the official PostgreSQL image.

Each of these commands plays a crucial role in demonstrating Docker's capabilities, especially for creating isolated development environments, installing dependencies, and running applications in containers. Docker simplifies the process of managing dependencies and ensures that applications run consistently across different environments.

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
