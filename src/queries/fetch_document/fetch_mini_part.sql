SELECT
    id,
    vbpl_id,
    vbpl_part_id,
    mini_part_number,
    mini_part_name
FROM vbpl_mini_part
WHERE vbpl_id = %(document_id)s;
