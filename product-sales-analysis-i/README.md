# Approach
I noticed that I would need to use a JOIN. In this case, an INNER JOIN, because I only want to bring the values that have a corresponding matching value in each table.

# Code
```
SELECT Product.product_name, Sales.year, Sales.price FROM Sales
INNER JOIN Product
ON Sales.product_id = Product.product_id
```