from scipy import stats
from YouTube_Analytics_2 import *

for feature in ['likes','dislikes','comment_count']:
    med_val = df[feature].median()
    group_high = df[df[feature] > med_val]['views']
    group_low = df[df[feature] <= med_val]['views']

    t_stat,p_val = stats.ttest_ind(group_high,group_low, equal_var=False)
    print(f"Hypothesis Test for {feature.upper()}")
    print(f"t-Statistic: {t_stat:.4f}, \np-value: {p_val}")

    if p_val<0.05:
        print("Not Correct")
    else:
        print("Correct")
