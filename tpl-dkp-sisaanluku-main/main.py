# TODO:
#   - write the valid items to a dataframe using pandas, and then save the dataframe to a JSON file named "data/posts.json"

import pandas as pd
from client.api_client import fetch_data
from utils.validators import validate_items

API_URL = "https://jsonplaceholder.typicode.com/posts"
JSON_FILE_PATH = "data/posts.json"

def main():
    print("Haetaan dataa…")

    items = fetch_data(API_URL)

    if items is None:
        print("Haku epäonnistui.")
        return
    
    print("Vahvistetaan")

    if validate_items(items):
        print("Vahvistettu")
    else:
        print("Ei vahvistettu")
        return

    df = pd.DataFrame(items)

    df.to_json(JSON_FILE_PATH)
    print("Kirjoitettu tiedostoon")

if __name__ == "__main__":
    main()