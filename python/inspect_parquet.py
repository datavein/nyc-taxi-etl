from pathlib import Path
import pandas as pd

DATA_DIR = Path("data") / "raw"

FILE_PATH = DATA_DIR / "yellow_tripdata_2026-01.parquet"

if not FILE_PATH.exists():
    raise FileNotFoundError(f"File not found: {FILE_PATH}")

df = pd.read_parquet(FILE_PATH)

print("="*50)
print("HEAD")
print(df.head())

print()

print("="*50)
print("INFO") 
df.info()
 
print()

print("="*50)
print("DTYPES")
print("="*50)
print(df.dtypes)

print()

print("="*50)
print("SHAPE")
print("="*50)
print(df.shape)

print()

print("="*50)
print("COLUMNS")
print("="*50)
print(df.columns)

print()

print("="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())

print()

print("=" * 50)
print("MISSING VALUES (%)")
print("=" * 50)

missing_percent = df.isna().mean() * 100

print(missing_percent)

print()
print("=" * 50)
print("NUMERIC STATISTICS")
print("=" * 50)
print(df.describe())

print()

print("=" * 50)
print("VendorID VALUE COUNTS")
print("=" * 50)

print(df["VendorID"].value_counts(dropna=False))