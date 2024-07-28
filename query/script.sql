
SELECT * FROM student;

SELECT * FROM course;

SELECT * FROM teacher_registration;

SELECT c.id, c.name, co.name AS course_name, t.name AS teacher_name, c.schedule
FROM class c
JOIN course co ON c.id_course = co.id
JOIN teacher_registration t ON c.id_prof = t.id;

SELECT s.name AS student_name, co.name AS course_name, r.data_birth
FROM registration r
JOIN student s ON r.id_student = s.id
JOIN course co ON r.id_course = co.id
WHERE s.name = 'João Silva';

SELECT d.date, d.begin, d.finish, d.local
FROM discipline d
JOIN course c ON d.id_course = c.id
WHERE c.name = 'Dança Clássica';
