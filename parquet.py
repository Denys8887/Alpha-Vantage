import pandas as pd
from ETL_single_ticker import tech_indicators_sma

df = pd.DataFrame(tech_indicators_sma(), columns=['SMA'])
df.to_parquet('df.snap.parquet', compression='snappy')
print(pd.read_parquet('df.snap.parquet'))
