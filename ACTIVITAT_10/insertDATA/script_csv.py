import pandas as pd
import create_and_insert as insert_data

def csv_to_json():
    df = pd.read_csv("paraules_temàtica_penjat.csv")
    d = df.to_dict(orient='list')

    return d

data = csv_to_json()

insert_data.create_table()

for i in range(500):
    insert_data.insert_record(i, data)