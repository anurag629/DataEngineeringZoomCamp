### Running PostgreSQL in Docker

**Windows:**
```bash
docker run -d -t ^
-e POSTGRES_USER=root ^
-e POSTGRES_PASSWORD=root ^
-e POSTGRES_DB=ny_taxi ^
-v "C:\path\to\ny_taxi_postgres_data:/var/lib/postgresql/data" ^
-p 5432:5432 ^
postgres:13
```

**Ubuntu:**
```bash
docker run -it \
-e POSTGRES_USER=root \
-e POSTGRES_PASSWORD=root \
-e POSTGRES_DB=ny_taxi \
-v "$(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data" \
-p 5432:5432 \
postgres:13
```

### Installing PGCLI

**Windows:**
```bash
pip install pgcli
```

**Ubuntu:**
```bash
pip install pgcli
```

### Connecting to PostgreSQL with PGCLI

**Windows and Ubuntu:**
```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

### Installing Jupyter Notebook

**Windows:**
```bash
pip install jupyter
```

**Ubuntu:**
```bash
pip install jupyter
```

### Reading CSV file with Pandas

>> Dataset Link: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

```python
import pandas as pd

# Adjust the path accordingly for both Windows and Ubuntu
df = pd.read_csv('C:\\path\\to\\file.csv') # Windows
# df = pd.read_csv('/home/username/path/to/file.csv') # Ubuntu
```

### Generating SQL Schema

Using Pandas(Dummy Schema as it might not work with postgres):

```python
schema = pd.io.sql.get_schema(df, name='taxi')
print(schema)
```

Using SQLAlchemy Schema(Recommended as it works with PostgreSQL):

```python
from sqlalchemy import create_engine

# Adjust the connection string for both Windows and Ubuntu
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
```

Now, we can use the Pandas `pd.io.sql.get_schema` method to generate the schema for the DataFrame using the SQLAlchemy engine:

```python
schema = pd.io.sql.get_schema(df, 'taxi', con=engine)
print(schema)
```

### Creating Table in PostgreSQL

```python
df.to_sql('yellow_taxi_data', engine, if_exists='replace', index=False)
```

### Inserting Data in Chunks

```python
for chunk in pd.read_csv('C:\\path\\to\\file.csv', chunksize=100000): # Windows
chunk.to_sql('yellow_taxi_data', engine, if_exists='append', index=False)

# For Ubuntu
# for chunk in pd.read_csv('/home/username/path/to/file.csv', chunksize=100000):
# chunk.to_sql('yellow_taxi_data', engine, if_exists='append', index=False)
```

Make sure to replace the paths with the actual ones where your files are located. If you have any further questions, feel free to ask!