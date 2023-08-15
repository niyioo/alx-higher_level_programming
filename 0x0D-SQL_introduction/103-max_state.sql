-- Task: Display the max temperature of each state ordered by State name.

-- Select the max temperature of each state.
SELECT state, MAX(temp_fahrenheit) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
