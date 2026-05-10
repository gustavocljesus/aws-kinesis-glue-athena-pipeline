-- Objetivo: consultar registros de um intervalo de datas
-- para investigação de possíveis falhas operacionais

SELECT
    id,
    type,
    data,
    event_timestamp,
    ROW_NUMBER() OVER (
        PARTITION BY id
        ORDER BY event_timestamp
    ) AS grupo_ordenado
FROM my_pipeline_engdados_project
WHERE data BETWEEN DATE '2026-02-05' AND DATE '2026-02-09'
ORDER BY id, grupo_ordenado;

