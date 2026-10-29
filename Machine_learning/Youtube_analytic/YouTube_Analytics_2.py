import matplotlib.pyplot as plt
import seaborn as sns
from YouTube_Analytics_1 import *

plt.figure(figsize=(10,10))
sns.histplot(df['views'],bins=50,kde=True)
plt.title("Video Views")
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(10,10))
sns.scatterplot(x=df['likes'], y=df['views'])
plt.title("Like Views")
plt.xlabel("Likes")
plt.ylabel("Views")
plt.show()

neumeric_cols= ['views','likes','dislikes','comment_count','title_length',]
if 'title'in df.columns and 'title_length' not in df.columns:
    df['title_length']= df['title'].apply(lambda x: len(str(x)))

corr_matric= df[neumeric_cols].corr()
print("\nCorrelation Matrix:")
print(corr_matric)

plt.figure(figsize=(10,10))
sns.heatmap(corr_matric, annot=True,cmap='coolwarm',fmt='.2f')
plt.title("Correlation Matrix")
plt.show()