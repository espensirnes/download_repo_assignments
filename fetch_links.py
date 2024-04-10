
#This module fetches data from link html documents downloaded from Canvas


import os
from bs4 import BeautifulSoup
import csv
import re

PATH_TO_LINKS = r'C:\Users\esi000\Downloads\submissions (6)'

def main():
	# Prepare CSV file to write extracted data
	f = open('usrnames2.csv', 'w', newline='', encoding='utf-8')
	writer = csv.writer(f, delimiter= ';')
	writer.writerow(['User', 'Group','Repository', 'Name', 'Title', 'URL'])  # Column headers

		# Iterate through all files in the directory
	for filename in os.listdir(PATH_TO_LINKS):
		process(filename, writer)


	f.close()


def process(filename, writer):
	if not filename.endswith(".html"):
		return
	filepath = os.path.join(PATH_TO_LINKS, filename)
	with open(filepath, 'r', encoding='utf-8') as f:
		soup = BeautifulSoup(f.read(), 'html.parser')

		# Extract title and URL
		title = soup.find('h1').text if soup.find('h1') else 'Title Not Found'
		link = soup.find('a')
		url = link['href'] if link else 'URL Not Found'

		# Extract user and repository from URL using regex
		match = re.search(r'github\.com/([^/]+)/([^/?]+)', url)
		if match:
			user, repo = match.groups()
		else:
			user, repo = 'User Not Found', 'Repo Not Found'
		title, name = title.split(':')
		# Write the extracted data to the CSV file
		writer.writerow([user, 0, repo, name, title, url])



main()