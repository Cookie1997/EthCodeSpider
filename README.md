# EthCodeSpider
A spider who can grab the information of smart contract in Ethereum  
该爬虫是为了爬取以太坊智能合约的代码信息，下文包括爬取的URL和输出格式。爬取的是网站etherscan.io上所有的智能合约信息，输出合约名称，内容，abi等信息，可以根据自己需要修改py代码，输出格式为txt。
## Functional description
This spider can grab the information of smart contract in Ethereum from several sites.  
Up to now, it can grab Contract Source Code, Contract ABI, Contract Creation Code adn Constructor Arguments.
## Operating system
Windows 7/8/8.1/10  
## Environment Dependency
python 3.6
## How to run
1. Run the address_spider.py to get the addresses in the folder.  
```
python address_spider.py
```
2. After running the program, run the code_spider.py to get the code etc in the same folder.
```
python code_spider.py
```
## Destination URL
```python
sites = [
('https://etherscan.io/contractsVerified/1?ps=100', 'etherscan'),
('https://ropsten.etherscan.io/contractsVerified/1?ps=100','ropsten_etherscan'),
('https://kovan.etherscan.io/contractsVerified/1?ps=100', 'kovan_etherscan'),
('https://rinkeby.etherscan.io/contractsVerified/1?ps=100', 'rinkeby_etherscan')
]
```
## Result Format
```
Contract Adress:
Contract Name:
Contract_Source_Code: 
Contract_ABI:
Contract_Creation_Code_ARM:
```
## Maintenance
The error information will be written in the log for the user to operation and maintenance.
## Contact information
If you have any question, please send message to [neublockchain@163.com](https://neublockchain@163.com). Good luck.
