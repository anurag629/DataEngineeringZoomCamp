Here are well-organized notes and explanations for all SQL commands and code snippets used in the video:

---

### **1. Loading Data**
**Command**:
```sql
SELECT * FROM zones;
```
- Displays all records in the `zones` table.
- Used to verify the data (zone names, boroughs, etc.) are correctly loaded.

---

### **2. Basic SELECT Query**
**Command**:
```sql
SELECT * FROM yellow_taxi_trips LIMIT 100;
```
- Retrieves the first 100 rows from the `yellow_taxi_trips` table.
- Useful for a quick look at the data structure and sample values.

---

### **3. Joining Tables**
#### A. **Using a Comma (Deprecated Method)**
**Command**:
```sql
SELECT * 
FROM yellow_taxi_trips t, zones lpu, zones ldo
WHERE t."PUlocationID" = lpu."LocationID" 
  AND t."DOlocationID" = ldo."LocationID";
```
- **Explanation**:
  - Joins `yellow_taxi_trips` with `zones` twice for pickup (`lpu`) and drop-off (`ldo`) locations.
  - Displays enriched data with zones replacing numeric IDs.

#### B. **Using Explicit JOIN**
**Command**:
```sql
SELECT t.pickup_datetime, t.dropoff_datetime, t.total_amount,
       lpu."Zone" AS pickup_zone, lpu."Borough" AS pickup_borough,
       ldo."Zone" AS dropoff_zone, ldo."Borough" AS dropoff_borough
FROM yellow_taxi_trips t
JOIN zones lpu ON t."PUlocationID" = lpu."LocationID"
JOIN zones ldo ON t."DOlocationID" = ldo."LocationID";
```
- **Explanation**:
  - Performs an **INNER JOIN**.
  - Selects only relevant fields like pickup/drop-off times, amounts, and zone names.

#### C. **LEFT JOIN**
**Command**:
```sql
SELECT t.pickup_datetime, t.dropoff_datetime, t.total_amount,
       COALESCE(lpu."Zone", 'Unknown') AS pickup_zone,
       COALESCE(ldo."Zone", 'Unknown') AS dropoff_zone
FROM yellow_taxi_trips t
LEFT JOIN zones lpu ON t."PUlocationID" = lpu."LocationID"
LEFT JOIN zones ldo ON t."DOlocationID" = ldo."LocationID";
```
- **Explanation**:
  - Ensures all rows from `yellow_taxi_trips` are retained even if there's no matching record in `zones`.
  - Uses `COALESCE` to replace `NULL` values with `'Unknown'`.

---

### **4. Checking Data Consistency**
#### A. **Finding Missing Data**
**Command**:
```sql
SELECT * 
FROM yellow_taxi_trips 
WHERE "PUlocationID" IS NULL OR "DOlocationID" IS NULL;
```
- Identifies records with missing pickup or drop-off location IDs.

#### B. **Checking IDs Not in `zones`**
**Command**:
```sql
SELECT "PUlocationID"
FROM yellow_taxi_trips
WHERE "PUlocationID" NOT IN (SELECT "LocationID" FROM zones);
```
- Checks if there are IDs in `yellow_taxi_trips` that don’t exist in the `zones` table.

---

### **5. Aggregations with GROUP BY**
#### A. **Trips per Day**
**Command**:
```sql
SELECT DATE_TRUNC('day', pickup_datetime) AS day, COUNT(*) AS trip_count
FROM yellow_taxi_trips
GROUP BY day
ORDER BY day ASC;
```
- **Explanation**:
  - Groups data by day using `DATE_TRUNC` to truncate timestamps to just the day.
  - Counts the number of trips per day (`COUNT(*)`).
  - Orders results in ascending order.

#### B. **Top Trip Days**
**Command**:
```sql
SELECT DATE_TRUNC('day', pickup_datetime) AS day, COUNT(*) AS trip_count
FROM yellow_taxi_trips
GROUP BY day
ORDER BY trip_count DESC
LIMIT 1;
```
- Displays the day with the most trips.

---

### **6. Aggregations by Multiple Columns**
**Command**:
```sql
SELECT DATE_TRUNC('day', pickup_datetime) AS day, lpu."Zone" AS pickup_zone, COUNT(*) AS trip_count
FROM yellow_taxi_trips t
JOIN zones lpu ON t."PUlocationID" = lpu."LocationID"
GROUP BY day, pickup_zone
ORDER BY day ASC, pickup_zone ASC;
```
- **Explanation**:
  - Groups data by both day and pickup zone.
  - Counts the number of trips for each zone per day.

---

### **7. Additional Aggregations**
#### A. **Max Fare per Day**
**Command**:
```sql
SELECT DATE_TRUNC('day', pickup_datetime) AS day, MAX(total_amount) AS max_fare
FROM yellow_taxi_trips
GROUP BY day
ORDER BY day ASC;
```
- Finds the highest fare (`MAX`) for each day.

#### B. **Passenger Count Statistics**
**Command**:
```sql
SELECT DATE_TRUNC('day', pickup_datetime) AS day, MAX(passenger_count) AS max_passengers
FROM yellow_taxi_trips
GROUP BY day
ORDER BY max_passengers DESC;
```
- Displays the maximum number of passengers in a trip per day.

---

### **8. Modifying Data**
**Command**:
```sql
DELETE FROM zones
WHERE "LocationID" = 142;
```
- Removes a specific record from the `zones` table.

---

### **SQL Function Highlights**
1. **`DATE_TRUNC`**:
   - Truncates timestamps to a specific granularity (e.g., day, month).
2. **`COALESCE`**:
   - Replaces `NULL` values with a default value.
3. **`GROUP BY`**:
   - Groups rows by one or more columns for aggregations.
4. **`ORDER BY`**:
   - Orders the results based on specified columns in ascending (`ASC`) or descending (`DESC`) order.

---

### **Cheat Sheet of Key SQL Commands**
| **Command**      | **Purpose**                                                      |
|-------------------|------------------------------------------------------------------|
| `SELECT`         | Retrieve data from one or more tables.                          |
| `JOIN`           | Combine rows from two or more tables based on a related column. |
| `LEFT JOIN`      | Retain unmatched rows from the left table in a join.            |
| `GROUP BY`       | Aggregate data by grouping it by specific columns.              |
| `ORDER BY`       | Sort data in ascending or descending order.                     |
| `COALESCE`       | Handle `NULL` values with default replacements.                 |
| `DATE_TRUNC`     | Extract specific parts of timestamps (e.g., day, month).        |

