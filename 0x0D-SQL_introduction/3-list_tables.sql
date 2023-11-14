-- SQL script with a stored procedure to list all tables in a given database

DELIMITER //
CREATE PROCEDURE ListTables(IN target_database VARCHAR(255))
BEGIN
    -- List all tables in the specified database
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = target_database;
END //
DELIMITER ;
