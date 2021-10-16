CREATE TABLE PATIENTS
    (
      CUSTOMER_NAME VARCHAR(255) PRIMARY KEY,
      CUSTOMER_ID VARCHAR(18) NOT NULL,
      CUSTOMER_OPEN_DATE DATE NOT NULL,
      LAST_CONSULTED_DATE DATE,
      VACCINATION_TYPE CHAR(5),
      DOCTOR_CONSULTED CHAR(255),
      STATE CHAR(5),
      COUNTRY CHAR(5),
      DOB DATE,
      FLAG CHAR(1)
      ); 
INSERT into multi_spe_hospital.patients values('Alex', '123457', '2010-10-12', '2012-10-13', 'MVD', 'Paul', 'SA' ,'USA' ,'1987-03-06', 'A'),
                           ('John', '123458', '2010-10-12', '2012-10-13', 'MVD','', 'TN', 'IND','1987-03-06','A'),
('Mathew','123459','2010-10-12','2012-10-13','MVD','','WAS','PHIL','1987-03-06','A'),
('Matt','12345','2010-10-12','2012-10-13','MVD','','BOS','NYC','1987-03-06','A'),
('Jacob', '1256', '2010-10-12','2012-10-13','MVD','', 'VIC', 'AU', '1987-03-06' ,'A');
SELECT * FROM multi_spe_hospital.patients;