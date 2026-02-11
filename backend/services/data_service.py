import pandas as pd
import json

def load_prices():
    df = pd.read_csv("../data/prices.csv")
    return df.to_dict(orient="records")

def load_events():
    df = pd.read_csv("../data/events.csv")
    return df.to_dict(orient="records")

def load_changepoints():
    with open("../data/changepoints.json") as f:
        return json.load(f)
