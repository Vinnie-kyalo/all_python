import pandas as pd
import mysql.connector

# Load data from Excel
df = pd.read_excel(r"C:\Users\KYALO\finance\inflation_data.xlsx", sheet_name="inflation_data")

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nightnurse@vinnie44040",
    database="finance"
)

mycursor = mydb.cursor()


for index, row in df.iterrows():
    month = row['month']
    food_inflation = row['food_inflation']
    fuel_inflation =row['fuel_inflation']
    
    
    sql_query = "INSERT INTO data_inflationdata (month, food_inflation,fuel_inflation) VALUES (%s, %s ,%s)"
    
    
    mycursor.execute(sql_query, (month, food_inflation,fuel_inflation))


mydb.commit()

print(mycursor.rowcount, "record(s) inserted.")


mycursor.close()
mydb.close()
