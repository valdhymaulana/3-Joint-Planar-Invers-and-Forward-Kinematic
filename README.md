# Simulasi Kinematika Planar Robot Lengan 3-DOF
Repositori ini berisi implementasi simulasi pergerakan lengan robot *Planar* (2D) dengan 3 Derajat Kebebasan (3-DOF) menggunakan Python dan Matplotlib. Program dibagi menjadi dua bagian utama sesuai dengan metode analisis kinematika: **Forward Kinematics** dan **Inverse Kinematics** berbasis geometri.

Parameter fisik *link* lengan robot yang digunakan dalam perhitungan ini adalah:
* $l_1 = 1.0$ (Panjang Link 1)
* $l_2 = 1.0$ (Panjang Link 2)
* $l_3 = 0.5$ (Panjang Link 3)

---

## 1. Forward Kinematics (`forward.py`)
Program ini mengeksekusi *The Forward Problem*, yaitu mencari posisi absolut ujung robot (*Task Space*) berdasarkan parameter input putaran sendi (*Joint Space*). 

**Konsep Matematika yang Digunakan:**
Perhitungan dilakukan menggunakan metode **Penjumlahan Vektor** trigonometri sederhana, di mana posisi ujung batang terakhir dihitung secara berantai dari titik dasar ($0,0$).
$$x_e = l_1 \cos\theta_1 + l_2 \cos(\theta_1 + \theta_2) + l_3 \cos(\theta_1 + \theta_2 + \theta_3)$$
$$y_e = l_1 \sin\theta_1 + l_2 \sin(\theta_1 + \theta_2) + l_3 \sin(\theta_1 + \theta_2 + \theta_3)$$

**Hasil End Of Factor Dari Eksekusi Program:**

<img width="435" height="195" alt="Screenshot 2026-03-31 124740" src="https://github.com/user-attachments/assets/c33f2144-c748-4ec3-8281-a76f07b26ae0" />

**Tampilan Join Robot Hasil Eksekusi Program:**

<img width="573" height="379" alt="Screenshot 2026-03-31 125120" src="https://github.com/user-attachments/assets/fd41880c-a9e7-44ea-8ce7-ffbf1304a11f" />

## 2. Inverse Kinematics (`inverse.py`)
Program ini mengeksekusi *The Inverse Problem* di mana pengguna hanya memasukkan input berupa **posisi koordinat Cartesian (X, Y)**, kemudian sistem bertugas mencari secara analitik berapa sudut derajat setiap sendi yang dibutuhkan agar ujung lengan mencapai titik koordinat tersebut.

Karena model 3-DOF memiliki redundansi terhadap target 2D (X, Y), program ini mengunci orientasi *End-Effector* ($\phi_e$) secara konstan sejajar dengan sumbu horizontal ($0^\circ$) agar solusi geometri dapat ditemukan.

**Konsep Matematika yang Digunakan (Pendekatan Geometri):**
Penyelesaian dibagi menjadi dua tahap, yaitu mengisolasi pergelangan (*wrist*) lalu menyelesaikannya menggunakan **Hukum Kosinus**.

**Tahap 1: Mencari Posisi Pergelangan (Wrist)**

$$x_w = x_e - l_3 \cos \phi_e$$
$$y_w = y_e - l_3 \sin \phi_e$$

**Tahap 2: Menghitung Sudut Sendi (Hukum Kosinus & Trigonometri)**
Pertama, hitung kuadrat jarak dari titik asal ke pergelangan ($r^2$):

$$r^2 = x_w^2 + y_w^2$$

Kemudian sudut untuk masing-masing sendi diselesaikan dengan:

$$\theta_2 = \arccos \left( \frac{r^2 - l_1^2 - l_2^2}{2 l_1 l_2} \right)$$
$$\theta_1 = \text{atan2}(y_w, x_w) - \text{atan2}(l_2 \sin \theta_2, l_1 + l_2 \cos \theta_2)$$
$$\theta_3 = \phi_e - \theta_1 - \theta_2$$

### 3. Sistem Proteksi Jangkauan Maksimal (Workspace & Singularitas)
Di realitas rekayasa fisik, lengan robot memiliki batas jangkauan maksimal (*Workspace*). Jika pengguna memasukkan koordinat $(X, Y)$ yang jaraknya melebihi rentangan fisik lengan, fungsi *Arccosine* pada Hukum Kosinus akan menghasilkan nilai imajiner (Math Domain Error) karena mencoba membentuk segitiga yang sisinya tidak terhubung.

Untuk mencegah *error* tersebut, program `inverse.py` dilengkapi dengan sistem validasi geometri. Jarak titik pusat ke pergelangan ($r$) dievaluasi dengan syarat:

$$r \le (l_1 + l_2)$$
$$\sqrt{x_w^2 + y_w^2} \le (l_1 + l_2)$$

Jika syarat batas fisik ini dilanggar, program akan memblokir kalkulasi matriks dan memberikan *feedback* kepada pengguna berupa pesan peringatan logikal:
`[ERROR] Target berada di luar jangkauan fisik lengan robot!`

<img width="448" height="107" alt="Screenshot 2026-03-31 130215" src="https://github.com/user-attachments/assets/13ed24f3-aadd-4ed4-a54d-d870521c42d7" />


**Hasil Eksekusi Program jika nilai dari end of factor yang kita igninkan adalah X bernilai 2 dan Y bernilai 1:**

<img width="591" height="578" alt="Screenshot 2026-03-31 130349" src="https://github.com/user-attachments/assets/d1f0138e-7f29-46d1-b0f1-265c1d212db0" />

**Dan Hasil perhuitungan sudutnya ialah:**

<img width="299" height="90" alt="Screenshot 2026-03-31 130752" src="https://github.com/user-attachments/assets/affaaadc-8813-438a-b9e6-1cb0f2c74884" />


---
