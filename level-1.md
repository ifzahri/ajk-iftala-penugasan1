# Level 1: Back to basic

## Penugasan
```
Apa yang harus dikerjakan?
1. Buat sebuah repository di GitHub. Nama repository dalam format ajk-[nama panggilan]-penugasan1. Repository ini juga sebagai tempat menaruh laporan pengerjaan untuk level selanjutnya.
Contoh: ajk-nur-penugasan1
Struktur: 
/src			(Berisi kode pengerjaan level 1 kalian)
README.md		(Readme utama)
level-1.md		(Laporan level 1)
level-2.md		(Laporan level 2)
level-3.md		(Laporan level 3)
level-4.md		(Laporan level 4)
2. Implementasikan penggunaan branching yang terdiri dari master, development, featureA, dan featureB. Codebase dibebaskan.
3. Implementasikan intruksi git untuk push, pull, stash, reset, diff, dan merge. Adanya tambahan intruksi git selain yang disebutkan akan lebih baik.
4. Implementasikan sebuah penanganan conflict di branch development ketika setelah merge dari branch featureA lalu merge dari branch featureB. Catatan: conflict bisa terjadi jika kedua branch mengerjakan di file dan line code yang sama. Buatlah skenario sendiri.
5. Gunakan merge no fast forward.

Buat dokumentasi pengerjaan kalian (level-1.md) yang setidaknya meliputi:
- Alur pengerjaan (sesuai dengan nomor soal)
- Penjelasan dari setiap alur
- Screenshot (atau record)
- Kondisi git graph (git log)
- Kendala atau kesulitan
```
## Jawaban
Implementasi dari branching sendiri dapat dilakukan sebagai berikut

1. Melakukan inisialisasi project menggunakan codebase yang ada, saya menggunakan codebase pribadi saya yaitu [Python Django Template](https://github.com/ifzahri/django-template)
2. Membuat command git sesuai dengan ketentuan, dengan cara
   ```bash
   git checkout main
   git checkout -b development
   git checkout -b feature1-add-title
   git checkout development
   git checkout -b feature2-add-description
   ```
   Berikut adalah hasil eksekusi command diatas
   ![Alt text](image.png)
3. 