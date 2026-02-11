import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)

    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df = df.sort_values("Date").reset_index(drop=True)

    return df


def compute_log_returns(df):
    df = df.copy()
    df["log_return"] = np.log(df["Price"]).diff()
    df = df.dropna().reset_index(drop=True)
    return df
