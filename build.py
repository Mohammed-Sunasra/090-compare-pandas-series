import pandas as pd


def equal_operator(ds1, ds2):
    return ds1 == ds2


def greater_than_operator(ds1, ds2):
    return ds1 > ds2

def less_than_operator(ds1, ds2):
    return ds1 < ds2

s1 = pd.Series([2, 4, 6, 8, 10])
s2 = pd.Series([1, 3, 5, 7, 10])

#print
print equal_operator(s1, s2)
print greater_than_operator(s1, s2)
print less_than_operator(s1, s2)
