import random
import requests
import json

def generate_super_lotto_numbers():
    # 生成5个主号码（1到35之间，不重复）
    main_numbers = random.sample(range(1, 36), 5)

    # 生成2个额外号码（1到12之间，不重复）
    extra_numbers = random.sample(range(1, 13), 2)

    return main_numbers, extra_numbers

def send_dingtalk_message(webhook_url, message):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": message
        }
    }
    requests.post(webhook_url, headers=headers, data=json.dumps(data))

# 生成大乐透号码
main_numbers, extra_numbers = generate_super_lotto_numbers()
message = f"我说一个事嗷,爸爸这周的DLT幸运数字如下:\n主号码: {sorted(main_numbers)}\n额外号码: {sorted(extra_numbers)}"

# 钉钉Webhook URL（替换为你自己的Webhook URL）
webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=eed64f94735a70d3cad24999263d33078f89f658ae7ed9aa66a4bdfe15a9872d'

# 发送消息
send_dingtalk_message(webhook_url, message)


