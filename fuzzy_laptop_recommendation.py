# Import library yang diperlukan
import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Baca dataset
print("Loading dataset...")
df = pd.read_excel('dataset laptop asus.xlsx')
print("\nContoh data laptop:")
print(df.head())

# Membuat variabel fuzzy
budget = ctrl.Antecedent(np.arange(0, 50000000, 1000000), 'budget')
performa = ctrl.Antecedent(np.arange(0, 10, 1), 'performa')
ukuran_layar = ctrl.Antecedent(np.arange(11, 18, 0.1), 'ukuran_layar')
rekomendasi = ctrl.Consequent(np.arange(0, 100, 1), 'rekomendasi')

# Membership function untuk budget
budget['rendah'] = fuzz.trimf(budget.universe, [0, 0, 15000000])
budget['sedang'] = fuzz.trimf(budget.universe, [10000000, 20000000, 30000000])
budget['tinggi'] = fuzz.trimf(budget.universe, [25000000, 50000000, 50000000])

plt.figure(figsize=(10, 5))
budget.view()
plt.title('Membership Function Budget')
plt.show()

# Membership function untuk performa
performa['basic'] = fuzz.trimf(performa.universe, [0, 0, 4])
performa['medium'] = fuzz.trimf(performa.universe, [3, 5, 7])
performa['tinggi'] = fuzz.trimf(performa.universe, [6, 10, 10])

plt.figure(figsize=(10, 5))
performa.view()
plt.title('Membership Function Performa')
plt.show()

# Membership function untuk ukuran layar
ukuran_layar['kecil'] = fuzz.trimf(ukuran_layar.universe, [11, 11, 14])
ukuran_layar['sedang'] = fuzz.trimf(ukuran_layar.universe, [13, 14, 15])
ukuran_layar['besar'] = fuzz.trimf(ukuran_layar.universe, [14, 17, 17])

plt.figure(figsize=(10, 5))
ukuran_layar.view()
plt.title('Membership Function Ukuran Layar')
plt.show()

# Membership function untuk rekomendasi
rekomendasi['tidak_rekomendasi'] = fuzz.trimf(rekomendasi.universe, [0, 0, 40])
rekomendasi['pertimbangkan'] = fuzz.trimf(rekomendasi.universe, [30, 50, 70])
rekomendasi['rekomendasi'] = fuzz.trimf(rekomendasi.universe, [60, 100, 100])

plt.figure(figsize=(10, 5))
rekomendasi.view()
plt.title('Membership Function Rekomendasi')
plt.show()

# Membuat aturan fuzzy
print("\nMembuat aturan fuzzy...")

# Aturan untuk budget rendah
rule1 = ctrl.Rule(budget['rendah'] & performa['basic'] & ukuran_layar['kecil'], rekomendasi['rekomendasi'])
rule2 = ctrl.Rule(budget['rendah'] & performa['basic'] & ukuran_layar['sedang'], rekomendasi['pertimbangkan'])
rule3 = ctrl.Rule(budget['rendah'] & performa['medium'] & ukuran_layar['kecil'], rekomendasi['pertimbangkan'])

# Aturan untuk budget sedang
rule4 = ctrl.Rule(budget['sedang'] & performa['medium'] & ukuran_layar['sedang'], rekomendasi['rekomendasi'])
rule5 = ctrl.Rule(budget['sedang'] & performa['tinggi'] & ukuran_layar['sedang'], rekomendasi['rekomendasi'])
rule6 = ctrl.Rule(budget['sedang'] & performa['medium'] & ukuran_layar['besar'], rekomendasi['pertimbangkan'])

# Aturan untuk budget tinggi
rule7 = ctrl.Rule(budget['tinggi'] & performa['tinggi'] & ukuran_layar['besar'], rekomendasi['rekomendasi'])
rule8 = ctrl.Rule(budget['tinggi'] & performa['tinggi'] & ukuran_layar['sedang'], rekomendasi['rekomendasi'])
rule9 = ctrl.Rule(budget['tinggi'] & performa['medium'] & ukuran_layar['besar'], rekomendasi['pertimbangkan'])

# Sistem kontrol dengan semua aturan
sistem_kontrol = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
sistem = ctrl.ControlSystemSimulation(sistem_kontrol)

def get_rekomendasi(budget_input, performa_input, layar_input):
    sistem.input['budget'] = budget_input
    sistem.input['performa'] = performa_input
    sistem.input['ukuran_layar'] = layar_input
    
    try:
        sistem.compute()
        return sistem.output['rekomendasi']
    except:
        return 0

# Input dari pengguna
print("=== Sistem Pakar Rekomendasi Laptop ASUS ===")
budget_input = float(input("Masukkan budget (dalam rupiah): "))
performa_input = float(input("Masukkan kebutuhan performa (0-10): "))
layar_input = float(input("Masukkan ukuran layar yang diinginkan (11-17 inch): "))

hasil = get_rekomendasi(budget_input, performa_input, layar_input)
print(f"\nNilai rekomendasi: {hasil:.2f}")

if hasil >= 60:
    print("Status: Sangat Direkomendasikan")
    print("\nKriteria pencarian:")
    print(f"- Budget: Rp {budget_input:,.0f}")
    print(f"- Performa: {performa_input}")
    print(f"- Ukuran Layar: {layar_input} inch")
elif hasil >= 40:
    print("Status: Pertimbangkan")
else:
    print("Status: Tidak Direkomendasikan") 