#!/bin/python3
import os


class OUTPUT:

    def __init__(self, file='address.txt', path=None, mode='w'):
        self.root = os.getcwd()
        self.mode = mode
        if path:
            full_path = self.root + '/data/' + path
            if os.path.exists(full_path):
                pass
            else:
                os.mkdir(full_path)
        self.path = full_path
        self.file = self.path+'/'+file

    def set_path(self, path):
        if path:
            full_path = self.root + '/data/' + path
            if os.path.exists(full_path):
                pass
            else:
                os.mkdir(full_path)
        self.path = full_path

    def get_file(self, file):
        _file = ""
        if file == None:
            _file = self.file
        else:
            _file = self.path + '/' + file
        return _file

    def write_file(self, file=None):
        _file = self.get_file(file)
        if self.path:
            self.file = open(_file, self.mode, encoding="utf-8")
        else:
            self.file = open(self.path + '/' + _file, self.mode, encoding="utf-8")

    def read_file(self, file=None):
        _file = self.get_file(file)
        if self.path:
            self.file = open(_file, 'r', encoding="utf-8")
        else:
            self.file = open(self.path + '/' + _file, 'r', encoding="utf-8")

    def write_data(self, data):
        self.file.writeline(data)

    def write_datas(self, datas):
        self.file.writelines(datas)

    def write_code(self, Contract_Source_Code, Contract_ABI, Contract_Creation_Code_16, Contract_Creation_Code_ARM, ContractName, address):
        self.file.write("Contract Adress: " + address + '\r\n')
        self.file.write("Contract Name: " + ContractName + '\r\n')
        self.file.write("Contract_Source_Code: \r\n")
        self.file.write(Contract_Source_Code)
        self.file.write('\r\n')
        self.file.write('Contract_ABI:\r\n')
        self.file.write(Contract_ABI)
        self.file.write('Contract_Creation_Code_16:\r\n')
        self.file.write(Contract_Creation_Code_16)
        self.file.write('\r\n')
        self.file.write('Contract_Creation_Code_ARM:\r\n')
        self.file.write(Contract_Creation_Code_ARM)
        self.file.write('\r\n')
        self.file.write("\r\n\r\n")
