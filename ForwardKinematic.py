import numpy as np
import matplotlib.pyplot as plt

# Parameter Fisik Lengan Robot (Panjang Link)
l1, l2, l3 = 1.0, 1.0, 0.5 

print("=== PROGRAM FORWARD KINEMATICS 3-DOF ===")
print("Input: Sudut Sendi (dalam derajat)")

# Input dari user
t1_deg = float(input("Masukkan Sudut Sendi 1 (Base): "))
t2_deg = float(input("Masukkan Sudut Sendi 2 (Elbow): "))
t3_deg = float(input("Masukkan Sudut Sendi 3 (Wrist): "))

# Konversi input derajat ke radian untuk fungsi trigonometri
t1 = np.radians(t1_deg)
t2 = np.radians(t2_deg)
t3 = np.radians(t3_deg)

# Kalkulasi Forward Kinematics (Penjumlahan Vektor)
x0, y0 = 0.0, 0.0
x1, y1 = l1 * np.cos(t1), l1 * np.sin(t1)
x2, y2 = x1 + l2 * np.cos(t1 + t2), y1 + l2 * np.sin(t1 + t2)
x3, y3 = x2 + l3 * np.cos(t1 + t2 + t3), y2 + l3 * np.sin(t1 + t2 + t3)

print("\n--- HASIL FORWARD KINEMATICS ---")
print(f"Posisi akhir End-Effector berada di koordinat:")
print(f"X = {x3:.2f}")
print(f"Y = {y3:.2f}")

# Visualisasi
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-3.0, 3.0)
ax.set_ylim(-1.0, 3.0)
ax.set_aspect('equal')
ax.grid(True, linestyle='--')

ax.plot([x0, x1, x2, x3], [y0, y1, y2, y3], 'o-', lw=5, markersize=8, color='#2980b9', markerfacecolor='#e74c3c')
ax.plot(x3, y3, 'g*', markersize=15, label=f"Posisi Akhir ({x3:.2f}, {y3:.2f})")

ax.set_title("Simulasi Forward Kinematics", fontweight='bold')
ax.legend()
plt.show()
