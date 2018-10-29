#coding:utf-8
import requests
import unittest



class Client(unittest.TestCase):

    def __init__(self,url,method,type=None):
        self.__url = url
        self.__method = method
        self.__type = type
        self.__herders = {}
        self.__data = {}
        self.__res = None
        self._type_equality_funcs = {}

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
                    self.__res = requests.post(url=self.__url,data=xml,headers=self.__herders)
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
    def res_json(self):
        if self.__res:
            try:
                return self.__res.json()
            except:
                print '响应执行JSON解析时错误'
                return None
        else:
            return None


    @property
    def res_text(self):
        if self.__res:
            return self.__res.text
        else:
            return None

    @property
    def res_status_code(self):
        if self.__res:
            return self.__res.status_code
        else:
            return None

    @property
    def res_time(self):
        if self.__res:
            return int(round(self.__res.elapsed.total_seconds() * 1000))
        else:
            return None

    @property
    def res_time_cn(self):
        if self.__res:
            t = int(round(self.__res.elapsed.total_seconds() * 1000))
            return "响应时间:%d" % t +"ms"
        else:
            return None


    @property
    def res_headers(self):
        if self.__res:
            return self.__res.headers
        else:
            return None



    def check_status_code(self,exp):
        self.assertEqual(self.res_status_code,exp)
        print '响应状态码[{a}],正确'.format(a=self.res_status_code)

    def check_res_less_time(self,exp):
        self.assertLess(self.res_time,exp)
        print '响应时间[{a}]ms,符合预期'.format(a=self.res_time)

    def check_equal(self,first,second):
        self.assertEqual(first,second)
        print 'equal断言成功：实际结果[{a}]，预期结果[{b}]'.format(a=first,b=second)

    def check_notequal(self,first,second):
        self.assertNotEqual(first,second)
        print 'notequal断言成功：实际结果[{a}]，预期结果[{b}]'.format(a=first, b=second)

class Method:
    GET = 'GET'
    POST = 'POST'


class Type:
    JSON = 0
    FROM = 1
    XML = 2
    STRING = 3
    FILES = 4







