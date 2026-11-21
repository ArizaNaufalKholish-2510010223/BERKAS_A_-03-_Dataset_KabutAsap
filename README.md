# Dataset Klasifikasi Ketebalan Kabut Asap — Kelompok 3

Dataset ini disusun untuk tugas Pertemuan 5. Kelompok 3 mengelompokkan citra menjadi **Tipis**, **Sedang**, dan **Tebal** berdasarkan seberapa jelas objek latar belakang terlihat melalui asap. Target tugas adalah minimal 150 citra secara keseluruhan. Pada pemeriksaan 21 November 2026, [dataset](dataset/) memuat **312 berkas dengan 224 gambar unik berdasarkan isi biner**. Ketiga kelas terwakili.

## Anggota dan kontribusi

Tabel ini mencatat pekerjaan yang terlihat pada perubahan berkas di GitHub. Tautan riwayat menampilkan commit lain dari akun yang sama pada cabang `main`.

| Nama | NIM | Peran | Kontribusi dalam repositori | Bukti commit |
|---|---|---|---|---|
| Ariza Naufal Kholish | 2510010223 | Ketua | Menyiapkan manifes dan skrip pemeriksaan, menambahkan 64 foto di tiga kelas, lalu merapikan nama berkas. | [Manifes dan skrip](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/eecdb874b55709704fe736650d05b0e968be066f) · [Penambahan foto](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/51abb0fffac3772a910cea7ba2faea023742dd0d) · [Penamaan foto](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/6d81ada55913fc466aedb2743c86399af9f13d79) · [Riwayat](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commits/main/?author=ArizaNaufalKholish-2510010223) |
| Muhammad Sidiq Maulana | 2510010287 | Anggota | Menambahkan dan merapikan citra kelas Sedang. | [Penambahan citra](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/9dfcf95f9c2651bdc9c2b8a863cf4b58af3f61ee) · [Penataan folder](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/1502ff0ab457182ab16bfdab9dfde032e3816b07) · [Riwayat](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commits/main/?author=MuhammadSidiqMaulana-2510010287) |
| M Mudrikah Hanafi | 2510010222 | Anggota | Menambahkan 90 citra kelas Tebal, kemudian menambahkan 3 citra ke subfolder jarak jauh. | [90 citra awal](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/93b44ae4af52502806bcf84f9a3722ad99b23e58) · [3 citra tambahan](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/3e38c7366a27bfa00bf6e1860a3c9ae57ca31d38) · [Riwayat](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commits/main/?author=muhammadmudrikahhanafi) |
| Muhammad Rafi Akmal Habibi | 2510010093 | Anggota | Menata nama berkas dan mengelompokkan citra kelas Tipis ke dalam subfolder jarak. | [Penataan berkas](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/2b5e04c5e6ad69e04a17b5b1188358b0eef43a1a) · [Pengelompokan jarak](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commit/1662390b10fe50ce46022cb706846d5dbfd21e19) · [Riwayat](https://github.com/ArizaNaufalKholish-2510010223/BERKAS_A_-03-_Dataset_KabutAsap/commits/main/?author=Muhammadrafiakmalhabibi-pixel) |

## Pedoman pelabelan

| Kelas | Ciri visual |
|---|---|
| Tipis | Asap terlihat samar. Bentuk dan detail objek di latar belakang masih terlihat jelas. |
| Sedang | Asap mengurangi kontras. Bentuk objek di latar belakang masih dapat dikenali, tetapi sebagian detailnya mulai kabur. |
| Tebal | Asap menutupi sebagian besar pemandangan. Objek di latar belakang sulit dikenali. |

Kelas ketebalan dan estimasi jarak pandang dicatat terpisah. Untuk memeriksa estimasi jarak, gunakan objek yang diketahui jaraknya dari kamera atau catatan jarak pandang pada lokasi dan waktu pengambilan.

## Isi dataset

Angka pada tabel menghitung berkas di setiap folder. Foto identik yang tersimpan di dua lokasi dihitung di kedua lokasi tersebut.

| Folder kelas | Kurang dari 100 m | 100–500 m | Lebih dari 500 m | Jumlah berkas |
|---|---:|---:|---:|---:|
| [Tipis](dataset/Tipis/) | 48 | 58 | 5 | 111 |
| [Sedang](dataset/Sedang/) | 23 | 49 | 14 | 86 |
| [Tebal](dataset/Tebal/) | 21 | 79 | 15 | 115 |
| **Total** | **92** | **186** | **34** | **312** |

Setiap kelas memiliki subfolder `kurang_dari_100`, `100-500`, dan `lebih_dari_500`. Rentang tengah mencakup batas 100 dan 500 meter. Penomoran dimulai dari 01 di setiap subfolder. Misalnya, [dataset/Tebal/100-500/01_sedang.webp](dataset/Tebal/100-500/01_sedang.webp) adalah foto kelas **Tebal** pada rentang **100–500 m**. Akhiran `dekat`, `sedang`, dan `jauh` pada nama berkas merujuk ke rentang jarak.

## Format metadata.csv

[metadata.csv](metadata.csv) menggunakan UTF-8 dan pemisah koma. Setiap baris data merujuk ke satu jalur berkas.

| Kolom | Isi |
|---|---|
| `path` | Jalur relatif terhadap direktori utama repositori, termasuk nama dan ekstensi berkas. |
| `ketebalan_asap` | Label yang tercatat di folder kelas, yaitu `Tipis`, `Sedang`, atau `Tebal`. |
| `jarak_pandang` | Nama subfolder jarak pada `path`, yaitu `kurang_dari_100`, `100-500`, atau `lebih_dari_500`. Setiap baris mengikuti lokasi berkasnya. |

Contoh baris dari manifes sebenarnya

```csv
path,ketebalan_asap,jarak_pandang
dataset/Tipis/kurang_dari_100/01_dekat.jpg,Tipis,kurang_dari_100
dataset/Sedang/kurang_dari_100/05_dekat.png,Sedang,kurang_dari_100
dataset/Tebal/kurang_dari_100/05_dekat.jpeg,Tebal,kurang_dari_100
```

## Hasil pemeriksaan dan batasan data

- **Ketebalan.** Peninjauan visual terhadap 312 berkas menemukan 116 yang tampak sesuai dengan kelas folder, 115 yang cenderung menyerupai kelas lain, dan 81 yang belum cukup jelas untuk diputuskan. Sebanyak 29 gambar unik memiliki salinan identik di kelas ketebalan berbeda. Manifes mempertahankan label folder agar setiap baris dapat ditelusuri ke berkas sumber.
- **Jarak pandang.** Seluruh 312 baris mencatat rentang sesuai subfolder masing-masing. Ada 92 berkas di `kurang_dari_100`, 186 di `100-500`, dan 34 di `lebih_dari_500`. Sebanyak 49 gambar unik memiliki salinan di beberapa rentang (127 berkas). Setiap salinan mengikuti subfolder tempatnya disimpan. Jarak pandang sebenarnya belum dikonfirmasi melalui pengukuran.

## Cara menggunakan dan memeriksa dataset

1. Unduh repositori melalui **Code → Download ZIP**, kemudian ekstrak arsipnya.
2. Buka `metadata.csv` di Excel atau LibreOffice Calc. Pilih pemisah **koma** jika diminta. Filter `ketebalan_asap` untuk memilih kelas dan `jarak_pandang` untuk memilih estimasi jarak.
3. Dari direktori utama repositori, buka gambar sesuai nilai `path` pada baris yang dipilih.

Untuk memeriksa keterbacaan gambar dan kecocokan manifes dengan folder, jalankan perintah berikut dari direktori utama repositori menggunakan Python dengan Pillow yang mendukung AVIF.

```sh
python -m pip install Pillow
python cek_dataset.py
```

[Skrip pemeriksaan](cek_dataset.py) memeriksa berkas gambar, baris CSV, kesesuaian label dengan folder, kesesuaian estimasi yang terisi dengan subfolder, dan target minimum. Kesesuaian visual ketebalan dinilai dengan pedoman pelabelan di atas.

## platform data Kaggle
https://www.kaggle.com/datasets/arizakholish/klasifikasi-ketebalan-kabut-asap-kelompok-3/data

## Lisensi

Repositori mencantumkan MIT License, hak cipta 2026 Ariza. [Teks lisensi](LICENSE)
