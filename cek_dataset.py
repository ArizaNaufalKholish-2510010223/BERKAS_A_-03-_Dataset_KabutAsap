"""Periksa gambar kabut asap dan label di metadata.csv."""

import csv
from collections import Counter
from pathlib import Path

from PIL import Image, ImageSequence

ROOT = Path(__file__).resolve().parent
DATASET = ROOT / "dataset"
MINIMUM = 150
KELAS = ("tipis", "sedang", "tebal")
EKSTENSI = {".jpg", ".jpeg", ".png", ".webp", ".avif", ".bmp", ".gif", ".tif", ".tiff"}


def baca_label(gambar, masalah):
    label = {}
    tercatat = set()

    with (ROOT / "metadata.csv").open(encoding="utf-8-sig", newline="") as file:
        baris_csv = csv.DictReader(file, strict=True)
        kolom = set(baris_csv.fieldnames or [])
        if {"path", "ketebalan_asap"} <= kolom:
            kolom_path, kolom_kelas = "path", "ketebalan_asap"
        elif {"file_path", "kelas"} <= kolom:
            kolom_path, kolom_kelas = "file_path", "kelas"
        else:
            raise ValueError("CSV memerlukan path dan ketebalan_asap, atau file_path dan kelas.")

        for baris in baris_csv:
            nomor = baris_csv.line_num
            lokasi = (baris.get(kolom_path) or "").strip().replace("\\", "/")
            lokasi = lokasi.removeprefix("./")
            kelas = (baris.get(kolom_kelas) or "").strip().casefold()

            if lokasi in tercatat:
                masalah.append(f"Baris {nomor} duplikat: {lokasi}")
                continue
            tercatat.add(lokasi)

            if lokasi not in gambar:
                masalah.append(f"Baris {nomor} merujuk gambar yang tidak ditemukan: {lokasi!r}")
                continue
            if kelas not in KELAS:
                masalah.append(f"Kelas kosong atau tidak valid: {lokasi}")
                continue

            bagian = gambar[lokasi].relative_to(DATASET).parts
            folder_kelas = bagian[0].casefold()
            if folder_kelas in KELAS and folder_kelas != kelas:
                masalah.append(f"Label berbeda dari folder kelas: {lokasi} ({kelas})")
                continue
            jarak = (baris.get("jarak_pandang") or "").strip()
            if jarak and (len(bagian) < 3 or jarak != bagian[1]):
                masalah.append(f"Estimasi jarak berbeda dari subfolder: {lokasi} ({jarak})")
                continue
            label[lokasi] = kelas

    for lokasi in sorted(gambar.keys() - tercatat):
        masalah.append(f"Gambar belum tercatat di metadata.csv: {lokasi}")
    return label


def main():
    if not DATASET.is_dir():
        print("Folder dataset tidak ditemukan.")
        return 1

    gambar = {
        file.relative_to(ROOT).as_posix(): file
        for file in sorted(DATASET.rglob("*"))
        if file.is_file() and file.suffix.lower() in EKSTENSI
    }
    masalah = []
    try:
        label = baca_label(gambar, masalah)
    except (OSError, ValueError, csv.Error) as error:
        print(f"Gagal membaca metadata.csv: {error}")
        return 1

    jumlah = Counter()
    for lokasi, file in gambar.items():
        try:
            with Image.open(file) as citra:
                citra.verify()
            with Image.open(file) as citra:
                for frame in ImageSequence.Iterator(citra):
                    frame.load()
        except (OSError, ValueError, SyntaxError, EOFError, Image.DecompressionBombError) as error:
            masalah.append(f"Gambar rusak atau tidak bisa dibaca: {lokasi} ({error})")
            continue
        if lokasi in label:
            jumlah[label[lokasi]] += 1

    total = sum(jumlah.values())
    print(f"Gambar ditemukan: {len(gambar)}")
    for kelas in KELAS:
        print(f"{kelas.capitalize()}: {jumlah[kelas]} gambar valid")
        if jumlah[kelas] == 0:
            masalah.append(f"Kelas {kelas} belum memiliki gambar valid.")
    print(f"Total gambar valid dengan label: {total}")
    if total < MINIMUM:
        masalah.append(f"Masih kurang {MINIMUM - total} gambar valid dari target {MINIMUM}.")

    for pesan in masalah:
        print(f"- {pesan}")
    if not masalah:
        print("Pemeriksaan lulus.")
    return int(bool(masalah))


if __name__ == "__main__":
    raise SystemExit(main())
