# ============================================================
#   MATEMATIKA DISKRIT — BEDA SETANGKUP (SYMMETRIC DIFFERENCE)
#   Implementasi: A ⊕ B = (A ∪ B) - (A ∩ B)
# ============================================================
# Dibuat sebagai bahan ajar Matematika Diskrit
# Topik: Operasi Himpunan — Beda Setangkup
# ============================================================


# ─────────────────────────────────────────────
# BAGIAN 1: FUNGSI OPERASI HIMPUNAN DASAR
# ─────────────────────────────────────────────

def gabungan(A: set, B: set) -> set:
    """
    Menghitung GABUNGAN (Union) dua himpunan.
    A ∪ B = himpunan semua elemen yang ada di A, di B, atau keduanya.
    """
    return A | B  # Operator '|' adalah union bawaan Python


def irisan(A: set, B: set) -> set:
    """
    Menghitung IRISAN (Intersection) dua himpunan.
    A ∩ B = himpunan semua elemen yang ada di A DAN juga di B.
    """
    return A & B  # Operator '&' adalah intersection bawaan Python


def beda_setangkup(A: set, B: set) -> set:
    """
    Menghitung BEDA SETANGKUP (Symmetric Difference) dua himpunan.

    DEFINISI:
        A ⊕ B = (A ∪ B) - (A ∩ B)
        Yaitu: elemen yang ada di A atau B, tetapi TIDAK keduanya sekaligus.

    LANGKAH ALGORITMA:
        Step 1: Hitung gabungan  → A ∪ B
        Step 2: Hitung irisan    → A ∩ B
        Step 3: Kurangi          → (A ∪ B) - (A ∩ B)
    """
    union = gabungan(A, B)          # Step 1: A ∪ B
    intersection = irisan(A, B)     # Step 2: A ∩ B
    hasil = union - intersection    # Step 3: Selisih keduanya
    return hasil


# ─────────────────────────────────────────────
# BAGIAN 2: FUNGSI VALIDASI INPUT
# ─────────────────────────────────────────────

def parse_input(teks: str, nama_himpunan: str) -> set:
    """
    Mem-parsing input string menjadi himpunan bilangan bulat.
    Contoh input: "2 4 6" → {2, 4, 6}
    Melakukan validasi: setiap elemen harus berupa angka.
    """
    elemen = teks.strip().split()  # Pisahkan input berdasarkan spasi

    if not elemen:
        raise ValueError(f"Himpunan {nama_himpunan} tidak boleh kosong!")

    hasil_set = set()
    for item in elemen:
        if not item.lstrip('-').isdigit():  # Izinkan angka negatif
            raise ValueError(
                f"'{item}' bukan bilangan bulat yang valid "
                f"untuk himpunan {nama_himpunan}!"
            )
        hasil_set.add(int(item))

    return hasil_set


# ─────────────────────────────────────────────
# BAGIAN 3: VISUALISASI TEXT-BASED
# ─────────────────────────────────────────────

def format_himpunan(s: set) -> str:
    """Menampilkan himpunan dalam format matematika: {a, b, c}"""
    if not s:
        return "∅ (himpunan kosong)"
    return "{" + ", ".join(str(x) for x in sorted(s)) + "}"


def visualisasi_diagram(A: set, B: set):
    """
    Menampilkan diagram Venn sederhana menggunakan karakter ASCII.
    Menunjukkan area A saja, irisan, dan B saja.
    """
    hanya_A = A - B          # Elemen eksklusif A
    irisan_AB = A & B        # Elemen bersama
    hanya_B = B - A          # Elemen eksklusif B

    print("\n  📊 DIAGRAM VENN (ASCII):")
    print("  " + "─" * 55)

    # Baris judul
    lebar = 55
    print(f"  {'Himpunan A':^18} {'∩':^3} {'Himpunan B':^18}")
    print("  " + "─" * 55)

    # Konversi ke list terurut untuk tampilan
    la = sorted(hanya_A)
    li = sorted(irisan_AB)
    lb = sorted(hanya_B)
    baris = max(len(la), len(li), len(lb), 1)

    for i in range(baris):
        ea = str(la[i]) if i < len(la) else ""
        ei = str(li[i]) if i < len(li) else ""
        eb = str(lb[i]) if i < len(lb) else ""
        print(f"  │ {ea:^16} │ {ei:^9} │ {eb:^16} │")

    print("  " + "─" * 55)
    print(f"  │ {'(hanya di A)':^16} │ {'(di A&B)':^9} │ {'(hanya di B)':^16} │")
    print("  " + "─" * 55)

    print()
    # Keterangan warna area beda setangkup
    print("  🔵 Beda Setangkup  = area KIRI + area KANAN (tanpa tengah)")
    print(f"  🔵 Elemen di A saja : {format_himpunan(hanya_A)}")
    print(f"  🔴 Elemen irisan    : {format_himpunan(irisan_AB)}  ← DIBUANG")
    print(f"  🟢 Elemen di B saja : {format_himpunan(hanya_B)}")


