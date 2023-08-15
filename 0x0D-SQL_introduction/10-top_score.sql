-- Task: List all records of the table second_table from the specified database.

-- Set the database name provided as an argument.
SET @db_name = hbtn_0c_0;

-- Show all records from the table, ordered by score (top first).
SELECT score, name
FROM @hbtn_0c_0.second_table
ORDER BY score DESC;
