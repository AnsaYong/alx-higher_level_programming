-- Lists all records of a table, excluding records missing certain values
SELECT score, name FROM second_table
WHERE name <> ''
ORDER BY score DESC;
