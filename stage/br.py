# coding:utf-8
from datetime import datetime
from dingtalkchatbot.chatbot import DingtalkChatbot

# Ruoxi粉丝群-webhook
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=eed64f94735a70d3cad24999263d33078f89f658ae7ed9aa66a4bdfe15a9872d'

def days_until_next_birthday(birthday):
    today = datetime.today()
    current_year = today.year
    next_birthday = datetime.strptime(f"{current_year}-{birthday}", "%Y-%m-%d")

    # 如果今年已经过了生日，就用明年
    if next_birthday < today:
        next_birthday = datetime.strptime(f"{current_year + 1}-{birthday}", "%Y-%m-%d")

    countdown = (next_birthday - today).days
    return countdown

def generate_birthdays_message(birthdays):
    message = "我说一个事嗷,生日倒计时:\n"
    for name, birthday in birthdays.items():
        days_left = days_until_next_birthday(birthday)
        if days_left == 364:
            message += f"祝 {name} 生日快乐哦！\n"
        else:
            message += f"距离 {name} 的下一个生日还有 {days_left} 天\n"
    return message

def send_dingtalk_message(webhook, message):
    try:
        ding = DingtalkChatbot(webhook)
        ding.send_text(msg=message, is_at_all=True)
    except Exception as e:
        print(f"Failed to send message: {e}")

if __name__ == "__main__":
    # 在这里输入要计算的生日信息
    birthdays = {
        "爸爸": "08-10",  # 月-日
        "妈妈": "12-11",
        "自己": "04-29",
        "奶奶": "10-30",
        "爷爷": "01-02"
    }
    # 生成生日倒计时信息
    message = generate_birthdays_message(birthdays)

    # 打印到控制台
    print(message)

    # 发送到钉钉群
    send_dingtalk_message(webhook, message)
