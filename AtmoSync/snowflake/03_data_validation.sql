-- AtmoSync: Intermodal Rail Data Validation

-- 1. Check total number of records
SELECT COUNT(*) AS ROW_COUNT
FROM ATMOSYNC.RAW.INTERMODAL_RAIL;

-- 2. Preview first 5 records
SELECT *
FROM ATMOSYNC.RAW.INTERMODAL_RAIL
LIMIT 5;