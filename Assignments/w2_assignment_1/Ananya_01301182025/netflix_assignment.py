import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, mean_squared_error, r2_score, classification_report
import warnings
warnings.filterwarnings('ignore')

# loading the dataset
df = pd.read_csv('Dataset_2.csv')

# -----------------------------------------------
# PART A - Dataset Understanding
# -----------------------------------------------

# Q1
print("First 5 records:")
print(df.head())

# Q2
print("\nNumber of rows and columns:")
print(df.shape)

# Q3
print("\nColumn names:")
print(df.columns.tolist())

# Q4
num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
print("\nNumerical columns:", num_cols)
print("Categorical columns:", cat_cols)

# Q5
print("\nMissing values:")
print(df.isnull().sum())

# -----------------------------------------------
# PART B - Exploratory Data Analysis
# -----------------------------------------------

# Q6
print("\nAverage age:", round(df['Age'].mean(), 2))

# Q7
print("Average watch hours per week:", round(df['WatchHoursPerWeek'].mean(), 2))

# Q8
print("Average monthly spending:", round(df['MonthlySpend'].mean(), 2))

# Q9
print("\nUsers per subscription type:")
print(df['SubscriptionType'].value_counts())

# Q10
renewed = (df['SubscriptionRenewed'] == 'Yes').mean() * 100
print(f"\nPercentage of users who renewed: {round(renewed, 2)}%")

# some plots for EDA
fig, axes = plt.subplots(2, 3, figsize=(15, 9))

df['Age'].hist(ax=axes[0,0], bins=20, color='steelblue', edgecolor='white')
axes[0,0].set_title('Age Distribution')

df['WatchHoursPerWeek'].hist(ax=axes[0,1], bins=20, color='coral', edgecolor='white')
axes[0,1].set_title('Watch Hours Per Week')

df['SubscriptionType'].value_counts().plot(kind='bar', ax=axes[0,2], color='mediumseagreen', edgecolor='white')
axes[0,2].set_title('Subscription Types')
axes[0,2].tick_params(axis='x', rotation=0)

df['SubscriptionRenewed'].value_counts().plot(kind='pie', ax=axes[1,0], autopct='%1.1f%%', colors=['#66b3ff','#ff9999'])
axes[1,0].set_title('Renewal Rate')
axes[1,0].set_ylabel('')

df['MonthlySpend'].hist(ax=axes[1,1], bins=20, color='mediumpurple', edgecolor='white')
axes[1,1].set_title('Monthly Spend')

df['FavoriteGenre'].value_counts().plot(kind='barh', ax=axes[1,2], color='sandybrown')
axes[1,2].set_title('Favourite Genres')

plt.suptitle('Netflix User Analytics - EDA', fontsize=13)
plt.tight_layout()
plt.savefig('eda_plots.png')
plt.show()

# -----------------------------------------------
# PART C - Data Preparation
# -----------------------------------------------

# Q11 - label encoding
df2 = df.copy()
le = LabelEncoder()

for col in ['Gender', 'SubscriptionType', 'FavoriteGenre', 'SubscriptionRenewed']:
    df2[col] = le.fit_transform(df2[col])

print("\nAfter encoding (first 3 rows):")
print(df2.head(3))

# Q12
X = df2.drop(columns=['UserID', 'SubscriptionRenewed'])
y = df2['SubscriptionRenewed']
print("\nFeatures:", X.columns.tolist())
print("Target: SubscriptionRenewed")

# Q13
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTraining size: {X_train.shape[0]}")
print(f"Testing size: {X_test.shape[0]}")

# -----------------------------------------------
# PART D - Decision Tree
# -----------------------------------------------

# Q14
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt.fit(X_train, y_train)

# Q15
y_pred_dt = dt.predict(X_test)
dt_acc = accuracy_score(y_test, y_pred_dt)
print(f"\nDecision Tree Accuracy: {round(dt_acc*100, 2)}%")
print(classification_report(y_test, y_pred_dt, target_names=['No', 'Yes']))

# Q16
cm = confusion_matrix(y_test, y_pred_dt)
print("Confusion Matrix:")
print(cm)
print(f"True Negatives: {cm[0,0]}, False Positives: {cm[0,1]}")
print(f"False Negatives: {cm[1,0]}, True Positives: {cm[1,1]}")

fig, ax = plt.subplots(figsize=(5,4))
ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No','Yes']).plot(ax=ax, cmap='Blues', colorbar=False)
ax.set_title('Decision Tree - Confusion Matrix')
plt.tight_layout()
plt.savefig('dt_confusion_matrix.png')
plt.show()

# feature importance plot
feat_imp = pd.Series(dt.feature_importances_, index=X.columns).sort_values()
feat_imp.plot(kind='barh', color='steelblue', figsize=(7,5))
plt.title('Feature Importances - Decision Tree')
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()

# -----------------------------------------------
# PART E - KNN
# -----------------------------------------------

# Q17
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
knn_acc = accuracy_score(y_test, y_pred_knn)
print(f"\nKNN (K=5) Accuracy: {round(knn_acc*100, 2)}%")

# Q18
print("\nModel Comparison:")
print(f"  Decision Tree : {round(dt_acc*100, 2)}%")
print(f"  KNN (K=5)     : {round(knn_acc*100, 2)}%")
if dt_acc >= knn_acc:
    print("  Decision Tree performed better")
else:
    print("  KNN performed better")

# -----------------------------------------------
# PART F - Linear Regression
# -----------------------------------------------

# Q19
X_reg = df2.drop(columns=['UserID', 'MonthlySpend', 'SubscriptionRenewed'])
y_reg = df2['MonthlySpend']

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(X_train_r, y_train_r)
y_pred_lr = lr.predict(X_test_r)

rmse = np.sqrt(mean_squared_error(y_test_r, y_pred_lr))
r2 = r2_score(y_test_r, y_pred_lr)
print(f"\nLinear Regression RMSE: {round(rmse, 2)}")
print(f"R2 Score: {round(r2, 4)}")

plt.figure(figsize=(7,5))
plt.scatter(y_test_r, y_pred_lr, alpha=0.5, color='coral')
plt.plot([y_test_r.min(), y_test_r.max()], [y_test_r.min(), y_test_r.max()], 'k--')
plt.xlabel('Actual Spend')
plt.ylabel('Predicted Spend')
plt.title(f'Linear Regression - Actual vs Predicted (R2={round(r2,3)})')
plt.tight_layout()
plt.savefig('linear_regression.png')
plt.show()

# Q20 - predicting for a new user
new_user = pd.DataFrame([{
    'Age': 30,
    'Gender': 0,
    'SubscriptionType': 1,
    'WatchHoursPerWeek': 20,
    'DevicesUsed': 3,
    'FavoriteGenre': 2,
    'AdClicks': 15
}])

pred = lr.predict(new_user)[0]
print(f"\nPredicted monthly spend for new user: Rs.{round(pred, 2)}")
print("This user is a 30 year old female with Premium subscription who watches 20 hrs/week.")
print("Based on these features the model predicts her monthly spend will be around Rs.", round(pred, 2))
