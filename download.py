#!/usr/bin/env python3
import requests
import os

def download(url):
	try:
		req = requests.get(url)
	except requests.exceptions.MissingSchema:
		print('Invalid Url {}'.format(url))
		return
	
	if req.status_code == 403:
		print("access error")
		return
	filename = url.split('/')[-1]
	if os.path.exists('./{}'.format(filename)):
		print('same file exists')
		return
	with open(filename,'w') as f:
		f.write(req.content.decode('utf-8'))
	print('Download over.')

if __name__ == '__main__':
	url = input('Enter a url:')
	download(url)
