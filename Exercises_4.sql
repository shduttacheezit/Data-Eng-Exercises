4. SQL Query-- 

CREATE TABLE customer (
    customer_id integer NOT NULL,
    name character varying(64) NOT NULL,
    address character varying(255) NOT NULL,
    phone character varying(15) NOT NULL
);

CREATE TABLE order (
    customer_id integer NOT NULL,
    pizza_id integer NOT NULL,
    quantity integer NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE pizza (
    pizza_id integer NOT NULL,
    name character varying(64) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Query to find all customers that ordered a pepperoni pizza in the last 30 days.   

SELECT Customer.Name AS CustomersWhoLovePepperoni, Order.Order_Date AS OrderDate, Pizza.name AS Pizza
FROM Customer 
    LEFT JOIN Order ON Customer.customer_id=Order.customer_id
    LEFT JOIN Pizza ON Order.Pizza_ID=Pizza.Pizza_ID 
WHERE Pizza.Name LIKE '%pepperoni%' AND Order.Order_Date BETWEEN datetime('now', '-30 days') AND datetime('now', 'localtime');


-- The following solution is in the case that there is only one customer who spent the most money in the last 30 days. 

SELECT Customer.Name AS CustomerWhoLovesPizzaMost, (Order.quantity * Pizza.price) AS Spent
From Customer 
    LEFT JOIN Order ON Customer.customer_id=Order.customer_id
    LEFT JOIN Pizza ON Order.Pizza_ID=Pizza.Pizza_ID 
WHERE Order.Order_Date BETWEEN datetime('now', '-30 days') AND datetime('now', 'localtime') 
ORDER BY Spent DESC
LIMIT 1;

