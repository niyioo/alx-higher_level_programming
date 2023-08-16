-- List all cities with their IDs, names, and corresponding state names
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;