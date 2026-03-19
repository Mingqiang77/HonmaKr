import json,requests
# 业务：邮箱/手机号-获取验证码

primaryIdType = "EMAIL"           # 验证类型【EMAIL-邮箱，MOBILE-手机号】
primaryId = "2513681734@qq.com"          # 2513681734@qq.com

stage_host = "https://test-api.honmagolf.kr"

url = stage_host + "/ecommerce//open/customer/发送密码重置验证码"

headers = {
    "Accept": "*/*",
    "store": "ST0001",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBTEwtTUFUQ0giLCJMT0dJTl9ERVRBSUwiOiJ7XCJpZFwiOjI4MjQwNjE4NTkyNjY1NyxcInBhcnRuZXJJZFwiOjEsXCJ1c2VyVHlwZVwiOlwiTUVNQkVSXCIsXCJ1c2VyTGV2ZWxcIjpudWxsLFwiYWNjb3VudFwiOm51bGwsXCJuYW1lXCI6bnVsbCxcInJvbGVDb2Rlc1wiOm51bGwsXCJyb2xlSWRzXCI6bnVsbCxcImRhdGFBdXRoc1wiOm51bGwsXCJleHRlbmRNYXBcIjpudWxsLFwidXVpZFwiOlwiM2E1ZmQ2ZTMtN2RmNC00MWUzLWFlYTUtZTE3NDhjZDhmNmYyXCJ9In0.REtieFAx92Zf8qQbQrtDzzzKhRihPiSXYnVCN-t37kU",
    "Content-Type": "application/json"
}
body = {
    "captchaCode": "",
    "name": "",
    "newPassword": "",
    "primaryId": primaryId,
    "primaryIdType": primaryIdType,
    "storeId": 279716559454209,
    "token": ""
}

print("发送密码重置验证码body==>",body)
response = requests.post(url, headers=headers, data=json.dumps(body))
print(response.status_code)
print(response.text)