from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = (
    PROJECT_ROOT / "data" / "raw" / "yellow_tripdata_2026-01.parquet")

def extract() -> pd.DataFrame:
    """
    Read paquet file into a Pandas DataFrame.
    """

    print("Read parquet file...")
    df = pd.read_parquet(RAW_DATA_PATH)
    print(f"Loaded {len(df):,} rows.")
    
    return df

def validate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate raw dataset.
    """

    print("\nValidating raw dataset...")

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")

    return df
def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert data types of columns.
    """
    print("\nConverting data types...")
    dtype_mapping = {
        "VendorID": "category",
        "passenger_count": "Int64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "category",
        "payment_type": "category"
    }
    for column, dtype in dtype_mapping.items():
        df[column] = df[column].astype(dtype)
    print("\nData types after conversion:")
    print(df.dtypes)
    return df

def calculate_trip_duration(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate trip duration in minutes.
    """

    print("\nCalculating trip duration...")

    df["trip_duration_minutes"] = (
        df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    return df

def profile_trip_duration(df: pd.DataFrame) -> None:
    """
    Profile trip statistics.
    """
    print("\nTrip duration statistics:")
    print(df["trip_duration_minutes"].describe())

    negative_trips = (df["trip_duration_minutes"] < 0).sum()
    print(f"Negative trip durations: {negative_trips:,}")

    long_trips = (df["trip_duration_minutes"] > 180).sum()
    print(f"Long trips (>180 minutes): {long_trips:,}")

    pd.set_option("display.max_columns", None)

    print("\nLongest trips:")
    print(
        df.sort_values("trip_duration_minutes", ascending=False)[[
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "trip_duration_minutes",
            "trip_distance",
            "fare_amount",
            "total_amount",

        ]
        ].head(10)
    ) 

def clean_trip_duration(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw dataset.
    """

    print("\nCleaning raw dataset...")
    rows_before = len(df)

    df = df[df["trip_duration_minutes"] >= 0]
    rows_after = len(df)
    print("\nCleaning results:")
    print(f"Rows before: {rows_before:,}")
    print(f"Rows after: {rows_after:,}")
    print(f"Rows removed: {rows_before - rows_after:,}")

    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform raw dataset.
    """

    print("\nTransforming raw dataset...")

    df = convert_data_types(df)

    df = calculate_trip_duration(df)

    profile_trip_duration(df)

    df = clean_trip_duration(df)

    return df

if __name__ == "__main__":
    df = extract()
    df = validate(df)
    df = transform(df)
    