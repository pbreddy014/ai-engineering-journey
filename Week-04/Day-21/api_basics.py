import json
import requests
import pandas as pd

def get_users():

    url = "https://jsonplaceholder.typicode.com/users"

    try:

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:

        print(
            "API request failed:",
            error
        )


users = get_users()

user_records = []

for user in users:

    record = {
        "Name": user["name"],
        "Email": user["email"],
        "City": user["address"]["city"],
        "Company": user["company"]["name"]
    }

    user_records.append(record)

users_df = pd.DataFrame(
    user_records
)

print(users_df)