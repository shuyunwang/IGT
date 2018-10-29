#coding:utf-8
import unittest
import json
from fat_config import *
import os

# class Driver_CO(unittest.TestCase):
#
#     def setUp(self):
#         print 'setup'
#
#     def test_01(self):
#         print 'case01'



# a = {'PatternType': 1, 'ChannelID': 5, 'FlightNumber': 'EK4447', 'PriceMark': u'1046313346149859328', 'DiscountAmount': 0, 'TotalPrice': 238, 'UID': 'M01589988', 'Luggage': '2', 'IsOpenIM': True, 'VehicleType': 1016, 'NeedLandingVisa': False, 'TakeOffTime': '2018-09-30 16:19:36', 'SelectAddServices': [], 'UseTime': '2018-09-30 16:19:36', 'ChannelName': 'H5\xe9\xa2\x84\xe8\xae\xa2', 'IsVip': False, 'Passenger': {'Mobile': '15811111111', 'HotelTelCode': '66', 'Name': '\xe8\xb1\x86\xe5\xa3\xb3\xe5\x84\xbf', 'FirstName': 'GGG', 'HotelTel': '888888', 'AreaCode': 86, 'LastName': 'TG', 'EmergencyTel': '', 'WeiXinNo': '', 'EmergencyTelCode': ''}, 'CtripPurchaseOrderID': 306654446553, 'Adults': '2', 'DuseLocation': {'Latitude': 13.689999, 'DetailAddress': '\xe7\xb4\xa0\xe4\xb8\x87\xe9\x82\xa3\xe6\x99\xae\xe5\x9b\xbd\xe9\x99\x85\xe6\x9c\xba\xe5\x9c\xba', 'Longitude': 100.750112, 'Address': '\xe7\xb4\xa0\xe4\xb8\x87\xe9\x82\xa3\xe6\x99\xae\xe5\x9b\xbd\xe9\x99\x85\xe6\x9c\xba\xe5\x9c\xba'}, 'UseType': 3, 'FixedCode': 'BKK', 'AuseLocation': {'Latitude': 13.740443, 'DetailAddress': '409-421/4 Yaowarat Rd, Khwaeng Samphanthawong, Khet Samphanthawong, Krung Thep Maha Nakhon 10100\xe6\xb3\xb0\xe5\x9b\xbd', 'Longitude': 100.509906, 'Address': '\xe6\x9b\xbc\xe8\xb0\xb7\xe4\xba\xac\xe5\x8d\x8e\xe9\x85\x92\xe5\xba\x97'}, 'SalesPrice': 238}
# print type(a)
# print type(json.dumps(a))


# with open(os.path.abspath('.')+'/fat_config.py','ab') as a:
#     for i in a.readlines():
#         if i[:6] == 'od':
#             i = i.writelines('od = '+ int(config.od) + 1)
# #
# # print config.od
# with open(os.path.abspath('.')+'/fat_config.py','arb') as a:
#     print a.readlines()
#     # for i in a.readlines():
#         # if i[:6] == 'od':
#         # print i

# a.writelines(['1','2'])
# a.close()306654448889
# print config.od

# print b
# with open(os.path.abspath('.')+'/fat_config.py','r+') as a:
#     a.seek(0,0)
#     for line in a.readlines():
#         if config.CtripPurchaseOrderID in line:
#             line = line.replace(config.CtripPurchaseOrderID,str(int(config.CtripPurchaseOrderID) + 1))
#             a.writelines(line)
#             # a.close()
#             break



#string_switch(os.path.abspath('.')+'/fat_config.py',config.CtripPurchaseOrderID,str(int(config.CtripPurchaseOrderID) + 1))


