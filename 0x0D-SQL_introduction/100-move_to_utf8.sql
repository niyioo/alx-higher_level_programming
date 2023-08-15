-- Task: Convert the hbtn_0c_0 database and the first_table table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).

-- Switch to the hbtn_0c_0 database.
USE hbtn_0c_0;

-- Alter the database character set and collation.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the table character set and collation.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
