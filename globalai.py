class Library:
    def __init__(self):
        self.file = open("kitaplar.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_kitaplar(self):
        self.file.seek(0)
        kitaplar = self.file.read().splitlines()
        if not kitaplar:
            print("Mevcut Kitap Bulunamadı.")
        else:
            print("Kitap Listesi:")
            for kitap in kitaplar:
                kitap_bilgisi = kitap.split(',')
                print(f"başlık: {kitap_bilgisi[0]}, yazar: {kitap_bilgisi[1]}")

    def kitap_ekle(self):
        baslik = input("Kitap Başlığı Giriniz: ")
        yazar = input("Yazar Adı Giriniz: ")
        yayin_yili = input("Yayınlanma Yılını Giriniz: ")
        sayfa = input("Sayfa Sayısını Giriniz: ")

        kitap_bilgisi = f"{baslik},{yazar},{yayin_yili},{sayfa}\n"
        self.file.write(kitap_bilgisi)
        print("Kitap Eklendi")

    def remove_kitap(self):
        baslik = input("Silmek İstediğiniz Kitabın Adını Giriniz: ")
        self.file.seek(0)
        kitaplar = self.file.readlines()
        found = False

        for kitap in kitaplar:
            if baslik in kitap:
                kitaplar.remove(kitap)
                found = True

        if found:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(kitaplar)
            print("Kitap Kaldırıldı.")
        else:
            print("Kitap Bulunamadı. ")

lib = Library()

while True:
    print("\n*** MENÜ ***")
    print("1) Kitap Listesi: ")
    print("2) Kitap Ekle: ")
    print("3) Kitap Kaldır: ")
    print("4) Çıkış")

    choice = input("Yapmak İstediğiniz İşlemi Seçiniz: ")

    if choice == "1":
        lib.list_kitaplar()
    elif choice == "2":
        lib.kitap_ekle()
    elif choice == "3":
        lib.remove_kitap()
    elif choice == "4":
        break
    else:
        print("Geçersiz seçim. Lütfen geçerli bir seçenek girin. ")