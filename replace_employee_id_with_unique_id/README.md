# Approach
I noticed that I would need to use a JOIN

# Code
```
SELECT uni.unique_id ,emp.name FROM Employees emp
LEFT JOIN EmployeeUNI uni ON emp.id = uni.id;
```