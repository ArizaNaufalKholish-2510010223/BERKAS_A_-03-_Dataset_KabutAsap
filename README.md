# Dataset Klasifikasi Ketebalan Kabut Asap

**Mata kuliah:** Sistem Berkas  
**Kelompok:** 3 (Kode 03)

## Deskripsi Dataset

Proyek ini mengumpulkan dan mengelompokkan citra kabut asap berdasarkan kepadatan asap yang terlihat dan kejelasan objek di dalam citra. Target pengumpulan adalah **minimal 150 citra total** yang mencakup tiga kelas: Tipis, Sedang, dan Tebal.

## Panduan Pelabelan

| Kelas | Label di CSV | Panduan |
|---|---|---|
| Tipis | `tipis` | Asap terlihat, tetapi objek dan detail latar masih cukup jelas. |
| Sedang | `sedang` | Asap mengurangi kejelasan detail, tetapi objek utama masih dapat dikenali. |
| Tebal | `tebal` | Asap menutupi banyak detail sehingga objek utama atau latar sulit dikenali. |

Estimasi jarak pandang dapat dicatat sebagai informasi tambahan dengan tiga kategori: kurang dari 100 m, 100–500 m, dan lebih dari 500 m.

## Struktur Repositori

| Berkas atau folder | Isi |
|---|---|
| `dataset/Tipis/` | Citra kelas Tipis |
| `dataset/Sedang/` | Citra kelas Sedang |
| `dataset/Tebal/` | Citra kelas Tebal |
| `metadata.csv` | Daftar lokasi citra dan label kelasnya |
| `cek_dataset.py` | Skrip untuk memeriksa kelengkapan label dan mendeteksi gambar yang tidak bisa dibaca |
| `.gitignore` | Aturan untuk mengecualikan berkas sistem operasi dan cache |
| `LICENSE` | Teks lisensi MIT |
| `README.md` | Dokumentasi dataset dan pembagian kerja kelompok |

## Cara Mengunduh dan Menggunakan Dataset

1. Buka halaman repositori di GitHub, klik **Code → Download ZIP**, lalu ekstrak berkas ZIP.
2. Buka folder hasil ekstraksi di VS Code.
3. Buka `metadata.csv` untuk melihat lokasi dan label setiap citra. Gunakan kolom `file_path` untuk menemukan gambar dan kolom `kelas` untuk mengetahui labelnya.

## Format Metadata

Berkas `metadata.csv` berada di folder utama repositori. Setiap citra dicatat dalam satu baris. Nama folder, nama file, dan ekstensi di `file_path` mengikuti lokasi file yang sebenarnya, termasuk jika gambar berada di subfolder jarak pandang.

Contoh format dengan nama file ilustrasi:

```csv
file_path,kelas
dataset/Sedang/100-500m/gambar_001.jpg,sedang
```

Jika estimasi jarak pandang dicatat di CSV, tambahkan kolom opsional `jarak_pandang`.

## Pemeriksaan Dataset

Jalankan perintah berikut di terminal VS Code dari folder utama repositori. Contoh ini menggunakan Python di Windows.

```bash
py -m pip install Pillow
py cek_dataset.py
```

Skrip memeriksa gambar yang belum tercatat di `metadata.csv`, jalur gambar yang tidak ditemukan, entri duplikat, label yang tidak valid, dan gambar yang tidak bisa dibaca. Skrip juga menampilkan jumlah citra valid per kelas dan memeriksa target minimum 150 citra.

## Anggota Kelompok dan Pembagian Kerja

Setiap anggota melakukan commit dan push menggunakan akun GitHub masing-masing. Kolom **Bukti commit** memuat tautan ke commit yang menunjukkan kontribusi anggota tersebut.

| Nama | NPM | Peran | Kontribusi | Bukti commit |
|---|---|---|---|---|
| Ariza Naufal Kholish | 2510010223 | Ketua | [Isi kontribusi Ariza] | [Tempel URL commit Ariza] |
| M Mudrikah Hanafi | 2510010222 | Anggota | [Isi kontribusi Mudrikah] | [Tempel URL commit Mudrikah] |
| Muhammad Rafi Akmal Habibi | 2510010093 | Anggota | [Isi kontribusi Rafi] | [Tempel URL commit Rafi] |
| Muhammad Sidiq Maulana | 2510010287 | Anggota | [Isi kontribusi Sidiq] | [Tempel URL commit Sidiq] |

## Lisensi

Teks lisensi MIT tersedia di berkas [LICENSE](LICENSE). Penggunaan citra dari pihak ketiga mengikuti ketentuan izin atau lisensi dari sumber masing-masing.
