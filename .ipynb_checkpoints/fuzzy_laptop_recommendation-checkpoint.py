import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Baca dataset
df = pd.read_excel('dataset laptop asus.xlsx')

# Membuat variabel fuzzy
budget = ctrl.Antecedent(np.arange(0, 50000000, 1000000), 'budget')
performa = ctrl.Antecedent(np.arange(0, 10, 1), 'performa')
ukuran_layar = ctrl.Antecedent(np.arange(11, 18, 0.1), 'ukuran_layar')
rekomendasi = ctrl.Consequent(np.arange(0, 100, 1), 'rekomendasi')

# Membership function untuk budget
budget['rendah'] = fuzz.trimf(budget.universe, [0, 0, 15000000])
budget['sedang'] = fuzz.trimf(budget.universe, [10000000, 20000000, 30000000])
budget['tinggi'] = fuzz.trimf(budget.universe, [25000000, 50000000, 50000000])

# Membership function untuk performa
performa['basic'] = fuzz.trimf(performa.universe, [0, 0, 4])
performa['medium'] = fuzz.trimf(performa.universe, [3, 5, 7])
performa['tinggi'] = fuzz.trimf(performa.universe, [6, 10, 10])

# Membership function untuk ukuran layar
ukuran_layar['kecil'] = fuzz.trimf(ukuran_layar.universe, [11, 11, 14])
ukuran_layar['sedang'] = fuzz.trimf(ukuran_layar.universe, [13, 14, 15])
ukuran_layar['besar'] = fuzz.trimf(ukuran_layar.universe, [14, 17, 17])

# Membership function untuk rekomendasi
rekomendasi['tidak_rekomendasi'] = fuzz.trimf(rekomendasi.universe, [0, 0, 40])
rekomendasi['pertimbangkan'] = fuzz.trimf(rekomendasi.universe, [30, 50, 70])
rekomendasi['rekomendasi'] = fuzz.trimf(rekomendasi.universe, [60, 100, 100])

# Aturan fuzzy
rule1 = ctrl.Rule(budget['rendah'] & performa['basic'] & ukuran_layar['kecil'], rekomendasi['rekomendasi'])
rule2 = ctrl.Rule(budget['tinggi'] & performa['tinggi'] & ukuran_layar['besar'], rekomendasi['rekomendasi'])
rule3 = ctrl.Rule(budget['sedang'] & performa['medium'] & ukuran_layar['sedang'], rekomendasi['pertimbangkan'])

# Sistem kontrol
sistem_kontrol = ctrl.ControlSystem([rule1, rule2, rule3])
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

# Contoh penggunaan
if __name__ == "__main__":
    print("Sistem Pakar Rekomendasi Laptop Asus")
    budget_input = float(input("Masukkan budget (dalam rupiah): "))
    performa_input = float(input("Masukkan kebutuhan performa (0-10): "))
    layar_input = float(input("Masukkan ukuran layar yang diinginkan (11-17 inch): "))
    
    hasil = get_rekomendasi(budget_input, performa_input, layar_input)
    print(f"\nNilai rekomendasi: {hasil}")
    
    if hasil >= 60:
        print("Status: Sangat Direkomendasikan")
    elif hasil >= 40:
        print("Status: Pertimbangkan")
    else:
        print("Status: Tidak Direkomendasikan") 