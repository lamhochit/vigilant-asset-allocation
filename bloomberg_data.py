from xbbg import blp


df = blp.bdh(tickers=['TSLA US Equity', 'BABA US Equity'], flds=['Last_Price'],
             start_date='2017-01-01', end_date='2022-12-31', Per='M', Fill='P', Days='A')


df.to_csv('data/sample_data.csv')
