import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect("dbname=test user=postgres")

# Create a cursor
cur = conn.cursor()

# Execute a parameterized query
cur.execute("INSERT INTO your_table (column1, column2, ...) VALUES (%s, %s, ...)", (value1, value2, ...))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()