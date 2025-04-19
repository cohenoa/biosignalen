import os
import pandas as pd
import exceptions as e
import UIFunctions as UIf
import helpfunctions as hf
import validation as valid


def get_LGE_data(data_set_path: str):
    """
    The function reads Excel sheets ('L', 'G' and 'ErrorLimitLambda') from the specified file path and returns clear DataFrames without missing values.

    :param data_set_path: The path to the Excel file containing the data.
    :return: l_df (pandas.DataFrame): A DataFrame containing the data from the 'L' sheet.
             g_df (pandas.DataFrame): A DataFrame containing the data from the 'G' sheet.
             err_limit_lambda (float): The error limit lambda.
    """
    l_df = pd.read_excel(data_set_path, sheet_name='L').fillna(0)
    l_df['compound_name'] = l_df['compound_name'].apply(lambda x: 'CONTROL' if x == 0 else x)
    l_df['2D_3D'] = l_df['2D_3D'].apply(lambda x: '-0-' if x == 0 else x)
    l_df['dosage'] = l_df['dosage'].apply(lambda x: '-0-' if x == 0 else x)
    l_df['time'] = l_df['time'].apply(lambda x: '0hr' if x == 0 else x)

    if 0 in l_df['cell_line_name'].values:
        e.InvalidCellLineException("Cell line name has missing values")

    g_df = pd.read_excel(data_set_path, sheet_name='G').fillna(0)

    if 0 in g_df['UID'].values:
        e.InvalidUIDException("UID has missing values")

    err_limit_lambda = pd.read_excel(data_set_path, sheet_name='ErrorLimitLambda').columns.values[0]

    return l_df, g_df, err_limit_lambda


def important_L(l_df: pd.DataFrame, err_limit: float, threshold: int, new_sheet: bool = False,
                sheet_name: str = 'important_L', data_path: str = '') -> pd.DataFrame:
    """
    This function returns a DataFrame with only the important columns. An important column is determined by whether the
    number of cells whose value is higher in absolute value than the error limit, is greater than or equal to the threshold.

    :param l_df: The DataFrame to be checked.
    :param err_limit: The error limit.
    :param threshold: The number of significant values.
    :param new_sheet: If True, creates a new sheet. Default is False.
    :param sheet_name: The name of the sheet to be created. Default is 'important_L'.
    :param data_path: The path where the new sheet will be created. Default is an empty string.
    :return: The DataFrame with only the important columns selected.
    """
    valid.is_valid_L(l_df)
    if threshold < 0:
        raise e.NegativeNumberException("Threshold should be positive number")
    new_df = l_df.loc[:, :5].copy()
    col_names = l_df.columns.tolist()
    time_col_idx = col_names.index('time')
    analysis_cols = [c for c in col_names[time_col_idx + 1:]]

    for col in analysis_cols:
        count = 0
        for cell in l_df[col]:
            if abs(cell) > err_limit:
                count += 1
        if count >= threshold:
            new_df[col] = l_df[col].copy()

    if new_sheet:
        print(f"Creating '{sheet_name}'..")
        UIf.create_new_sheet(new_df, data_path, sheet_name)

    return new_df


def filter_by_col(df: pd.DataFrame, col: str, filter_list: list, new_sheet: bool = False,
                  sheet_name: str = 'filter_by_col', data_path: str = '') -> pd.DataFrame:
    """
    This function filters data by a certain column and by a list of values it receives.

    :param df: The DataFrame to filter.
    :param col: The column according to which the filtering will be performed.
    :param filter_list: A list of values that we would like to appear in the selected column.
    :param new_sheet: If True, creates a new sheet. Default is False.
    :param sheet_name: The name of the sheet to be created. Default is 'filter_by_col'.
    :param data_path: The path where the new sheet will be created. Default is an empty string.
    :return: The DataFrame after filtering.
    """
    valid.is_valid_L(df)
    filter_df = df.loc[(df[col].isin(filter_list))]
    if len(filter_df) == 0:
        print(f"There is no data to show by '{col}' filtering")

    if new_sheet:
        print(f"Creating '{sheet_name}'..")
        UIf.create_new_sheet(filter_df, data_path, sheet_name)

    return filter_df


