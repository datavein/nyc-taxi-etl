/*
==============================
  Create Schema 
  Project: NYC_Taxi_ETL
==============================
*/

USE NYC_Taxi_ETL;
GO

IF NOT EXISTS (
    SELECT *
    FROM sys.schemas
    WHERE name = 'staging'
)
BEGIN
    EXEC('CREATE SCHEMA staging');
END
GO

IF NOT EXISTS (
    SELECT *
    FROM sys.schemas
    WHERE name = 'warehouse'
)
BEGIN
    EXEC('CREATE SCHEMA warehouse');
END
GO

IF NOT EXISTS(
    SELECT *
    FROM sys.schemas
    WHERE name = 'dimention'
)
BEGIN
    EXEC('CREATE SCHEMA dimension');
END
GO