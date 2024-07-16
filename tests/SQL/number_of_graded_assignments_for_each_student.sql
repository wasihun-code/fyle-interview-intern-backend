-- Write query to get number of graded assignments for each student:
SELECT COUNT(*)
FROM assignments 
WHERE grade IS NOT NULL 
GROUP BY student_id;
