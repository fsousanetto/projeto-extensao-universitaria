CREATE OR REPLACE FUNCTION insert_registration(
    p_id_student INT,
    p_id_course INT,
    p_data_birth DATE
) RETURNS VOID AS $$
BEGIN
    INSERT INTO registration (id_student, id_course, data_birth)
    VALUES (p_id_student, p_id_course, p_data_birth);
END;
$$ LANGUAGE plpgsql;
