# Approach
I noticed that I would need to use a JOIN. in this case, a LEFT JOIN, because I wanted to bring all the values from the Employees table, and the matching values of the EmployeeUNI table, to bring the null values from the employees too.

# Code
```sql
SELECT uni.unique_id ,emp.name FROM Employees emp
LEFT JOIN EmployeeUNI uni ON emp.id = uni.id;
```
