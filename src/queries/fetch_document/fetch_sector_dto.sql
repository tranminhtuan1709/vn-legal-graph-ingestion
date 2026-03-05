SELECT
    id,
    linh_vuc
FROM vbpl_sector
WHERE id IN ({sector_ids});
