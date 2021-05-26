import pandas as pd

def data_manipulation(data):
    ds = pd.read_csv(data)
    ds.rename(columns={'Date;': 'Date', 'Product Name;': 'Product Name'}, inplace=True)
    ds['Date'] = [x[:-1] for x in ds['Date']]
    ds['Product Name'] = [x[:-1] for x in ds['Product Name']]
    return ds