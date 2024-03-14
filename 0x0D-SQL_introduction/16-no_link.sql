-- list all rows except where name is NULL

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ""
ORDER BY score DESC;
