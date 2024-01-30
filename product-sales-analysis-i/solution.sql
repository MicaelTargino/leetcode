SELECT Product.product_name, Sales.year, Sales.price FROM Sales
INNER JOIN Product
ON Sales.product_id = Product.product_id
-- inner join because only bring the values that have a correspondent match in each table