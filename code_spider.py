#!/bin/python3

from lib import *
import os
import sys
import logging

logging.basicConfig(filename='logs/code-spider.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
cache_file_url = "cache/code.temp"
code_sites = [
    'etherscan',
    'ropsten_etherscan',
    'kovan_etherscan',
    'rinkeby_etherscan',
    'tobalaba_etherscan'
]


def record_status(url, title, current, totals, success, error):
    with open(cache_file_url, "w") as f:
        f.write("{url},{title},{current},{totals},{success},{error}".format(
            url=url, title=title, current=current, totals=totals, success=success, error=error))


def remore_status():
    with open(cache_file_url, "w") as f:
        f.write("")


def read_index(status):
    index, url = 0, ""
    if status:
        for path in code_sites:
            if path == status['title'] and status['url'] != "":
                url = status['url']
                break
            elif path == status['title'] and status['url'] == "":
                index += 1
                break
            else:
                index += 1
        if index == len(code_sites) and url == "":
            index = 0
    return index, url


def read_url_index(lines, url):
    for index in range(0, len(lines)):
        if url == lines[index]:
            return index
    return 0


class SPIDER(SPIDER_BASE):

    def run(self, address, ContractName, DateVerified):
        try:
            content = self.urlload.dorequest(address)
            if content:
                Contract_Source_Code, Contract_ABI, Contract_Creation_Code_16, Contract_Creation_Code_ARM = self.urlparse.parsecode(
                    content, address)
                self.output.write_file(DateVerified + '.txt')
                self.output.write_code(Contract_Source_Code, Contract_ABI, Contract_Creation_Code_16,
                                       Contract_Creation_Code_ARM, ContractName, address.split('/')[-1])
                return True
            else:
                logging.info(address + " - spider wrong : " + content)
        except Exception as e:
            logging.info(address + " - spider wrong : " + str(e))


def run(path=None, file='address.txt', status=None):
    full_path = file if path == None else (
        os.getcwd() + '/data/' + path + "/" + file)
    try:
        lines = []
        file_handler = open(full_path, mode="r")
        lines = file_handler.readlines()
        file_handler.close()    

        if lines == [] or lines == None:
            logging.info("read_file full_path: {full_path} spider_wrong: {msg}".format(
                full_path=full_path, msg="file is empty!"))
            return
        print(status)
        spider = SPIDER(path=path, mode="a+", status=status)
        totals, total, succeed, error, index = 0, 0, 0, 0, 0
        cache_next_url = ""
        if status:
            totals = status["totals"]
            total = status["total"]
            succeed = status["success"]
            error = status["error"]
            index = read_url_index(lines, status['url'])
        else:
            totals = len(lines)
        _lines = lines[index:]
        for index in range(0, totals):
            line = lines[index]
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
            record_status(url=lines[index+1].split('#')[0] if index+1 < totals else "", title=path, current=total,
                          totals=totals, success=succeed, error=error)
        sys.stdout.flush()
        pass
    except Exception as e:
        raise e
        logging.info("open_file_status:error full_path: {full_path} spider_wrong: {msg}".format(
            full_path=full_path, msg=str(e)))
        pass
    else:
        logging.info("open_file_status:succeed full_path: {full_path}".format(
            full_path=full_path))
        pass


def init():
    try:
        status = {}
        with open(cache_file_url, "r") as f:
            data = f.readlines()
            data_list = data[0].strip().split(',')
            status['url'] = data_list[0]
            status['title'] = data_list[1]
            status['total'] = int(data_list[2])
            status['totals'] = int(data_list[3])
            status['success'] = int(data_list[4])
            status['error'] = int(data_list[5])
        return status
    except Exception as e:
        return None


def main(status=None):
    index, url = read_index(status)
    _code_sites = code_sites[index:]
    for site in _code_sites:
        run(path=site, status=status)


if __name__ == '__main__':
    main(init())
