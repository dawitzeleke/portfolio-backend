from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

DB_USER_NAME = os.getenv("DB_USER_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "todo_db")

# MongoDB connection URI (Cloud-hosted MongoDB Atlas in this case)
uri = f"mongodb+srv://{DB_USER_NAME}:{DB_PASSWORD}@dz-portfolio.puf7loi.mongodb.net/?appName=dz-portfolio"

# Create a MongoDB client
client = MongoClient(uri)

# Define database
db = client[DB_NAME]
