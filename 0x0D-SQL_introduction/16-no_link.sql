-- Task: List records with names from the table second_table in the specified database.

-- Show records with names, ordered by score (descending).
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
