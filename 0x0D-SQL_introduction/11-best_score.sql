-- Lists records based on their valuse from the score column
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
