USE StudentDB;
CREATE TABLE Students(
StudentID INT IDENTITY(1,1) PRIMARY KEY,
Name VARCHAR(50),
Age INT,
Course VARCHAR(50)
);
INSERT INTO Students(Name,Age,Course)
VALUES('Swetha',22,'Python');
SELECT*FROM Students;