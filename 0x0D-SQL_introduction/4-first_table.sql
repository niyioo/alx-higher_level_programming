-- Task: Create a table called first_table in the current database if it doesn't exist.

-- Set the table structure.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
