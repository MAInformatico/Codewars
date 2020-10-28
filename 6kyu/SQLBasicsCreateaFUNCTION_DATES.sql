-- Working on: PostgreSQL
CREATE FUNCTION agecalculator(date timestamp) RETURNS integer AS $$
BEGIN
  RETURN (SELECT EXTRACT(year FROM age(date)))::int;
END;
 $$ LANGUAGE plpgsql;   
