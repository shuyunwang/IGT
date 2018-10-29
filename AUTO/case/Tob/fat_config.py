#coding:utf-8
from public import *
from hit import *
import os

#公共配置
class config:
    #-----------------------------------------------测试账户-----------------------------------------------------#
    #武成龙测试账户
    d_username = '15699998163'
    d_password = get_md5('123456')
    u_phone = '15811111111'
    #杨波测试账户
    yb_username = '15801290727'
    yb_password = get_md5('1234qwer')
    #携程uid
    u_id = 'M01589988'
    #DriverCarId
    yb_dcid = 'C00000088960'
    #将订单号+1
    # string_switch(os.path.abspath('.') + '/fat_config.py', config.CtripPurchaseOrderID,str(int(config.CtripPurchaseOrderID) + 1))
    #订单号
    CtripPurchaseOrderID = '306654448901'
    #-----------------------------------------------环境&域名----------------------------------------------------#
    #测试环境司机端
    driver_url = 'http://101.200.178.68:8081'
    #测试环境创建订单
    client_url = 'http://10.5.1.2:8080'
    #查价域名
    query_url = 'http://101.200.178.68:8686'

    #----------------------------------------------接口地址路径---------------------------------------------------#
    path = {}
    #登录接口地址
    path['login'] = '/service/driver/login'
    #获取乘客取消列表
    path['queryorder'] = '/service/ordernew/queryorders'
    #获取sid
    path['sid'] = '/service/sys/applysid'
    #包车创建订单接口
    # path['createorder2'] = '/json/createTempOrder'
    #获取待接单列表
    path['queryorders'] = '/service/ordernew/queryorders'
    #接单接口
    path['rob'] = '/service/order/robOrder'
    #创建供应商单
    path['venorder'] = ''
    #查价接口
    path['pricemark'] = '/test/UVPlane/13588/OCH/productmultiquery/1.0/20171030193102/0c3d96217765f3f3ca224438b7df723'
    #创建接送机订单
    path['createorder'] = '/test/UVPlane/13588/OCH/ordercreate/1.0/20170113214818/d30497c6ebdf343eda442717522bc6b6'
    #------------------------------------------------------------------------------------------------------------#
    #获取sid
    sid_data = {
        "appver": "2.18.0",
        "swidth": 414,
        "sheigh": 736,
        "imei": "0ab5577e254bdea5a0a2fca9a5ac5810",
        "os": "ios",
        "facmodel": "iPhone 7 Plus",
        "fac": "apple"
    }
    try:
        s = Client(url=driver_url + path['sid'], method=Method.POST, type=Type.JSON)
        s.set_data(data=sid_data)
        s.send()
        sid = s.res_json['sid']
        gg_class.sid = sid
        # print self.sid
    except:
        print '获取sid失败，请检查获取sid接口'
