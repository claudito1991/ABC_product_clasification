import pandas as pd
import xlsxwriter


def load_dataset(path, header=0):
    df = pd.read_excel(path, header=header)
    return df


def column_with_desired_data(
    raw_dataframe, art, descrip, vpd, stock, a="", b="", c="", d=""
):
    result_df = raw_dataframe[[art, descrip, vpd, stock]]
    if a != "":
        result_df = result_df.rename(columns={art: a})

    if b != "":
        result_df = result_df.rename(columns={descrip: b})

    if c != "":
        result_df = result_df.rename(columns={vpd: c})

    if d != "":
        result_df = result_df.rename(columns={stock: d})

    return result_df


def sorted_and_cumulative_df(df, column_to_sort, cum_name):
    df = df.sort_values(column_to_sort, ascending=False)
    df[cum_name] = df[column_to_sort].cumsum()
    return df


def vpd_weight(df, cum_column, weights_name):
    total_vpd = list(df[cum_column])[-1]
    df[weights_name] = df[cum_column].apply(lambda x: (x / total_vpd) * 100)
    return df


def compare_with_limits(x, a, b):
    if x <= a:
        return "A"
    elif x <= b and x > a:
        return "B"
    else:
        return "C"


def abc_classification(df, weights_column, a=80, b=95, category_col_name="categoria"):
    df[category_col_name] = df[weights_column].apply(
        lambda x: compare_with_limits(x, a, b)
    )
    return df


def dataframe_dictionary(complete_dataframe, category_column):
    dict_df = {}
    dict_df["A"] = complete_dataframe[complete_dataframe[category_column] == "A"]
    dict_df["B"] = complete_dataframe[complete_dataframe[category_column] == "B"]
    dict_df["C"] = complete_dataframe[complete_dataframe[category_column] == "C"]
    return dict_df


def stock_with_price(
    df1, column_df1, df2, column_df2, value_column, price_column_name, stock_column_name
):
    df1 = df1.set_index(column_df1)
    df2 = df2.set_index(column_df2)
    result = pd.concat([df1, df2], axis=1, join="inner")
    result[value_column] = result[price_column_name] * result[stock_column_name]
    result[value_column] = result[value_column].apply(lambda x: int(x))
    return result


def delete_rows_from_df(df, article_column, *args):
    for i in args:
        df = df[df[article_column] != i]
    return df


def export_excel(df_dict, df_stats, file_name):
    writer = pd.ExcelWriter(file_name + ".xlsx", engine="xlsxwriter")

    for i in df_dict:
        df_dict[i].to_excel(writer, sheet_name=i)
        workbook = writer.book
        worksheet = writer.sheets[i]
        cell_format = workbook.add_format({"border": 1})

        for j in range(140):
            worksheet.set_row(j, 25, cell_format)
            worksheet.set_column(j, width=10, last_col=12)
            if j == 2:
                worksheet.set_column(j, width=42, last_col=12)
    df_stats.to_excel(writer, sheet_name="Stats")
    workbook = writer.book
    worksheet = writer.sheets[i]
    cell_format = workbook.add_format({"border": 1})
    writer.close()


def abc_statistics(complete_dataframe, classification_column, value_column, a=80, b=95):
    total_value = complete_dataframe[value_column].sum()
    lista_df = []

    category_list = ["A", "B", "C"]

    for i in category_list:
        aux_list = []
        aux_list.append(i)
        aux_list.append(
            complete_dataframe[complete_dataframe[classification_column] == i][
                value_column
            ].sum()
        )
        aux_list.append(
            round(
                complete_dataframe[complete_dataframe[classification_column] == i][
                    value_column
                ].sum()
                / total_value
                * 100,
                2,
            )
        )
        if i == "A":
            aux_list.append(a)
        elif i == "B":
            aux_list.append(b - a)
        else:
            aux_list.append(100 - b)
        lista_df.append(aux_list)

    df_stats = pd.DataFrame(lista_df)
    df_stats = df_stats.rename(
        columns={
            0: "Categoría",
            1: "Valorizado",
            2: "Peso porcentual(%)",
            3: "Target peso porcentual(%)",
        }
    )
    return df_stats
