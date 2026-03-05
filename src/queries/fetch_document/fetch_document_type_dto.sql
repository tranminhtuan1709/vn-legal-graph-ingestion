SELECT
    id,
    loai_van_ban
FROM vbpl_doc_type
WHERE id IN ({document_type_ids});
