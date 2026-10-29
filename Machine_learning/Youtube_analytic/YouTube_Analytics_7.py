from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from YouTube_Analytics_6 import *


# 1. 5-Fold Cross-Validation setup
cv_lr = cross_val_score(LinearRegression(), X, y_reg, cv=5, scoring='r2')
cv_log = cross_val_score(LogisticRegression(max_iter=1000), X, y_clf, cv=5, scoring='accuracy')

print(f"Linear Regression 5-Fold R² Scores: {cv_lr}")
print(f"Mean R²: {cv_lr.mean():.4f} (+/- {cv_lr.var():.4f})")

print(f"\nLogistic Regression 5-Fold Accuracy Scores: {cv_log}")
print(f"Mean Accuracy: {cv_log.mean():.4f} (+/- {cv_log.var():.4f})")

# 2. Scaling Comparison: MinMaxScaler
minmax_scaler = MinMaxScaler()
X_train_minmax = X_train.copy()
X_train_minmax[numeric_cols] = minmax_scaler.fit_transform(X_train[numeric_cols])

# Re-train to check stability variations
lr_minmax = LinearRegression().fit(X_train_minmax, y_train_reg)
print("\nMinMax Scaled Baseline completed successfully.")
