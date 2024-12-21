### Commands to Run pgAdmin in Docker:

1. **Pull and Run pgAdmin Docker Container:**

```bash
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4
```

2. **Create a Docker Network:**

```bash
docker network create pg_network
```

3. **Run PostgreSQL Container in the Created Network:**

```bash
docker run -it \
    -e POSTGRES_USER=root \
    -e POSTGRES_PASSWORD=root \
    -e POSTGRES_DB=ny_taxi \
    -v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data" \
    -p 5432:5432 \
    --network pg_network \
    --name pg_database \
    postgres:13
```

4. **Run pgAdmin Container in the Same Network:**

```bash
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@gmail.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network pg_network \
    dpage/pgadmin4
```

### Steps in pgAdmin:

1. **Access pgAdmin:**
- Navigate to `http://localhost:8080` in your web browser.
- Use the email and password you specified (`admin@admin.com` and `root`).

2. **Create a New Server in pgAdmin:**
- Right-click on "Servers" and select "Create" > "Server..."
- Name the server (e.g., "docker_localhost").
- In the connection tab, set:
    - **Host name/address:** `pg_database` (this is the service name of the PostgreSQL container).
    - **Username:** `root`.
    - **Password:** `root`.

These notes outline how to set up pgAdmin and connect it to a PostgreSQL database using Docker. If you have any further questions or need clarification on any part, feel free to ask!