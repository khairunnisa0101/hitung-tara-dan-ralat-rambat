import math

# === Konstanta Tetap ===
# Kapasitas kalor air (J/kg°C)
Ca = 1000
# Kapasitas kalor kalorimeter (J/kg°C)
Ckal = 210
# Arus listrik (Ampere)
I = 2
# Hambatan (Ohm)
R = 4.1
# Massa air (kg)
Ma = 0.147
# Massa kalorimeter (kg)
Mk = 0.054
# Ketidakpastian suhu (°C)
deltaT = 0.5
# Ketidakpastian massa (kg)
deltaM = 0.00005

# === Input dari pengguna ===
t = float(input("Masukkan waktu (dalam detik): "))
percobaan = float(input("Masukkan nomor percobaan (1 / lainnya): "))
T1 = float(input("Masukkan suhu akhir pada waktu ke-t (°C): "))

# Suhu awal (T0) tergantung percobaan ke berapa
if percobaan == 1:
    T0 = 23
else:
    T0 = 24

# === Perhitungan nilai tara ===
tara = ((Ma * Ca + Mk * Ckal) * (T1 - T0)) / ((I ** 2) * R * t)

# === Hitung turunan parsial untuk ralat rambat ===
parsialMa = (Ca * (T1 - T0)) / ((I ** 2) * R * t)
parsialMk = (Ckal * (T1 - T0)) / ((I ** 2) * R * t)
parsialDeltaT = (Ma * Ca + Mk * Ckal) / ((I ** 2) * R * t)

# === Perhitungan ralat rambat menggunakan propagasi ketidakpastian ===
ralatrambat = math.sqrt(
    (parsialMa * deltaM) ** 2 +
    (parsialMk * deltaM) ** 2 +
    (parsialDeltaT * deltaT) ** 2
)

# === Menampilkan hasil ===
print("\n=== HASIL PERHITUNGAN ===")
print("Tara (η) = ", round(tara, 6))
print("Parsial terhadap Ma = ", round(parsialMa, 6))
print("Parsial terhadap Mk = ", round(parsialMk, 6))
print("Parsial terhadap ΔT = ", round(parsialDeltaT, 6))
print("Ralat rambat = ", round(ralatrambat, 6))
