# Tugas Mata Kuliah Komputasi Numerik: Implementasi Metode Gauss-Seidel dalam Bahasa Python (Soal Nomor 16)

# Kelompok a02 - Komputasi Numerik m

# Anggota Kelompok:
# 1. Nama: Farrel Aqilla Novianto          - NRP: 5025241015
# 2. Nama: Muhammad Nabil Fauzan           - NRP: 5025241024
# 3. Nama: Himawan Rakha Badra             - NRP: 5025241028
# 4. Nama: Vityaz Ali Firdaus              - NRP: 5025241050
# 5. Nama: Raden Kurniawan Agung Fitrianto - NRP: 5025241104

# Kode program:

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
