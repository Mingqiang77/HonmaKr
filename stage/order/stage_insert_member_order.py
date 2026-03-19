import time
from datetime import datetime

from db_config.db_config import dbStage


ORDER_NUMBER_SUFFIX = "member"
SUB_ORDER_SUFFIX = "subOrderNumber"
ORDER_NUMBER_MULTIPLIER = 1000
SUB_ORDER_MULTIPLIER = 100

MEMBER_ID = 290737047011329
AMOUNT = 1000
STORE_ID = 2
STORE_CODE = "ARF"
CHANNEL_CODE = "HonmaKrOffline"
CHANNEL_ID = "208818057248769"
ORDER_STATUS = "TRADE_FINISHED"
ORDER_TIME = "2024-06-13 13:00:00"

ITEM_SALE_PRICE = 1000
ITEM_QUANTITY = 1
ITEM_ADJUSTMENT_PRICE = ITEM_SALE_PRICE * ITEM_QUANTITY
MST_SKU_ID = "281694293393409"
ITEM_SKU_CODE = "mqTest0802002"
ITEM_CATEGORY = "SC0002"

HEADER_ID_SQL = (
    "SELECT max(id) as max_ord_order_header_id "
    "from member_domain.ord_order_header"
)
DETAIL_ID_SQL = (
    "SELECT max(id) as max_ord_header_detail_id "
    "from member_domain.ord_order_detail"
)


def generate_order_number(suffix, multiplier):
    return f"{int(round(time.time() * multiplier))}{suffix}"


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_next_order_ids():
    order_row = dbStage.query(HEADER_ID_SQL)
    detail_row = dbStage.query(DETAIL_ID_SQL)

    order_id = int(order_row[0]["max_ord_order_header_id"]) + 1
    detail_id = int(detail_row[0]["max_ord_header_detail_id"]) + 1
    return order_id, detail_id


def build_order_header_sql(order_id, order_number, current_time):
    return f"""
    INSERT INTO member_domain.ord_order_header
    (id, mbr_member_id, activity_id, order_number, return_service_flag, original_top_order_number, third_order_number, channel_id, channel_code, store_id, store_code, member_name, member_code, country, province, city, district, mobile, progress_step, order_time, order_operated_type, order_saled_type, order_status, third_order_status, expected_delivery_time, expected_arrival_time, actual_delivery_time, actual_arrival_time, payment_time, trade_end_time, audit_mode, audit_status, audit_time, cancel_time, canceled_reason, payment_status, refund_status, delivery_status, delivery_order_count, shipping_type, shipping_status, shipping_specified_mode, shipping_payment_mode, need_invoice_flag, buyer_memo, seller_comment, item_quantity, product_total_amount, promotion_adjustment_total_amount, coupon_adjustment_total_amount, adjustment_total_amount, origin_freight_fee, freight_fee, payble_amount, order_total_amount, payed_amount, refunded_amount, basic_status, platform_source, packing_box_flag, packing_box_price, expected_ware_house, expected_logistics_express, order_trading_tag, trading_next_time, merge_flag, seller_flag, point_need_calculate_time, point_calculated_flag, point_calculate_time, try_calculate_times, exist_skip_calc_point_coupon_flag, ba_no, coupon_no, relate_order_header_id, relate_order_number, relate_third_order_number, sort_id, membership_system_id, partner_id, version, deleted, create_time, create_user_id, update_time, update_user_id, create_user_name, update_user_name)
    VALUES({order_id}, {MEMBER_ID}, NULL, '{order_number}', 0, NULL, '{order_number}', '{CHANNEL_ID}', '{CHANNEL_CODE}', '{STORE_ID}', '{STORE_CODE}', NULL, 'GX20240701001', NULL, NULL, NULL, NULL, NULL, 0, '{ORDER_TIME}', 1, 11, 1, '{ORDER_STATUS}', NULL, NULL, NULL, NULL, '{ORDER_TIME}', '{ORDER_TIME}', 1, 0, NULL, NULL, NULL, 1, 0, 1, 0, 13, 1, 0, 11, 0, NULL, NULL, {ITEM_QUANTITY}, NULL, 0.00000, NULL, 0.00000, 0.00000, 0.00000, {AMOUNT}, {AMOUNT}, {AMOUNT}, 0.00000, 0, 'memberHub', 0, NULL, NULL, NULL, NULL, '2023-08-15 16:50:53', 0, 0, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, 100, 1, 1, 0, 0, '{current_time}', '60073', '{current_time}', NULL, 'mqTest', 'mqTest');
    """.strip()


def build_order_detail_sql(detail_id, order_id, order_number, sub_order_number, current_time):
    return f"""
    INSERT INTO member_domain.ord_order_detail
    (id, ord_order_header_id, mbr_member_id, mst_sku_id, third_order_number, channel_code, sub_order_number, item_name, item_product_code, item_sku_code, item_category, item_size, item_sale_price, item_adjustment_unit_price, item_quantity, deliveried_quantity, delivery_status, item_adjustment_total_price, third_refund_id, ref_sub_order_number, exist_exception_flag, sort_id, membership_system_id, partner_id, version, deleted, create_time, create_user_id, update_time, update_user_id, create_user_name, update_user_name)
    VALUES({detail_id}, {order_id}, {MEMBER_ID}, {MST_SKU_ID}, '{order_number}', '{CHANNEL_CODE}', '{sub_order_number}', NULL, 'HM00003008', '{ITEM_SKU_CODE}', '{ITEM_CATEGORY}', NULL, {ITEM_SALE_PRICE}, 0.00000, {ITEM_QUANTITY}, NULL, NULL, {ITEM_ADJUSTMENT_PRICE}, NULL, NULL, NULL, 100, 1, 1, 0, 0, '{current_time}', '10556826', '{current_time}', NULL, 'mqTest', 'mqTest');
    """.strip()


def insert_member_order():
    order_number = generate_order_number(ORDER_NUMBER_SUFFIX, ORDER_NUMBER_MULTIPLIER)
    sub_order_number = generate_order_number(SUB_ORDER_SUFFIX, SUB_ORDER_MULTIPLIER)
    current_time = get_current_time()
    order_id, detail_id = get_next_order_ids()

    print("order_number ==>", order_number)
    print("sub_order_number ==>", sub_order_number)

    header_sql = build_order_header_sql(order_id, order_number, current_time)
    detail_sql = build_order_detail_sql(
        detail_id=detail_id,
        order_id=order_id,
        order_number=order_number,
        sub_order_number=order_number,
        current_time=current_time,
    )

    dbStage.execute(header_sql)
    dbStage.execute(detail_sql)

    # Keep the generated sub-order number for optional future detail inserts.
    # detail_sql_2 = build_order_detail_sql(
    #     detail_id=detail_id + 1,
    #     order_id=order_id,
    #     order_number=order_number,
    #     sub_order_number=sub_order_number,
    #     current_time=current_time,
    # )
    # dbStage.execute(detail_sql_2)

    dbStage.close()


if __name__ == "__main__":
    insert_member_order()