def tampilkan_proses(A: set, B: set):
    """
    Menampilkan seluruh proses perhitungan beda setangkup
    secara bertahap dan terstruktur.
    """
    union = gabungan(A, B)
    intersection = irisan(A, B)
    hasil = beda_setangkup(A, B)

    # ── Header ──────────────────────────────────────
    print("\n" + "═" * 60)
    print("  🔢  BEDA SETANGKUP (Symmetric Difference)  ⊕")
    print("═" * 60)

    # ── Input ───────────────────────────────────────
    print("\n  📥 INPUT HIMPUNAN:")
    print(f"     A = {format_himpunan(A)}")
    print(f"     B = {format_himpunan(B)}")

    # ── Diagram Venn ────────────────────────────────
    visualisasi_diagram(A, B)

    # ── Langkah-langkah ─────────────────────────────
    print("\n  📐 LANGKAH PERHITUNGAN:")
    print("  " + "─" * 50)

    print(f"\n  Step 1 │ Hitung A ∪ B (Gabungan/Union)")
    print(f"         │ A ∪ B = semua elemen dari A dan B")
    print(f"         │ A ∪ B = {format_himpunan(union)}")

    print(f"\n  Step 2 │ Hitung A ∩ B (Irisan/Intersection)")
    print(f"         │ A ∩ B = elemen yang ada di A DAN di B")
    print(f"         │ A ∩ B = {format_himpunan(intersection)}")

    print(f"\n  Step 3 │ Kurangi: (A ∪ B) - (A ∩ B)")
    print(f"         │ = {format_himpunan(union)} - {format_himpunan(intersection)}")
    print(f"         │ = buang elemen irisan dari gabungan")

    # ── Hasil ───────────────────────────────────────
    print("\n" + "═" * 60)
    print(f"  ✅ HASIL:  A ⊕ B = {format_himpunan(hasil)}")
    print("═" * 60)

    # ── Verifikasi Manual ───────────────────────────
    print("\n  🔍 VERIFIKASI MANUAL:")
    print(f"     • Elemen di A saja     : {format_himpunan(A - B)}")
    print(f"     • Elemen di B saja     : {format_himpunan(B - A)}")
    print(f"     • Gabungan keduanya    : {format_himpunan((A - B) | (B - A))}")
    print(f"     • Sama dengan A ⊕ B?  : {'✅ YA' if hasil == (A - B) | (B - A) else '❌ TIDAK'}")

    # ── Properti ────────────────────────────────────
    print("\n  📌 PROPERTI YANG TERPENUHI:")
    print(f"     • Komutatif  (A⊕B = B⊕A)  : "
          f"{'✅' if beda_setangkup(A, B) == beda_setangkup(B, A) else '❌'}")
    print(f"     • |A⊕B| = |A|+|B|-2|A∩B| : "
          f"{'✅' if len(hasil) == len(A)+len(B)-2*len(intersection) else '❌'}")

    print()


# ─────────────────────────────────────────────
# BAGIAN 4: CONTOH DEMO LANGSUNG
# ─────────────────────────────────────────────

def demo_contoh():
    """Menjalankan contoh kasus bawaan sesuai spesifikasi tugas."""
    print("\n" + "━" * 60)
    print("  📚 CONTOH KASUS (Demo Otomatis)")
    print("━" * 60)
    print("  A = {2, 4, 6}   |   B = {2, 3, 5}")

    A = {2, 4, 6}
    B = {2, 3, 5}
    tampilkan_proses(A, B)

    # Contoh tambahan: irisan kosong
    print("\n" + "━" * 60)
    print("  📚 CONTOH KASUS 2 (Irisan Kosong)")
    print("━" * 60)
    print("  A = {1, 3, 5}   |   B = {2, 4, 6}")

    A2 = {1, 3, 5}
    B2 = {2, 4, 6}
    tampilkan_proses(A2, B2)


# ─────────────────────────────────────────────
# BAGIAN 5: MAIN — PROGRAM UTAMA
# ─────────────────────────────────────────────

def main():
    """
    Fungsi utama program.
    Menampilkan menu: jalankan demo atau masukkan input sendiri.
    """
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + "  MATEMATIKA DISKRIT — BEDA SETANGKUP (A ⊕ B)  ".center(58) + "║")
    print("║" + "  Implementasi: (A ∪ B) - (A ∩ B)  ".center(58) + "║")
    print("╚" + "═" * 58 + "╝")

    print("\n  Pilih mode:")
    print("  [1] Jalankan contoh demo otomatis")
    print("  [2] Masukkan himpunan sendiri")
    print("  [3] Keduanya")

    pilihan = input("\n  Pilihan Anda (1/2/3): ").strip()

    if pilihan in ("1", "3"):
        demo_contoh()

    if pilihan in ("2", "3"):
        print("\n" + "─" * 60)
        print("  📝 INPUT MANUAL")
        print("  Masukkan elemen himpunan dipisahkan spasi.")
        print("  Contoh: 2 4 6")
        print("─" * 60)

        while True:
            try:
                input_A = input("\n  Masukkan elemen Himpunan A: ")
                A = parse_input(input_A, "A")

                input_B = input("  Masukkan elemen Himpunan B: ")
                B = parse_input(input_B, "B")

                tampilkan_proses(A, B)
                break

            except ValueError as e:
                print(f"\n  ⚠️  Error: {e}")
                print("  Silakan coba lagi.\n")

    if pilihan not in ("1", "2", "3"):
        print("\n  Pilihan tidak valid. Menjalankan demo otomatis...")
        demo_contoh()

    print("  Terima kasih! Program selesai.\n")


# ─────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()