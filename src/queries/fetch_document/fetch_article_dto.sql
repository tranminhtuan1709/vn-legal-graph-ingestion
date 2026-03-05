SELECT
    id,
    vbpl_id,
    vbpl_big_part_id,
    vbpl_chapter_id,
    vbpl_part_id,
    vbpl_mini_part_id,
    section_number,
    section_name,
    section_content,
    so_phu_luc,
    effective_date
FROM vbpl_section
WHERE vbpl_id = %(document_id)s;
