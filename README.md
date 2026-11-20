# Dataset Klasifikasi Ketebalan Kabut Asap — Kelompok 3

Repositori ini disusun oleh Kelompok 3 untuk tugas Pertemuan 5. Tujuannya adalah mengumpulkan dan memberi label pada citra kabut asap berdasarkan ketebalan asap yang terlihat. Target tugas adalah minimal **150 citra secara keseluruhan**, mencakup kelas **Tipis**, **Sedang**, dan **Tebal**. Jika tersedia, estimasi jarak pandang dicatat sebagai informasi tambahan untuk setiap citra.

## Anggota kelompok dan pembagian kerja

| Nama | NIM | Peran | Rencana pembagian kerja | Bukti commit |
|---|---|---|---|---|
| Ariza Naufal Kholish | 2510010223 | Ketua | Menyiapkan repositori dan README, menggabungkan metadata, serta memeriksa kesesuaian label dengan folder. | [Commit Ariza](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_ARIZA) |
| Muhammad Sidiq Maulana | 2510010287 | Anggota | Mengumpulkan citra kelas Tipis, memeriksa label, dan mencatat datanya di CSV. | [Commit Sidiq](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_SIDIQ) |
| M Mudrikah Hanafi | 2510010222 | Anggota | Mengumpulkan citra kelas Sedang, memeriksa label, dan mencatat datanya di CSV. | [Commit Mudrikah](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_MUDRIKAH) |
| Muhammad Rafi Akmal Habibi | 2510010093 | Anggota | Mengumpulkan citra kelas Tebal, memeriksa label, dan mencatat datanya di CSV. | [Commit Rafi](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_RAFI) |

Setiap anggota melakukan *commit* dan *push* menggunakan akun GitHub masing-masing. Pesan *commit* menjelaskan pekerjaan yang dilakukan, misalnya `Menambahkan 12 citra kelas Tipis beserta metadata`.

## Pedoman pelabelan

| Kelas | Ciri visual |
|---|---|
| Tipis | Asap terlihat samar. Bentuk dan detail objek di latar belakang masih terlihat jelas. |
| Sedang | Asap mengurangi kontras. Bentuk objek di latar belakang masih dapat dikenali, tetapi sebagian detailnya mulai kabur. |
| Tebal | Asap menutupi sebagian besar pemandangan. Objek di latar belakang sulit dikenali. |

Ketebalan asap dinilai dari tampilan citra. Estimasi jarak pandang dicatat secara terpisah jika tersedia acuan jarak, misalnya bangunan yang diketahui jaraknya dari kamera. Jika label ketebalan meragukan, minta anggota lain meninjau citra tersebut.

## Struktur repositori

| Lokasi | Keterangan |
|---|---|
| `dataset/Tipis/` | Citra berlabel Tipis |
| `dataset/Sedang/` | Citra berlabel Sedang |
| `dataset/Tebal/` | Citra berlabel Tebal |
| `metadata.csv` | Daftar lokasi file, label ketebalan asap, dan estimasi jarak pandang untuk setiap citra |
| `README.md` | Deskripsi tugas, anggota, pedoman label, dan cara menggunakan dataset |
| `.gitignore` | Aturan untuk mengabaikan berkas sistem dan cache, seperti `.DS_Store`, `Thumbs.db`, dan `__pycache__/` |
| `LICENSE` | Teks lisensi yang dipilih kelompok |

Di dalam setiap folder kelas, citra dapat dikelompokkan lagi berdasarkan estimasi jarak pandang.

| Nama subfolder | Estimasi jarak pandang |
|---|---|
| `kurang_100m/` | Kurang dari 100 meter |
| `100_500m/` | 100 sampai 500 meter, termasuk kedua batasnya |
| `lebih_500m/` | Lebih dari 500 meter |

Contoh: `dataset/Tebal/lebih_500m/asap_001.jpg` berarti citra berlabel **Tebal** dengan estimasi jarak pandang **lebih dari 500 meter**. Jika jarak pandang belum diketahui, simpan citra langsung di folder kelas, misalnya `dataset/Tebal/asap_002.jpg`.

## Format metadata.csv

Setiap citra dicatat satu kali. Kolom `path` berisi lokasi file relatif terhadap folder utama repositori. Kolom `ketebalan_asap` mengikuti nama folder kelas. Kolom `jarak_pandang` mengikuti nama subfolder dan dikosongkan jika estimasinya belum tersedia.

Contoh isi `metadata.csv`:

    path,ketebalan_asap,jarak_pandang
    dataset/Tebal/lebih_500m/asap_001.jpg,Tebal,lebih_500m
    dataset/Tebal/asap_002.jpg,Tebal,
    dataset/Tipis/lebih_500m/asap_003.jpg,Tipis,lebih_500m
    dataset/Sedang/100_500m/asap_004.jpg,Sedang,100_500m

## Cara mengunduh dan menggunakan dataset

1. Buka halaman utama repositori GitHub, pilih **Code**, lalu klik **Download ZIP**.
2. Ekstrak ZIP dan buka `metadata.csv` menggunakan Excel, LibreOffice Calc, atau aplikasi pembaca CSV. Jika diminta memilih pemisah kolom, pilih **koma**.
3. Filter kolom `ketebalan_asap` untuk memilih kelas atau `jarak_pandang` untuk memilih rentang jarak.
4. Buka citra sesuai lokasi pada kolom `path`. Untuk tugas klasifikasi, gunakan `ketebalan_asap` sebagai label target.

## Lisensi

Lisensi repositori: **[isi nama lisensi pilihan kelompok]**. Teks lengkap tersedia pada berkas [LICENSE](LICENSE).
