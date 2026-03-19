import time
from datetime import datetime
from db_config.db_config import dbStage

# 会员id  [退单内写死的'item_sku_code'：TM10077268   'item_category':duoKit]
mbr_member_id = 290737952980993
ord_order_header_id = 295270234324994    # 正向单(ord_order_header表)主键id
third_order_number = '1729160531469member'    # 正向单(ord_order_header表)的order_number
item_sal_price = 100   # 明细单商品单价 如：300
item_quantity = -1   # 退单商品数量 如：-1
item_adjustment_total_price = item_sal_price * item_quantity   # 退款总金额 如：-300
third_refund_id = int(round(time.time() * 1000))   # 随机生成 third_refund_id

refund_amount = -100    # 主单发起退款累计金额
order_total_amount = 0  # 主单退款后的金额
ord_item_quantity = 0  # 主单退款后的sku数量

# 获取当前时间
now = datetime.now()
# 格式化时间为年月日时分秒
now_time = now.strftime('%Y-%m-%d %H:%M:%S')

# Step1：查询明细单最大主键id，然后+1
max_ord_order_detail_id = dbStage.query("SELECT max(id) as max_ord_header_detail_id from member_domain.ord_order_detail")
detail_max_id = max_ord_order_detail_id[0]['max_ord_header_detail_id']
detail_id = int(detail_max_id)+1

# Step2：查询订单明细正向单的sub_order_number
queryOrderDetailSubOrderNumber = f"SELECT sub_order_number FROM member_domain.ord_order_detail WHERE ord_order_header_id = '{ord_order_header_id}'"
# 执行带有参数的SQL查询，将 ord_order_header_id 的值传递给查询语句中的占位符，然后执行查询获取结果。
sub = dbStage.query(queryOrderDetailSubOrderNumber)
sub_order_number = sub[0]['sub_order_number']
# print("sub_order_number:",sub_order_number)

# Step3：在正向明细单上面挂一个负向单
insertOrderDetailSql = f"INSERT INTO member_domain.ord_order_detail\
    (id, ord_order_header_id, mbr_member_id, mst_sku_id, third_order_number, channel_code, sub_order_number, item_name, item_product_code, item_sku_code, item_category, item_size, item_sale_price, item_adjustment_unit_price, item_quantity, deliveried_quantity, delivery_status, item_adjustment_total_price, third_refund_id, ref_sub_order_number, exist_exception_flag, sort_id, membership_system_id, partner_id, version, deleted, create_time, create_user_id, update_time, update_user_id, create_user_name, update_user_name)\
    VALUES({detail_id}, {ord_order_header_id}, {mbr_member_id}, 242163984629769, '{third_order_number}', 'CH00000002', '{third_refund_id}', NULL, 'HM00003008', 'TM10077268', 'duoKit', NULL,{item_sal_price}, 0.00000,{item_quantity}, NULL, NULL,{item_adjustment_total_price},{third_refund_id}, '{sub_order_number}', NULL, 100, 1, 1, 0, 0,'{now_time}', '10556826', '{now_time}', NULL, 'test', NULL);"
# 执行插入操作
dbStage.execute(insertOrderDetailSql)

# Step4：更新主单表的计算flag、退款金额、实付金额
updateOrderFlag = f"UPDATE member_domain.ord_order_header SET point_calculated_flag = NULL,refunded_amount = {refund_amount},order_total_amount = {order_total_amount},item_quantity={ord_item_quantity} WHERE order_number = '{third_order_number}'"
dbStage.execute(updateOrderFlag)
print("third_order_number:", third_order_number)
# 关闭连接
dbStage.close()
