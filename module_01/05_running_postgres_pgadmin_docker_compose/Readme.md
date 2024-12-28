In the previous lesson, we learned how to run a PostgreSQL container using Docker. In this lesson, we will learn how to run a PostgreSQL container and a pgAdmin container using Docker Compose.

## Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

## Running PostgreSQL and pgAdmin with Docker Compose

To run PostgreSQL and pgAdmin with Docker Compose, we need to create a `docker-compose.yml` file. This file will define the services we want to run. In this case, we want to run a PostgreSQL service and a pgAdmin service.

Here is an example of a `docker-compose.yml` file that defines a PostgreSQL service and a pgAdmin service:

```yaml
version: '3'

services:
  pgdatabase:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=postgres
    volumes:
      - "./ny_taxi_data:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=root@gmail.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"
```
    
Now, let's run the following command to start the services defined in the `docker-compose.yml` file:

```bash
docker-compose up
```

Or, if you want to run the services in the background, you can run the following command:

```bash
docker-compose up -d
```

Here, `-d` flag is used to run the services in detached mode.

Now, you can access pgAdmin by going to `http://localhost:8080` in your web browser. You can log in using the email and password you specified in the `docker-compose.yml` file.

And, at last close the services using the following command:

```bash
docker-compose down
```