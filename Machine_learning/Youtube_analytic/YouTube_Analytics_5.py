from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from YouTube_Analytics_4 import *
from matplotlib import pyplot as plt

# 1. Train Model
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train_reg)


# Predict
y_pred_reg = lr_model.predict(X_test_scaled)

mse = mean_squared_error(y_test_reg, y_pred_reg)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test_reg, y_pred_reg)
r2 = r2_score(y_test_reg, y_pred_reg)

print("Linear Regression Evaluation Metrics:")
print(f"MSE : {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE : {mae:.2f}")
print(f"R²  : {r2:.4f}")

# 4. Feature Importance / Coefficients
coefficients = pd.Series(lr_model.coef_, index=X_features).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=coefficients.values, y=coefficients.index)
plt.title('Feature Importance (Linear Regression Coefficients)')
plt.xlabel('Coefficient Value')
plt.ylabel('Features')
plt.show()
