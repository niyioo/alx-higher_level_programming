-- Create the database 'hbtn_0d_2' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user 'user_0d_2' with the password 'user_0d_2_pwd' if the user doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on all tables in the 'hbtn_0d_2' database to the user 'user_0d_2' from 'localhost'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
