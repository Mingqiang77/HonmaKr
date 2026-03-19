import time
from datetime import datetime
from db_config.db_config import dbStage

# 业务：honmaKr-stage插入会员订单

# 生成会员订单号函数
def generate_order_number():
    result = int(round(time.time() * 1000))
    return str(result) + "member"

# 会员ID列表
mbr_member_ids = [280074062397441,
281501124001793,
281501124001799,
281501124001804,
281501126098945,
281501126098947,
281501126098949,
281501126098954,
281501126098958,
281501128196099,
281501128196100,
281501128196101,
281501128196105,
281501128196106,
281501128196107,
281501130293251,
281501130293254,
281501132390402,
281501132390405,
281501132390407,
281501132390411,
281501134487555,
281501134487556,
281501134487561,
281501134487562,
281501134487563,
281501134487568,
281501134487579,
281501134487601,
281501136584705,
281501136584707,
281501136584714,
281501136584719,
281501136584721,
281501138681859,
281501138681862,
281501138681865,
281501138681866,
281501138681877,
281501138681891,
281501144973313,
281501144973316,
281501144973317,
281501144973323,
281501144973327,
281501144973332,
281501147070465,
281501147070466,
281501147070471,
281501147070472,
281501147070475,
281501147070480,
281501149167617,
281501149167620,
281501149167621,
281501149167623,
281501151264773,
281501151264774,
281501151264777,
281501151264789,
281501151264793,
281501151264802,
281501153361921,
281501153361924,
281501153361926,
281501153361928,
281501153361932,
281501153361935,
281501155459073,
281501155459076,
281501155459079,
281501155459080,
281501155459087,
281501155459089,
281501157556225,
281501157556226,
281501157556232,
281501157556233,
281501157556235,
281501157556239,
281501157556242,
281501159653377,
281501159653383,
281501159653388,
281501159653389,
281501159653392,
281501159653394,
281501161750529,
281501161750534,
281501161750537,
281501163847681,
281501163847682,
281501163847685,
281501163847687,
281501163847694,
281501163847695,
281501163847708,
281501165944833,
281501165944837,
281501165944838,
281501165944839,
281501165944844,
281501165944846,
281501165944849,
281501165944852,
281501165944881,
281501174333441,
281501176430593,
281501176430594,
281501176430595,
281501176430598,
281501176430609,
281501178527747,
281501178527749,
281501178527762
]

amount = 500  # 订单总金额
store_id = 2   # 店铺id
store_code = 'ARF'  # 店铺code
channel_code = 'HonmaKrOffline'  # 渠道code
channel_id = '208818057248769'   # 渠道id
status = "TRADE_FINISHED"   # 订单状态
order_time = "2024-06-01 12:00:00"   # 下单时间

# 子单相关字段
item_sale_price = 100    # 单价
item_quantity = 5  # 购买sku数量
item_adjustment_price = item_sale_price * item_quantity  # 购买sku总价
mst_sku_id = '276271584509953'
item_sku_code = 'HM2407030002'
item_category = 'HonmaKrSkuCategory'   # 品类code

# 获取当前时间
now = datetime.now()
# 格式化时间为年月日时分秒
now_time = now.strftime('%Y-%m-%d %H:%M:%S')

