from func.getConn import getConn


class QuoInfo:
    def __init__(self, remark):

        self.remark = str(remark).strip()

        sqlq = 'select ' \
               'id_quotation, name_mer, name_custom, num_order, price_order, date_mer, date_order, name_order, ' \
               'fab_1_desc, fab_1_consume_custom, fab_1_consume_cost, fab_1_width, fab_1_raw_material_price, ' \
               'fab_1_weight, fab_1_calc_method, fab_1_cost_for_custom, fab_1_cost, fab_1_remark, ' \
               'fab_2_desc, fab_2_consume_custom, fab_2_consume_cost, fab_2_width, fab_2_raw_material_price, ' \
               'fab_2_weight, fab_2_calc_method, fab_2_cost_for_custom, fab_2_cost, fab_2_remark, ' \
               'fab_3_desc, fab_3_consume_custom, fab_3_consume_cost, fab_3_width, fab_3_raw_material_price, ' \
               'fab_3_weight, fab_3_calc_method, fab_3_cost_for_custom, fab_3_cost, fab_3_remark, ' \
               'fab_4_desc, fab_4_consume_custom, fab_4_consume_cost, fab_4_width, fab_4_raw_material_price,' \
               'fab_4_weight, fab_4_calc_method, fab_4_cost_for_custom, fab_4_cost, fab_4_remark, ' \
               'fab_5_desc, fab_5_consume_custom, fab_5_consume_cost, fab_5_width, fab_5_raw_material_price, ' \
               'fab_5_weight, fab_5_calc_method, fab_5_cost_for_custom, fab_5_cost, fab_5_remark, ' \
               'ass_1_item, ass_1_desc, ass_1_cost_for_custom, ass_1_cost, ' \
               'ass_2_item, ass_2_desc, ass_2_cost_for_custom, ass_2_cost, ' \
               'ass_3_item, ass_3_desc, ass_3_cost_for_custom, ass_3_cost, ' \
               'ass_4_item, ass_4_desc, ass_4_cost_for_custom, ass_4_cost, ' \
               'ass_5_item, ass_5_desc, ass_5_cost_for_custom, ass_5_cost, ' \
               'ass_6_item, ass_6_desc, ass_6_cost_for_custom, ass_6_cost, ' \
               'ass_7_item, ass_7_desc, ass_7_cost_for_custom, ass_7_cost, ' \
               'pack_desc, pack_custom, pack_cost, freight_desc, freight_custom, freight_cost, ' \
               'mini_price, price_workshop_offer, price_workshop_to_custom, price_workshop_pre_cost, ' \
               'cost_total_for_custom, cost_total_basic, extra_desc, ' \
               'profit_add_for_custom, profit_add_for_cost, quota_total_for_custom, cost_total, create_time ' \
               'from quotation_info ' \
               'where remark = "{}";'.format(self.remark)
        data = getConn().query1(sqlq)

        if data is None:
            [self.id_quotation, self.name_mer, self.name_custom, self.num_order,
             self.price_order, self.date_mer, self.date_order, self.name_order,
             self.fab_1_desc, self.fab_1_consume_custom, self.fab_1_consume_cost,
             self.fab_1_width, self.fab_1_raw_material_price, self.fab_1_weight, self.fab_1_calc_method,
             self.fab_1_cost_for_custom, self.fab_1_cost, self.fab_1_remark,
             self.fab_2_desc, self.fab_2_consume_custom, self.fab_2_consume_cost,
             self.fab_2_width, self.fab_2_raw_material_price, self.fab_2_weight, self.fab_2_calc_method,
             self.fab_2_cost_for_custom, self.fab_2_cost, self.fab_2_remark,
             self.fab_3_desc, self.fab_3_consume_custom, self.fab_3_consume_cost,
             self.fab_3_width, self.fab_3_raw_material_price, self.fab_3_weight, self.fab_3_calc_method,
             self.fab_3_cost_for_custom, self.fab_3_cost, self.fab_3_remark,
             self.fab_4_desc, self.fab_4_consume_custom, self.fab_4_consume_cost,
             self.fab_4_width, self.fab_4_raw_material_price, self.fab_4_weight, self.fab_4_calc_method,
             self.fab_4_cost_for_custom, self.fab_4_cost, self.fab_4_remark,
             self.fab_5_desc, self.fab_5_consume_custom, self.fab_5_consume_cost,
             self.fab_5_width, self.fab_5_raw_material_price, self.fab_5_weight, self.fab_5_calc_method,
             self.fab_5_cost_for_custom, self.fab_5_cost, self.fab_5_remark,
             self.ass_1_item, self.ass_1_desc, self.ass_1_cost_for_custom, self.ass_1_cost,
             self.ass_2_item, self.ass_2_desc, self.ass_2_cost_for_custom, self.ass_2_cost,
             self.ass_3_item, self.ass_3_desc, self.ass_3_cost_for_custom, self.ass_3_cost,
             self.ass_4_item, self.ass_4_desc, self.ass_4_cost_for_custom, self.ass_4_cost,
             self.ass_5_item, self.ass_5_desc, self.ass_5_cost_for_custom, self.ass_5_cost,
             self.ass_6_item, self.ass_6_desc, self.ass_6_cost_for_custom, self.ass_6_cost,
             self.ass_7_item, self.ass_7_desc, self.ass_7_cost_for_custom, self.ass_7_cost,
             self.pack_desc, self.pack_custom, self.pack_cost, self.freight_desc,
             self.freight_custom, self.freight_cost,
             self.mini_price, self.price_workshop_offer, self.price_workshop_to_custom, self.price_workshop_pre_cost,
             self.cost_total_for_custom, self.cost_total_basic, self.extra_desc,
             self.profit_add_for_custom, self.profit_add_for_cost, self.quota_total_for_custom,
             self.cost_total, self.quota_create_time] = [None] * 104
        else:
            [self.id_quotation, self.name_mer, self.name_custom, self.num_order,
             self.price_order, self.date_mer, self.date_order, self.name_order,
             self.fab_1_desc, self.fab_1_consume_custom, self.fab_1_consume_cost,
             self.fab_1_width, self.fab_1_raw_material_price, self.fab_1_weight, self.fab_1_calc_method,
             self.fab_1_cost_for_custom, self.fab_1_cost, self.fab_1_remark,
             self.fab_2_desc, self.fab_2_consume_custom, self.fab_2_consume_cost,
             self.fab_2_width, self.fab_2_raw_material_price, self.fab_2_weight, self.fab_2_calc_method,
             self.fab_2_cost_for_custom, self.fab_2_cost, self.fab_2_remark,
             self.fab_3_desc, self.fab_3_consume_custom, self.fab_3_consume_cost,
             self.fab_3_width, self.fab_3_raw_material_price, self.fab_3_weight, self.fab_3_calc_method,
             self.fab_3_cost_for_custom, self.fab_3_cost, self.fab_3_remark,
             self.fab_4_desc, self.fab_4_consume_custom, self.fab_4_consume_cost,
             self.fab_4_width, self.fab_4_raw_material_price, self.fab_4_weight, self.fab_4_calc_method,
             self.fab_4_cost_for_custom, self.fab_4_cost, self.fab_4_remark,
             self.fab_5_desc, self.fab_5_consume_custom, self.fab_5_consume_cost,
             self.fab_5_width, self.fab_5_raw_material_price, self.fab_5_weight, self.fab_5_calc_method,
             self.fab_5_cost_for_custom, self.fab_5_cost, self.fab_5_remark,
             self.ass_1_item, self.ass_1_desc, self.ass_1_cost_for_custom, self.ass_1_cost,
             self.ass_2_item, self.ass_2_desc, self.ass_2_cost_for_custom, self.ass_2_cost,
             self.ass_3_item, self.ass_3_desc, self.ass_3_cost_for_custom, self.ass_3_cost,
             self.ass_4_item, self.ass_4_desc, self.ass_4_cost_for_custom, self.ass_4_cost,
             self.ass_5_item, self.ass_5_desc, self.ass_5_cost_for_custom, self.ass_5_cost,
             self.ass_6_item, self.ass_6_desc, self.ass_6_cost_for_custom, self.ass_6_cost,
             self.ass_7_item, self.ass_7_desc, self.ass_7_cost_for_custom, self.ass_7_cost,
             self.pack_desc, self.pack_custom, self.pack_cost, self.freight_desc,
             self.freight_custom, self.freight_cost,
             self.mini_price, self.price_workshop_offer, self.price_workshop_to_custom, self.price_workshop_pre_cost,
             self.cost_total_for_custom, self.cost_total_basic, self.extra_desc,
             self.profit_add_for_custom, self.profit_add_for_cost, self.quota_total_for_custom,
             self.cost_total, self.quota_create_time] = data

