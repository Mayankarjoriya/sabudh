from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, roc_curve
from YouTube_Analytics_5 import *
from matplotlib import pyplot as plt


# 1. Train Model
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train_scaled, y_train_clf)

# 2. Predict
y_pred_clf = log_model.predict(X_test_scaled)
y_pred_prob = log_model.predict_proba(X_test_scaled)[:, 1]

# 3. Evaluate Metrics
print("Logistic Regression Evaluation Metrics:")
print(f"Accuracy : {accuracy_score(y_test_clf, y_pred_clf):.4f}")
print(f"Precision: {precision_score(y_test_clf, y_pred_clf):.4f}")
print(f"Recall   : {recall_score(y_test_clf, y_pred_clf):.4f}")
print(f"F1-Score : {f1_score(y_test_clf, y_pred_clf):.4f}")
print(f"ROC-AUC  : {roc_auc_score(y_test_clf, y_pred_prob):.4f}")

# 4. Plot Confusion Matrix
cm = confusion_matrix(y_test_clf, y_pred_clf)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# 5. Plot ROC Curve
fpr, tpr, _ = roc_curve(y_test_clf, y_pred_prob)
plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, label=f'ROC-AUC = {roc_auc_score(y_test_clf, y_pred_prob):.4f}')
plt.plot([0, 1], [0, 1], 'k--')
plt.title('ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
