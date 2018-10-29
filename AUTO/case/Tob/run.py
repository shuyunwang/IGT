#coding:utf-8
import unittest
import HTMLTestRunnerCN
import sys
import datetime


if __name__ == '__main__':
    # suite = unittest.defaultTestLoader.discover(start_dir=sys.argv[0]+'//..//',pattern='FAT_*.py')
    suite = unittest.defaultTestLoader.discover(start_dir='./', pattern='FAT_*.py')
    # HTMLTestRunnerCN.HTMLTestRunner(stream=open(sys.argv[0]+'//..//report.html','wb')).run(suite)
    HTMLTestRunnerCN.HTMLTestReportCN(title='自营测试报告',description='环境:FAT',tester='9527'
                                    ,stream=open('./report/ERP_report_{a}.html'.format(a=datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
                                                 'wb')).run(suite)
    # unittest.TextTestRunner().run(suite)
