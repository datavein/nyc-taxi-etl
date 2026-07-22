# NYC taxi ETL Pipeline

This project demonstrates an end-to-end ETL pipeline built with Python and Pandas using the NYC Yellow Taxi Trip Records dataset.

The pipeline extracts raw data from a Parquet file, validates the dataset, performs data transformation and cleaning, and saves the processed dataset.

The project is being developed incrementally to simulate a real-world Data Engineering workflow. Future improvements include implementing the same ETL process with Microsoft SQL Server using BULK INSERT, orchestrating the pipeline, and building an interactive Power BI dashboard.

![Python](https://img.shields.io/badge/Python-3.13-blue)

![Pandas](https://img.shields.io/badge/Pandas-2.x-green)

![Parquet](https://img.shields.io/badge/Data-Parquet-blueviolet)

![Git](https://img.shields.io/badge/Git-Version%20Control-orange)

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

## Project Overview 

This project demonstrate end-to-end ETL pipeline build with Python and Pandas using the NYC Yellow Taxi Trip Records dataset.

The pipeline follows a modular ETL architecture consisting four stages:

- Extract
- Validate
- Transform
- Load

Before running the ETL pipeline, the project provides a data inspection utility that explores the raw dataset, validates its structure, and identifies potential data quality issues.

During the transformation stage, teh pipeline performs data profiling, calculates trip duration, detects anomalies, removes invaid records and exports the cleaned dataset as a new Parquet file.

The project is being developed incrementally to simulate a real-world Data Engineering workflow. Future version will include Microsoft SQL Server, SQL-based ETL, orcestration and bussines intelligance reporting. 

## Features

- Modular ETL architecture
- Automatic dataset validation
- Data type conversion 
- Trip duration calculation
- Data profiling
- Anomaly detection
- Invalid record removal
- Processed dataset export
- Modular and extensible project structure