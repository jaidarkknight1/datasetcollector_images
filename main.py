import requests
from bs4 import BeautifulSoup
import os

# Define the search query and URL
url = "https://www.google.com/search?q=cats&tbm=isch"

# Send an https get request and store it in r
r = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title.text)

# Find and download the images
images = soup.find_all('img')

for i, image in enumerate(images):
    name = f"Cat Image {i+1}" # Use 'image' as a default name if alt attribute is not present
    link = image.get('src')
    if link and link.startswith("http"):  # Check if the link is not empty and starts with "http"
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print(name)
    else:
        print(f"Skipped image: {name} (Invalid or empty link)")
