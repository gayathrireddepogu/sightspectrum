create database gayu;
drop database gayu;
use gayu;
create table class_1(
   sid int,sname varchar(10),
   sgender varchar(10)
);
select * from class_1;
insert into class_1 values (1,'gayu','f');
drop table class_1;
create table employee(
eid int primary key,ename varchar(50)
);
drop table employee;
select * from employee;
insert into employee values(1,'srihan');
commit;
rollback;


