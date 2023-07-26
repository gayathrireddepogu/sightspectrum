create database school;
use school;
create table students(id int primary key,name varchar(30),marks int,percentage decimal(3,2));
select * from students
insert into students values(1,'sai',78,2.5),(2,'sai',34,4.35);
alter table students add class int;
update students
set class = 67 
where id = 1
update  students 
set class = 68
where id = 2
select id,name,marks,class from students;
select * from students;
update students 
set class = 43
where id = 1
update students
set marks = 76
where id = 2
alter table mark as 'percentage' and percentage as 'mark'; 