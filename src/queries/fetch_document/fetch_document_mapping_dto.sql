SELECT
    id,
    from_document_id,
    to_document_id,
    relationship_type
FROM vbpl_doc_map
WHERE
    from_document_id = %(document_id)s OR
    to_document_id = %(document_id)s;
