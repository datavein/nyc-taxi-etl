from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = (
    PROJECT_ROOT / "data" / "raw" / "yellow_tripdata_2026-01.parquet")

PROCESSED_DATA_PATH = (
    PROJECT_ROOT / "data" / "processed" / "yellow_tripdata_2026-01_cleaned.parquet")

def create_output_directory() -> None:
    """
    Create the output directory if it doesn't exist.
    """
    print("\nChecking output directory...")
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    print("Output directory is ready.")

def save_processed_dataset(df: pd.DataFrame) -> None:
    """
    Save the processed dataset to a Parquet file.
    """
    print("\nSaving processed dataset...")
    df.to_parquet(PROCESSED_DATA_PATH, index=False)
    print("Processed dataset saved.")

def verify_saved_dataset() -> None:
    """
    Verify that the processed dataset was saved correctly.
    """
    print("\nVerifying saved dataset...")
    if PROCESSED_DATA_PATH.exists():
        print("Processed dataset verified successfully.")
    else:
        raise FileNotFoundError(f"Processed dataset not found: {PROCESSED_DATA_PATH}")

def print_load_summary(df: pd.DataFrame) -> None:
    """
    Print load summary.
    """
    print("\nLoad summary:")
    print(f"Output file path: {PROCESSED_DATA_PATH}")
    print(f"Number of rows: {len(df):,}")
    print(f"Number of columns: {len(df.columns)}")
    print("\nETL pipeline completed successfully.")

def load(df: pd.DataFrame) -> None:
    """
    Load the processed dataset.
    """
    print("\nLoading processed dataset...")
    create_output_directory()
    save_processed_dataset(df)
    verify_saved_dataset()
    print_load_summary(df)

