# -*- coding: utf-8 -*-
import json,requests
from urllib.parse import quote
# 业务：账号密码修改

captchaCode = "658638"   # 验证码
primaryIdType = "EMAIL"  # 验证类型【EMAIL-邮箱，MOBILE-手机号】
primaryId = "2513681734@qq.com"
newPassword = "Zmq@000004"     # 新密码

stage_host = "https://test-api.honmagolf.kr"

# 验证码校验接口
def collateCode():
    endpoint = "/ecommerce//open/customer/校验验证码"
    encoded_endpoint = quote(endpoint)  # 对路径中的中文进行编码
    collateCodeUrl = stage_host + encoded_endpoint

    headers = {
        "Accept": "*/*",
        "store": "ST0001",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBTEwtTUFUQ0giLCJMT0dJTl9ERVRBSUwiOiJ7XCJpZFwiOjI4MjQwNjE4NTkyNjY1NyxcInBhcnRuZXJJZFwiOjEsXCJ1c2VyVHlwZVwiOlwiTUVNQkVSXCIsXCJ1c2VyTGV2ZWxcIjpudWxsLFwiYWNjb3VudFwiOm51bGwsXCJuYW1lXCI6bnVsbCxcInJvbGVDb2Rlc1wiOm51bGwsXCJyb2xlSWRzXCI6bnVsbCxcImRhdGFBdXRoc1wiOm51bGwsXCJleHRlbmRNYXBcIjpudWxsLFwidXVpZFwiOlwiM2E1ZmQ2ZTMtN2RmNC00MWUzLWFlYTUtZTE3NDhjZDhmNmYyXCJ9In0.REtieFAx92Zf8qQbQrtDzzzKhRihPiSXYnVCN-t37kU",
        "Content-Type": "application/json"
    }
    body = {
        "captchaCode": captchaCode,
        "name": "",
        "newPassword": "",
        "primaryId": primaryId,
        "primaryIdType": primaryIdType,
        "storeId": 279716559454209,
        "token": ""
    }
    print("校验验证码body==>",body)
    response = requests.post(collateCodeUrl, headers=headers, data=json.dumps(body))
    print("验证码校验接口返回:", response.json())
    return response.json()["data"]

# 密码重置接口
def resetPassword(token):
    endpoint = "/ecommerce//open/customer/密码重置"
    encoded_endpoint = quote(endpoint)  # 对路径中的中文进行编码
    resetPasswordUrl = stage_host + encoded_endpoint

    headers = {
        "Accept": "*/*",
        "store": "ST0001",
        "Content-Type": "application/json"
    }
    body1 = {
        "captchaCode": captchaCode,
        "name": "",
        "newPassword": newPassword,
        "primaryId": primaryId,
        "primaryIdType": primaryIdType,
        "storeId": 279716559454209,
        "token": token
    }
    print("密码重置body==>", body1)
    response = requests.post(resetPasswordUrl, headers=headers, data=json.dumps(body1))
    print("密码重置接口返回:", response.json())

if __name__ == '__main__':
    token = collateCode()
    resetPassword(token)

"""
BERES 09：281327228289025
类目介绍页 /category-introduction/281327228289025

BeZEAL3：282740687831041
类目介绍页 /category-introduction/282740687831041

PLP页面取虚拟类目管理商品

原生页面 ：
KIWAMI VI  /products/category/VC0006
BeZEAL3     /products/category/VC0005
T//WORLD TW757  /products/category/VC0004
BERES 09    /products/category/VC0003

KIWAMI V    /products/category/VC0007
TR20/TR21   /products/category/VC0008

T//WORLD GS  /products/category/VC0009
BERES AIZU/BERES BLACK  /products/category/VC0010
BERES 07    /products/categoryVC0011

클럽
BERES 09
"""