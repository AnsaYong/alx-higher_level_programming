-- Lists all cities contained in the database hbtn_0d_usa
-- List all cities with their IDs, names, and corresponding state names
SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM hbtn_0d_usa.cities
JOIN hbtn_0d_usa.states ON cities.state_id = states.id
ORDER BY cities.id ASC;
