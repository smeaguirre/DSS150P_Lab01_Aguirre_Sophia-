-- Create the lab schema
CREATE SCHEMA IF NOT EXISTS lab;

-- Create the customers table based on earlier profiling
CREATE TABLE IF NOT EXISTS lab.customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255), -- Nullable based on profiling (3 missing)
    city VARCHAR(100),  -- Nullable based on profiling (2 missing)
    signup_date DATE NOT NULL,
    customer_segment VARCHAR(50) NOT NULL,
    
    -- CHECK constraint: Ensure customer_id is never an empty string
    CONSTRAINT ck_customer_id_not_empty CHECK (LENGTH(customer_id) > 0)
);