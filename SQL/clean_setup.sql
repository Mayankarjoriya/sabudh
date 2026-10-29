CREATE DATABASE FinanceHub;
USE FinanceHub;
– Step 2: Create Tables
-- Customers table - Bank customers information
CREATE TABLE Customers (
customer_id INT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
phone VARCHAR(20),
date_of_birth DATE,
address VARCHAR(200),
city VARCHAR(50),
state VARCHAR(50),
country VARCHAR(50),
zip_code VARCHAR(20),
registration_date DATE NOT NULL,
customer_type VARCHAR(30) DEFAULT 'Individual',
risk_profile VARCHAR(20) DEFAULT 'Medium',
credit_score INT,
annual_income DECIMAL(12, 2),
kyc_verified BOOLEAN DEFAULT FALSE
);
-- Accounts table - Bank accounts
CREATE TABLE Accounts (
account_id INT PRIMARY KEY,
customer_id INT NOT NULL,
account_number VARCHAR(20) UNIQUE NOT NULL,
account_type VARCHAR(30) NOT NULL,
account_status VARCHAR(20) DEFAULT 'Active',
opening_date DATE NOT NULL,
current_balance DECIMAL(15, 2) DEFAULT 0.00,
currency VARCHAR(10) DEFAULT 'USD',
interest_rate DECIMAL(5, 2) DEFAULT 0.00,
minimum_balance DECIMAL(12, 2) DEFAULT 0.00,
branch_code VARCHAR(20),
last_transaction_date DATE,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Transactions table - All financial transactions
CREATE TABLE Transactions (
transaction_id INT PRIMARY KEY,
account_id INT NOT NULL,
transaction_type VARCHAR(30) NOT NULL,
transaction_date DATETIME NOT NULL,
amount DECIMAL(15, 2) NOT NULL,
balance_after DECIMAL(15, 2),
description VARCHAR(200),
reference_number VARCHAR(50) UNIQUE,
transaction_status VARCHAR(20) DEFAULT 'Completed',
channel VARCHAR(30),
category VARCHAR(50),
FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

-- Loans table - Loan information
CREATE TABLE Loans (
loan_id INT PRIMARY KEY,
customer_id INT NOT NULL,
loan_type VARCHAR(30) NOT NULL,
loan_amount DECIMAL(15, 2) NOT NULL,
interest_rate DECIMAL(5, 2) NOT NULL,
tenure_months INT NOT NULL,
monthly_emi DECIMAL(12, 2) NOT NULL,
outstanding_balance DECIMAL(15, 2) NOT NULL,
disbursement_date DATE NOT NULL,
maturity_date DATE NOT NULL,
loan_status VARCHAR(20) DEFAULT 'Active',
collateral_type VARCHAR(50),
collateral_value DECIMAL(15, 2),
purpose VARCHAR(100),
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
-- LoanPayments table - Loan EMI payments
CREATE TABLE LoanPayments (
payment_id INT PRIMARY KEY,
loan_id INT NOT NULL,
payment_date DATE NOT NULL,
amount_paid DECIMAL(12, 2) NOT NULL,
principal_amount DECIMAL(12, 2) NOT NULL,
interest_amount DECIMAL(12, 2) NOT NULL,
outstanding_balance DECIMAL(15, 2) NOT NULL,
payment_status VARCHAR(20) DEFAULT 'Paid',
payment_method VARCHAR(30),
late_fee DECIMAL(8, 2) DEFAULT 0.00,
FOREIGN KEY (loan_id) REFERENCES Loans(loan_id)
);
-- CreditCards table - Credit card information
CREATE TABLE CreditCards (
card_id INT PRIMARY KEY,
customer_id INT NOT NULL,
card_number VARCHAR(20) UNIQUE NOT NULL,
card_type VARCHAR(30) NOT NULL,
credit_limit DECIMAL(12, 2) NOT NULL,
available_credit DECIMAL(12, 2) NOT NULL,
current_balance DECIMAL(12, 2) DEFAULT 0.00,
interest_rate DECIMAL(5, 2) NOT NULL,
issue_date DATE NOT NULL,
expiry_date DATE NOT NULL,
card_status VARCHAR(20) DEFAULT 'Active',
reward_points INT DEFAULT 0,
annual_fee DECIMAL(8, 2) DEFAULT 0.00,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- CardTransactions table - Credit card transactions
CREATE TABLE CardTransactions (
card_transaction_id INT PRIMARY KEY,
card_id INT NOT NULL,
transaction_date DATETIME NOT NULL,
merchant_name VARCHAR(100),
merchant_category VARCHAR(50),
amount DECIMAL(12, 2) NOT NULL,
transaction_type VARCHAR(20) NOT NULL,
transaction_status VARCHAR(20) DEFAULT 'Posted',
foreign_transaction BOOLEAN DEFAULT FALSE,
reward_points_earned INT DEFAULT 0,
FOREIGN KEY (card_id) REFERENCES CreditCards(card_id)
);
-- Investments table - Investment portfolios
CREATE TABLE Investments (
investment_id INT PRIMARY KEY,
customer_id INT NOT NULL,
investment_type VARCHAR(50) NOT NULL,
security_name VARCHAR(100),
quantity DECIMAL(15, 4),
purchase_price DECIMAL(15, 2) NOT NULL,
current_price DECIMAL(15, 2),
purchase_date DATE NOT NULL,
maturity_date DATE,
investment_status VARCHAR(20) DEFAULT 'Active',
risk_level VARCHAR(20),
returns_percentage DECIMAL(8, 2),
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
-- Branches table - Bank branches
CREATE TABLE Branches (
branch_id INT PRIMARY KEY,
branch_code VARCHAR(20) UNIQUE NOT NULL,
branch_name VARCHAR(100) NOT NULL,
address VARCHAR(200),
city VARCHAR(50),
state VARCHAR(50),
country VARCHAR(50),
phone VARCHAR(20),
manager_name VARCHAR(100),
opening_date DATE,
branch_type VARCHAR(30),
total_customers INT DEFAULT 0,
is_active BOOLEAN DEFAULT TRUE
);

-- Employees table - Bank employees
CREATE TABLE Employees (
employee_id INT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
phone VARCHAR(20),
hire_date DATE NOT NULL,
job_title VARCHAR(100) NOT NULL,
department VARCHAR(50) NOT NULL,
branch_id INT,
manager_id INT,
salary DECIMAL(12, 2),
performance_rating DECIMAL(3, 2),
is_active BOOLEAN DEFAULT TRUE,
FOREIGN KEY (branch_id) REFERENCES Branches(branch_id),
FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);
-- CustomerService table - Customer service interactions
CREATE TABLE CustomerService (
ticket_id INT PRIMARY KEY,
customer_id INT NOT NULL,
employee_id INT,
ticket_date DATETIME NOT NULL,
issue_category VARCHAR(50) NOT NULL,
issue_description TEXT,
priority VARCHAR(20) DEFAULT 'Medium',
status VARCHAR(20) DEFAULT 'Open',
resolution_date DATETIME,
satisfaction_rating INT CHECK (satisfaction_rating BETWEEN 1 AND 5),
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
);
-- FraudAlerts table - Fraud detection alerts
CREATE TABLE FraudAlerts (
alert_id INT PRIMARY KEY,
customer_id INT NOT NULL,
account_id INT,
alert_date DATETIME NOT NULL,
alert_type VARCHAR(50) NOT NULL,
risk_score INT CHECK (risk_score BETWEEN 0 AND 100),
description TEXT,
status VARCHAR(20) DEFAULT 'Pending',
investigated_by INT,
resolution_date DATETIME,
is_fraud_confirmed BOOLEAN,
FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
FOREIGN KEY (account_id) REFERENCES Accounts(account_id),
FOREIGN KEY (investigated_by) REFERENCES Employees(employee_id)
);

-- Tools table - Tools used by analysts
CREATE TABLE Tools (
tool_id INT PRIMARY KEY,
tool_name VARCHAR(100) NOT NULL,
tool_category VARCHAR(50),
cost DECIMAL(10, 2),
license_type VARCHAR(50),
version VARCHAR(20),
is_active BOOLEAN DEFAULT TRUE
);
-- AnalystTools table - Junction table for analysts and their tools
CREATE TABLE AnalystTools (
employee_id INT NOT NULL,
tool_id INT NOT NULL,
proficiency_level VARCHAR(20),
is_primary_tool BOOLEAN DEFAULT FALSE,
last_used_date DATE,
PRIMARY KEY (employee_id, tool_id),
FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
FOREIGN KEY (tool_id) REFERENCES Tools(tool_id)
);
-- TrainingPrograms table - Training programs available
CREATE TABLE TrainingPrograms (
program_id INT PRIMARY KEY,
program_name VARCHAR(100) NOT NULL,
program_category VARCHAR(50),
duration_hours INT,
cost DECIMAL(10, 2),
provider VARCHAR(100),
start_date DATE,
end_date DATE
);
-- AnalystTraining table - Junction table for analysts and training
CREATE TABLE AnalystTraining (
training_record_id INT PRIMARY KEY,
employee_id INT NOT NULL,
program_id INT NOT NULL,
completion_date DATE,
score INT CHECK (score BETWEEN 0 AND 100),
is_certified BOOLEAN DEFAULT FALSE,
FOREIGN KEY (employee_id) REFERENCES Employees(employee_id),
FOREIGN KEY (program_id) REFERENCES TrainingPrograms(program_id)
);

-- Step 3: Insert Sample Data
-- Insert Customers
INSERT INTO Customers VALUES
(1001, 'John', 'Anderson', 'john.anderson@email.com', '555-0101', '1985-03-15', '123 Park Ave', 'New York', 'NY',
'USA', '10001', '2020-01-15', 'Individual', 'Low', 720, 95000.00, TRUE),
(1002, 'Sarah', 'Williams', 'sarah.w@email.com', '555-0102', '1990-07-22', '456 Market St', 'San Francisco',
'CA', 'USA', '94102', '2020-02-20', 'Individual', 'Medium', 680, 78000.00, TRUE),
(1003, 'Michael', 'Brown', 'michael.b@email.com', '555-0103', '1978-11-10', '789 Main St', 'Chicago', 'IL', 'USA',
'60601', '2020-03-18', 'Individual', 'Medium', 695, 120000.00, TRUE),
(1004, 'Emily', 'Davis', 'emily.davis@email.com', '555-0104', '1988-05-30', '321 Oak Rd', 'Boston', 'MA', 'USA',
'02101', '2020-04-12', 'Individual', 'High', 750, 150000.00, TRUE),
(1005, 'Robert', 'Johnson', 'robert.j@email.com', '555-0105', '1982-09-14', '654 Pine St', 'Seattle', 'WA', 'USA',
'98101', '2020-05-25', 'Individual', 'Low', 710, 88000.00, TRUE),
(1006, 'Jennifer', 'Martinez', 'jennifer.m@email.com', '555-0106', '1992-12-08', '987 Elm Ave', 'Miami', 'FL',
'USA', '33101', '2020-06-30', 'Individual', 'Medium', 670, 65000.00, TRUE),
(1007, 'David', 'Garcia', 'david.garcia@email.com', '555-0107', '1975-04-25', '147 Cedar Ln', 'Houston', 'TX',
'USA', '77001', '2020-08-15', 'Individual', 'High', 780, 180000.00, TRUE),
(1008, 'Lisa', 'Rodriguez', 'lisa.r@email.com', '555-0108', '1987-06-18', '258 Birch Dr', 'Phoenix', 'AZ', 'USA',
'85001', '2020-09-22', 'Individual', 'Medium', 705, 92000.00, TRUE),
(1009, 'James', 'Wilson', 'james.wilson@email.com', '555-0109', '1980-10-05', '369 Maple Ct', 'Denver', 'CO',
'USA', '80201', '2020-10-10', 'Individual', 'Low', 690, 75000.00, TRUE),
(1010, 'Patricia', 'Lee', 'patricia.lee@email.com', '555-0110', '1995-02-28', '741 Spruce Way', 'Portland', 'OR',
'USA', '97201', '2020-11-18', 'Individual', 'Medium', 665, 62000.00, TRUE),
(1011, 'William', 'Taylor', 'william.t@email.com', '555-0111', '1983-08-12', '852 Walnut Pl', 'Austin', 'TX', 'USA',
'78701', '2021-01-05', 'Individual', 'High', 740, 135000.00, TRUE),
(1012, 'Linda', 'Thomas', 'linda.thomas@email.com', '555-0112', '1991-03-20', '963 Ash Blvd', 'Atlanta', 'GA',
'USA', '30301', '2021-02-14', 'Individual', 'Medium', 685, 82000.00, TRUE),
(1013, 'Richard', 'Moore', 'richard.m@email.com', '555-0113', '1986-07-09', '159 Fir St', 'Dallas', 'TX', 'USA',
'75201', '2021-03-22', 'Individual', 'Low', 700, 98000.00, TRUE),
(1014, 'Mary', 'Jackson', 'mary.jackson@email.com', '555-0114', '1979-11-30', '357 Cypress Ave', 'Philadelphia',
'PA', 'USA', '19101', '2021-04-18', 'Business', 'Medium', 730, 200000.00, TRUE),
(1015, 'Thomas', 'White', 'thomas.white@email.com', '555-0115', '1993-01-16', '456 Redwood Dr', 'San Diego',
'CA', 'USA', '92101', '2021-05-12', 'Individual', 'High', 760, 145000.00, TRUE);
-- Insert Branches
INSERT INTO Branches VALUES
(1, 'NYC001', 'New York Main Branch', '500 Fifth Ave', 'New York', 'NY', 'USA', '555-2001', 'Robert Smith',
'2015-01-15', 'Main', 1500, TRUE),
(2, 'SF001', 'San Francisco Downtown', '100 Market St', 'San Francisco', 'CA', 'USA', '555-2002', 'Maria Chen',
'2016-03-20', 'Main', 1200, TRUE),
(3, 'CHI001', 'Chicago Loop Branch', '200 State St', 'Chicago', 'IL', 'USA', '555-2003', 'James Brown',
'2016-06-10', 'Main', 980, TRUE),
(4, 'BOS001', 'Boston Financial District', '75 State St', 'Boston', 'MA', 'USA', '555-2004', 'Sarah Johnson',
'2017-02-15', 'Main', 850, TRUE),
(5, 'SEA001', 'Seattle Downtown', '400 Pike St', 'Seattle', 'WA', 'USA', '555-2005', 'David Lee', '2017-08-22',
'Regional', 720, TRUE);

-- Insert Employees
INSERT INTO Employees VALUES
(2001, 'Robert', 'Smith', 'robert.smith@financehub.com', '555-3001', '2015-01-15', 'Branch Manager',
'Operations', 1, NULL, 125000.00, 4.5, TRUE),
(2002, 'Maria', 'Chen', 'maria.chen@financehub.com', '555-3002', '2016-03-20', 'Branch Manager',
'Operations', 2, NULL, 120000.00, 4.7, TRUE),
(2003, 'James', 'Brown', 'james.brown@financehub.com', '555-3003', '2016-06-10', 'Branch Manager',
'Operations', 3, NULL, 118000.00, 4.3, TRUE),
(2004, 'Sarah', 'Johnson', 'sarah.johnson@financehub.com', '555-3004', '2017-02-15', 'Branch Manager',
'Operations', 4, NULL, 115000.00, 4.6, TRUE),
(2005, 'David', 'Lee', 'david.lee@financehub.com', '555-3005', '2017-08-22', 'Branch Manager', 'Operations',
5, NULL, 110000.00, 4.4, TRUE),
(2006, 'Jennifer', 'Wilson', 'jennifer.wilson@financehub.com', '555-3006', '2018-01-10', 'Loan Officer',
'Lending', 1, 2001, 75000.00, 4.2, TRUE),
(2007, 'Michael', 'Davis', 'michael.davis@financehub.com', '555-3007', '2018-03-15', 'Financial Advisor',
'Wealth Management', 1, 2001, 85000.00, 4.8, TRUE),
(2008, 'Amanda', 'Martinez', 'amanda.m@financehub.com', '555-3008', '2018-06-20', 'Customer Service Rep', 'Customer Service', 2, 2002, 45000.00, 4.1, TRUE),
(2009, 'Christopher', 'Garcia', 'chris.garcia@financehub.com', '555-3009', '2019-01-12', 'Fraud Analyst',
'Risk Management', 1, 2001, 68000.00, 4.5, TRUE),
(2010, 'Jessica', 'Rodriguez', 'jessica.r@financehub.com', '555-3010', '2019-04-18', 'Investment Specialist',
'Wealth Management', 2, 2002, 92000.00, 4.7, TRUE),
(2011, 'Daniel', 'Taylor', 'daniel.t@financehub.com', '555-3011', '2019-08-22', 'Credit Analyst', 'Lending', 3,
2003, 72000.00, 4.3, TRUE),
(2012, 'Emily', 'Thomas', 'emily.thomas@financehub.com', '555-3012', '2020-01-15', 'Customer Service Rep',
'Customer Service', 1, 2001, 47000.00, 4.6, TRUE),
(2013, 'Matthew', 'Moore', 'matthew.moore@financehub.com', '555-3013', '2020-05-20', 'Loan Officer',
'Lending', 2, 2002, 78000.00, 4.4, TRUE),
(2014, 'Ashley', 'Jackson', 'ashley.j@financehub.com', '555-3014', '2020-09-10', 'Financial Advisor', 'Wealth Management', 4, 2004, 88000.00, 4.5, TRUE),
(2015, 'Joshua', 'White', 'joshua.white@financehub.com', '555-3015', '2021-02-14', 'Fraud Analyst', 'Risk Management', 2, 2002, 70000.00, 4.2, TRUE);
-- Insert Accounts
INSERT INTO Accounts VALUES
(5001, 1001, 'ACC10010001', 'Savings', 'Active', '2020-01-15', 45000.00, 'USD', 2.50, 1000.00, 'NYC001',
'2024-03-15'),
(5002, 1001, 'ACC10010002', 'Checking', 'Active', '2020-01-15', 12500.00, 'USD', 0.00, 0.00, 'NYC001',
'2024-03-14'),
(5003, 1002, 'ACC10020001', 'Savings', 'Active', '2020-02-20', 28000.00, 'USD', 2.50, 1000.00, 'SF001',
'2024-03-10'),
(5004, 1003, 'ACC10030001', 'Checking', 'Active', '2020-03-18', 18500.00, 'USD', 0.00, 0.00, 'CHI001',
'2024-03-12'),
(5005, 1003, 'ACC10030002', 'Money Market', 'Active', '2020-06-22', 75000.00, 'USD', 3.25, 5000.00, 'CHI001',
'2024-03-08'),
(5006, 1004, 'ACC10040001', 'Savings', 'Active', '2020-04-12', 95000.00, 'USD', 2.75, 1000.00, 'BOS001',
'2024-03-16'),
(5007, 1004, 'ACC10040002', 'Checking', 'Active', '2020-04-12', 22000.00, 'USD', 0.00, 0.00, 'BOS001',
'2024-03-14'),
(5008, 1005, 'ACC10050001', 'Savings', 'Active', '2020-05-25', 35000.00, 'USD', 2.50, 1000.00, 'SEA001',
'2024-03-11'),
(5009, 1006, 'ACC10060001', 'Checking', 'Active', '2020-06-30', 8500.00, 'USD', 0.00, 0.00, 'NYC001',
'2024-03-13'),

(5010, 1007, 'ACC10070001', 'Money Market', 'Active', '2020-08-15', 125000.00, 'USD', 3.50, 5000.00, 'NYC001',
'2024-03-15'),
(5011, 1008, 'ACC10080001', 'Savings', 'Active', '2020-09-22', 42000.00, 'USD', 2.50, 1000.00, 'SF001',
'2024-03-09'),
(5012, 1009, 'ACC10090001', 'Checking', 'Active', '2020-10-10', 15000.00, 'USD', 0.00, 0.00, 'CHI001',
'2024-03-12'),
(5013, 1010, 'ACC10100001', 'Savings', 'Active', '2020-11-18', 18000.00, 'USD', 2.50, 1000.00, 'SEA001',
'2024-03-10'),
(5014, 1011, 'ACC10110001', 'Savings', 'Active', '2021-01-05', 68000.00, 'USD', 2.75, 1000.00, 'BOS001',
'2024-03-14'),
(5015, 1012, 'ACC10120001', 'Checking', 'Active', '2021-02-14', 11000.00, 'USD', 0.00, 0.00, 'SF001', '2024-03-11');
-- Insert Transactions (Sample 30 transactions)
INSERT INTO Transactions VALUES
(10001, 5001, 'Deposit', '2024-01-05 10:15:00', 5000.00, 50000.00, 'Salary Credit', 'TXN10001', 'Completed',
'Online Banking', 'Income'),
(10002, 5002, 'Withdrawal', '2024-01-06 14:30:00', 500.00, 12000.00, 'ATM Withdrawal', 'TXN10002',
'Completed', 'ATM', 'Cash'),
(10003, 5001, 'Transfer Out', '2024-01-10 09:45:00', 2000.00, 48000.00, 'Bill Payment', 'TXN10003',
'Completed', 'Online Banking', 'Bills'),
(10004, 5003, 'Deposit', '2024-01-12 11:20:00', 3500.00, 31500.00, 'Freelance Payment', 'TXN10004',
'Completed', 'Wire Transfer', 'Income'),
(10005, 5004, 'Withdrawal', '2024-01-15 16:10:00', 1200.00, 17300.00, 'Grocery Shopping', 'TXN10005',
'Completed', 'Debit Card', 'Shopping'),
(10006, 5006, 'Deposit', '2024-01-18 10:30:00', 8000.00, 103000.00, 'Bonus Credit', 'TXN10006', 'Completed',
'Direct Deposit', 'Income'),
(10007, 5002, 'Transfer In', '2024-01-20 13:45:00', 1500.00, 13500.00, 'From Savings', 'TXN10007',
'Completed', 'Online Banking', 'Transfer'),
(10008, 5008, 'Withdrawal', '2024-01-22 15:20:00', 800.00, 34200.00, 'Restaurant', 'TXN10008',
'Completed', 'Debit Card', 'Dining'),
(10009, 5010, 'Deposit', '2024-01-25 09:15:00', 10000.00, 135000.00, 'Investment Returns', 'TXN10009',
'Completed', 'Wire Transfer', 'Investment'),
(10010, 5011, 'Withdrawal', '2024-01-28 12:40:00', 2500.00, 39500.00, 'Rent Payment', 'TXN10010',
'Completed', 'Check', 'Housing'),
(10011, 5001, 'Withdrawal', '2024-02-02 11:30:00', 300.00, 47700.00, 'Utility Bills', 'TXN10011', 'Completed',
'Online Banking', 'Bills'),
(10012, 5005, 'Deposit', '2024-02-05 14:15:00', 5000.00, 80000.00, 'Business Revenue', 'TXN10012',
'Completed', 'Wire Transfer', 'Income'),
(10013, 5007, 'Withdrawal', '2024-02-08 10:20:00', 1500.00, 20500.00, 'Medical Expenses', 'TXN10013',
'Completed', 'Debit Card', 'Healthcare'),
(10014, 5009, 'Deposit', '2024-02-10 16:45:00', 2000.00, 10500.00, 'Refund', 'TXN10014', 'Completed', 'ACH',
'Refund'),
(10015, 5012, 'Withdrawal', '2024-02-12 13:30:00', 600.00, 14400.00, 'Subscription Services', 'TXN10015',
'Completed', 'Auto Debit', 'Entertainment'),
(10016, 5014, 'Deposit', '2024-02-15 09:50:00', 7000.00, 75000.00, 'Salary Credit', 'TXN10016', 'Completed',
'Direct Deposit', 'Income'),
(10017, 5003, 'Withdrawal', '2024-02-18 15:10:00', 900.00, 30600.00, 'Fuel', 'TXN10017', 'Completed', 'Debit Card', 'Transportation'),
(10018, 5006, 'Transfer Out', '2024-02-20 11:25:00', 15000.00, 88000.00, 'Investment Transfer', 'TXN10018',
'Completed', 'Online Banking', 'Investment'),
(10019, 5001, 'Deposit', '2024-02-22 10:15:00', 4000.00, 51700.00, 'Dividend Income', 'TXN10019',
'Completed', 'ACH', 'Income'),

(10020, 5008, 'Withdrawal', '2024-02-25 14:40:00', 1200.00, 33000.00, 'Insurance Premium', 'TXN10020',
'Completed', 'Auto Debit', 'Insurance'),
(10021, 5013, 'Deposit', '2024-02-28 09:30:00', 2500.00, 20500.00, 'Bonus', 'TXN10021', 'Completed', 'Direct Deposit', 'Income'),
(10022, 5004, 'Withdrawal', '2024-03-01 16:20:00', 450.00, 16850.00, 'Clothing Purchase', 'TXN10022',
'Completed', 'Debit Card', 'Shopping'),
(10023, 5010, 'Withdrawal', '2024-03-03 11:15:00', 3000.00, 132000.00, 'Home Maintenance', 'TXN10023',
'Completed', 'Check', 'Housing'),
(10024, 5002, 'Deposit', '2024-03-05 13:45:00', 1000.00, 14500.00, 'Cashback Credit', 'TXN10024',
'Completed', 'ACH', 'Income'),
(10025, 5011, 'Withdrawal', '2024-03-08 10:30:00', 2000.00, 37500.00, 'Tuition Fee', 'TXN10025',
'Completed', 'Wire Transfer', 'Education'),
(10026, 5015, 'Deposit', '2024-03-10 15:20:00', 3000.00, 14000.00, 'Project Payment', 'TXN10026',
'Completed', 'Wire Transfer', 'Income'),
(10027, 5005, 'Deposit', '2024-03-12 09:40:00', 6000.00, 86000.00, 'Interest Credit', 'TXN10027',
'Completed', 'Auto Credit', 'Income'),
(10028, 5007, 'Withdrawal', '2024-03-14 14:10:00', 800.00, 21200.00, 'Pet Care', 'TXN10028', 'Completed',
'Debit Card', 'Personal'),
(10029, 5009, 'Withdrawal', '2024-03-15 11:50:00', 350.00, 10150.00, 'Phone Bill', 'TXN10029', 'Completed',
'Auto Debit', 'Bills'),
(10030, 5014, 'Withdrawal', '2024-03-16 16:35:00', 1500.00, 73500.00, 'Travel Booking', 'TXN10030',
'Completed', 'Online Banking', 'Travel');
-- Insert Loans
INSERT INTO Loans VALUES
(3001, 1001, 'Home Loan', 350000.00, 6.75, 240, 2625.00, 325000.00, '2021-06-15', '2041-06-15', 'Active',
'Property', 450000.00, 'Home Purchase'),
(3002, 1003, 'Personal Loan', 50000.00, 10.50, 60, 1068.00, 42000.00, '2022-03-10', '2027-03-10', 'Active',
'None', 0.00, 'Debt Consolidation'),
(3003, 1004, 'Auto Loan', 45000.00, 7.25, 60, 898.00, 32000.00, '2022-08-20', '2027-08-20', 'Active',
'Vehicle', 52000.00, 'Car Purchase'),
(3004, 1007, 'Business Loan', 200000.00, 8.50, 84, 3250.00, 175000.00, '2021-10-05', '2028-10-05', 'Active',
'Commercial Property', 280000.00, 'Business Expansion'),
(3005, 1008, 'Education Loan', 80000.00, 6.00, 120, 888.00, 65000.00, '2022-01-15', '2032-01-15', 'Active',
'None', 0.00, 'Higher Education'),
(3006, 1011, 'Home Loan', 425000.00, 6.50, 300, 2688.00, 410000.00, '2021-08-22', '2046-08-22', 'Active',
'Property', 550000.00, 'Home Purchase'),
(3007, 1014, 'Business Loan', 150000.00, 9.00, 72, 2450.00, 125000.00, '2022-04-18', '2028-04-18', 'Active',
'Equipment', 180000.00, 'Equipment Purchase'),
(3008, 1002, 'Personal Loan', 30000.00, 11.00, 48, 778.00, 18000.00, '2023-02-10', '2027-02-10', 'Active',
'None', 0.00, 'Home Renovation'),
(3009, 1006, 'Auto Loan', 35000.00, 7.75, 60, 706.00, 28000.00, '2022-09-15', '2027-09-15', 'Active', 'Vehicle',
40000.00, 'Car Purchase'),
(3010, 1009, 'Personal Loan', 25000.00, 10.00, 36, 806.00, 15000.00, '2023-06-01', '2026-06-01', 'Active',
'None', 0.00, 'Medical Emergency');
-- Insert LoanPayments (Sample payments)
INSERT INTO LoanPayments VALUES
(4001, 3001, '2024-01-15', 2625.00, 875.00, 1750.00, 324125.00, 'Paid', 'Auto Debit', 0.00),
(4002, 3001, '2024-02-15', 2625.00, 880.00, 1745.00, 323245.00, 'Paid', 'Auto Debit', 0.00),
(4003, 3001, '2024-03-15', 2625.00, 885.00, 1740.00, 322360.00, 'Paid', 'Auto Debit', 0.00),
(4004, 3002, '2024-01-10', 1068.00, 630.00, 438.00, 41370.00, 'Paid', 'Online Transfer', 0.00),
(4005, 3002, '2024-02-10', 1068.00, 635.00, 433.00, 40735.00, 'Paid', 'Online Transfer', 0.00),
(4006, 3002, '2024-03-10', 1068.00, 640.00, 428.00, 40095.00, 'Paid', 'Online Transfer', 0.00),

(4007, 3003, '2024-01-20', 898.00, 705.00, 193.00, 31295.00, 'Paid', 'Auto Debit', 0.00),
(4008, 3003, '2024-02-20', 898.00, 710.00, 188.00, 30585.00, 'Paid', 'Auto Debit', 0.00),
(4009, 3003, '2024-03-20', 898.00, 715.00, 183.00, 29870.00, 'Paid', 'Auto Debit', 0.00),
(4010, 3004, '2024-01-05', 3250.00, 2000.00, 1250.00, 173000.00, 'Paid', 'Wire Transfer', 0.00),
(4011, 3004, '2024-02-05', 3250.00, 2015.00, 1235.00, 170985.00, 'Paid', 'Wire Transfer', 0.00),
(4012, 3004, '2024-03-05', 3250.00, 2030.00, 1220.00, 168955.00, 'Paid', 'Wire Transfer', 0.00),
(4013, 3005, '2024-01-15', 888.00, 563.00, 325.00, 64437.00, 'Paid', 'Auto Debit', 0.00),
(4014, 3005, '2024-02-15', 888.00, 566.00, 322.00, 63871.00, 'Paid', 'Auto Debit', 0.00),
(4015, 3005, '2024-03-15', 888.00, 569.00, 319.00, 63302.00, 'Paid', 'Auto Debit', 0.00),
(4016, 3006, '2024-01-22', 2688.00, 1465.00, 1223.00, 408535.00, 'Paid', 'Auto Debit', 0.00),
(4017, 3006, '2024-02-22', 2688.00, 1473.00, 1215.00, 407062.00, 'Paid', 'Auto Debit', 0.00),
(4018, 3006, '2024-03-22', 2688.00, 1481.00, 1207.00, 405581.00, 'Paid', 'Auto Debit', 0.00),
(4019, 3008, '2024-02-10', 778.00, 513.00, 265.00, 17487.00, 'Paid', 'Online Transfer', 0.00),
(4020, 3008, '2024-03-10', 778.00, 518.00, 260.00, 16969.00, 'Paid', 'Online Transfer', 0.00);
-- Insert CreditCards
INSERT INTO CreditCards VALUES
(6001, 1001, '4532-XXXX-XXXX-1234', 'Platinum', 50000.00, 42000.00, 8000.00, 18.99, '2020-02-01',
'2025-02-01', 'Active', 12500, 499.00),
(6002, 1002, '5425-XXXX-XXXX-5678', 'Gold', 30000.00, 24500.00, 5500.00, 21.49, '2020-03-15',
'2025-03-15', 'Active', 6800, 199.00),
(6003, 1003, '3782-XXXX-XXXX-9012', 'Platinum', 75000.00, 68000.00, 7000.00, 17.99, '2020-04-10',
'2025-04-10', 'Active', 18200, 599.00),
(6004, 1004, '6011-XXXX-XXXX-3456', 'Signature', 100000.00, 88000.00, 12000.00, 16.99, '2020-05-20',
'2025-05-20', 'Active', 24500, 799.00),
(6005, 1005, '4532-XXXX-XXXX-7890', 'Silver', 20000.00, 16500.00, 3500.00, 22.99, '2020-06-12',
'2025-06-12', 'Active', 4200, 99.00),
(6006, 1007, '5425-XXXX-XXXX-2345', 'Platinum', 80000.00, 70000.00, 10000.00, 17.49, '2020-09-05',
'2025-09-05', 'Active', 22000, 599.00),
(6007, 1008, '4532-XXXX-XXXX-6789', 'Gold', 40000.00, 35000.00, 5000.00, 20.99, '2020-10-18',
'2025-10-18', 'Active', 8500, 199.00),
(6008, 1011, '3782-XXXX-XXXX-0123', 'Platinum', 60000.00, 52000.00, 8000.00, 18.49, '2021-01-22',
'2026-01-22', 'Active', 14800, 499.00),
(6009, 1012, '5425-XXXX-XXXX-4567', 'Silver', 25000.00, 21000.00, 4000.00, 22.49, '2021-03-10',
'2026-03-10', 'Active', 5500, 99.00),
(6010, 1015, '6011-XXXX-XXXX-8901', 'Gold', 45000.00, 38000.00, 7000.00, 19.99, '2021-06-15', '2026-06-15',
'Active', 10200, 199.00);
-- Insert CardTransactions (Sample 25 transactions)
INSERT INTO CardTransactions VALUES
(7001, 6001, '2024-01-05 14:25:00', 'Amazon.com', 'Online Shopping', 450.00, 'Purchase', 'Posted', FALSE,
45),
(7002, 6002, '2024-01-08 10:15:00', 'Walmart', 'Groceries', 180.00, 'Purchase', 'Posted', FALSE, 18),
(7003, 6001, '2024-01-12 16:30:00', 'Delta Airlines', 'Travel', 850.00, 'Purchase', 'Posted', FALSE, 170),
(7004, 6003, '2024-01-15 11:45:00', 'Apple Store', 'Electronics', 1200.00, 'Purchase', 'Posted', FALSE, 240),
(7005, 6004, '2024-01-18 09:20:00', 'Hilton Hotels', 'Travel', 650.00, 'Purchase', 'Posted', FALSE, 130),
(7006, 6005, '2024-01-20 14:10:00', 'Shell Gas Station', 'Fuel', 75.00, 'Purchase', 'Posted', FALSE, 8),
(7007, 6006, '2024-01-22 15:40:00', 'Best Buy', 'Electronics', 920.00, 'Purchase', 'Posted', FALSE, 184),
(7008, 6007, '2024-01-25 12:30:00', 'Target', 'Shopping', 235.00, 'Purchase', 'Posted', FALSE, 24),
(7009, 6001, '2024-01-28 10:50:00', 'Starbucks', 'Dining', 35.00, 'Purchase', 'Posted', FALSE, 7),
(7010, 6008, '2024-02-02 16:15:00', 'Costco', 'Groceries', 380.00, 'Purchase', 'Posted', FALSE, 38),
(7011, 6003, '2024-02-05 11:25:00', 'Home Depot', 'Home Improvement', 560.00, 'Purchase', 'Posted', FALSE,
112),

(7012, 6002, '2024-02-08 14:40:00', 'Uber', 'Transportation', 45.00, 'Purchase', 'Posted', FALSE, 5),
(7013, 6004, '2024-02-10 09:30:00', 'Marriott Hotels', 'Travel', 720.00, 'Purchase', 'Posted', FALSE, 144),
(7014, 6009, '2024-02-12 15:20:00', 'CVS Pharmacy', 'Healthcare', 125.00, 'Purchase', 'Posted', FALSE, 13),
(7015, 6010, '2024-02-15 12:10:00', 'Nike Store', 'Apparel', 290.00, 'Purchase', 'Posted', FALSE, 58),
(7016, 6001, '2024-02-18 10:45:00', 'Whole Foods', 'Groceries', 165.00, 'Purchase', 'Posted', FALSE, 17),
(7017, 6006, '2024-02-20 16:30:00', 'British Airways', 'Travel', 1450.00, 'Purchase', 'Posted', TRUE, 290),
(7018, 6007, '2024-02-22 11:15:00', 'Netflix', 'Entertainment', 15.99, 'Purchase', 'Posted', FALSE, 2),
(7019, 6003, '2024-02-25 14:50:00', 'Sephora', 'Beauty', 185.00, 'Purchase', 'Posted', FALSE, 37),
(7020, 6008, '2024-02-28 09:40:00', 'Chipotle', 'Dining', 42.00, 'Purchase', 'Posted', FALSE, 8),
(7021, 6002, '2024-03-02 15:25:00', 'Exxon', 'Fuel', 68.00, 'Purchase', 'Posted', FALSE, 7),
(7022, 6004, '2024-03-05 12:35:00', 'Nordstrom', 'Apparel', 485.00, 'Purchase', 'Posted', FALSE, 97),
(7023, 6001, '2024-03-08 10:20:00', 'Amazon.com', 'Online Shopping', 325.00, 'Purchase', 'Posted', FALSE,
65),
(7024, 6010, '2024-03-12 16:10:00', 'United Airlines', 'Travel', 680.00, 'Purchase', 'Posted', FALSE, 136),
(7025, 6005, '2024-03-15 11:30:00', 'Walgreens', 'Healthcare', 95.00, 'Purchase', 'Posted', FALSE, 10);
-- Insert Investments
INSERT INTO Investments VALUES
(8001, 1001, 'Stocks', 'Apple Inc (AAPL)', 100.000, 15000.00, 17500.00, '2021-03-15', NULL, 'Active', 'Medium',
16.67),
(8002, 1003, 'Mutual Fund', 'Vanguard S&P 500', 500.000, 25000.00, 32000.00, '2020-06-20', NULL,
'Active', 'Low', 28.00),
(8003, 1004, 'Bonds', 'US Treasury 10Y', 50000.000, 50000.00, 52500.00, '2021-01-10', '2031-01-10', 'Active',
'Low', 5.00),
(8004, 1007, 'Stocks', 'Microsoft (MSFT)', 150.000, 45000.00, 58500.00, '2021-08-05', NULL, 'Active',
'Medium', 30.00),
(8005, 1004, 'Stocks', 'Tesla (TSLA)', 75.000, 18000.00, 13500.00, '2022-02-15', NULL, 'Active', 'High', -25.00),
(8006, 1011, 'Mutual Fund', 'Fidelity Growth Fund', 800.000, 40000.00, 48000.00, '2021-05-22', NULL,
'Active', 'Medium', 20.00),
(8007, 1003, 'Bonds', 'Corporate Bond AAA', 30000.000, 30000.00, 32100.00, '2022-03-10', '2027-03-10',
'Active', 'Low', 7.00),
(8008, 1015, 'Stocks', 'Amazon (AMZN)', 80.000, 24000.00, 27200.00, '2021-11-18', NULL, 'Active', 'Medium',
13.33),
(8009, 1007, 'Real Estate Fund', 'Vanguard REIT Index', 600.000, 60000.00, 69000.00, '2020-09-25', NULL,
'Active', 'Medium', 15.00),
(8010, 1014, 'Stocks', 'Google (GOOGL)', 120.000, 36000.00, 43200.00, '2021-07-12', NULL, 'Active', 'Medium',
20.00),
(8011, 1001, 'Mutual Fund', 'BlackRock Equity Fund', 400.000, 20000.00, 23600.00, '2022-01-20', NULL,
'Active', 'Low', 18.00),
(8012, 1008, 'Bonds', 'Municipal Bond', 25000.000, 25000.00, 26250.00, '2022-06-15', '2032-06-15', 'Active',
'Low', 5.00),
(8013, 1011, 'Stocks', 'NVIDIA (NVDA)', 50.000, 22000.00, 35000.00, '2021-10-08', NULL, 'Active', 'High',
59.09),
(8014, 1015, 'Mutual Fund', 'T. Rowe Price Growth', 350.000, 17500.00, 21000.00, '2022-04-12', NULL, 'Active',
'Medium', 20.00),
(8015, 1012, 'Stocks', 'Meta (META)', 90.000, 27000.00, 32400.00, '2021-12-05', NULL, 'Active', 'High', 20.00);
-- Insert CustomerService tickets
INSERT INTO CustomerService VALUES
(9001, 1001, 2012, '2024-01-10 09:30:00', 'Account Access', 'Unable to login to online banking', 'High',
'Resolved', '2024-01-10 11:15:00', 5),
(9002, 1002, 2008, '2024-01-15 14:20:00', 'Card Issue', 'Credit card declined at merchant', 'Medium',
'Resolved', '2024-01-15 16:45:00', 4),

(9003, 1003, 2012, '2024-01-22 10:45:00', 'Transaction Dispute', 'Unauthorized transaction on account',
'High', 'Resolved', '2024-01-25 14:30:00', 3),
(9004, 1005, 2008, '2024-02-05 11:15:00', 'Loan Inquiry', 'Question about loan payment schedule', 'Low',
'Resolved', '2024-02-05 12:00:00', 5),
(9005, 1006, 2012, '2024-02-12 15:30:00', 'Account Balance', 'Discrepancy in account balance', 'Medium',
'Resolved', '2024-02-13 10:20:00', 4),
(9006, 1008, 2008, '2024-02-18 09:50:00', 'Card Request', 'Request for credit limit increase', 'Low',
'Resolved', '2024-02-20 14:15:00', 5),
(9007, 1009, 2012, '2024-02-25 13:40:00', 'Online Banking', 'Password reset request', 'Medium', 'Resolved',
'2024-02-25 14:10:00', 5),
(9008, 1010, 2008, '2024-03-02 10:20:00', 'Transaction Dispute', 'Wrong amount debited', 'High', 'In
Progress', NULL, NULL),
(9009, 1012, 2012, '2024-03-08 16:15:00', 'Card Issue', 'Lost credit card', 'High', 'Resolved', '2024-03-08
17:30:00', 5),
(9010, 1004, 2008, '2024-03-14 11:30:00', 'Investment Query', 'Portfolio performance inquiry', 'Low',
'Resolved', '2024-03-14 13:45:00', 4);
-- Insert FraudAlerts
INSERT INTO FraudAlerts VALUES
(9501, 1002, 5003, '2024-01-20 03:15:00', 'Unusual Transaction', 75, 'Large withdrawal at unusual hour',
'Resolved', 2009, '2024-01-20 09:30:00', FALSE),
(9502, 1006, 5009, '2024-02-05 23:45:00', 'Multiple Login Attempts', 85, 'Multiple failed login attempts from foreign IP', 'Resolved', 2009, '2024-02-06 10:15:00', TRUE),
(9503, 1003, NULL, '2024-02-15 02:30:00', 'Card Fraud', 92, 'Multiple card transactions in different countries', 'Resolved', 2015, '2024-02-15 11:20:00', TRUE),
(9504, 1009, 5012, '2024-02-28 04:20:00', 'Unusual Transaction', 68, 'Transaction amount significantly above average', 'Resolved', 2009, '2024-02-28 10:45:00', FALSE),
(9505, 1010, 5013, '2024-03-10 01:15:00', 'Account Takeover', 95, 'Suspicious changes to account information', 'Under Investigation', 2015, NULL, NULL);
-- Insert Tools
INSERT INTO Tools VALUES
(1, 'Tableau', 'Data Visualization', 840.00, 'Annual', '2023.3', TRUE),
(2, 'Python', 'Programming', 0.00, 'Open Source', '3.11', TRUE),
(3, 'SQL Server', 'Database', 1200.00, 'Annual', '2022', TRUE),
(4, 'Power BI', 'Data Visualization', 120.00, 'Monthly', 'Pro', TRUE),
(5, 'Excel', 'Spreadsheet', 150.00, 'Annual', '2021', TRUE);
-- Insert AnalystTools
INSERT INTO AnalystTools VALUES
(2007, 1, 'Expert', TRUE, '2024-03-15'),
(2007, 2, 'Advanced', TRUE, '2024-03-10'),
(2007, 3, 'Expert', TRUE, '2024-03-14'),
(2010, 1, 'Expert', TRUE, '2024-03-12'),
(2010, 4, 'Advanced', FALSE, '2024-03-08'),
(2011, 3, 'Expert', TRUE, '2024-03-16'),
(2011, 5, 'Advanced', FALSE, '2024-03-11');
-- Insert TrainingPrograms
INSERT INTO TrainingPrograms VALUES
(501, 'Advanced SQL Analytics', 'Technical', 40, 799.00, 'DataCamp', '2024-01-10', '2024-02-10'),
(502, 'Financial Risk Management', 'Finance', 32, 1200.00, 'CFA Institute', '2024-02-01', '2024-03-01'),
(503, 'Python for Finance', 'Technical', 48, 899.00, 'Coursera', '2024-01-15', '2024-03-15'),

(504, 'Customer Service Excellence', 'Soft Skills', 16, 299.00, 'Internal', '2024-02-15', '2024-02-20'),
(505, 'Fraud Detection Techniques', 'Risk Management', 24, 650.00, 'ACFE', '2024-03-01', '2024-03-20');
-- Insert AnalystTraining
INSERT INTO AnalystTraining VALUES
(10001, 2007, 501, '2024-02-10', 95, TRUE),
(10002, 2010, 502, '2024-03-01', 88, TRUE),
(10003, 2011, 501, '2024-02-10', 92, TRUE),
(10004, 2008, 504, '2024-02-20', 90, TRUE),
(10005, 2009, 505, '2024-03-20', 87, TRUE),
(10006, 2012, 504, '2024-02-20', 85, TRUE),
(10007, 2014, 503, '2024-03-15', 91, TRUE),
(10008, 2015, 505, '2024-03-20', 89, TRUE);