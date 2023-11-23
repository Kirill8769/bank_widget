import csv
import json
import os

import pandas as pd

path_file_1 = os.path.join("data", "transactions.csv")
path_file_2 = os.path.join("data", "transactions_excel.xlsx")
print(os.path.isfile(path_file_1))
print(os.path.isfile(path_file_2))
print(os.getcwd())
