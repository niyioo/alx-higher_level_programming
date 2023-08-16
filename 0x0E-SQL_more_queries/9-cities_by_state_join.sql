-- List all cities with their IDs, names, and corresponding state names
SELECT cities.id, cities.name, states.name AS state_name
FROM states
INNER JOIN cities ON cities.state_id = states.id
ORDER BY cities.id ASC;
