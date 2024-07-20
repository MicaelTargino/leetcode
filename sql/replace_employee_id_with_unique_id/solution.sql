SELECT uni.unique_id ,emp.name FROM Employees emp
LEFT JOIN EmployeeUNI uni ON emp.id = uni.id;
-- left join was needed to bring the null values too