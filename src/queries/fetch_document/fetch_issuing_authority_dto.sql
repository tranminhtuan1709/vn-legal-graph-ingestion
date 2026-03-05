SELECT
    id,
    co_quan_ban_hanh
FROM vbpl_issuing_authority
WHERE id IN ({issuing_authority_ids});
