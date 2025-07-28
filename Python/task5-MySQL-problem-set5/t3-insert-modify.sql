INSERT INTO users (user_id, name, age, department, email) VALUES
(101, 'Ananya', 22, 'Computer Science', 'ananya23@gmail.com'),
(102, 'Raj', 19, 'Mechanical', 'raj345@gmail.com'),
(103, 'Sneha', 23, 'Electronics', 'sneha897@gmail.com'),
(104, 'Arjun', 20, 'Civil', 'arjun123@gmail.com'),
(105, 'Meera', 21, 'Information Tech', 'meera2157@gmail.com');


UPDATE users SET department = 'Computer Science' WHERE user_id =103;


DELETE FROM users WHERE user_id = 105;



