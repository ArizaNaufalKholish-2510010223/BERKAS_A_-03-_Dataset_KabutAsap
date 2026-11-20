# Dataset Klasifikasi Ketebalan Kabut Asap | Kelompok 3

Repositori ini merupakan hasil kerja Kelompok 3 untuk tugas Pertemuan 5. Tujuan tugas ini adalah menyusun dataset citra kabut asap yang dapat digunakan untuk klasifikasi ketebalan asap. Setiap citra diberi satu label berdasarkan kepadatan asap yang tampak dan seberapa jelas objek di latar belakang masih terlihat.

## Target dan pedoman pelabelan

Target minimum dataset adalah **150 citra secara keseluruhan** yang mencakup tiga kelas berikut.

| Kelas | Pedoman pelabelan |
|---|---|
| Tipis | Asap terlihat samar. Objek di latar belakang masih terlihat jelas dan detailnya mudah dikenali. |
| Sedang | Asap mengurangi kontras. Bentuk objek di latar belakang masih dapat dikenali, tetapi sebagian detailnya mulai kabur. |
| Tebal | Asap menutupi sebagian besar pemandangan. Objek di latar belakang sulit dikenali atau tidak terlihat. |

Jika sebuah citra sulit dibedakan antara dua kelas, anggota yang memberi label meminta anggota lain untuk meninjaunya. Kedua anggota menyepakati label akhir sebelum memasukkan citra ke folder kelas.

## Ketua, anggota, dan rencana pembagian kerja

| Nama | NIM | Peran | Rencana tugas | Bukti commit |
|---|---|---|---|---|
| Ariza Naufal Kholish | 2510010223 | Ketua | Menyiapkan struktur repositori, menyusun README, dan memeriksa konsistensi label bersama anggota. | [Commit Ariza](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_ARIZA) |
| Muhammad Sidiq Maulana | 2510010287 | Anggota | Mengumpulkan, menyeleksi, dan memberi label citra untuk kelas Tipis. | [Commit Sidiq](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_SIDIQ) |
| M Mudrikah Hanafi | 2510010222 | Anggota | Mengumpulkan, menyeleksi, dan memberi label citra untuk kelas Sedang. | [Commit Mudrikah](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_MUDRIKAH) |
| Muhammad Rafi Akmal Habibi | 2510010093 | Anggota | Mengumpulkan, menyeleksi, dan memberi label citra untuk kelas Tebal. | [Commit Rafi](https://github.com/PEMILIK/REPOSITORI/commits?author=USERNAME_RAFI) |

Setiap anggota melakukan **commit dan push melalui akun GitHub masing-masing**. Pesan commit menjelaskan pekerjaan yang dilakukan, misalnya `Menambahkan 12 citra kelas Tipis` atau `Memperbaiki label 3 citra setelah peninjauan`.

## Struktur dataset

Dataset menggunakan nama folder sebagai label kelas.

| Lokasi | Isi |
|---|---|
| `dataset/Tipis/` | Citra dengan label Tipis |
| `dataset/Sedang/` | Citra dengan label Sedang |
| `dataset/Tebal/` | Citra dengan label Tebal |
| `README.md` | Deskripsi tugas, pedoman label, cara penggunaan, dan pembagian kerja |
| `.gitignore` | Aturan untuk mengabaikan berkas sistem operasi dan cache |
| `LICENSE` | Teks lisensi yang dipilih kelompok |

## Cara mengunduh dan menggunakan dataset

1. Pada halaman utama repositori GitHub, klik **Code** lalu **Download ZIP**.
2. Ekstrak berkas ZIP dan buka folder `dataset/`.
3. Buka folder `Tipis/`, `Sedang/`, atau `Tebal/` untuk melihat citra pada kelas tersebut.
4. Saat menggunakan citra untuk analisis atau pelatihan model, gunakan nama folder induk sebagai label. Sebagai contoh, citra dengan jalur `dataset/Sedang/asap_001.jpg` memiliki label `Sedang`.
