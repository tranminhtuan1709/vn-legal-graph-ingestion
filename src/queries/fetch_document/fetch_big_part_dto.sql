SELECT
    id,
    vbpl_id,
    big_part_number,
    big_part_name
FROM vbpl_big_part
WHERE vbpl_id = %(document_id)s;
