CREATE OR REPLACE FUNCTION insert_course(
    p_name VARCHAR,
    p_description TEXT,
    p_duration INT,
    p_type VARCHAR
) RETURNS VOID AS $$
BEGIN
    INSERT INTO course (name, description, duration, type)
    VALUES (p_name, p_description, p_duration, p_type);
END;
$$ LANGUAGE plpgsql;
