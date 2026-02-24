-- showing data
SELECT id, name FROM cities INNER JOIN states 
ON states.id = cities.id
ORDER BY id ASC
