import numpy as np
import matplotlib.pyplot as plt

# Parameter Fisik Lengan Robot
l1, l2, l3 = 1.0, 1.0, 0.5 

print("=== PROGRAM INVERSE KINEMATICS 3-DOF ===")
print("Input: Posisi Koordinat Target (Task Space)")

# Murni hanya menerima input X dan Y sesuai instruksi tugas
TARGET_X = float(input("Masukkan target koordinat X: "))
TARGET_Y = float(input("Masukkan target koordinat Y: "))

# Mengunci orientasi capit selalu menghadap depan (0 derajat) 
# agar sistem 3-DOF bisa diselesaikan secara geometris
phi = 0.0 

# Langkah 1: Mencari posisi pergelangan tangan (Wrist)
xw = TARGET_X - l3 * np.cos(phi)
yw = TARGET_Y - l3 * np.sin(phi)

# Langkah 2: Evaluasi Hukum Kosinus
r_kuadrat = xw**2 + yw**2

# Proteksi jangkauan maksimal
if np.sqrt(r_kuadrat) > (l1 + l2):
    print("\n[ERROR] Target berada di luar jangkauan fisik lengan robot!")
else:
    # Perhitungan Inverse menggunakan Trigonometri & Hukum Kosinus
    cos_theta2 = (r_kuadrat - l1**2 - l2**2) / (2 * l1 * l2)
    theta2 = np.arccos(cos_theta2) # Konfigurasi elbow-down
    
    theta1 = np.arctan2(yw, xw) - np.arctan2(l2 * np.sin(theta2), l1 + l2 * np.cos(theta2))
    theta3 = phi - theta1 - theta2
    
    print("\n--- HASIL INVERSE KINEMATICS ---")
    print("hitung sudut sendi yang dibutuhkan:")
    print(f"Sudut Sendi 1 (Base): {np.degrees(theta1):.2f} derajat")
    print(f"Sudut Sendi 2 (Elbow): {np.degrees(theta2):.2f} derajat")
    print(f"Sudut Sendi 3 (Wrist): {np.degrees(theta3):.2f} derajat")

    # Visualisasi (Membuktikan hasil perhitungan dengan menggambar ulang garisnya)
    x0, y0 = 0.0, 0.0
    x1, y1 = l1 * np.cos(theta1), l1 * np.sin(theta1)
    x2, y2 = x1 + l2 * np.cos(theta1 + theta2), y1 + l2 * np.sin(theta1 + theta2)
    x3, y3 = x2 + l3 * np.cos(phi), y2 + l3 * np.sin(phi)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(-3.0, 3.0)
    ax.set_ylim(-1.0, 3.0)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--')
    
    ax.plot(TARGET_X, TARGET_Y, 'go', markersize=12, label="Titik Target Input")
    ax.plot([x0, x1, x2, x3], [y0, y1, y2, y3], 'o-', lw=5, markersize=8, color='#2c3e50', markerfacecolor='#e74c3c')
    
    ax.set_title("Simulasi Inverse Kinematics", fontweight='bold')
    ax.legend()
    plt.show()
