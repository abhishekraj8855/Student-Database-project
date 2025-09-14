import sqlite3
import pandas as pd

df = pd.read_csv("studentsheet.csv")

#SQLite database connect

conn = sqlite3.connect("students.db")

# 3️CSV data ko SQL table me save karo
df.to_sql('students', conn, if_exists='replace', index=False)
print("Data saved to table 'students'.")

# table data reaad karke pandas dataframe me le aao

df = pd.read_sql("SELECT * FROM students LIMIT 5", conn)

print(df)

#connection close

conn.close()