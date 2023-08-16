-- Create the user 'user_0d_1' with the password 'user_0d_1_pwd' if the user doesn't already exist
CREATE USER
    IF NOT EXISTS 'user_0d_1'
    IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges on all databases and tables to the user 'user_0d_1' when connecting from the 'localhost' host
GRANT ALL PRIVILEGES
    ON *.*
    TO 'user_0d_1'@'localhost';
