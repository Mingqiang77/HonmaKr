import requests
import time
import random
from datetime import datetime, date


def generate_random_mobile(prefix="176", suffix="-M", total_length=11):
    """生成固定前缀和后缀的随机手机号。"""
    body_length = total_length - len(prefix)
    if body_length <= 0:
        raise ValueError("total_length must be greater than the prefix length")

    random_digits = f"{random.randint(0, 10 ** body_length - 1):0{body_length}d}"
    return f"{prefix}{random_digits}{suffix}"


def generate_random_birthday(start_year=1992, end_year=2020):
    """生成随机生日，返回YYYY-MM-DD格式字符串"""
    start_date = f"{start_year}-01-01"
    end_date = f"{end_year}-12-31"
    start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
    end_timestamp = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())
    random_timestamp = random.randint(start_timestamp, end_timestamp)
    return datetime.fromtimestamp(random_timestamp).strftime("%Y-%m-%d")


def calculate_age(birthday_str):
    """根据生日计算年龄"""
    today = date.today()
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age


def add_honma_member():
    """调用接口插入HonmaKr会员，包含完整异常处理"""
    # 1. 生成随机参数
    mobile = generate_random_mobile()
    wxNickname = f"mqHonmaKrWxNickName{int(round(time.time() * 1000))}"
    ouid = f"mqHonmaKrOuid{int(round(time.time()))}"
    unionId = f"mqHonmaKrUnionId{int(round(time.time() * 2000))}"

    # 随机邮箱
    domain_list = ["example.com", "test.com", "mail.com"]
    email = f"mqTest{int(round(time.time() * 100))}@{random.choice(domain_list)}"

    # 生日和年龄
    memberBirthday = generate_random_birthday()
    age = calculate_age(memberBirthday)

    # 性别和姓名
    sex = "女"
    name = f"MqHonmaKrMemberName{random.randint(1, 99999)}"

    # 2. 接口配置
    addMemberUrl = "https://test-api.honmagolf.kr/customerCrm/open/v1/member/memberActiveRegisterBind"
    headers = {
        "thirdtoken": "07f536131cde4ddeaf8d796405b9b7f0",
        "Content-Type": "application/json"
    }
    params = {
        "appCode": "HonmaKrEcshop",
        "attributeMap": {
            "mobile": mobile,
            "email": email,
            "wxNickname": wxNickname,
            "unionId": unionId,
            "ouid": ouid,
            "fromChannel": "honmaKr",
            "registerStore": "10201",
            "memberBirthday": memberBirthday,
            "sex": sex,
            "age": age,
            "name": name
        },
        "membershipSystemId": 1,
        "partnerId": 1
    }

    # 3. 发送请求并处理响应（核心异常处理）
    try:
        print(f"开始调用接口，请求参数：\n{params}")
        response = requests.post(
            addMemberUrl,
            headers=headers,
            json=params,
            timeout=30  # 增加超时保护
        )

        # 打印响应基础信息（调试用）
        print(f"接口响应状态码：{response.status_code}")
        print(f"接口响应原始内容：{response.text}")

        # 检查HTTP状态码（4xx/5xx直接抛异常）
        response.raise_for_status()

        # 安全解析JSON（空内容返回空字典）
        response_data = response.json() if response.text.strip() else {}

        # 安全取值（避免KeyError）
        memberid = response_data.get('data', {}).get('memberId')

        if memberid:
            print(f"新增会员成功 ===> 会员id：{memberid} | 邮箱：{email}")
        else:
            print(f"新增会员失败：接口返回无memberId，响应数据：{response_data}")

        return memberid, email

    # 捕获JSON解析错误
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSON解析失败：{str(e)} | 响应内容：{response.text}")
        return None, email

    # 捕获HTTP请求错误（超时、连接失败、4xx/5xx）
    except requests.exceptions.RequestException as e:
        print(f"接口请求失败：{str(e)}")
        return None, email

    # 捕获其他未知错误
    except Exception as e:
        print(f"未知错误：{str(e)}")
        return None, email


# 执行主函数
if __name__ == "__main__":
    add_honma_member()
