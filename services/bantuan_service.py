from services.anomaly_service import check_anomaly


def recommend_bantuan(data):

    # ============================================
    # 1️⃣ ANOMALY CHECK (Layer Audit)
    # ============================================

    anomaly_result = check_anomaly(data)
    is_anomaly = anomaly_result["is_anomaly"]
    anomaly_score = anomaly_result["anomaly_score"]

    # ============================================
    # 2️⃣ BASE URGENCY CALCULATION
    # ============================================

    base_urgency = 0

    if data.economic_score <= 2:
        base_urgency += 40

    if data.employment_flag == 0:
        base_urgency += 25

    if data.age_bucket == 3:
        base_urgency += 20

    # ============================================
    # 3️⃣ HITUNG TOTAL EXISTING PROGRAM
    # ============================================

    total_existing = sum([
        data.penerima_bpnt,
        data.penerima_bst,
        data.penerima_pkh,
        data.penerima_sembako,
        data.penerima_prakerja,
        data.penerima_kur,
        data.penerima_cbp
    ])

    # Penalti jika sudah banyak bantuan
    if total_existing >= 3:
        base_urgency -= 15

    # Penalti tambahan jika anomali
    if is_anomaly:
        base_urgency -= 10

    # ============================================
    # 4️⃣ EVALUASI PROGRAM
    # ============================================

    candidates = []
    eligible_but_receiving = []

    # -------------------------
    # PKH (Lansia Miskin)
    # -------------------------

    if data.age_bucket == 3 and data.economic_score <= 2:

        reason = "Lansia dengan kondisi ekonomi rendah"

        if not data.penerima_pkh:
            candidates.append({
                "program": "PKH",
                "score": base_urgency + 10,
                "reason": reason
            })
        else:
            eligible_but_receiving.append({
                "program": "PKH",
                "reason": reason
            })

    # -------------------------
    # Prakerja (Produktif Tidak Bekerja)
    # -------------------------

    if data.employment_flag == 0 and data.age_bucket == 2:

        reason = "Usia produktif dan tidak bekerja"

        if not data.penerima_prakerja:
            candidates.append({
                "program": "Prakerja",
                "score": base_urgency + 5,
                "reason": reason
            })
        else:
            eligible_but_receiving.append({
                "program": "Prakerja",
                "reason": reason
            })

    # -------------------------
    # Bantuan Tunai
    # -------------------------

    if data.economic_score <= 2:

        reason = "Desil rendah dan membutuhkan bantuan langsung"

        if not data.penerima_bpnt and not data.penerima_bst:
            candidates.append({
                "program": "Bantuan Tunai",
                "score": base_urgency,
                "reason": reason
            })
        else:
            eligible_but_receiving.append({
                "program": "Bantuan Tunai",
                "reason": reason
            })

    # -------------------------
    # UMKM Support
    # -------------------------

    if data.employment_flag == 1 and data.economic_score <= 3:

        reason = "Memiliki aktivitas ekonomi dan perlu penguatan usaha"

        if not data.penerima_kur:
            candidates.append({
                "program": "UMKM Support",
                "score": base_urgency - 5,
                "reason": reason
            })
        else:
            eligible_but_receiving.append({
                "program": "UMKM Support",
                "reason": reason
            })

    # ============================================
    # 5️⃣ AMBIL 1 PROGRAM PRIORITAS TERTINGGI
    # ============================================

    if candidates:
        candidates = sorted(candidates, key=lambda x: x["score"], reverse=True)
        top_program = candidates[0]
    else:
        top_program = None

    # ============================================
    # 6️⃣ RESPONSE FINAL
    # ============================================

    return {
        "recommended_program": top_program,
        "urgency_score": max(base_urgency, 0),
        "needs_verification": True if is_anomaly else False,
        "anomaly_score": anomaly_score,
        "eligible_but_already_receiving": eligible_but_receiving,
        "total_existing_programs": total_existing
    }