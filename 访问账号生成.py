
# coding: utf-8
# 组合 各个part 
import json
import urllib
import urllib.request
from urllib import request


def get_token(host):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json; charset=UTF-8"}
    #示例URL: http://api.haitunpt.com/sms/?api=login&user=用户名&pass=密码
    #{"msg":"success","code":0,"token":"xxxxxxxxxxx"}
    req = request.Request(url=host, headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    res_json = json.loads(res.decode('utf-8'))
    return (res_json["msg"],res_json["code"],res_json["token"])


#登陆接码平台 获取token
get_token('http://api.haitunpt.com/sms/?api=login&user=qinqin123&pass=138259jyq520')
#user=qinqin123
#pass=123456jyq123




def get_Phone(host):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json; charset=UTF-8"}

    req = request.Request(url=host, headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    res_json = json.loads(res.decode('utf-8'))
    #return (res_json["msg"],res_json["code"],res_json["phone"])
    return (res_json["msg"],res_json["code"])



#小红书项目对应的sid=22795
get_Phone('http://api.haitunpt.com/sms/?api=getPhone&token=f73b8e09e0ecc5ccffe25ab6e0f51b8f237107ad&sid=22795')
#获取项目对应手机号码生成账户



###获取验证码(getMessage)
def get_Message(host):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json; charset=UTF-8"}

    req = request.Request(url=host, headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    res_json = json.loads(res.decode('utf-8'))
    #return (res_json["msg"],res_json["code"],res_json["phone"])
    return (res_json["msg"],res_json["code"],res_json["sms"],res_json["yzm"])




#示例URL:http://api.haitunpt.com/sms/?api=getMessage&token=登陆返回的令牌&sid=项目ID&phone=取到的手机号码

get_Message(host)
#获取验证码成功注册后进行下一步