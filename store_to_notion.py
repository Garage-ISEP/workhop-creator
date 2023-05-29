import os
from datetime import datetime
from notion.client import NotionClient


def store_to_notion(lab, name, description, date, hour, location, classroom):
    # Get Notion API token from environment variables
    notion_token = os.getenv("NOTION_API_TOKEN")

    # Connect to Notion client
    client = NotionClient(token_v2=notion_token)

    # Get the Notion database
    database_url = "https://www.notion.so/your-database-url"
    cv = client.get_collection_view(database_url)

    # Create a new page in the database
    new_page = cv.collection.add_row()

    # Set the properties of the new page
    new_page.title = name
    new_page.lab = lab
    new_page.description = description
    new_page.date = datetime.strptime(date, "%Y-%m-%d").date()
    new_page.hour = hour
    new_page.location = location
    new_page.classroom = classroom

    print("Event information stored in Notion!")

