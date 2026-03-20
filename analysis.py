import pandas as pd

# ==============================
# 📊 Load Dataset
# ==============================
df = pd.read_csv('data/Mall_Customers.csv')

print("\n📌 Dataset Preview:")
print(df.head())

print("\n📌 Columns:")
print(df.columns)


# ==============================
# 🎯 1. Average Spending by Gender
# ==============================
print("\n🔹 Average Spending by Gender:")
avg_spending = df.groupby('Genre')['Spending_Score'].mean()
print(avg_spending)


# ==============================
# 🎯 2. High Value Customers
# ==============================
high_spenders = df[df['Spending_Score'] > 80]

print("\n🔹 Number of High Value Customers:", len(high_spenders))
print(high_spenders.head())


# ==============================
# 🎯 3. Customer Segmentation
# ==============================
def segment(score):
    if score > 70:
        return "High Spender"
    elif score > 40:
        return "Medium Spender"
    else:
        return "Low Spender"

df['Segment'] = df['Spending_Score'].apply(segment)

print("\n🔹 Customer Segmentation:")
print(df['Segment'].value_counts())


# ==============================
# 🎯 4. Age Group Analysis
# ==============================
df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[0, 25, 40, 60, 100],
    labels=['Young', 'Adult', 'Mid', 'Senior']
)

print("\n🔹 Spending by Age Group:")
print(df.groupby('Age_Group')['Spending_Score'].mean())


# ==============================
# 🎯 5. Income vs Spending
# ==============================
print("\n🔹 Income vs Spending Correlation:")
print(df[['Annual_Income_(k$)', 'Spending_Score']].corr())


# ==============================
# 🤖 Final Insight Summary
# ==============================
print("\n💡 Key Insights:")
print("- High spending customers form a small but valuable segment.")
print("- Income does not strongly correlate with spending.")
print("- Younger customers tend to spend more.")
print("- Customer segmentation helps target marketing strategies.")
df.to_csv('output/customer_analysis.csv', index=False)