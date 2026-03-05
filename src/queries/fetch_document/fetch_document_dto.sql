SELECT
    id,
    so_ky_hieu,
    ten_hien_thi,
    DATE(ngay_ban_hanh) AS ngay_ban_hanh,
    DATE(ngay_co_hieu_luc) AS ngay_co_hieu_luc,
    DATE(ngay_het_han) AS ngay_het_han,
    trang_thai,
    chu_thich_nho,
    loai_van_ban,
    id_loai_van_ban,
    linh_vuc,
    id_linh_vuc,
    co_quan_ban_hanh,
    id_co_quan_ban_hanh
FROM vbpl
WHERE id = %(document_id)s;
