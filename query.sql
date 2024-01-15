WITH users AS (

  SELECT 'John Doe' as name, 'john.doe@example.com' as email
  UNION
  SELECT 'Jane Smith' as name, 'jane.smith@example.com' as email
  UNION
  SELECT 'Samuel Jackson' as name, 'samuel.jackson@example.com' as email

)
-- Retrieve some records from the users table
SELECT * 
FROM users
WHERE name LIKE 'J%';
