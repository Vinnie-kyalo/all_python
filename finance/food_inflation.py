import pandas as pd
import mysql.connector

# Load data from Excel
df = pd.read_excel(r"C:\Users\KYALO\finance\food_inflation.xlsx", sheet_name="food_inflation")

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nightnurse@vinnie44040",
    database="finance"
)

mycursor = mydb.cursor()


for index, row in df.iterrows():
    month_id = row['Month']
    value = row['food_inflation']
    
    
    sql_query = "INSERT INTO data_monthlyfoodinflation (Month, food_inflation) VALUES (%s, %s)"
    
    
    mycursor.execute(sql_query, (month_id, value))


mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")


mycursor.close()
mydb.close()
