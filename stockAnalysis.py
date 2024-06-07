import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def analyze_stock(ticker, start_date, end_date):
    # 使用yfinance下载股票数据
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # 显示前几行数据
    print(stock_data.head())

    # 绘制收盘价走势图
    plt.figure(figsize=(12, 6))
    stock_data['Close'].plot(title=f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Close Price (USD)")
    plt.show()

    # 计算对数收益率 (日收益率)
    log_returns1 = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
    log_returns1 = log_returns1.dropna()

    # 显示对数收益率
    print(log_returns1.head())

    plt.figure(figsize=(12, 6))
    log_returns1.plot(title=f"{ticker} Stock Price Log Returns (Daily)")
    plt.xlabel("Date")
    plt.ylabel("Log Returns")
    plt.show()

    # 计算对数收益率 (月收益率)
    log_returns30 = np.log(stock_data['Close'] / stock_data['Close'].shift(30))
    log_returns30 = log_returns30.dropna()

    # 显示对数收益率
    print(log_returns30.head())

    plt.figure(figsize=(12, 6))
    log_returns30.plot(title=f"{ticker} Stock Price Log Returns (30 Days)")
    plt.xlabel("Date")
    plt.ylabel("Log Returns")
    plt.show()

    # 计算实现波动率
    volatility30 = np.sqrt(np.sum(log_returns30**2))
    
    # 打印波动率
    print(f"30-day Realized Volatility for {ticker}: {volatility30}")

analyze_stock("NVDA", "2020-01-01", "2024-06-07")