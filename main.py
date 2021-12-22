# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:57:33 2021

Tutorial of plotly candlestick
link to tutorial:
    youtube.com/watch?v=jRZEBat_n7c&list=PLj_dto2iVEP6eWSYjbBzhFccqy4u2HO52&index=7&t=10s
You can find the data at https://www.cryptodatadownload.com/data/bitstamp/
 - BTC/USD daily
 
 Run with terminal $python main.py
@author: moazi
"""

import pandas as pd
import plotly.graph_objs as go


def format_data(df):
    # reverse time axis in asceding order
    df = df.iloc[::-1]
    # change from UTC to pd.datetime
    df['date'] = pd.to_datetime(df['date'])
    # add in 20 week moving average
    df['20WMA'] = df['close'].rolling(window=140).mean()
    
    return df
    

def genFigure(df):
    # gen candle stick figure with formatted data
    fig = go.Figure(data=[
        go.Candlestick(x=df['date'],open=df['open'],
                       high=df['high'], low=df['low'], close=df['close'])])
    # format layout to my taste
    fig.update_layout(template="plotly_dark",
                      xaxis_title = "Date",
                      yaxis_title = "BTC/USD Prices")
    # add in 20WMA 
    fig.add_trace(
        go.Scatter(x=df['date'], y=df['20WMA'], name="20WeekMovingAvg")
        )
    
    return fig



if __name__ == "__main__":
    df = pd.read_csv("Bitstamp_BTCUSD_d.csv", skiprows=1)
    df = format_data(df)
    figure = genFigure(df)
    figure.show()