SELECT p.id, p.name, COUNT(1) AS toy_count FROM people AS p LEFT JOIN toys AS t ON t.people_id = p.id GROUP BY p.id, p.name
