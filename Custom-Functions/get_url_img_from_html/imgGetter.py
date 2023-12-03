from bs4 import BeautifulSoup
import json
html_content ="Copy it here "

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all image tags
img_tags = soup.find_all('img')

# Extract the 'src' attribute from each image tag
img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

# Create a dictionary with the image URLs
data = {'image_urls': img_urls}

# Save the data to a JSON file
with open('image_urls.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

print("Image URLs have been saved to image_urls.json")
