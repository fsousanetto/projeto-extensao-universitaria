CREATE OR REPLACE FUNCTION insert_student(
    p_name VARCHAR,
    p_date_birth DATE,
    p_cpf VARCHAR,
    p_address VARCHAR,
    p_phone VARCHAR,
    p_email VARCHAR
) RETURNS VOID AS $$
BEGIN
    INSERT INTO student (name, date_birthc, cpf, address, phone, email)
    VALUES (p_name, p_date_birth, p_cpf, p_address, p_phone, p_email);
END;
$$ LANGUAGE plpgsql;
