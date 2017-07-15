from internetarchive import search_items
from internetarchive import download
import requests
import sys

if len(sys.argv) == 1:
    raise Exception('A search term must be provided')

coll = search_items(sys.argv[1])

num = 0

for item in coll:
	try:
		download(item['identifier'], verbose=True, on_the_fly=True, glob_pattern='*mobi')
	except requests.exceptions.HTTPError as e:
		print("Could not download file")
