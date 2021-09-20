import pandas as pd
import numpy as np
from pandas_datareader import data as dr
import matplotlib.pyplot as plt

tickers = ["PFE", "MRNA", "AZN", "JNJ"]
vac_stock = pd.DataFrame()
for x in tickers:
    vac_stock[x] = dr.DataReader(
        x, data_source="yahoo", start="2019-1-1")["Adj Close"]
# Efficient Frontier
num_stock = len(tickers)
log_returns = np.log(vac_stock / vac_stock.shift(1))
mean_log_returns = log_returns.mean()
weights = np.random.random(num_stock)
weights /= np.sum(weights)
(weights[0] + weights[1] + weights[2] + weights[3])
#  Portfolio Covariance
cov_log_returns = log_returns.cov()
#  Portfolio Correlation
corr_log_returns = log_returns.corr()
# Expected Portfolio Return
returns = np.sum(weights * mean_log_returns)
# Expected Porfolio Variance
var = np.dot(weights.T, np.dot(cov_log_returns, weights))
# Expected Portfolio Volatility (Standard Deviation)
std = np.sqrt(var)
# Testing
p_returns = []
p_volatility = []
for x in range(2000):
    weights = np.random.random(num_stock)
    weights /= np.sum(weights)
    p_returns.append(np.sum(weights * mean_log_returns))
    p_volatility.append(
        np.sqrt(np.dot(weights.T, np.dot(cov_log_returns, weights))))
p_returns = np.array(p_returns)
p_volatility = np.array(p_volatility)
# Graph
portfolios = pd.DataFrame({"Return": p_returns, 'Volatility': p_volatility})
portfolios.plot(x="Volatility", y="Return", kind="scatter", figsize=(10, 6))
plt.title("Efficient Frontier")
plt.xlabel("Volatility")
plt.ylabel("Return")
plt.show()
