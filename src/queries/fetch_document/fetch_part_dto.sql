SELECT
    id,
    vbpl_id,
    vbpl_chapter_id,
    part_number,
    part_name
FROM vbpl_big_part
WHERE vbpl_id = %(document_id)s;
