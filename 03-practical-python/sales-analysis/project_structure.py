import os

print("Current directory:", os.getcwd())

data_path = "data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")
