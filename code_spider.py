#!/bin/python3

from lib import *
import os
import sys
import logging

logging.basicConfig(filename='logs/code-spider.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

code_sites = [
    'etherscan',
    'ropsten_etherscan',
    'kovan_etherscan',
    'rinkeby_etherscan',
    'tobalaba_etherscan'
]


class SPIDER(SPIDER_BASE):
    def run(self, address, ContractName, DateVerified):
        try:
            content = self.urlload.dorequest(address)
            if content:
                Contract_Source_Code, Contract_ABI, Contract_Creation_Code_16, Contract_Creation_Code_ARM = self.urlparse.parsecode(
                    content, address)
                self.output.append_file(DateVerified + '.txt')
                self.output.write_code(Contract_Source_Code, Contract_ABI, Contract_Creation_Code_16,
                                       Contract_Creation_Code_ARM, ContractName, address.split('/')[-1])
                return True
            else:
                logging.info(address + " - spider wrong : " + content)
        except Exception as e:
            logging.info(address + " - spider wrong : " + str(e))


def run(path=None, file='address.txt'):
    full_path = file if path == None else (os.getcwd() + '/'+path+"/"+file)
    try:
        file = open(full_path)
        lines = file.readlines()
        spider = SPIDER()
        spider.output.set_path(path)
        totals = len(lines)
        total, succeed, error = 0, 0, 0
        for line in lines:
            line = line.split(',')
            ans = spider.run(line[0].split('#')[0], line[1],
                                 line[2].replace('\n', ''))
            if ans:
                succeed += 1
            else:
                error += 1
            total += 1
            sys.stdout.write(process_bar_text(
                path, total, totals, succeed, error))
        sys.stdout.flush()
        pass
    except Exception as e:
        logging.info("open_file_status:error full_path: {full_path} spider_wrong: {msg}".format(
            full_path=full_path, msg=str(e)))
        pass
    else:
        logging.info("open_file_status:succeed full_path: {full_path}".format(
            full_path=full_path))
        pass


def main():
    for site in code_sites:
        run(path=site)


if __name__ == '__main__':
    main()
