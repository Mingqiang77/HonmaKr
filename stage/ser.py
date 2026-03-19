def auto_reply(user_message):
    # 将用户消息转换为小写以便于匹配
    message = user_message.lower()

    # 欢迎语
    if "你好" in message or "您好" in message:
        return "您好，欢迎联系客户服务！请问有什么可以帮您的吗？"

    # 营业时间
    elif "营业时间" in message:
        return "我们的营业时间是周一至周五，上午9点到下午6点。如有任何问题，请在此期间联系我们。谢谢！"

    # 产品或服务信息
    elif "产品" in message or "服务" in message:
        return "我们的产品包括A、B和C。您可以访问我们的网站获取更多详细信息。如果有其他问题，请随时告诉我！"

    # 订单查询
    elif "订单" in message or "查询" in message:
        return "请提供您的订单号，我们会尽快为您查询订单状态。"

    # 运费和配送
    elif "运费" in message or "配送" in message:
        return "我们的标准运费是X元，预计配送时间为3-5个工作日。具体费用和时间可能因地区而异，请提供您的详细地址以便我们确认。"

    # 技术支持
    elif "技术支持" in message or "技术问题" in message:
        return "对于技术支持问题，请详细描述您遇到的问题和相关设备信息，我们的技术团队会尽快联系您。"

    # 投诉与反馈
    elif "投诉" in message or "反馈" in message:
        return "很抱歉给您带来不便，请详细描述您的问题或建议，我们会尽快处理并回复您。感谢您的反馈！"

    # 延迟回复
    elif "等待" in message or "忙碌" in message:
        return "您好，目前我们的客服人员正在忙碌中，您的问题我们已记录，会尽快回复您，谢谢您的耐心等待！"

    # 默认回复
    else:
        return "谢谢您的咨询，祝您有美好的一天！如果还有其他问题，请随时联系。"

# 示例用法
user_message = "咁"
reply = auto_reply(user_message)
print(reply)