def analyze_L(important_l: pd.DataFrame, err_limit_lambda: float, data_path: str, fixed_col: str = 'time',
              p_value: float = 0.05, save_path: str = os.getcwd()):
    """
    This function analyzes pairs of compounds in a dictionary of Pandas dataframes.

    :param important_l: The DataFrame with only the important columns.
    :param err_limit_lambda: The error limit lambda.
    :param data_path: The path where the original dataframes are stored.
    :param fixed_col: The name of the column that will remain fixed in each pair. Default is 'time'.
    :param p_value: The p-value threshold for determining whether the difference between means is significant. Default is 0.05.
    :param save_path: The path where the exported data and plots will be saved.
    :return: files with new information about sheet 'L' after the analysis.
    """
    cell_line_list = UIf.pop_up_cell_GUI(important_l)

    for cell_line in cell_line_list:
        control_list, inhibitor_list = [], []
        only_avg, control_treatment = True, False
        for file_iter in range(4):
            if file_iter == 1:
                only_avg = False
            elif file_iter == 2:
                control_treatment = True
            elif file_iter == 3:
                only_avg = True

            keys_to_remove, compound_names = [], []
            averages = {}
            cell_df = important_l.loc[important_l['cell_line_name'] == cell_line]
            if (len(control_list) == 0) and (len(inhibitor_list) == 0):
                control_list, inhibitor_list = UIf.pop_up_compound_GUI(cell_df, cell_line)
            pairs_dict, cl, il = hf.df_to_dict(cell_df, cell_line, control_list, inhibitor_list, control_treatment,
                                               fixed_col=fixed_col)

            sheet_name = UIf.get_sheet_name(cell_line, only_avg, control_treatment, fixed_col)
            print(f"Analyzing '{sheet_name}'..")

            for key, sub_df in pairs_dict.items():
                dfs_to_concat = []
                analysis_cols = hf.get_analysis_columns(sub_df)
                for process in analysis_cols:
                    df_first, df_second = hf.get_comparison_data(sub_df, key, process, cl, il, control_treatment,
                                                                 fixed_col)
                    df_with_res_row = hf.create_reason_dataframe(sub_df, process, p_value, df_first, df_second,
                                                                 err_limit_lambda)
                    if df_with_res_row is not None:
                        averages[process] = (df_first.mean(), df_second.mean())
                        dfs_to_concat.append(df_with_res_row)

                if len(dfs_to_concat) == 0:
                    keys_to_remove.append(key)
                else:
                    if only_avg:
                        dfs_to_concat, compound_names = hf.create_updated_dataframes(dfs_to_concat, averages, sub_df,
                                                                                     control_treatment, compound_names)

                    new_df = pd.concat(dfs_to_concat, axis=1)
                    new_df = new_df.reindex(sorted(new_df.columns), axis=1)

                    if only_avg:
                        pairs_dict[key] = hf.create_pairs_dataframe_only_avg(sub_df, new_df, control_treatment,
                                                                             fixed_col)
                    else:
                        pairs_dict[key] = hf.create_pairs_dataframe_all_data(sub_df, new_df)

            for key in keys_to_remove:
                pairs_dict.pop(key)

            if pairs_dict:
                pairs_df = hf.create_pairs_df(pairs_dict)
                UIf.export_data(file_iter, pairs_df, pairs_dict, cell_line, fixed_col, data_path, save_path, sheet_name)

            else:
                print(f"No interesting data found for '{sheet_name}'\n")


def analyze_G(g_df: pd.DataFrame, important_l: pd.DataFrame, data_path: str, save_path: str = os.getcwd(),
              edge_percents: float = 0.1):
    """
    This function accepts columns representing processes and sorts for each process its proteins.
    In addition, the function saves the plot of each process.

    :param g_df: The G_values DataFrame.
    :param important_l: The DataFrame with only the important columns to sort its G_values.
    :param data_path: The path where the original dataframes are stored.
    :param save_path: The path where the exported data and plots will be saved.
    :param edge_percents: The percentage of proteins to be considered as the edge for each process. The default is 0.1 (10%).
    :return: files with new information about sheet 'G' after the analysis.
    """
    valid.is_valid_path(data_path, directory=False)
    valid.is_valid_path(save_path)

    folder_name = UIf.get_folder_name(data_path)
    G_path = os.path.join(save_path, folder_name, 'G')
    graph_save_path = os.path.join(G_path, 'Graphs')

    cols = hf.get_analysis_columns(important_l)
    important_g = pd.DataFrame(columns=pd.MultiIndex.from_product([cols, ['UID', 'Effect']]))
    edges = pd.DataFrame(columns=pd.MultiIndex.from_product([cols, ['UID', 'Effect']]))

    names_g, values_g = {}, {}
    for col in important_g.columns:
        if col[1] == 'UID':
            names_g = g_df[col[1]].to_dict()
        else:
            values_g = g_df[col[0]].to_dict()
            sorted_values_g = dict(sorted(values_g.items(), key=lambda item: item[1]))
            list_values_g = list(sorted_values_g.values())

            sorted_names_g = dict(sorted(names_g.items(), key=lambda item: sorted_values_g[item[0]]))
            list_names_g = list(sorted_names_g.values())

            os.makedirs(graph_save_path, exist_ok=True)
            UIf.plot_G_values(f'Process {col[0]}', list_names_g, list_values_g, graph_save_path, edge_percents)

            lower_edges, lower_values, upper_edges, upper_values = hf.find_edges(list_names_g, list_values_g,
                                                                                 edge_percents)
            full_edges_list = lower_edges + upper_edges
            full_values_list = lower_values + upper_values

            edges[(col[0], 'UID')] = full_edges_list
            edges[col] = full_values_list

            important_g[(col[0], 'UID')] = list_names_g
            important_g[col] = list_values_g

    edges_save_path = os.path.join(G_path, 'edges.csv')
    important_g_save_path = os.path.join(G_path, 'sort_G.csv')

    edges.to_csv(edges_save_path, index=False)
    important_g.to_csv(important_g_save_path, index=False)
