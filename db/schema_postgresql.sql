/* CUSTOMERS */

CREATE TABLE customers (
  customerNumber SERIAL PRIMARY KEY,
  customerName varchar(50) NOT NULL,
  contactFirstName varchar(50) NOT NULL,
  phone varchar(50) NOT NULL,
  address varchar(50) NOT NULL,
  city varchar(50) NOT NULL,
  state varchar(50) DEFAULT NULL,
  postalCode varchar(15) DEFAULT NULL,
  country varchar(50) NOT NULL,
  salesRepEmployeeNumber int DEFAULT NULL,
  creditLimit decimal(10,2) DEFAULT NULL
);


/* EMPLOYEES */

CREATE TABLE employees (
  employeeNumber SERIAL PRIMARY KEY,
  Name varchar(50) NOT NULL,
  extension varchar(10) NOT NULL,
  email varchar(100) NOT NULL,
  reportsTo int DEFAULT NULL,
  jobTitle varchar(50) NOT NULL,
  officeCity varchar(50) NOT NULL,
  officePhone varchar(50) NOT NULL,
  officeAddress varchar(50) NOT NULL,
  officeState varchar(50) DEFAULT NULL,
  officeCountry varchar(50) NOT NULL,
  officePostalCode varchar(15) NOT NULL,
  officeTerritory varchar(10) NOT NULL
);



/* PAYMENTS */

CREATE TABLE payments (
  customerNumber int NOT NULL,
  checkNumber varchar(50) NOT NULL,
  paymentDate date NOT NULL,
  amount decimal(10,2) NOT NULL,
  PRIMARY KEY (customerNumber,checkNumber),
  constraint fk_payments_customers foreign key (customerNumber) REFERENCES customers (customerNumber)
);


/* PRODUCTS */


CREATE TABLE products (
  productCode varchar(15) NOT NULL,
  productName varchar(70) NOT NULL,
  productLine varchar(50) NOT NULL,
  lineTextDescription varchar(4000) DEFAULT NULL,
  lineHtmlDescription text,
  lineImage bytea,
  PRIMARY KEY (productCode)
);


