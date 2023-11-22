import csv
import json
import os
import pandas as pd


path_file_1 = os.path.join("..", "data", "transactions.csv")
path_file_2 = os.path.join("..", "data", "transactions_excel.xlsx")
print(os.path.isfile(path_file_1))
print(os.path.isfile(path_file_2))


def get_read_csv(filepath: str):
    format_file = filepath[-4:]
    print(format_file)
    if "csv" in format_file:
        df_csv = pd.read_csv(filepath, delimiter=";", encoding="UTF-8")
        print(df_csv.columns)
        transactions_csv = df_csv.to_json(orient="records", force_ascii=False)
        print(transactions_csv)
    elif "xlsx" in format_file:
        df_xlsx = pd.read_excel(filepath)
        print(df_xlsx.columns)
        transactions_xlsx = df_xlsx.to_json(orient="records", force_ascii=False)
        print(transactions_xlsx)


get_read_csv(path_file_1)
get_read_csv(path_file_2)