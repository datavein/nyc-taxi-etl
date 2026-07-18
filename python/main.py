from transform_data import extract, validate, transform
from load_data import load

def main() -> None:
    """
    Run the ETL pipeline.
    """
    df = extract()
    df = validate(df)
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()