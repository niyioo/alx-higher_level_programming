-- Create the table 'unique_id' with columns 'id' (INT) and 'name' (VARCHAR)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);