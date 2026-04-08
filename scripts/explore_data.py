import pandas as pd

# Load the dataset
print("Loading dataset... please wait")
df = pd.read_excel("data/online_retail_II.xlsx", 
                   sheet_name="Year 2010-2011")

# Basic exploration
print(f"\n✅ Total Rows: {df.shape[0]}")
print(f"✅ Total Columns: {df.shape[1]}")
print(f"\n📋 Column Names: {df.columns.tolist()}")
print(f"\n🔍 First 5 rows:\n{df.head()}")
print(f"\n❌ Missing Values:\n{df.isnull().sum()}")

# Save as CSV
df.to_csv("data/retail_raw.csv", index=False)
print("\n✅ Saved as retail_raw.csv!")