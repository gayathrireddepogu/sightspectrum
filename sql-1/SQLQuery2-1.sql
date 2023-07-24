CREATE DATABASE gayathri;
USE gayathri;
CREATE TABLE student(
stid INT PRIMARY KEY,
sname VARCHAR(20) UNIQUE,
sage INT,
sgender VARCHAR(5),
sgroup VARCHAR(20)
);
INSERT INTO student(stid,sname,sage,sgender,sgroup) VALUES(1,'gayu',21,'f','ece');
select * from student;





