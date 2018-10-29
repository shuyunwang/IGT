#coding:utf-8
from hit import *
from fat_config import *
from public import *
import json
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class OCH_query(unittest.TestCase):
    '''查价接口测试'''

    def setUp(self):
        '''初始化请求参数'''

        self.query_data = {
            "UseType":3,
            "PatternType":2,
            "VehicleTypeList":[

            ],
            "DuseLocation":{
                "Longitude":98.3025859,
                "Latitude":7.843020099999999,
                "Address":"Hotel IKON Phuket",
                "DetailAddress":"400 Patak Rd, Tambon Karon, Amphoe Mueang Phuket, Chang Wat Phuket 83100泰国"
            },
            "AuseLocation":{
                "Longitude":98.306465,
                "Latitude":8.111095,
                "Address":"普吉国际机场",
                "DetailAddress":"普吉国际机场"
            },
            "Distance":43000,
            "During":5340,
            "UseTime":YMDHMS(minutes='+1'),
            "FixedCode":"HKT",
            "VendorIdList":[
                15999
            ],
            "IsToBRequest":1
            }

    def test_01(self):
        '''正常请求'''
        query = Client(url=config.query_url + config.path['pricemark'],method=Method.POST,type=Type.JSON)
        query.set_data(data=self.query_data)
        query.send()
        # print query.res_text
        query.check_status_code(200)
        query.check_res_less_time(1000)
        query.check_equal(query.res_json['MsgCode'],'OK')
        query.check_equal(query.res_json['VendorPriceDtoList'][0]['VendorId'],15999)
        query.check_notequal(query.res_json['VendorPriceDtoList'][0]['PriceMark'],None)

    def test_02(self):
        '''传多个车型查询'''
        self.query_data['VendorIdList']=[13588,15999,17999,18999,15888,15999]
        # print self.query_data
        query = Client(url=config.query_url + config.path['pricemark'],method=Method.POST,type=Type.JSON)
        query.set_data(data=self.query_data)
        query.send()
        # print query.res_text
        query.check_status_code(200)
        query.check_equal(query.res_json['MsgCode'],'OK')
        query.check_equal(len(query.res_json['VendorPriceDtoList']),6)

    def test_03(self):
        '''不传品牌ID'''
        self.query_data.pop('VendorIdList')
        # print json.dumps(self.query_data,encoding="UTF-8", ensure_ascii=False)
        query = Client(url=config.query_url + config.path['pricemark'],method=Method.POST,type=Type.JSON)
        query.set_data(data=self.query_data)
        query.send()
        # print query.res_text
        query.check_status_code(200)
        query.check_equal(query.res_json['MsgCode'],'NO_VEHICLE')
        query.check_equal(query.res_json['Message'],'车型不提供服务')
