/*
====================================
Create Database
Project: NYC Taxi ETL
====================================
*/

IF DB_ID('NYC_Taxi_ETL') IS NULL
BEGIN
    CREATE DATABASE [NYC_Taxi_ETL];
END
GO

USE [NYC_Taxi_ETL];
GO