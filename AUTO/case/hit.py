#coding:utf-8
import requests



class Client:

    def __init__(self,url,method,type=None):
        self.__url = url
        self.__method = method
        self.__type = type
        self.__herders = {}
        self.__data = {}
        self.__res = None

    def add_header(self,key,value):
        self.__herders[key] = value

    def set_data(self,data):
        self.__data = data

    def send(self):
        if self.__method == 'GET':
            self.__res = requests.get(url=self.__url,params=self.__data,headers=self.__herders)
        elif self.__method == 'POST':
            if self.__type == 0:
                self.add_header('Content-Type', 'application/json')
                self.__res = requests.post(url=self.__url, json=self.__data, headers=self.__herders)
            elif self.__type == 1:
                self.__res = requests.post(url=self.__url,data=self.__data,headers=self.__herders)
            elif self.__type == 2:
                xml = self.__data.get('xml')
                if xml:
                    self.add_header('Content-Type','text/xml')
                    self.__res = requests.post(url=self.__url,data=self.__data,headers=self.__herders)
                else:
                    raise Exception('XML正文请按以下格式填写：{‘xml’：‘XXXXXX’}')
            elif self.__type == 3:
                self.add_header('Content-Type','application/x-www-form-urlencoded')
                self.__res = requests.post(url=self.__url,data=self.__data,headers=self.__herders)
            elif self.__type == 4:
                self.__res = requests.post(url=self.__url, files=self.__data, headers=self.__herders)
            elif self.__type == None:
                self.__res = requests.post(url=self.__url,headers=self.__herders)
            else:
                raise Exception('不支持的Type正文格式')
        else:
            raise Exception('不支持的请求方法类型，只支持GET、POST请求')

    @property
    def text(self):
        return self.__res.text

class Method:
    GET = 'GET'
    POST = 'POST'


class Type:
    JSON = 0
    FROM = 1
    XML = 2
    STRING = 3
    FILES = 4



