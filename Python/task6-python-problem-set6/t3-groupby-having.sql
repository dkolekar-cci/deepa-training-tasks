SELECT department, COUNT(*) AS total_students FROM Students GROUP BY department;

SELECT department, COUNT(*) AS student_count FROM Students GROUP BY department HAVING COUNT(*) > 1;

SELECT course_id, AVG(marks) AS average_marks FROM Enrollments GROUP BY course_id;
