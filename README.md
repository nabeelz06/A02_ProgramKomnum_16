# Tugas Mata Kuliah Komputasi Numerik: Implementasi Metode Gauss-Seidel dalam Bahasa Python (Soal Nomor 16)

## Anggota Kelompok:
1. **Farrel Aqilla Novianto**              - NRP: 5025241015  
2. **Muhammad Nabil Fauzan**               - NRP: 5025241024  
3. **Himawan Rakha Badra**                 - NRP: 5025241028  
4. **Vityaz Ali Firdaus**                  - NRP: 5025241050  
5. **Raden Kurniawan Agung Fitrianto**     - NRP: 5025241104  

---

## Deskripsi Soal:
Diberikan sistem persamaan linear berikut:  

5 a0     + 25 a1     + 135 a2     = 485

25 a0    + 135 a1    + 775 a2     = 2785

135 a0   + 775 a1    + 4659 a2    = 16751

Tugas adalah mencari nilai a0, a1, dan a2 menggunakan **metode Gauss-Seidel** dengan melakukan iterasi hingga iterasi ke-2. Setiap nilai a0, a1, dan a2 pada tiap iterasi harus ditampilkan.

---

## Kode Program:
```python
import numpy as np

def gauss_seidel(iterations, m):
    a0, a1, a2 = 0.0, 0.0, 0.0
    for i in range(1, iterations + 1):
        a0 = np.round((m[0][3] - m[0][1] * a1 - m[0][2] * a2) / m[0][0], 2)
        a1 = np.round((m[1][3] - m[1][0] * a0 - m[1][2] * a2) / m[1][1], 2)
        a2 = np.round((m[2][3] - m[2][0] * a0 - m[2][1] * a1) / m[2][2], 2)
        print(f"Iterasi {i}: a0 = {a0:.2f}, a1 = {a1:.2f}, a2 = {a2:.2f}")

matrix = np.array([[5, 25, 135, 485], [25, 135, 775, 2785], [135, 775, 4659, 16751]])

gauss_seidel(2, matrix)
```

---

## Output:
Iterasi 1: a0 = 97.00, a1 = 2.67, a2 = 0.34

Iterasi 2: a0 = 74.47, a1 = 4.89, a2 = 0.62

---

## Penjelasan:

Baris 1

```import numpy as np```

Mengimpor library numpy sebagai np

Baris 3

```def gauss_seidel(iterations, m):```

Mendefinisikan fungsi gauss_seidel dengan parameter iterations (jumlah iterasi yang diinginkan).

Baris 4

```a0, a1, a2 = 0.0, 0.0, 0.0```

Inisialisasi nilai awal variabel a0, a1, dan a2 ke 0.0 sebagai tebakan awal.

Baris 5

```for i in range(1, iterations + 1):```

Melakukan perulangan dari 1 hingga iterations. Karena diminta hingga iterasi ke-2, fungsi nanti akan dipanggil dengan iterations = 2.

Baris 6

```a0 = np.round((m[0][3] - m[0][1] * a1 - m[0][2] * a2) / m[0][0], 2)```

Menghitung nilai baru a0 dari persamaan pertama. Menggunakan nilai a1 dan a2 dari iterasi sebelumnya. Kemudian dibulatkan 2 angka di belakang koma.

Baris 7

```a1 = np.round((m[1][3] - m[1][0] * a0 - m[1][2] * a2) / m[1][1], 2)```

Menghitung nilai baru a1 dari persamaan kedua. Di sini, a0 sudah diperbarui, tapi a2 masih dari sebelumnya. 

Baris 8

```a2 = np.round((m[2][3] - m[2][0] * a0 - m[2][1] * a1) / m[2][2], 2)```

Menghitung nilai baru a2 dari persamaan ketiga. Sekarang a0 dan a1 sudah diperbarui.

Baris 9

```print(f"Iterasi {i}: a0 = {a0:.2f}, a1 = {a1:.2f}, a2 = {a2:.2f}")```

Mencetak hasil iterasi ke-i dengan pembulatan 2 angka di belakang koma, sesuai syarat tugas.

Baris 11

```matrix = np.array([[5, 25, 135, 485], [25, 135, 775, 2785], [135, 775, 4659, 16751]])```

Memasukkan soal sebagai matrix menggunakan array yang ada pada library numpy.

Baris 13

```gauss_seidel(2, matrix)```

Memanggil fungsi gauss_seidel dengan iterasi sebanyak 2 kali, sesuai perintah soal.
