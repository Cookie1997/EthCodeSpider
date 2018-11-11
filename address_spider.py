#!/bin/python3

from owef_urlmanage import URLMAN
from owef_urlload import URLLOAD
from owef_urlparse import RESPARSE
from owef_dataoutput import OUTPUT
from owef_process_bar import *
import sys
import logging

logging.basicConfig(filename='address-spider.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


sites = [
('https://etherscan.io/contractsVerified/1?ps=100', 'etherscan'),
('https://ropsten.etherscan.io/contractsVerified/1?ps=100','ropsten_etherscan'),
('https://kovan.etherscan.io/contractsVerified/1?ps=100', 'kovan_etherscan'),
('https://rinkeby.etherscan.io/contractsVerified/1?ps=100', 'rinkeby_etherscan')
]
#,('https://tobalaba.etherscan.com/contractsVerified/1?ps=100', 'tobalaba_etherscan')
class SPIDER:
	def __init__(self, start_url='https://etherscan.io/contractsVerified/1?ps=100', path=None):
		self.urlmanage = URLMAN()
		self.urlload = URLLOAD()
		self.urlparse = RESPARSE()
		self.output = OUTPUT(path=path)
		self.output.write_file()
		self.spider_name = path
		self.run(start_url)
	def run(self, url):
		self.urlmanage.seturl(url)
		totals_content = self.urlload.dorequest(url)
		totals = self.urlparse.parse_list_page_count(totals_content)
		total, success, error = 0, 0, 0
		while self.urlmanage.has_new_url():
			url = self.urlmanage.get_newurl()
			content = self.urlload.dorequest(url)
			if content:
				data, next_url = self.urlparse.parselist(content, url)
				self.output.write_datas(data)
				self.urlmanage.seturl(next_url)
				success+=1
			else:
				error+=1
				logging.log(url + " - spider wrong : " + content)
			total += 1
			sys.stdout.write(process_bar_text(self.spider_name, total, totals, success, error))
		sys.stdout.flush()

def main():
	for url, path in sites:
		spider = SPIDER(url, path)

if __name__ == '__main__':
	main()