### Detailed Notes: Data Engineering Zoomcamp - Automating Data Pipelines with Docker and PostgreSQL

---

### **1. Introduction**
The video focuses on automating data ingestion by:
- Converting a Jupyter notebook into a Python script.
- Using Docker to encapsulate and run the pipeline.
- Ingesting NYC Taxi data into PostgreSQL.

---

### **2. Convert Jupyter Notebook to a Python Script**

**Command:**
```bash
jupyter nbconvert --to script upload_data.ipynb
```

- Converts the Jupyter notebook into a Python script (`upload_data.py`).
- Clean the script by:
  - Moving all imports to the top.
  - Removing unnecessary lines like `%time` magic and inline prints.

**Example Code:**
```python
import pandas as pd
from sqlalchemy import create_engine

def ingest_data():
    engine = create_engine('postgresql://user:password@host:port/dbname')
    df = pd.read_csv("data.csv")
    df.to_sql('table_name', engine, if_exists='replace')
```

---

### **3. Add Command-Line Arguments with `argparse`**

**Code:**
```python
import argparse

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    csv_url = params.url

    # Download CSV file
    os.system(f"wget {csv_url} -O data.csv")

    # Load data to PostgreSQL
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df = pd.read_csv('data.csv')
    df.to_sql(name=table_name, con=engine, if_exists='replace')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data to PostgreSQL')
    parser.add_argument('--user', help='username for PostgreSQL')
    parser.add_argument('--password', help='password for PostgreSQL')
    parser.add_argument('--host', help='host for PostgreSQL')
    parser.add_argument('--port', help='port for PostgreSQL', type=int)
    parser.add_argument('--db', help='database name')
    parser.add_argument('--table_name', help='target table name')
    parser.add_argument('--url', help='URL of the CSV file')
    args = parser.parse_args()

    main(args)
```

**Run the Script:**
```bash
python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="https://path/to/csv/file.csv"
```

---

### **4. Dockerizing the Pipeline**

**Create `Dockerfile`:**
```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY ingest_data.py ingest_data.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "ingest_data.py"]
```

**Install Required Packages (`requirements.txt`):**
```text
pandas
sqlalchemy
psycopg2-binary
```

**Build the Docker Image:**
```bash
docker build -t data_ingest:v1 .
```

**Run the Docker Container:**
```bash
docker run -it \
    --network=pg-network \
    data_ingest:v1 \
    --user root \
    --password root \
    --host pg-database \
    --port 5432 \
    --db ny_taxi \
    --table_name yellow_taxi_trips \
    --url "https://path/to/csv/file.csv"
```

---

### **5. Testing with PostgreSQL**

- Drop the existing table in PGAdmin or PostgreSQL:
```sql
DROP TABLE yellow_taxi_trips;
```

- Verify the new table is created:
```sql
SELECT * FROM yellow_taxi_trips LIMIT 10;
```

---

### **6. Using a Local HTTP Server for Testing**

If file downloads are slow, host files locally using Python’s built-in HTTP server.

**Command:**
```bash
python -m http.server 8000
```

- Access files at: `http://<your-ip>:8000/`

**Find Your Local IP Address:**
```bash
ifconfig # For Linux/Mac
ipconfig # For Windows
```

Update the script with the new URL:
```bash
--url "http://<your-ip>:8000/file.csv"
```

---

### **7. Running the Script in a Docker Network**

**Create a Docker Network:**
```bash
docker network create pg-network
```

**Run PostgreSQL Container:**
```bash
docker run -d \
    --network=pg-network \
    --name pg-database \
    -e POSTGRES_USER=root \
    -e POSTGRES_PASSWORD=root \
    -e POSTGRES_DB=ny_taxi \
    postgres:13
```

**Run Data Ingest Container:**
```bash
docker run -it \
    --network=pg-network \
    data_ingest:v1 \
    --user root \
    --password root \
    --host pg-database \
    --port 5432 \
    --db ny_taxi \
    --table_name yellow_taxi_trips \
    --url "http://<your-ip>:8000/file.csv"
```

---

### **8. Common Issues and Solutions**
- **Problem:** `localhost` does not work inside Docker.
  - **Solution:** Use the container name (e.g., `pg-database`) as the host.
- **Problem:** Passing passwords via the command line is insecure.
  - **Solution:** Use environment variables or secure vaults for sensitive data.

---

### **9. Next Steps**
- Explore `Docker Compose` to manage multi-container applications.
- Replace manual processes with Airflow for orchestration and scheduling.

---

These notes provide all key commands and code snippets discussed in the video. Let me know if you need clarification on any part!