for mbr_member_id in mbr_member_ids:
    # 生成会员订单号
    tid = generate_order_number()
    print("订单号:", tid)

    # 订单主表主键最大值+1
    max_ord_order_header_id = dbStage.query("SELECT max(id) as max_ord_order_header_id from member_domain.ord_order_header")
    ord_max_id = max_ord_order_header_id[0]['max_ord_order_header_id']
    ord_id = int(ord_max_id) + 1

    # 子单表主键最大值+1
    max_ord_order_detail_id = dbStage.query("SELECT max(id) as max_ord_header_detail_id from member_domain.ord_order_detail")
    detail_max_id = max_ord_order_detail_id[0]['max_ord_header_detail_id']
    detail_id = int(detail_max_id) + 1

    # 插入主单
    insertsql = f"""
    INSERT INTO member_domain.ord_order_header
    (id, mbr_member_id, activity_id, order_number, return_service_flag, original_top_order_number, third_order_number, channel_id, channel_code, store_id, store_code, member_name, member_code, country, province, city, district, mobile, progress_step, order_time, order_operated_type, order_saled_type, order_status, third_order_status, expected_delivery_time, expected_arrival_time, actual_delivery_time, actual_arrival_time, payment_time, trade_end_time, audit_mode, audit_status, audit_time, cancel_time, canceled_reason, payment_status, refund_status, delivery_status, delivery_order_count, shipping_type, shipping_status, shipping_specified_mode, shipping_payment_mode, need_invoice_flag, buyer_memo, seller_comment, item_quantity, product_total_amount, promotion_adjustment_total_amount, coupon_adjustment_total_amount, adjustment_total_amount, origin_freight_fee, freight_fee, payble_amount, order_total_amount, payed_amount, refunded_amount, basic_status, platform_source, packing_box_flag, packing_box_price, expected_ware_house, expected_logistics_express, order_trading_tag, trading_next_time, merge_flag, seller_flag, point_need_calculate_time, point_calculated_flag, point_calculate_time, try_calculate_times, exist_skip_calc_point_coupon_flag, ba_no, coupon_no, relate_order_header_id, relate_order_number, relate_third_order_number, sort_id, membership_system_id, partner_id, version, deleted, create_time, create_user_id, update_time, update_user_id, create_user_name, update_user_name)
    VALUES({ord_id}, {mbr_member_id}, NULL, '{tid}', 0, NULL, '{tid}', '{channel_id}', '{channel_code}', '{store_id}', '{store_code}', NULL, 'GX20240701001', NULL, NULL, NULL, NULL, NULL, 0, '{order_time}', 1, 11, 1, 'TRADE_FINISHED', NULL, NULL, NULL, NULL, '{order_time}', '{order_time}', 1, 0, NULL, NULL, NULL, 1, 0, 1, 0, 13, 1, 0, 11, 0, NULL, NULL, {item_quantity}, NULL, 0.00000, NULL, 0.00000, 0.00000, 0.00000, {amount}, {amount}, {amount}, 0.00000, 0, 'memberHub', 0, NULL, NULL, NULL, NULL, '2023-08-15 16:50:53', 0, 0, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 100, 1, 1, 0, 0, '{now_time}', '60073', '{now_time}', NULL, 'mqTest', 'mqTest');
    """
    dbStage.execute(insertsql)

    # 插入明细单
    sqldetail = f"""
    INSERT INTO member_domain.ord_order_detail
    (id, ord_order_header_id, mbr_member_id, mst_sku_id, third_order_number, channel_code, sub_order_number, item_name, item_product_code, item_sku_code, item_category, item_size, item_sale_price, item_adjustment_unit_price, item_quantity, deliveried_quantity, delivery_status, item_adjustment_total_price, third_refund_id, ref_sub_order_number, exist_exception_flag, sort_id, membership_system_id, partner_id, version, deleted, create_time, create_user_id, update_time, update_user_id, create_user_name, update_user_name)
    VALUES({detail_id}, {ord_id}, {mbr_member_id}, {mst_sku_id}, '{tid}', '{channel_code}', '{tid}', NULL, 'HM00003008', '{item_sku_code}', '{item_category}', NULL, {item_sale_price}, 0.00000, {item_quantity}, NULL, NULL, {item_adjustment_price}, NULL, NULL, NULL, 100, 1, 1, 0, 0, '{now_time}', '10556826', '{now_time}', NULL, 'mqTest', 'mqTest');
    """
    dbStage.execute(sqldetail)

# 关闭数据库连接
dbStage.close()