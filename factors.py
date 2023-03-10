import numpy as np
import pandas as pd
import datetime as dt


def fast_momentum():
    """
    Calculate the aggregated rolling fast momentum filter for a time series
    Filter formula: 12*p0/p1+4*p0/p3+2*p0/p6+1*p0/p12 -19, where pt equals price p with lag t
    """
