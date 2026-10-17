import random
import time

mazeretler = [
    "Trafik o kadar yoğundu ki, arabamın içinde zaman genişlemesi yaşadım. Einstein bile şaşırdı.",
    "Kedi evin anahtarını yutmuş, ben de veterinerde kedi için mazeret bekledim.",
    "Uyanınca saat 07:00'ydi ama saat 07:00'nin kendisi gecikmiş.",
    "Evden çıkarken kapı kilitlendi ve anahtar içeride kaldı, ama asıl sorun kapının varlığı.",
    "Metro geldi ama içinde sadece bir tane yolcu vardı ve o da ben değildim.",
    "Kahvaltı yaparken ekmek bitti, ekmek almak için çıktım, ekmekçi de gecikmiş.",
    "Bugün takvimde bir gün atlanmış, ben de o günü yaşamaya çalıştım.",
    "Bilgisayar açılmadı çünkü elektriğin kendisi gecikmiş."
]

def mazeret_uret():
    print("Gecikme Mazeret Üreteci çalışıyor...")
    time.sleep(1)
    secilen = random.choice(mazeretler)
    print(f"\nResmi Mazeret: {secilen}")
    print("\nBu mazeret %100 gerçek değildir ama %100 gereklidir.")
    print("Lütfen patrona iletin, yoksa evren çöker.")

if __name__ == "__main__":
    mazeret_uret()
    print("\nBir tane daha ister misiniz? (Hayır deyin, çünkü evet demezsiniz)")
