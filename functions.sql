
CREATE OR REPLACE FUNCTION search_contacts(p text)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM phonebook
    WHERE name ILIKE '%' || p || '%'
       OR phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION get_contacts_page(lim INT, off INT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone
    FROM phonebook
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;