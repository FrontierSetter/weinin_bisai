SELECT	
    VIN, collectTime, longitude, latitude 
FROM  
    E100_LOC_BATCH 
WHERE 
    ID IN (
        SELECT 
            max( ID ) 
        FROM
            E100_LOC_BATCH
        WHERE 
            addTime IN (
                SELECT
                    max( addTime )
                FROM 
                    E100_LOC_BATCH
                WHERE 
                    UNIX_TIMESTAMP( addTime ) <  1593302400
                GROUP BY
                    VIN ) 
            GROUP BY VIN )
    ;
    
122 rows in set (22.32 sec)


-- ====================================================================

SELECT	
    VIN, collectTime, longitude, latitude 
FROM  
    E100_LOC_BATCH 
WHERE 
    ID IN (
        SELECT 
            max( ID ) 
        FROM
            E100_LOC_BATCH
        WHERE 
            UNIX_TIMESTAMP( addTime ) <  1593302400 
        GROUP BY 
            VIN )
    ;

122 rows in set (15.19 sec)

-- ========================================================

SELECT	
    VIN, collectTime, longitude, latitude 
FROM  
    E100_LOC_BATCH 
WHERE 
    ID IN (
        SELECT 
            max( ID ) 
        FROM
            E100_LOC_BATCH
        WHERE 
            UNIX_TIMESTAMP( addTime ) < 1593302400 AND UNIX_TIMESTAMP( addTime ) > 1588118400
        GROUP BY 
            VIN )
    ;

122 rows in set (15.32 sec)
-- ====================================================
SELECT * FROM (SELECT * FROM posts ORDER BY dateline DESC) BIAOMING GROUP BY tid ORDER BY dateline DESC LIMIT 10

SELECT	
    VIN, collectTime, longitude, latitude 
FROM (
    SELECT
        *
    FROM
        E100_LOC_BATCH
    ORDER BY
        collectTime DESC) BIAOMING
GROUP BY 
    VIN
ORDER BY
    collectTime DESC
LIMIT 
    10
;

sql_mode=only_full_group_by

-- ===========================================

SELECT 
    max( ID ) 
FROM
    E100_LOC_BATCH
WHERE 
    UNIX_TIMESTAMP( addTime ) < 1593302400 AND UNIX_TIMESTAMP( addTime ) > 1588118400
GROUP BY 
    VIN 
;

122 rows in set (9.25 sec)

SELECT 
    max( ID ) 
FROM
    E100_LOC_BATCH
WHERE 
    UNIX_TIMESTAMP( addTime ) BETWEEN 1588118400 AND 1593302400
GROUP BY 
    VIN 
;
122 rows in set (8.96 sec)

-- ===========================================

SELECT	
    VIN, collectTime, longitude, latitude 
FROM  
    E100_LOC_BATCH 
WHERE 
    EXISTS (
        SELECT 
            1
        FROM (
            SELECT 
                max( ID ) 
            FROM
                E100_LOC_BATCH
            WHERE 
                UNIX_TIMESTAMP( addTime ) BETWEEN 1588118400 AND 1593302400
            GROUP BY 
                VIN ) BIAOMING
        WHERE
            E100_LOC_BATCH.ID = ID  
    )
;

CREATE INDEX vin_index
ON E100_LOC_BATCH (VIN)