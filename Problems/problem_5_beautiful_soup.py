"""
Print the text of the two buttons on the Google homepage.

Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
from bs4 import BeautifulSoup

with open('Problems/data/google.html', 'r') as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# Find all button elements
#buttons = soup.find_all('input', {'class': 'lsb'})
buttons = soup.find_all('input', {'type': 'submit'})

# Print the text of each button
for button in buttons:
    print(button.get('value'))