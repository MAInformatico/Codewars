 SELECT p.id, p.name, COUNT(s.sale) AS sale_count, RANK() OVER (ORDER BY COUNT(s.sale)) AS sale_rank
 FROM people p JOIN sales s ON s.people_id = p.id
 GROUP BY p.id;
