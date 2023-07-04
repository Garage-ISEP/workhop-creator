import os

import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

notion_page_id = os.getenv("NOTION_WORKSHOP_ID")
NOTION_KEY = os.getenv("NOTION_KEY")

headers = {
    "Authorization": "Bearer " + NOTION_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def create_event_notion(name, lab, description, date, hour, location):
    year = datetime.now().year  # Specify the desired year
    # Concatenate the year with the date string
    date_string_with_year = f"{date} {year}"

    # Parse the date string
    _date = datetime.strptime(date_string_with_year, "%d %b %Y")
    _date_string = _date.strftime("%Y-%m-%d")  # Convert datetime object to string

    url = f"https://api.notion.com/v1/pages"
    data = {
        "parent": {"database_id": notion_page_id},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Lab": {
                "multi_select": [
                    {
                        "name": lab
                    }
                ]
            },
            "Description": {
                "rich_text": [
                    {
                        "text": {
                            "content": description
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                    "start": _date_string
                }
            },
            "Hour": {
                "rich_text": [
                    {
                        "text": {
                            "content": hour
                        }
                    }
                ]
            },
            "Location": {
                "rich_text": [
                    {
                        "text": {
                            "content": location
                        }
                    }
                ]
            }
        }
    }

    res = requests.post(url, headers=headers, json=data)
    print(res.json())


# Example usage
#create_event_notion("Blockchain Event", "Blockchain", "An event about blockchain technology", "2 JUL", "14:00", "Virtual")