import pandas as pd

df =pd.read_csv('/home/mayank/Desktop/sabudh/Machine_learning/Resources/USvideos.csv')

print("\n",df.head())
print("\n",df.info())
print("\n",df.describe())


viral_threshold = df['views'].quantile(0.75)
df['viral']= (df['views'] > viral_threshold.astype(int))

print(f"\nViral Threshhold (75th percentile of views):  {viral_threshold}")
print(f"Value counts for viral column:\n {df['viral'].value_counts()}")
