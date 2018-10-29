#coding:utf-8
from hit import *
import datetime



#get请求

# client_get = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString',method=Method.GET)
# client_get.set_data(data={'theRegionCode':'3113'})
# client_get.send()
# print client_get.text

#post请求：url-encode
# client_url = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString',method=Method.POST,
#                     type=Type.STRING)
# client_url.set_data(data={'theRegionCode':'3113'})
# client_url.send()
# print client_url.text

#post请求：xml
# xml = '''<?xml version="1.0" encoding="utf-8"?>
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <getSupportCityString xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3113</theRegionCode>
#     </getSupportCityString>
#   </soap12:Body>
# </soap12:Envelope>'''
#
# client_xml = Client(url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx',method=Method.POST,
#                     type=Type.XML)
# client_xml.set_data({'xml':xml})
# client_xml.send()
# print client_xml.text


#post请求：json
json = {"adult":2,"checkindt":"2018-09-26","checkoutdt":"2018-09-27","children":0,"childrenages":[],"cid":219,"filter":{},"ip":"101.201.150.62","keyword":"","natlycd":"CN","pageindex":1,"pagesize":10,"reqhead":{"biztype":33,"channelid":14632,"cid":"101.201.150.62","cury":"cny","lang":"zh-cn","ptgroup":101,"pttype":101,"rmstoken":"","sf":"online","ticket":"","token":"","ubt":{"abtest":{},"pageid":"10650004908","pvid":"4","sid":"1","vid":"1537806340122.u9xjg"},"uid":"_GJYC2724892764","union":{"aid":"","ouid":"","sid":""}},"roomcount":1,"tobauth":"83225E2DB549C28EA43E5E5883E64A9A"}

#配置url，method和Type请求方法类型
client_json = Client(url='http://www.cpool.cn/sbtob/api/15020/hotelRestListQuery.json',
                     method=Method.POST,type=Type.JSON)
#配置请求参数
client_json.set_data(data=json)

#发请求
client_json.send()

#获取响应内容
# print client_json.res_text

#解析json
# print client_json.res_json

#获取响应头信息
# print client_json.res_headers

#获取响应时间
# print client_json.res_time

#获取带中文的响应时间
# print client_json.res_time_cn

#检查返回状态码
# client_json.check_status_code(200)

#检查响应时间
# client_json.check_res_less_time(1000)

#断言
# client_json.check_equal(client_json.res_json['resstatus']['rcode'],'200')


print (datetime.datetime.now() + datetime.timedelta(minutes=-1)).strftime('%Y-%m-%d %H:%M:%S')