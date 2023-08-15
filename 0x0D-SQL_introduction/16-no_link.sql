-- Lists all records of the  second_table having a name value
-- Records are ordered by a descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
