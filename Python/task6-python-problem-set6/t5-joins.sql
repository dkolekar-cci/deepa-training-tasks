SELECT Students.name, Courses.course_name FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.student_id
JOIN Courses ON Enrollments.course_id = Courses.course_id;

SELECT Students.name, Courses.course_name, Enrollments.marks FROM Enrollments
JOIN Students ON Enrollments.student_id = Students.student_id
JOIN Courses ON Enrollments.course_id = Courses.course_id;

SELECT Courses.course_name, AVG(Enrollments.marks) AS average_marks FROM Enrollments
JOIN Courses ON Enrollments.course_id = Courses.course_id
GROUP BY Courses.course_name;

SELECT Students.name FROM Students
LEFT JOIN Enrollments ON Students.student_id = Enrollments.student_id
WHERE Enrollments.enrollment_id IS NULL;


