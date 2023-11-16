-- List all cities of California without using JOIN
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
