from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from YouTube_Analytics_3 import *


# 1. Selection & Engineering
numeric_cols = ['likes', 'dislikes', 'comment_count', 'title_length']
categorical_cols = ['category_id'] # channel_title is dropped here to avoid extreme dimensionality

# 2. One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Update feature lists after encoding
encoded_cols = [col for col in df_encoded.columns if col.startswith('category_id_')]
X_features = numeric_cols + encoded_cols

X = df_encoded[X_features]
y_reg = df_encoded['views']
y_clf = df_encoded['viral']

# 3. Train-Test Split (80%-20%)
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)
_, _, y_train_clf, y_test_clf = train_test_split(X, y_clf, test_size=0.2, random_state=42)

# 4. Feature Scaling using StandardScaler
scaler = StandardScaler()
X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()

X_train_scaled[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_test_scaled[numeric_cols] = scaler.transform(X_test[numeric_cols])
