#coding:utf-8
import datetime
import hashlib

class gg_class():
    sid = None
    orderid = None
    roborderid = None
    pricemark = None
    vorder = None
    g_list = {}

#获取YYYY-MM-DD HH:MM:SS格式时间
def YMDHMS(day=None,hours=None,minutes=None):
    if day and hours and minutes:
        raise Exception("day、hours、minutes只能传一个")
    elif day and hours:
        raise Exception("day和hours只能传一个")
    elif hours and minutes:
        raise Exception("hours和minutes只能传一个")
    elif day and minutes:
        raise Exception("day和minutes只能传一个")
    if day:
        try:
            if day[0] == '+':
                return (datetime.datetime.now() + datetime.timedelta(days=int(day[1:]))).strftime('%Y-%m-%d %H:%M:%S')
            elif day[0] == '-':
                return (datetime.datetime.now() - datetime.timedelta(days=int(day[1:]))).strftime('%Y-%m-%d %H:%M:%S')
            else:
                raise Exception("不支持的时间参数，应该是“YMDHMS(day='+1')”或“YMDHMS(day='-1')”的格式")
        except:
            raise Exception("不支持的时间参数，应该是“YMDHMS(day='+1')”或“YMDHMS(day='-1')”的格式")
    elif hours:
        try:
            if hours[0] == '+':
                return (datetime.datetime.now() + datetime.timedelta(hours=int(hours[1:]))).strftime('%Y-%m-%d %H:%M:%S')
            elif hours[0] == '-':
                return (datetime.datetime.now() - datetime.timedelta(hours=int(hours[1:]))).strftime('%Y-%m-%d %H:%M:%S')
            else:
                raise Exception("不支持的时间参数，应该是“YMDHMS(hours='+1')”或“YMDHMS(hours='-1')”的格式")
        except:
            raise Exception("不支持的时间参数，应该是“YMDHMS(hours='+1')”或“YMDHMS(hours='-1')”的格式")
    elif minutes:
        try:
            if minutes[0] == '+':
                return (datetime.datetime.now() + datetime.timedelta(minutes=int(minutes[1:]))).strftime('%Y-%m-%d %H:%M:%S')
            elif minutes[0] == '-':
                return (datetime.datetime.now() - datetime.timedelta(minutes=int(minutes[1:]))).strftime('%Y-%m-%d %H:%M:%S')
            else:
                raise Exception("不支持的时间参数，应该是“YMDHMS(minutes='+1')”或“YMDHMS(minutes='-1')”的格式")
        except:
            raise Exception("不支持的时间参数，应该是“YMDHMS(minutes='+1')”或“YMDHMS(minutes='-1')”的格式")
    else:
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')




#获取YYYY-MM-DD HH:MM:SS格式时间
def YYMMDD(day=None):
    if day:
        try:
            if day[0] == '+':
                return (datetime.datetime.now() + datetime.timedelta(days=int(day[1:]))).strftime('%Y-%m-%d')
            elif day[0] == '-':
                return (datetime.datetime.now() - datetime.timedelta(days=int(day[1:]))).strftime('%Y-%m-%d')
            else:
                raise Exception("不支持的时间参数，应该是“YYMMDD('+1')”或“YYMMDD('-1')”的格式")
        except:
            raise Exception("不支持的时间参数，应该是“YYMMDD('+1')”或“YYMMDD('-1')”的格式")
    else:
        return datetime.datetime.now().strftime('%Y-%m-%d')

#获取md5加密的值
def get_md5(key):
    m2 = hashlib.md5()
    m2.update(key.encode('utf-8'))
    return m2.hexdigest()


#全文中搜索替换或者单行替换
#x=文件 y=原文 z=替换
def string_switch(x, y, z, s=1):
    with open(x, "r") as f:
        # readlines以列表的形式将文件读出
        lines = f.readlines()

    with open(x, "w") as f_w:
        # 定义一个数字，用来记录在读取文件时在列表中的位置
        n = 0
        # 默认选项，只替换第一次匹配到的行中的字符串
        if s == 1:
            for line in lines:
                if y in line:
                    line = line.replace(y, z)
                    f_w.write(line)
                    n += 1
                    break
                f_w.write(line)
                n += 1
            # 将剩余的文本内容继续输出
            for i in range(n, len(lines)):
                f_w.write(lines[i])
        # 全局匹配替换
        elif s == 'g':
            for line in lines:
                if y in line:
                    line = line.replace(y, z)
                f_w.write(line)