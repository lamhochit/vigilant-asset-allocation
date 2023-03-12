import numpy as np
import pandas as pd
import datetime as dt


def fast_momentum(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the rolling fast momentum filter for a time series
    Filter formula: 12*p0/p1+4*p0/p3+2*p0/p6+1*p0/p12 -19, where pt equals price p with lag t
    Fast momentum is a modification from the classic 13612 factor
    """
    fast_momentum_df = 12 * df.pct_change(periods=1) + 4 * df.pct_change(periods=3) + 2 * df.pct_change(periods=1) + \
                       1 * df.pct_change(periods=12)

    return fast_momentum_df


def portfolio_construction(df: pd.DataFrame, t: int, breadth_threshold: int, risky_assets: list,
                           safety_assets: list) -> pd.DataFrame:
    """
    Calculate the rolling fast crash protection for a time series
    Breadth momentum = how many bad assets in the universe
    bad assets (b) are defined by non-positive momentum
    Breadth protection threshold (B)
    CF = b/B if b<B, and CF=1 when b>=B
    """
    risky_df = df[risky_assets]
    safety_df = df[safety_assets]
    cf_df = np.minimum(np.floor(risky_df.apply(pd.Series.nlargest,
                                               axis=1, n=t).apply(lambda x: len(x[x <= 0]), axis=1) /
                                breadth_threshold * t) / t, 1)
    allocation_df = (1 - cf_df) / t
    return risky_df
    return cf_df, allocation_df, risky_df.apply(pd.Series.nlargest, axis=1, n=t).apply(lambda x: len(x[x <= 0]), axis=1)


if __name__ == '__main__':
    data_df = pd.read_csv('data/historical_universe.csv', index_col=0)
    momentum_df = fast_momentum(data_df)
    x = portfolio_construction(momentum_df, t=4, breadth_threshold=4,
                                risky_assets=['SPY US Equity', 'IWM US Equity', 'QQQ US Equity', 'VGK US Equity',
                                              'EWJ US Equity', 'EEM US Equity',
                                              'EFA US Equity', 'ACWX US Equity', 'IYR US Equity', 'GSG US Equity',
                                              'GLD US Equity',
                                              'TLT US Equity', 'HYG US Equity',
                                              'AGG US Equity'],
                                safety_assets=['IEF US Equity', 'LQD US Equity', 'SHY US Equity'])
