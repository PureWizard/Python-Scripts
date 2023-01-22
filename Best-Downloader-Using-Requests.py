import os
import requests

def download_file(url):
    local_filename = url.split("/")[-1]
    i = 1
    while os.path.exists(local_filename):
        # split the filename and extension
        name, ext = os.path.splitext(local_filename)
        # create a new name by adding a number to the name
        local_filename = f"{name}_{i}{ext}"
        i += 1

    with open(local_filename, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
    return local_filename

url = input("Enter the URL of the file you want to download:")
local_filename = download_file(url)
print(f"File downloaded and saved as {local_filename}")
