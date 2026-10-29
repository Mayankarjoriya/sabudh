
import pandas as pd

dataset = '/home/mayank/Desktop/sabudh/Python/Dataset/archive/Sport car price.csv'

data = pd.read_csv(dataset)
dataset = pd.DataFrame(data)

print(dataset.head(5))

b = len(dataset)
dataset = dataset.drop_duplicates()
print(f"Removed {b-len(dataset)} duplicated rows")

c = len(dataset)
df = dataset.dropna()
print(f" Missing values: {c - len(df)} ")
print(df.info())
print(df.head(10))

neumeric_cols= ["Engine Size (L)","Torque (lb-ft)","0-60 MPH Time (seconds)","Horsepower"]

for col in neumeric_cols:
    print(col,"is: ",df[col].dtype)

    df[col] = pd.to_numeric(df[col], errors ='coerce')
    print(f"\n{col} is changed to neumeric")


df['Price (in USD)'] = (
    df['Price (in USD)']
    .astype(str)
    .str.replace('[$,]', '', regex=True)
    .astype(float)
)  
leng = len(df)
df = df.dropna()
print("Removed null Rows",leng-len(df))    
print(df.head(10))

for col in neumeric_cols:
    print(col,"is: ",df[col].dtype)

print(df.info())
print(df.head(10))

numeric_df = df.select_dtypes(include=[np.number])

summary_stats = {
    "Mean":numeric_df.mean(),
    "Median":numeric_df.median(),
    "Mode":numeric_df.mode(),
    "Standard Deviation":numeric_df.std(),
    "Min":numeric_df.min(),
    "Max":numeric_df.max(),
    "Range":numeric_df.max() - numeric_df.min()
}

avg_price_make = df.groupby('Car Make')['Price (in USD)'].mean().sort_values(ascending=False)
avg_price_make = avg_price_make.round(2)
avg_hp_year = df.groupby('Year')['Horsepower'].mean().sort_index()
avg_hp_year = avg_hp_year.round(2)

import matplotlib.pyplot as plt

plt.figure(figsize=(12,7))
plt.scatter(df["Horsepower"],df['Price (in USD)'], 
           alpha=0.6, edgecolors='k',linewidths=0.5,s=80)
slope, intercept = np.polyfit(df['Horsepower'],df['Price (in USD)'],1)

x_line = np.linspace(df['Horsepower'].min(),df["Horsepower"].max(),100)
y_line = slope * x_line + intercept
plt.plot(x_line,y_line, "r-",linewidth=2.5,
        label=f"y = {slope:.2f}x + {intercept:.2f}")

plt.xlabel("Horsepower",fontsize=12)
plt.ylabel("Price", fontsize=12)
plt.title('Sports Car Price vs HorsePower', fontsize = 14)
plt.legend()

