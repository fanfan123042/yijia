from func.getConn import getConn


class BomItemPurchaseData:
    def __init__(self, remark, item):
        self.remark = str(remark).strip()
        self.item = str(item).strip()

        sql = 'select ' \
              'id_purchase, purchase_method, data_from, vat_rate, calculate_method, ' \
              'calculate_same_color, calculate_same_consume, calculate_same_wastage, ' \
              'calculate_same_raw_price, calculate_same_width, calculate_same_weight, ' \
              'date_inspection, date_launching_test, ' \
              'custom_color_1_desc, material_color_1_desc, purchase_width_1, purchase_consume_1, ' \
              'purchase_wastage_cut_1, purchase_wastage_shrink_1, purchase_wastage_num_1, ' \
              'purchase_weight_1, purchase_raw_price_1, purchase_suggest_num_1, purchase_suggest_amount_1, ' \
              'purchase_num_1, purchase_amount_1, purchase_back_num_1, purchase_back_amount_1, ' \
              'num_used_before_bulk_1, change_rate_1, bulk_weight_1, bulk_width_1, bulk_consume_1, ' \
              'num_cut_pre_1, rate_with_num_order_1, num_cut_1, surplus_raw_1, ' \
              'custom_color_2_desc, material_color_2_desc, purchase_width_2, purchase_consume_2, ' \
              'purchase_wastage_cut_2, purchase_wastage_shrink_2, purchase_wastage_num_2, ' \
              'purchase_weight_2, purchase_raw_price_2, purchase_suggest_num_2, purchase_suggest_amount_2, ' \
              'purchase_num_2, purchase_amount_2, purchase_back_num_2, purchase_back_amount_2, ' \
              'num_used_before_bulk_2, change_rate_2, bulk_weight_2, bulk_width_2, bulk_consume_2, ' \
              'num_cut_pre_2, rate_with_num_order_2, num_cut_2, surplus_raw_2, ' \
              'custom_color_3_desc, material_color_3_desc, purchase_width_3, purchase_consume_3, ' \
              'purchase_wastage_cut_3, purchase_wastage_shrink_3, purchase_wastage_num_3, ' \
              'purchase_weight_3, purchase_raw_price_3, purchase_suggest_num_3, purchase_suggest_amount_3, ' \
              'purchase_num_3, purchase_amount_3, purchase_back_num_3, purchase_back_amount_3, ' \
              'num_used_before_bulk_3, change_rate_3, bulk_weight_3, bulk_width_3, bulk_consume_3, ' \
              'num_cut_pre_3, rate_with_num_order_3, num_cut_3, surplus_raw_3, ' \
              'custom_color_4_desc, material_color_4_desc, purchase_width_4, purchase_consume_4, ' \
              'purchase_wastage_cut_4, purchase_wastage_shrink_4, purchase_wastage_num_4, ' \
              'purchase_weight_4, purchase_raw_price_4, purchase_suggest_num_4, purchase_suggest_amount_4, ' \
              'purchase_num_4, purchase_amount_4, purchase_back_num_4, purchase_back_amount_4, ' \
              'num_used_before_bulk_4, change_rate_4, bulk_weight_4, bulk_width_4, bulk_consume_4, ' \
              'num_cut_pre_4, rate_with_num_order_4, num_cut_4, surplus_raw_4, ' \
              'custom_color_5_desc, material_color_5_desc, purchase_width_5, purchase_consume_5, ' \
              'purchase_wastage_cut_5, purchase_wastage_shrink_5, purchase_wastage_num_5, ' \
              'purchase_weight_5, purchase_raw_price_5, purchase_suggest_num_5, purchase_suggest_amount_5, ' \
              'purchase_num_5, purchase_amount_5, purchase_back_num_5, purchase_back_amount_5, ' \
              'num_used_before_bulk_5, change_rate_5, bulk_weight_5, bulk_width_5, bulk_consume_5, ' \
              'num_cut_pre_5, rate_with_num_order_5, num_cut_5, surplus_raw_5, ' \
              'purchase_remark, purchase_suggest_num, purchase_suggest_amount, purchase_num, ' \
              'purchase_amount, purchase_back_num, purchase_back_amount, num_used_before_bulk, num_cut_pre, ' \
              'rate_with_num_order, num_cut, surplus_raw, ' \
              'amount_addition, amount_deduction, purchase_amount_all, unit_price_num_order, ' \
              'unit_price_num_order_without_vat, unit_price_num_cut, unit_price_num_cut_without_vat, ' \
              'unit_price_num_ship, unit_price_num_ship_without_vat, profit_unit_price_num_order, ' \
              'profit_amount_num_order, profit_unit_price_num_cut, profit_amount_num_cut, ' \
              'profit_unit_price_num_ship, profit_amount_num_ship, update_time, create_time, updater, ' \
              'purchase_amount_all_without_vat ' \
              'from plat225.bom_purchase ' \
              'where remark = "{}" and item = "{}";'.format(self.remark, self.item)

        data = getConn().query1(sql)
        if data is None:
            [self.id_purchase, self.purchase_method, self.data_from, self.vat_rate, self.calculate_method,
             self.calculate_same_color, self.calculate_same_consume, self.calculate_same_wastage,
             self.calculate_same_raw_price, self.calculate_same_width,
             self.calculate_same_weight, self.date_inspection, self.date_launching_test,
             self.custom_color_1_desc, self.material_color_1_desc, self.purchase_width_1, self.purchase_consume_1,
             self.purchase_wastage_cut_1, self.purchase_wastage_shrink_1, self.purchase_wastage_num_1,
             self.purchase_weight_1, self.purchase_raw_price_1, self.purchase_suggest_num_1,
             self.purchase_suggest_amount_1, self.purchase_num_1, self.purchase_amount_1, self.purchase_back_num_1,
             self.purchase_back_amount_1, self.num_used_before_bulk_1, self.change_rate_1, self.bulk_weight_1,
             self.bulk_width_1, self.bulk_consume_1, self.num_cut_pre_1, self.rate_with_num_order_1,
             self.num_cut_1, self.surplus_raw_1,
             self.custom_color_2_desc, self.material_color_2_desc, self.purchase_width_2, self.purchase_consume_2,
             self.purchase_wastage_cut_2, self.purchase_wastage_shrink_2, self.purchase_wastage_num_2,
             self.purchase_weight_2, self.purchase_raw_price_2, self.purchase_suggest_num_2,
             self.purchase_suggest_amount_2, self.purchase_num_2, self.purchase_amount_2, self.purchase_back_num_2,
             self.purchase_back_amount_2, self.num_used_before_bulk_2, self.change_rate_2, self.bulk_weight_2,
             self.bulk_width_2, self.bulk_consume_2, self.num_cut_pre_2, self.rate_with_num_order_2,
             self.num_cut_2, self.surplus_raw_2,
             self.custom_color_3_desc, self.material_color_3_desc, self.purchase_width_3, self.purchase_consume_3,
             self.purchase_wastage_cut_3, self.purchase_wastage_shrink_3, self.purchase_wastage_num_3,
             self.purchase_weight_3, self.purchase_raw_price_3, self.purchase_suggest_num_3,
             self.purchase_suggest_amount_3, self.purchase_num_3, self.purchase_amount_3, self.purchase_back_num_3,
             self.purchase_back_amount_3, self.num_used_before_bulk_3, self.change_rate_3, self.bulk_weight_3,
             self.bulk_width_3, self.bulk_consume_3, self.num_cut_pre_3, self.rate_with_num_order_3,
             self.num_cut_3, self.surplus_raw_3,
             self.custom_color_4_desc, self.material_color_4_desc, self.purchase_width_4, self.purchase_consume_4,
             self.purchase_wastage_cut_4, self.purchase_wastage_shrink_4, self.purchase_wastage_num_4,
             self.purchase_weight_4, self.purchase_raw_price_4, self.purchase_suggest_num_4,
             self.purchase_suggest_amount_4, self.purchase_num_4, self.purchase_amount_4, self.purchase_back_num_4,
             self.purchase_back_amount_4, self.num_used_before_bulk_4, self.change_rate_4, self.bulk_weight_4,
             self.bulk_width_4, self.bulk_consume_4, self.num_cut_pre_4, self.rate_with_num_order_4,
             self.num_cut_4, self.surplus_raw_4,
             self.custom_color_5_desc, self.material_color_5_desc, self.purchase_width_5, self.purchase_consume_5,
             self.purchase_wastage_cut_5, self.purchase_wastage_shrink_5, self.purchase_wastage_num_5,
             self.purchase_weight_5, self.purchase_raw_price_5, self.purchase_suggest_num_5,
             self.purchase_suggest_amount_5, self.purchase_num_5, self.purchase_amount_5, self.purchase_back_num_5,
             self.purchase_back_amount_5, self.num_used_before_bulk_5, self.change_rate_5, self.bulk_weight_5,
             self.bulk_width_5, self.bulk_consume_5, self.num_cut_pre_5, self.rate_with_num_order_5,
             self.num_cut_5, self.surplus_raw_5,
             self.purchase_remark, self.purchase_suggest_num, self.purchase_suggest_amount, self.purchase_num,
             self.purchase_amount, self.purchase_back_num, self.purchase_back_amount,
             self.num_used_before_bulk, self.num_cut_pre, self.rate_with_num_order, self.num_cut, self.surplus_raw,
             self.amount_addition, self.amount_deduction, self.purchase_amount_all, self.unit_price_num_order,
             self.unit_price_num_order_without_vat, self.unit_price_num_cut, self.unit_price_num_cut_without_vat,
             self.unit_price_num_ship, self.unit_price_num_ship_without_vat, self.profit_unit_price_num_order,
             self.profit_amount_num_order, self.profit_unit_price_num_cut, self.profit_amount_num_cut,
             self.profit_unit_price_num_ship, self.profit_amount_num_ship,
             self.update_time, self.create_time, self.updater, self.purchase_amount_all_without_vat] = [None] * 164

        else:
            [self.id_purchase, self.purchase_method, self.data_from, self.vat_rate, self.calculate_method,
             self.calculate_same_color, self.calculate_same_consume, self.calculate_same_wastage,
             self.calculate_same_raw_price, self.calculate_same_width,
             self.calculate_same_weight, self.date_inspection, self.date_launching_test,
             self.custom_color_1_desc, self.material_color_1_desc, self.purchase_width_1, self.purchase_consume_1,
             self.purchase_wastage_cut_1, self.purchase_wastage_shrink_1, self.purchase_wastage_num_1,
             self.purchase_weight_1, self.purchase_raw_price_1, self.purchase_suggest_num_1,
             self.purchase_suggest_amount_1, self.purchase_num_1, self.purchase_amount_1, self.purchase_back_num_1,
             self.purchase_back_amount_1, self.num_used_before_bulk_1, self.change_rate_1, self.bulk_weight_1,
             self.bulk_width_1, self.bulk_consume_1, self.num_cut_pre_1, self.rate_with_num_order_1,
             self.num_cut_1, self.surplus_raw_1,
             self.custom_color_2_desc, self.material_color_2_desc, self.purchase_width_2, self.purchase_consume_2,
             self.purchase_wastage_cut_2, self.purchase_wastage_shrink_2, self.purchase_wastage_num_2,
             self.purchase_weight_2, self.purchase_raw_price_2, self.purchase_suggest_num_2,
             self.purchase_suggest_amount_2, self.purchase_num_2, self.purchase_amount_2, self.purchase_back_num_2,
             self.purchase_back_amount_2, self.num_used_before_bulk_2, self.change_rate_2, self.bulk_weight_2,
             self.bulk_width_2, self.bulk_consume_2, self.num_cut_pre_2, self.rate_with_num_order_2,
             self.num_cut_2, self.surplus_raw_2,
             self.custom_color_3_desc, self.material_color_3_desc, self.purchase_width_3, self.purchase_consume_3,
             self.purchase_wastage_cut_3, self.purchase_wastage_shrink_3, self.purchase_wastage_num_3,
             self.purchase_weight_3, self.purchase_raw_price_3, self.purchase_suggest_num_3,
             self.purchase_suggest_amount_3, self.purchase_num_3, self.purchase_amount_3, self.purchase_back_num_3,
             self.purchase_back_amount_3, self.num_used_before_bulk_3, self.change_rate_3, self.bulk_weight_3,
             self.bulk_width_3, self.bulk_consume_3, self.num_cut_pre_3, self.rate_with_num_order_3,
             self.num_cut_3, self.surplus_raw_3,
             self.custom_color_4_desc, self.material_color_4_desc, self.purchase_width_4, self.purchase_consume_4,
             self.purchase_wastage_cut_4, self.purchase_wastage_shrink_4, self.purchase_wastage_num_4,
             self.purchase_weight_4, self.purchase_raw_price_4, self.purchase_suggest_num_4,
             self.purchase_suggest_amount_4, self.purchase_num_4, self.purchase_amount_4, self.purchase_back_num_4,
             self.purchase_back_amount_4, self.num_used_before_bulk_4, self.change_rate_4, self.bulk_weight_4,
             self.bulk_width_4, self.bulk_consume_4, self.num_cut_pre_4, self.rate_with_num_order_4,
             self.num_cut_4, self.surplus_raw_4,
             self.custom_color_5_desc, self.material_color_5_desc, self.purchase_width_5, self.purchase_consume_5,
             self.purchase_wastage_cut_5, self.purchase_wastage_shrink_5, self.purchase_wastage_num_5,
             self.purchase_weight_5, self.purchase_raw_price_5, self.purchase_suggest_num_5,
             self.purchase_suggest_amount_5, self.purchase_num_5, self.purchase_amount_5, self.purchase_back_num_5,
             self.purchase_back_amount_5, self.num_used_before_bulk_5, self.change_rate_5, self.bulk_weight_5,
             self.bulk_width_5, self.bulk_consume_5, self.num_cut_pre_5, self.rate_with_num_order_5,
             self.num_cut_5, self.surplus_raw_5,
             self.purchase_remark, self.purchase_suggest_num, self.purchase_suggest_amount, self.purchase_num,
             self.purchase_amount, self.purchase_back_num, self.purchase_back_amount,
             self.num_used_before_bulk, self.num_cut_pre, self.rate_with_num_order, self.num_cut, self.surplus_raw,
             self.amount_addition, self.amount_deduction, self.purchase_amount_all, self.unit_price_num_order,
             self.unit_price_num_order_without_vat, self.unit_price_num_cut, self.unit_price_num_cut_without_vat,
             self.unit_price_num_ship, self.unit_price_num_ship_without_vat, self.profit_unit_price_num_order,
             self.profit_amount_num_order, self.profit_unit_price_num_cut, self.profit_amount_num_cut,
             self.profit_unit_price_num_ship, self.profit_amount_num_ship,
             self.update_time, self.create_time, self.updater, self.purchase_amount_all_without_vat] = data


if __name__ == '__main__':
    items = BomItemPurchaseData('PF2104PF2104002', '【f1】')
    print(items.item, items.num_cut, items.bulk_width_1)

