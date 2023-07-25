CREATE DATABASE string;
USE string;
CREATE TABLE collect (
colid INT PRIMARY KEY,
colname VARCHAR(200),
colemail VARCHAR(255),
colgender VARCHAR(20) 
);
INSERT INTO collect (colid,colname, colemail,colgender) VALUES (1,'GAYU', 'gayathri6.sightspectrum@gmail.com','f');
INSERT INTO collect (colid,colname, colemail,colgender) VALUES (2,'Gopi', 'gopi.sightspectrum@gmail.com','m');
INSERT INTO collect (colid,colname, colemail,colgender) VALUES (3,'janu', 'janu.sightspectrum@gmail.com','f');
INSERT INTO collect (colid,colname, colemail,colgender) VALUES (4,'sailu', 'sailu.sightspectrum@gmail.com','f');
INSERT INTO collect (colid,colname, colemail,colgender) VALUES (5,'rufi', 'rufi.sightspectrum@gmail.com','f');
SELECT * FROM collect;
