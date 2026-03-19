import requests,time,random
from datetime import datetime
from datetime import date
"""
业务：honmaKr-prod-插入会员
"""
# 随机生成176开头的11位手机号并且拼接一个"-M"
prefix = "17"  # 手机号的前三位固定为176
# 生成后八位
last_eight_digits = ''.join(random.choice('0123456789') for _ in range(9))
# 拼接成手机号
phone_number = prefix + last_eight_digits
# 添加"-M"
mobile = phone_number + "-M"

# 随机生成 wxNickname
result = int(round(time.time() * 1000))
wxNickname = "mqHonmaKrWxNickName" + str(result)

# 随机生成 ouid
result1 = int(round(time.time()))
ouid ="mqHonmaKrOuid" + str(result1)

# 随机生成 unionId
result2 = int(round(time.time() * 2000))
unionId = "mqHonmaKrUnionId" + str(result2)

# 随机生成email
domain_list = ["example.com", "test.com", "mail.com"]
domain = random.choice(domain_list)
email1 = int(round(time.time() * 100))
email2 = "mqTest" + str(email1)
email = f"{email2}@{domain}"

# 随机生成生日
start_date = "1992-01-01"
end_date = "2020-12-31"
start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
end_timestamp = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())
random_timestamp = random.randint(start_timestamp, end_timestamp)
memberBirthday = datetime.fromtimestamp(random_timestamp).strftime("%Y-%m-%d")

# 获取今天的日期
today = date.today()
# 将日期转换为字符串格式
today_str = today.strftime("%Y-%m-%d")

# 输出结果
current_date = datetime.strptime(today_str, "%Y-%m-%d")
random_date1 = datetime.strptime(memberBirthday, "%Y-%m-%d")
age = current_date.year - random_date1.year
if (current_date.month, current_date.day) < (random_date1.month, random_date1.day):
    age -= 1
# print(age)

# 性别
sex = "男"

# 随机生成姓名
random_number = random.randint(1, 99999)
# 拼接memberName
name = "MqHonmaKrMemberName" + str(random_number)

# 会员激活-注册-绑定接口
addMemberUrl = "https://api.honmagolf.kr/customerCrm/open/v1/member/memberActiveRegisterBind"
# 请求头
headers = {
            "thirdtoken": "a6e51617717c4a6887f16e8445332203",
            "Content-Type": "application/json"
          }
# 请求体数据
params = {
            "appCode": "honmaKrPos",
            "attributeMap": {
                "mobile": mobile,
                "email": email,
                "wxNickname": wxNickname,
                # "tmallOmid": tmallOmid,
                "unionId": unionId,     # 微信UnionId
                "ouid": ouid,
                "fromChannel": "honmaKr",
                "registerStore": "10201",
                # "firstBindChannel": "taobao",
                "memberBirthday": memberBirthday,
                "sex": sex,
                "age": age,
                "name": name
            },
            "membershipSystemId": 1,
            "partnerId": 1
        }
# 发送POST请求
response = requests.post(addMemberUrl, headers=headers, json=params)
memberid = response.json()['data']['memberId']
print("新增会员id===>", memberid,"|","新增email===>", email)