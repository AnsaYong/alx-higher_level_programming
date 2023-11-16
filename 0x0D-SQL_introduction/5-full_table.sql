-- Get table description by querying the system tables that store
-- information about the database schema
SELECT COLUMN_NAME, DATA_TYPES, IS_NULLABLE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = first_table;
