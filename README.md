# Tugas Mata Kuliah Komputasi Numerik: Implementasi Metode Gauss-Seidel dalam Bahasa Python (Soal Nomor 16)

## Anggota Kelompok
1. **Farrel Aqilla Novianto**           - NRP: 5025241015  
2. **Muhammad Nabil Fauzan**            - NRP: 5025241024  
3. **Himawan Rakha Badra**              - NRP: 5025241028  
4. **Vityaz Ali Firdaus**               - NRP: 5025241050  
5. **Raden Kurniawan Agung Fitrianto**  - NRP: 5025241104  

---

## Deskripsi Soal
Diberikan sistem persamaan linear berikut:  
\[
\begin{cases}
5a_0 + 25a_1 + 135a_2 = 485 \\
25a_0 + 135a_1 + 775a_2 = 2785 \\
135a_0 + 775a_1 + 4659a_2 = 16751
\end{cases}
\]  
Tugas adalah mencari nilai \(a_0\), \(a_1\), dan \(a_2\) menggunakan **metode Gauss-Seidel** dengan melakukan iterasi hingga iterasi ke-2. Setiap nilai \(a_0\), \(a_1\), dan \(a_2\) pada tiap iterasi harus ditampilkan.

---

## Kode Program
```python
def gauss_seidel(iterations):
    a0, a1, a2 = 0.0, 0.0, 0.0
    for i in range(1, iterations + 1):
        a0 = (485 - 25 * a1 - 135 * a2) / 5
        a1 = (2785 - 25 * a0 - 775 * a2) / 135
        a2 = (16751 - 135 * a0 - 775 * a1) / 4659
        print(f"Iterasi {i}: a0 = {a0:.2f}, a1 = {a1:.2f}, a2 = {a2:.2f}")

gauss_seidel(2)
```
---

## Output
Iterasi 1: a0 = 97.00, a1 = 2.67, a2 = 0.34
Iterasi 2: a0 = 74.46, a1 = 4.88, a2 = 0.63

---

## Penjelasan

Baris 1
``` def gauss_seidel(iterations): ```
Mendefinisikan fungsi gauss_seidel dengan parameter iterations (jumlah iterasi yang diinginkan).

Baris 2
``` a0, a1, a2 = 0.0, 0.0, 0.0 ```
Inisialisasi nilai awal variabel a0, a1, dan a2 ke 0.0 sebagai tebakan awal.

Baris 3
``` for i in range(1, iterations + 1): ```
Melakukan perulangan dari 1 hingga iterations. Karena diminta hingga iterasi ke-2, fungsi nanti akan dipanggil dengan iterations = 2.

Baris 4
``` a0 = (485 - 25 * a1 - 135 * a2) / 5 ```
Menghitung nilai baru a0 dari persamaan pertama menggunakan nilai a1 dan a2 dari iterasi sebelumnya.

Baris 5
``` a1 = (2785 - 25 * a0 - 775 * a2) / 135 ```
Menghitung nilai baru a1 dari persamaan kedua. Di sini, a0 sudah diperbarui, tapi a2 masih dari sebelumnya.

Baris 6
``` a2 = (16751 - 135 * a0 - 775 * a1) / 4659 ```
Menghitung nilai baru a2 dari persamaan ketiga. Sekarang a0 dan a1 sudah diperbarui.

Baris 7
``` print(f"Iterasi {i}: a0 = {a0:.2f}, a1 = {a1:.2f}, a2 = {a2:.2f}") ```
Mencetak hasil iterasi ke-i dengan pembulatan 2 angka di belakang koma, sesuai syarat tugas.

Baris 9
``` gauss_seidel(2) ```
Memanggil fungsi gauss_seidel dengan iterasi sebanyak 2 kali, sesuai perintah soal.
