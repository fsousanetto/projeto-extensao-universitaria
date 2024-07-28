CREATE OR REPLACE FUNCTION insert_class(
    p_id_course INT,
    p_id_prof INT,
    p_name VARCHAR,
    p_schedule TIME
) RETURNS VOID AS $$
BEGIN
    INSERT INTO class (id_course, id_prof, name, schedule)
    VALUES (p_id_course, p_id_prof, p_name, p_schedule);
END;
$$ LANGUAGE plpgsql;
