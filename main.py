import oncosensepy as osp

if __name__ == '__main__':
    data_name = 'supp_data_26'
    data_set_path = r'Data/' + data_name + '.xlsx'

    l_df, g_df, err_limit_lambda = osp.get_LGE_data(data_set_path)

    important_l = osp.important_L(l_df, err_limit_lambda, 2,
                                  new_sheet=False,
                                  sheet_name='important_L',
                                  data_path=data_set_path)

    # filter_dosage = osp.filter_by_col(important_l, 'dosage', ['0.00001nm', '1nm', '40nm', '1uM'], new_sheet=False,
    #                                   sheet_name='important_L', data_path=data_set_path)
    #
    # filter_time = osp.filter_by_col(filter_dosage, 'time', ['0hr', '24hr'], new_sheet=False, sheet_name='important_L',
    #                                 data_path=data_set_path)
    #
    osp.analyze_G(g_df, important_l, data_set_path, edge_percents=0.1)

    osp.analyze_L(important_l, err_limit_lambda, data_set_path, fixed_col='time', p_value=0.05)
    # osp.analyze_L(important_l, err_limit_lambda, data_set_path, fixed_col='dosage', p_value=0.05) # delete # to activate
