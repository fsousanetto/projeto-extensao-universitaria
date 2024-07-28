CREATE OR REPLACE FUNCTION insert_teacher_registration(
    p_name VARCHAR,
    p_speciality VARCHAR,
    p_phone VARCHAR,
    p_email VARCHAR
) RETURNS VOID AS $$
BEGIN
    INSERT INTO teacher_registration (name, speciality, phone, email)
    VALUES (p_name, p_speciality, p_phone, p_email);
END;
$$ LANGUAGE plpgsql;
