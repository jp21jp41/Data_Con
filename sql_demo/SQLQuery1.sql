USE master
GO
IF NOT EXISTS (
   SELECT name
   FROM sys.databases
   WHERE name = N'TutorialDB'
)
CREATE DATABASE [TutorialDB]
GO

USE [TutorialDB]

-- Create a new table called 'Customers' in schema 'dbo'
-- Drop the table if it already exists
IF OBJECT_ID('dbo.Customers', 'U') IS NOT NULL
    DROP TABLE dbo.Customers
GO

-- Create the table in the specified schema
CREATE TABLE dbo.Customers (
    CustomerId INT NOT NULL PRIMARY KEY, -- primary key column
    Name NVARCHAR(50) NOT NULL,
    Location NVARCHAR(50) NOT NULL,
    Email NVARCHAR(50) NOT NULL
);
GO

-- Insert rows into table 'Customers'
INSERT INTO dbo.Customers
   ([CustomerId],[Name],[Location],[Email])
VALUES
   ( 1, N'Orlando', N'Australia', N''),
   ( 2, N'Keith', N'India', N'keith0@adventure-works.com'),
   ( 3, N'Donna', N'Germany', N'donna0@adventure-works.com'),
   ( 4, N'Janet', N'United States', N'janet1@adventure-works.com')
GO



-- Select rows from table 'Customers'
SELECT * FROM dbo.sales_data

SELECT REGION, SUM(Sales_Amount) AS "Sales Amount", SUM(Quantity_Sold) AS "Total Sold" FROM dbo.sales_data
GROUP BY REGION ORDER BY "Sales Amount";



