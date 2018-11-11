#!/bin/python3

import requests
import time

class URLLOAD:
	def dorequest(self, url):
		time.sleep(1) # add by zyx
		res = requests.get(url, verify=True)
		if res.status_code == 200:
			return res.text