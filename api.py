from fastapi import FastAPI
import deta
from data_manipulation import data_manipulation

app = FastAPI()

INPUT_PATH = "../data/qutrix_chart_work.csv"
ds = data_manipulation(INPUT_PATH)

def data_iter():
    data = []
    col = ds.columns
    for i in range(len(ds)):
        response = {col[0]: ds[col[0]][i],
                    col[1]: ds[col[1]][i],
                    col[2]: str(ds[col[2]][i])}
        data.append(response)
    return data

@app.get("/api")
def apiQuery():
    data = data_iter()
    return data




    # unique_data = ds['Product Name'].unique()
    # return
