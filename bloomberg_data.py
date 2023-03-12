from xbbg import blp

tickers = ['SPY US Equity', 'IWM US Equity', 'QQQ US Equity', 'VGK US Equity', 'EWJ US Equity', 'EEM US Equity',
           'EFA US Equity', 'ACWX US Equity', 'IYR US Equity', 'GSG US Equity', 'GLD US Equity', 'SHY US Equity',
           'IEF US Equity', 'TLT US Equity', 'LQD US Equity', 'HYG US Equity', 'AGG US Equity']

df = blp.bdh(tickers=tickers, flds=['Last_Price'],
             start_date='2008-03-01', end_date='2023-02-28', Per='M', Fill='P', Days='A')

df.columns = df.columns.levels[0]
df.to_csv('data/historical_universe.csv')
