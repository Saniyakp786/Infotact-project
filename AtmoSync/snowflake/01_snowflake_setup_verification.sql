-- AtmoSync Day 25: Snowflake Setup Verification
-- Read-only checks. These commands do not create, replace, or delete objects.

-- 1. Verify available warehouses
SHOW WAREHOUSES;

-- 2. Verify ATMOSYNC database
SHOW DATABASES LIKE 'ATMOSYNC';

-- 3. Verify schemas
SHOW SCHEMAS IN DATABASE ATMOSYNC;

-- 4. Verify RAW tables
SHOW TABLES IN SCHEMA ATMOSYNC.RAW;

-- 5. Verify Intermodal Rail record count
SELECT COUNT(*) AS ROW_COUNT
FROM ATMOSYNC.RAW.INTERMODAL_RAIL;