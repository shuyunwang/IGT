#coding:utf-8
from hit import *
from fat_config import *
from public import *
import unittest
import os
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Driver_login(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        '''初始化操作'''

        #将订单号+1
        string_switch(os.path.abspath('.') + '/fat_config.py', config.CtripPurchaseOrderID,str(int(config.CtripPurchaseOrderID) + 1))



    def setUp(self):
        '''初始化请求参数'''
        #登录请求参数
        self.login_data = {
            "loginMode": 2,
            "countryTelCode": "33",
            "useraccount": config.yb_username,
            "passwd": config.yb_password,
            "sid": config.sid
        }
        #查询订单列表请求参数
        self.queryorders_data = {
            "rollDirection":"down",
            "sortType":1,
            "queryConditions":{
                "endTime":YMDHMS(),
                "startTime":YMDHMS(day='-5'),
                "orderStatus":4
            },
            "sid":config.sid,
            "versionType":2,
            "optchannel":2,
            "orderType":99,
            "rowCount":10
        }
        #查价请求参数
        self.productmultiquery_data = {
            "UseType":3,
            "PatternType":1,
            "VehicleTypeList":[
                1016
            ],
            "DuseLocation":{
                "Longitude":100.750112,
                "Latitude":13.689999,
                "Address":"素万那普国际机场",
                "DetailAddress":"素万那普国际机场"
            },
            "AuseLocation":{
                "Longitude":100.509906,
                "Latitude":13.740443,
                "Address":"曼谷京华酒店",
                "DetailAddress":"409-421/4 Yaowarat Rd, Khwaeng Samphanthawong, Khet Samphanthawong, Krung Thep Maha Nakhon 10100泰国"
            },
            "Distance":36000,
            "During":2160,
            "UseTime":YMDHMS(minutes='+1'),
            "FixedCode":"BKK",
            "VendorIdList":[
                13588
            ],
            "IsToBRequest":1
        }



        #创建订单请求参数
        self.createorder_data = dict(UseType=3, PatternType=1, UID=config.u_id, IsOpenIM=1, ChannelID=5,
                                     ChannelName="H5预订", TotalPrice=238, SalesPrice=238, PriceMark=gg_class.pricemark,
                                     CtripPurchaseOrderID=config.CtripPurchaseOrderID, VehicleType=1016, Passenger={
                "AreaCode": 86,
                "Mobile": config.u_phone,
                "Name": "豆壳儿",
                "FirstName": "GGG",
                "LastName": "TG",
                "HotelTelCode": "66",
                "HotelTel": "888888",
                "EmergencyTelCode": "",
                "EmergencyTel": "",
                "WeiXinNo": ""
            }, FixedCode="BKK", FlightNumber="EK4447", DuseLocation={
                "Longitude": 100.750112,
                "Latitude": 13.689999,
                "Address": "素万那普国际机场",
                "DetailAddress": "素万那普国际机场"
            }, AuseLocation={
                "Longitude": 100.509906,
                "Latitude": 13.740443,
                "Address": "曼谷京华酒店",
                "DetailAddress": "409-421/4 Yaowarat Rd, Khwaeng Samphanthawong, Khet Samphanthawong, Krung Thep Maha Nakhon 10100泰国"
            }, UseTime=YMDHMS(minutes='+2'), TakeOffTime=YMDHMS(minutes='+2'), DiscountAmount=0, SelectAddServices=[

            ], Adults="2", IsVip=0, NeedLandingVisa=0, Luggage="2")

        self.queryorder_data = {
            "optchannel":0,
            "orderType":99,
            "queryConditions":{
                "orderStatus":0
            },
            "rollDirection":"down",
            "rowCount":10,
            "sid":gg_class.sid,
            "sortType":1,
            "versionType":"2"
        }


    def test_01(self):
        '''登录接口测试'''
        login = Client(url=config.driver_url + config.path['login'],method=Method.POST,type=Type.JSON)
        login.set_data(data=self.login_data)
        login.send()
        # print login.res_text
        login.check_equal(login.res_json['errorcode'],'00000')
        login.check_equal(login.res_json['user']['driverId'],'D00000000241')
        login.check_status_code(200)
        login.check_res_less_time(500)


    def test_02(self):
        '''获取乘客取消列表'''
        queryorders = Client(url=config.driver_url + config.path['queryorder'],method=Method.POST,type=Type.JSON)
        queryorders.set_data(data=self.queryorders_data)
        queryorders.send()
        # print queryorders.res_text
        queryorders.check_equal(queryorders.res_json['errorcode'],'00000')
        queryorders.check_status_code(200)
        queryorders.check_res_less_time(500)


    def test_03(self):
        '''获取pricemark'''
        pricemark = Client(url=config.query_url + config.path['pricemark'],method=Method.POST,type=Type.JSON)
        pricemark.set_data(data=self.productmultiquery_data)
        pricemark.send()
        pricemark.check_status_code(200)
        pricemark.check_equal(pricemark.res_json['VendorPriceDtoList'][0]['MsgCode'],'OK')
        gg_class.pricemark = pricemark.res_json['VendorPriceDtoList'][0]['PriceMark']

    def test_04(self):
        '''创建接送机订单'''
        createorder = Client(url=config.query_url + config.path['createorder'],method=Method.POST,type=Type.JSON)
        createorder.set_data(data=self.createorder_data)
        # print json.dumps(self.createorder_data,encoding="UTF-8", ensure_ascii=False)
        createorder.send()
        # print createorder.res_text
        createorder.check_status_code(200)
        createorder.check_equal(createorder.res_json['MsgCode'],'OK')
        # print createorder.res_json['VendorOrderId']
        gg_class.orderid = createorder.res_json['VendorOrderId']


    # def test_05(self):
    #     '''查询待接单列表'''
    #     #获取待接单列表，拿出下单时匹配的robOrderId
    #     queryorder = Client(url=config.driver_url + config.path['queryorders'],method=Method.POST,type=Type.JSON)
    #     queryorder.set_data(data=self.queryorder_data)
    #     queryorder.send()
    #     # print type(json.dumps(queryorder.res_json['orderlist'],ensure_ascii=False))
    #     # print type(queryorder.res_json['orderlist'])
    #     print gg_class.sid
    #     for i in queryorder.res_json['orderlist']:
    #         print gg_class.orderid
    #         print i['order']['orderId']
    #         print '------------------------------------------------'
    #         if i['order']['orderId'] == gg_class.orderid:
    #             print '一样'
    #         else:
    #             print '不一样'
    #         print '--------------------------------'

        # for i in queryorder.res_json['orderlist']:
        #     print json.dumps(i)
        #     print '--------------------------------'
        #     # print a
        #     # if i['order']['channelOrderId'] == gg_class.orderid:
        #     #     gg_class.roborderid = i['order']['robOrderId']
        #     #     print i['order']['robOrderId']
        #     break
        #     # print self.robOrderId
        # # except:
        # #     return Exception('没有找到匹配的robOrderId')
        # print '-----------------------------------------'


if __name__ == '__main__':
    unittest.main()
