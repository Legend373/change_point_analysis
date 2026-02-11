import matplotlib.pyplot as plt

def plot_price(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["Price"])
    plt.title("Brent Oil Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()


def plot_returns(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["log_return"])
    plt.title("Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.show()
