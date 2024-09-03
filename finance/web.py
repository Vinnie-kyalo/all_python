from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# Set up the WebDriver (ensure you have the correct driver installed)
driver = webdriver.Chrome()  # or `webdriver.Firefox()`, etc.

# Navigate to the URL
driver.get("https://www.centralbank.go.ke/monthly-economic-indicators/")

# Get the page source after JavaScript has rendered the content
html = driver.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the table by inspecting the class or ID
table = soup.find("table")  # Adjust the parameters as needed

if table:
    # Extract table headers
    headers = [th.text.strip() for th in table.find_all("th")]
    print("Headers:", headers)  # Print headers for verification
    
    # Extract table rows
    rows = []
    for row in table.find_all("tr")[1:]:  # Skip the header row
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        rows.append(row_data)
    
    # Print first few rows for verification
    print("Sample data rows:")
    for row in rows[:5]:
        print(row)
    
    # Create a DataFrame from the data
    df = pd.DataFrame(rows, columns=headers)
    
    # Save the data to a CSV file
    df.to_csv("cbk_monthly_economic_indicators.csv", index=False)
    print("Data scraped and saved to cbk_monthly_economic_indicators.csv")
else:
    print("Table not found on the page.")

# Close the browser
driver.quit()
