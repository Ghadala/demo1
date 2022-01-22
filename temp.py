import pandas as pd
data=pd.read_csv(r'C:\Users\alasa\Downloads\temperature--791487693.csv')



df=data[data.isnull()]
print(data)
data.fillna(method='bfill')
data.to_csv("tempnew.csv", index=False)
# Press the green button in the gutter to run the script.
