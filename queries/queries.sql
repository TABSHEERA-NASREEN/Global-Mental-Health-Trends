-- Top 5 countries by highest average mental health value\ 
SELECT Country, AVG(Value) as avg_val
FROM mental_health
GROUP BY Country
ORDER BY avg_val DESC
LIMIT 5;

-- Trend over years
SELECT Year, AVG(Value) as avg_val
FROM mental_health
GROUP BY Year
ORDER BY Year;
