# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:23:51 2021

This script extracts stock financial data from Morningstar and analyzes it using various
financial models, including Discounted Cash Flow, Benjamin Graham Formula, and Dividend
Discount Model. The results are plotted for easy visualization.

"""

import pandas as pd
import matplotlib.pyplot as plt
from grab_data import extract_data

def time_series_format(ticker, column, ttm_remove=False):
    data = extract_data(ticker)
    if ttm_remove:
        data.drop('TTM', inplace=True)
    test = pd.Series(data[column], index=data.index)
    return test
    
def plot_layout(ticker, plot_style='ggplot'):
    plt.style.use(plot_style)
    fig, axes = plt.subplots(nrows=2, ncols=2)
    eps = time_series_format(ticker, 'Earnings Per Share USD')
    debt_equity_ratio = time_series_format(ticker, 'Debt/Equity')
    net_margin = time_series_format(ticker, 'Net Margin %')
    fcf = time_series_format(ticker, 'Free Cash Flow USD Mil')
    eps.plot(ax=axes[0, 0]).set_title('EPS Growth History')
    debt_equity_ratio.plot(ax=axes[0, 1]).set_title('Historic Debt/Equity Ratio')
    net_margin.plot(ax=axes[1, 0]).set_title('Net Margin History')
    fcf.plot(ax=axes[1, 1]).set_title('Free Cash Flow History')
    plt.tight_layout()
    plt.show()

