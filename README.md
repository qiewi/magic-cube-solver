<div align="center">
  ![magic_cube](https://github.com/user-attachments/assets/bcb96ac3-b5d3-4929-85ee-936f5e8f8391)
  <h1 align="center">Magic Cube Solver - Local Search</h1>

   <div align="center">
     Tugas Besar 1 IF3070 Dasar Inteligensi Artifisial - Algoritma Local Search & Magic Cube 5x5x5
    </div>
</div>

## 📋 <a name="table">Table of Contents</a>

1. 🤖 [Introduction](#introduction)
2. ⚙️ [Tech Stack](#tech-stack)
3. 🔋 [Features](#features)
4. 🚀 [Setup](#quick-start)

## <a name="introduction">🚨 Introduction</a>

Tugas Besar I pada kuliah IF3070 Dasar Inteligensi Buatan dan IF3170 Inteligensi Buatan bertujuan agar peserta kuliah mendapatkan wawasan tentang bagaimana cara mengimplementasikan algoritma local search untuk mencari solusi suatu permasalahan. Pada tugas ini, peserta kuliah akan ditugaskan untuk mengimplementasikan algoritma local search untuk mencari solusi Diagonal Magic Cube.


## <a name="tech-stack">⚙️ Tech Stack</a>

- Python
- Matplotlib

## <a name="features">🔋 Features</a>

👉 **Home Page**: Tampilan Layar Terminal
<br>
![Screenshot 2024-11-10 003339](https://github.com/user-attachments/assets/d24f9579-4aa3-46c9-b79b-296a63d71b42)
<br>

👉 **Menu Page**: Pilihan Menu Algoritma
<br>
![Screenshot 2024-11-10 003358](https://github.com/user-attachments/assets/435554e7-b8f9-4fa1-851d-4bc1b77d0773)
<br>

👉 **Progress Page**: Tampilan Progress Iterasi
<br>
![Screenshot 2024-11-10 003415](https://github.com/user-attachments/assets/2fd0fdcd-b07d-4d78-a5ab-bb8a151669c9)
<br>

👉 **Cube State Page**: Tampilan Initial dan Final State dari Cube
<br>
![Screenshot 2024-11-10 003431](https://github.com/user-attachments/assets/5d9292e9-b342-4d19-92a2-469a7266da17)
<br>

👉 **Result Page**: Tampilan Hasil Algoritma Searching 
<br>
![Screenshot 2024-11-10 003446](https://github.com/user-attachments/assets/13aaaf5f-8d12-45c6-82a5-7f4c2156ea3f)
<br>

dan lain-lainnya.

## Anggota Kelompok

| Identitas                          | Tugas |
| -----------------------------------|-----------------|
| 18222105 - Audra Zelvania P.       | Steepest Ascent Hill Climbing  |
|                                    | Stochastic Hill Climbing |
| 18222118 - Rizqi Andhika P.        | Genetic Algorithm |
|                                    | Visualisasi & Main |
| 18222125 - Sekar Anindita N.       | Simulated Annealing |
|                                    | Run Algorithm |
| 18222138 - Khayla Belva A.         | Random Restart Hill Climbing |
|                                    | Sideways Move Hill Climbing |

## <a name="quick-start">🚀 Setup</a>

Ikuti langkah-langkah berikut ini untuk melakukan setup program di komputer kalian

**Prerequisites**

Pastikan Anda mempunyai Git

- [Git](https://git-scm.com/)

**Melakukan Clone Repository**

Lakukan Clone Repository
```bash
git clone https://github.com/qiewi/magic-cube-solver.git
```

**Cara Kompilasi Program**

1. Masuk ke folder src melalui terminal
```bash
cd src
```

2. Ketik "python main.py" pada terminal
```bash
python main.py
```

Open Terminal, lalu expand hingga full screen
(disarankan menggunakan layar besar / mac os agar tampilan dapat dilihat secara penuh)

Silahkan menjalankan program sesuai dengan keinginan.

## Struktur Program
```
 src
 │
 ├─── algorithm
 │       ├─── genetic_algorithm.py
 │       ├─── hill_climbing.py
 │       └─── simulated_annealing.py
 │           
 ├─── driver
 │       ├─── genetic-driver.py
 │       ├─── hillclimb-driver.py
 │       └─── simulated-driver.py 
 │           
 ├─── handlers
 │       └─── algorithm.py 
 │           
 ├─── models
 │       └─── cube.py 
 │
 ├─── main.py
 │
 └─── Visual.py 

```
