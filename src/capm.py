"""
E[R] = Riskfree + beta(E[Rmarket]- Riskfree)
beta = cov[R, Rmarket]/Var[Rmarket]
Using S&P 500 Index as the proxy for the market return and the 3-month Treasury 
constant maturity rate as the risk-free rate
"""

# getting the data
from iexfinance.stocks import Stock

appl = Stock('AAPL', output_format='pandas')
appl.get_price()




