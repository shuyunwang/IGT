#coding:utf-8
from fat_config import *
from hit import *
from public import *
import os
import unittest



class Driver(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''取sid+登录'''
        #获取sid请求参数
        self.sid_data = {
            "appver": "2.18.0",
            "swidth": 414,
            "sheigh": 736,
            "imei": "0ab5577e254bdea5a0a2fca9a5ac5810",
            "os": "ios",
            "facmodel": "iPhone 7 Plus",
            "fac": "apple"
        }

        #获取sid
        try:
            sid = Client(url=config.driver_url + config.path['sid'], method=Method.POST, type=Type.JSON)
            sid.set_data(data=self.sid_data)
            sid.send()
            gg_class.sid = sid.res_json['sid']
        except:
            print sid.res_text
            return Exception('获取sid失败，请检查获取sid接口')

        #登录请求参数
        self.login_data = {
            "loginMode": 2,
            "countryTelCode": "33",
            "useraccount": config.yb_username,
            "passwd": config.yb_password,
            "sid": gg_class.sid
        }

        #登录
        try:
            login = Client(url=config.driver_url + config.path['login'],method=Method.POST,type=Type.JSON)
            login.set_data(data=self.login_data)
            login.send()
        except:
            print login.res_text
            return Exception('登录司机端失败')



    def test_01(self):
        '''创建包车订单'''
        self.co_data = {
            "chtype": "5",
            "vehicleTypeId": 99,
            "travelStep": 3,
            "orderRemark": "",
            "mobile": config.u_phone,
            "wechat": "",
            "pttype": "88",
            "cityId": 359,
            "nameEn": "GGG/TG",
            "head": {
                "syscode": "09",
                "extension": [
                    {
                        "name": "protocal",
                        "value": "http"
                    },
                    {
                        "name": "mobile-auth-login-type",
                        "value": "MemberLogin"
                    },
                    {
                        "name": "uid",
                        "value": "E00102286"
                    },
                    {
                        "name": "IsMemberAuth",
                        "value": "true"
                    }
                ],
                "ctok": "",
                "auth": "41CDE1D902062AF16EE911E267AD2DD65336257CC1B1C8E5D4228EC2130BD9D0",
                "lang": "01",
                "cver": "1.0",
                "cid": "09031065110620677480",
                "sid": "8888"
            },
            "biztype": 33,
            "duration": 2,
            "wlver": "0.02061156",
            "adultQuantity": 2,
            "name": "自动化脚本测试",
            "otel": "",
            "useTime": YMDHMS(minutes='+1'),
            "childQuantity": 0,
            "cityIds": "359",
            "email": ""
        }

        co = Client(url=config.client_url + config.path['createorder'],method=Method.POST,type=Type.JSON)
        co.set_data(data=self.co_data)
        co.send()
        co.check_equal(co.res_json['rencode'],'200')
        # co.check_res_less_time(500)
        # self.orderId = co.res_json['orderId']
        # print self.orderId
        gg_class.orderid = co.res_json['orderId']
        print gg_class.orderid
        print '---------------------------------'


    def test_02(self):
        '''查询待接单列表'''
        self.qo_data = {
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

        #获取待接单列表，拿出下单时匹配的robOrderId
        try:
            qo = Client(url=config.driver_url + config.path['queryorders'],method=Method.POST,type=Type.JSON)
            qo.set_data(data=self.qo_data)
            qo.send()
            a = qo.res_json['orderlist']
            for i in a:
                print i['order']['channelOrderId']
                print gg_class.orderid
                print '--------------------------------'
                if i['order']['channelOrderId'] == gg_class.orderid:
                    gg_class.roborderid = i['order']['robOrderId']
                    print i['order']['robOrderId']
                    break
            # print self.robOrderId
        except:
            return Exception('没有找到匹配的robOrderId')
        print '-----------------------------------------'
        print gg_class.sid
        print gg_class.orderid
        print gg_class.roborderid

    # def test_C03(self):
    #     print 'test03'
    #     self.robdata = {
    #         "carId":config.yb_dcid,
    #         "orderId":gg_class.orderid,
    #         "robOrderId":gg_class.roborderid,
    #         "sid":gg_class.sid
    #     }
    #     print gg_class.sid
    #     print gg_class.orderid
    #     print gg_class.roborderid
    #     ro = Client(url=config.driver_url + config.path['rob'],method=Method.POST,type=Type.JSON)
    #     ro.set_data(data=self.robdata)
    #     ro.send()
    #     print ro.res_text
