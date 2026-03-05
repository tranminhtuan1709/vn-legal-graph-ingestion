SELECT
    id,
    vbpl_id,
    vbpl_big_part_id,
    chapter_number,
    chapter_name
FROM vbpl_chapter
WHERE vbpl_id = %(document_id)s;
