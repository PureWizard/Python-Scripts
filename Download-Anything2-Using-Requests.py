import requests

def download_file(url, local_filename):
    # open in binary mode
    with open(local_filename, "wb") as file:
        # get request
        response = requests.get(url)
        file.write(response.content)

url = input("Enter the URL of the file you want to download: ")
local_filename = input("Enter the output name: ")
download_file(url, local_filename)
print(f"File downloaded and saved to {local_filename}")
