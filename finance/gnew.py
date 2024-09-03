from gnews import GNews
import mysql.connector
from mysql.connector import Error

# Initialize GNews client
news_client = GNews()

try:
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nightnurse@vinnie44040",
        database="gnew_inflation",
        port=3306  # Default MySQL port
    )
    
    if conn.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object
        cur = conn.cursor()

        # Create the table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gnew_inflation (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title TEXT,
                description TEXT,
                link TEXT,
                published_at DATETIME,
                source TEXT
            );
        """)
        conn.commit()

        # Search for news articles about "Kenya Inflation"
        news_articles = news_client.get_news("Kenya Inflation")

        # Insert news articles into the database
        for article in news_articles:
            # Print article fields for inspection
            print("Article fields:", article)

            title = article.get('title', 'N/A')
            description = article.get('description', 'N/A')
            link = article.get('url', 'N/A')
            published_at = article.get('publishedAt', 'N/A')
            source = article.get('source', {}).get('name', 'N/A')

            cur.execute("""
                INSERT INTO gnew_inflation (title, description, link, published_at, source)
                VALUES (%s, %s, %s, %s, %s)
            """, (title, description, link, published_at, source))

        conn.commit()
        print("News data successfully scraped and saved to the database!")

except Error as e:
    print(f"Error: {e}")

finally:
    if conn.is_connected():
        cur.close()
        conn.close()
