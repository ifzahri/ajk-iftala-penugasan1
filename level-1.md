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
   ![Branch on local](/src/docs/image-5.png)

   Perubahan tersebut masih disimpan pada local changes, dan belum dapat terlihat di remote atau GitHub. Maka dari itu, perlu melakukan push pada tiap branchnya agar dapat terlihat di remote repository, dengan command sebagai berikut
   ```bash
    git push -u origin main
    git push -u origin development
    git push -u origin feature1-add-title
    git push -u origin feature2-add-description
   ```
   Setelah itu, perubahan akan muncul pada remote
   ![Branch on remote](/src/docs/image-2.png)

3. Seluruh kegiatan dibawah dilakukan pada branch `development`, berikut adalah contoh implementasi pada local tentang command-command git yang berkaitan
- Pull
  
  Pull digunakan untuk mengambil konten dari remote dan melakukan update pada local untuk mencocokkan konten tersebut, command yang digunakan adalah
  `git pull origin main`.
  ![pull](/src/docs/image-13.png)

- Stash
  
  Stash digunakan untuk mentimpan perubahan sementara yang belum akan dicommit, yang mana nantinya akan di-apply perubahan yang terjadi, command yang digunakan untuk melakukan stash adalah `git stash`, dan untuk menyimpan perubahannya, dapat menggunakan `git stash apply`.
  ![stash](/src/docs/image-15.png)

- Reset
  
  Command reset dijadikan untuk membatalkan perubahan yang ada di working directory, untuk melakukan reset, maka bisa menggunakan `git reset --hard HEAD`, dimana `--hard` adalah opsi untuk merubah seluruh perubahan dan dikembalikan ke commit tertentu, dan `HEAD` sendiri sebagai penanda ke last commit terakhir pada branch directory.
  ![reset](/src/docs/image-14.png)

- Diff
  
  Diff adalah command untuk menunjukkan perubahan pada commit, antara kedua commit, dan staging changes.
  ![diff](/src/docs/image-11.png)
- Merge
  
  Merge digunakan untuk menggabungkan perubahan perubahan yang ada pada branch yang berbeda.
  ```
  git checkout development
  git merge feature1-add-title
  git merge feature2-add-description
  ```
  ![merge branch](/src/docs/image-12.png)
- Branch
  
  Branch adalah command untuk menampilkan daftar branch, membuat branch, dan melakukan delete branch
  ```
  git branch -v                     # melihat daftar branch
  git branch new-branch             # membuat branch
  git branch -d branch-to-delete    # menghapus branch
  ```
  ![branch](/src/docs/image-5.png)

- Checkout
  
  Checkout dilakukan ketika diperlukan untuk erpindah antara branch dengan command `git checkout main`
  ![checkout](/src/docs/image-6.png)

- Add
  
  `git add .` dijadikan command untuk menambahkan file yang telah dirubah pada local ke staging changes.
  ![Add](/src/docs/image-16.png)

- Commit
  
  Untuk melakukan commit, maka digunakan `git commit -m "message"`
![Alt text](/src/docs/image-3.png)
- Push
  
  Push adalah command untuk menyimpan perubahan dari local changes ke remote changes
  ![push](/src/docs/image-4.png)
  
4. Implemetasi git conflict dapat dilakukan dengan step by step sebagai berikut

- Membuat perubahan pada masing-masing feature pada line yang sama, disini saya merubah line pada `src/example_app/views.py` menjadi `print('Hello from feature1')` pada `feature1-add-title` dan `print('Hello from feature2')` pada `feature2-add-description`, yang mana ketika di-merge akan menghasilkan error.
  ![conflict](/src/docs/image-7.png)
- Error terjadi dikarenakan saya melakukan push terlebih dahulu pada file dari `feature1-add-title` ke `development`, dan dikarenakan adanya perubahan pada baris yang sama pada `feature1-add-title` dengan `feature2-add-description`, maka terjadi conflict ketika `feature2-add-description` di merge ke `development`
  ![resolve](/src/docs/image-8.png)
   

5. Untuk melakukan merge secara no fast forward atau `--no-ff` maka saya perlu meresolve conflict, dimana saya menggabungkan line pada `feature2-add-description` dan `feature1-add-title` dengan cara incoming first. Lalu, saya melakukan commit dan merge kedua feature ke branch `development`
   ![merging](/src/docs/image-9.png)
   ![no-fast-forward](/src/docs/image-10.png)
   Kemudian, saya memanfaatkan fitur Pull Request pada GitHub untuk menggabungkan branch `development` dengan `main`
   ![PR](/src/docs/image-18.png)

## Lampiran
- Git log pada repository (menggunakan GitLens)
![Log](/src/docs/image-17.png)