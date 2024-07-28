CREATE OR REPLACE FUNCTION insert_discipline(
    p_id_course INT,
    p_date DATE,
    p_begin TIME,
    p_finish TIME,
    p_local VARCHAR
) RETURNS VOID AS $$
BEGIN
    INSERT INTO discipline (id_course, date, begin, finish, local)
    VALUES (p_id_course, p_date, p_begin, p_finish, p_local);
END;
$$ LANGUAGE plpgsql;
