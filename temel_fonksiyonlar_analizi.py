"""
Temel Python Fonksiyonlari ile Veri Analizi Ornegi
Bu betik; liste, dongu, kosul, fonksiyon, dosya yazma ve temel veri analizi adimlarini gostermek icin hazirlanmistir.
Colab, Posit Cloud (Python ortami) veya yerel bilgisayarda calistirilabilir.
"""

import csv
import statistics
from pathlib import Path

# 1) Ornek veri seti
students = [
    {"ad": "Ayse",  "vize": 78, "final": 84},
    {"ad": "Mehmet","vize": 65, "final": 72},
    {"ad": "Zeynep","vize": 90, "final": 95},
    {"ad": "Can",   "vize": 55, "final": 60},
    {"ad": "Elif",  "vize": 88, "final": 91},
    {"ad": "Ali",   "vize": 70, "final": 68},
    {"ad": "Ece",   "vize": 92, "final": 89},
    {"ad": "Mert",  "vize": 40, "final": 58},
]

# 2) Temel fonksiyonlar
def not_hesapla(vize, final):
    """Donem sonu notunu hesaplar."""
    return round(vize * 0.4 + final * 0.6, 2)

def harf_notu(ortalama):
    """Sayisal notu harf notuna cevirir."""
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 60:
        return "DC"
    elif ortalama >= 50:
        return "DD"
    else:
        return "FF"

def durum_belirle(ortalama):
    """Gecme/kalma durumunu dondurur."""
    return "Gecti" if ortalama >= 60 else "Kaldi"

# 3) Veri zenginlestirme
for ogrenci in students:
    ort = not_hesapla(ogrenci["vize"], ogrenci["final"])
    ogrenci["ortalama"] = ort
    ogrenci["harf"] = harf_notu(ort)
    ogrenci["durum"] = durum_belirle(ort)

# 4) Ozet istatistikler
ortalamalar = [o["ortalama"] for o in students]
sinif_ortalamasi = round(statistics.mean(ortalamalar), 2)
en_yuksek = max(ortalamalar)
en_dusuk = min(ortalamalar)
medyan = statistics.median(ortalamalar)
gecen_sayisi = len([o for o in students if o["durum"] == "Gecti"])
kalan_sayisi = len(students) - gecen_sayisi

# 5) Sonuclari ekrana yazdirma
print("=== OGRENCI SONUCLARI ===")
for o in students:
    print(f'{o["ad"]:8} | Ortalama: {o["ortalama"]:5} | Harf: {o["harf"]:2} | Durum: {o["durum"]}')

print("\n=== OZET ISTATISTIKLER ===")
print("Ogrenci sayisi     :", len(students))
print("Sinif ortalamasi   :", sinif_ortalamasi)
print("En yuksek not      :", en_yuksek)
print("En dusuk not       :", en_dusuk)
print("Medyan             :", medyan)
print("Gecen ogrenci      :", gecen_sayisi)
print("Kalan ogrenci      :", kalan_sayisi)

# 6) CSV olarak kaydetme
output_file = Path("ogrenci_sonuclari.csv")
with output_file.open("w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["ad", "vize", "final", "ortalama", "harf", "durum"])
    writer.writeheader()
    writer.writerows(students)

print(f"\nSonuclar '{output_file}' dosyasina kaydedildi.")
