import time,requests
from datetime import datetime
from db_config.db_config import dbProd


# 业务：honmaKr-prod插入会员订单
"""
mst_sku_id = '296636622569473'
item_sku_code = '3290000960120017'
item_category = '100200200540' 

mst_sku_id = '295427637575681'
item_sku_code = '2300391124760040'
item_category = '400400100300'   # 品类code
"""

# 生成会员订单号
result = int(round(time.time() * 1000))
tid = str(result) + "honmaKr"
print("订单号:", tid)
mbr_member_id = 297626541686785     # 276099447652355  0704生日
amount = 5000  # 订单总金额
store_id = 302902873161777   # 店铺id
store_code = 'ST1372'  # 店铺code
channel_code = 'HonmaKrOffline'  # 渠道code
channel_id = '208818057248769'   # 渠道id
status = "TRADE_FINISHED"   # 订单状态
order_time = "2024-12-01 12:00:00"   # 下单时间
# 子单相关字段
item_sale_price = 1000    # 单价
item_quantity = 5  # 购买sku数量
item_adjustment_price = item_sale_price * item_quantity  # 购买sku总价
mst_sku_id = '296636622569473'
item_sku_code = '3290000960120017'
item_category = '100200200540'
# 获取当前时间
now = datetime.now()
# 格式化时间为年月日时分秒
now_time = now.strftime('%Y-%m-%d %H:%M:%S')

# 订单主表主键最大值+1
max_ord_order_header_id = dbProd.query("SELECT max(id) as max_ord_order_header_id from member_domain.ord_order_header")
ord_max_id = max_ord_order_header_id[0]['max_ord_order_header_id']
ord_id = int(ord_max_id)+1
# print(ord_id)

# 子单表主键最大值+1
max_ord_order_detail_id = dbProd.query("SELECT max(id) as max_ord_header_detail_id from member_domain.ord_order_detail")
detail_max_id = max_ord_order_detail_id[0]['max_ord_header_detail_id']
detail_id = int(detail_max_id)+1
# print(detail_id)

# 插入主单
insertsql = f"INSERT INTO member_domain.ord_order_header" \
            f"(id, mbr_member_id, activity_id, order_number, return_service_flag, original_top_order_number, third_order_number, channel_id, channel_code, store_id, store_code, member_name, member_code, country, province, city, district, mobile, progress_step, order_time, order_operated_type, order_saled_type, order_status, third_order_status, expected_delivery_time, expected_arrival_time, actual_delivery_time, actual_arrival_time, payment_time, trade_end_time, audit_mode, audit_status, audit_time, cancel_time, canceled_reason, payment_status, refund_status, delivery_status, delivery_order_count, shipping_type, shipping_status, shipping_specified_mode, shipping_payment_mode, need_invoice_flag, buyer_memo, seller_comment, item_quantity, product_total_amount, promotion_adjustment_total_amount, coupon_adjustment_total_amount, adjustment_total_amount, origin_freight_fee, freight_fee, payble_amount, order_total_amount, payed_amount, refunded_amount, basic_status, platform_source, packing_box_flag, packing_box_price, expected_ware_house, expected_logistics_express, order_trading_tag, trading_next_time, merge_flag, seller_flag, point_need_calculate_time, point_calculated_flag, point_calculate_time, try_calculate_times, exist_skip_calc_point_coupon_flag, ba_no, coupon_no, relate_order_header_id, relate_order_number, relate_third_order_number, sort_id, membership_system_id, partner_id, version, deleted, create_time, create_user_id, update_time, update_user_id, create_user_name, update_user_name)" \
            f"VALUES({ord_id},{mbr_member_id},NULL, '{tid}', 0, NULL,'{tid}', '{channel_id}','{channel_code}','{store_id}','{store_code}', NULL, 'GX20240701001', NULL, NULL, NULL, NULL, NULL, 0, '{order_time}', 1, 11, 1, 'TRADE_FINISHED', NULL, NULL, NULL, NULL, '{order_time}', '{order_time}', 1, 0, NULL, NULL, NULL, 1, 0, 1, 0, 13, 1, 0, 11, 0, NULL, NULL,{item_quantity}, NULL, 0.00000, NULL, 0.00000, 0.00000, 0.00000, {amount}, {amount}, {amount}, 0.00000, 0, 'memberHub', 0, NULL, NULL, NULL, NULL, '2023-08-15 16:50:53', 0, 0, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 100, 1, 1, 0, 0, '{now_time}', '60073', '{now_time}', NULL, 'mqTest','mqTest');"
dbProd.execute(insertsql)
# 插入明细单
sqldetail = f"INSERT INTO member_domain.ord_order_detail" \
            f"(id, ord_order_header_id, mbr_member_id, mst_sku_id, third_order_number, channel_code, sub_order_number, item_name, item_product_code, item_sku_code, item_category, item_size, item_sale_price, item_adjustment_unit_price, item_quantity, deliveried_quantity, delivery_status, item_adjustment_total_price, third_refund_id, ref_sub_order_number, exist_exception_flag, sort_id, membership_system_id, partner_id, version, deleted, create_time, create_user_id, update_time, update_user_id, create_user_name, update_user_name)" \
            f"VALUES({detail_id},{ord_id},{mbr_member_id},{mst_sku_id}, '{tid}', '{channel_code}', '{tid}', NULL, 'HM00003008','{item_sku_code}','{item_category}', NULL, {item_sale_price}, 0.00000, {item_quantity}, NULL, NULL, {item_adjustment_price}, NULL, NULL, NULL, 100, 1, 1, 0, 0, '{now_time}', '10556826', '{now_time}', NULL, 'mqTest', 'mqTest');"
dbProd.execute(sqldetail)

# 关闭数据库连接
dbProd.close()