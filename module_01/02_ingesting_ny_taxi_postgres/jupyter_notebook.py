import pandas as pd

print(pd.__version__)


df = pd.read_csv("yellow_tripdata_2021-01.csv", nrows=1000)

# Parse the dates
df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])


schema = pd.io.sql.get_schema(df, name='taxi')
print(schema)

from sqlalchemy import create_engine


# Adjust the connection string for both Windows and Ubuntu
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


engine.connect()

schema = pd.io.sql.get_schema(df, 'taxi', con=engine)
print(schema)


df_iter = pd.read_csv("yellow_tripdata_2021-01.csv", iterator=True, chunksize=1000)


df = next(df_iter)


len(df)



df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)


df.to_sql('yellow_taxi_data', engine, if_exists='replace', index=False)


from time import time
while True:
    try:
        t_start = time()
        df = next(df_iter)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql('yellow_taxi_data', engine, if_exists='append', index=False)
        t_end = time()
        print(f"Chunk loaded in {t_end - t_start} seconds")
    except StopIteration:
        break
    
print("All data loaded")