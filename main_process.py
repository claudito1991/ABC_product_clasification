import pandas as pd
import classificationABC as cls


def main_process(file_path,art_col_name, descrip_col_name, vpd_col_name, stock_col_name, price_file_path,price_art_col_name, price_price_col_name ):
    base_dataframe = cls.load_dataset(file_path)
    df = cls.column_with_desired_data(base_dataframe, art_col_name, descrip_col_name, vpd_col_name, stock_col_name ,a='articulo',b='descripcion',c = 'vpd',d='stock')
    df = cls.delete_rows_from_df(df,'articulo',2731,2776,2705)
    df = cls.sorted_and_cumulative_df(df,'vpd','acumulado VPD')
    df = cls.vpd_weight(df,'acumulado VPD','Peso de VPD acum.')
    result_df = cls.abc_classification(df,'Peso de VPD acum.')  
    df_pc_raw = pd.read_excel(price_file_path, header = 1)
    df_pc_filtered = df_pc_raw[[price_art_col_name,price_price_col_name]]
    stock_classified_with_value = cls.stock_with_price(result_df,'articulo',df_pc_filtered,price_art_col_name,'Valorizado',price_price_col_name,'stock')
    stock_classified_with_value
    df_dict = cls.dataframe_dictionary(stock_classified_with_value,'categoria')
    return df_dict

    