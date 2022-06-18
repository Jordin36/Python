import pandas_datareader as pdr
import pandas as pd
data_vars=['UNRATE','FEDFUNDS','INDPRO']
fed_data1=pdr.get_data_fred(data_vars)
summary=(fed_data1.describe())
print(summary)
import statsmodels.formula.api as smf
reg1='INDPRO~UNRATE+FEDFUNDS'
reg1output=smf.ols(reg1,fed_data1).fit()
print(reg1output.summary())
print('R2: ',reg1output.rsquared)