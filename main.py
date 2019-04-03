import pymysql

db = pymysql.connect("localhost", "root", "", "cse224")
cursor = db.cursor()


def signup():
    name = input("Adınızı ve soyadınızı giriniz.")
    userName = input("Kullanıcı adı giriniz.")
    password = input("Şifre giriniz.")
    # cursor.execute('insert into users values("%s", "%s", "%s")' % (name, userName, password))
    sql = "INSERT INTO users(name, username, password) VALUES ('%s', '%s', '%s' )" % (name, userName, password)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def login():
    v = 0
    r = 4
    for i in range(0, 3):
        r -= 1
        userName = input("Kullanıcı adı giriniz.")
        password = input("Şifre giriniz.")
        sql = "SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (userName, password)
        try:
            cursor.execute(sql)
            if cursor.fetchone() is not None:
                print("Başarılı")
                v = 1
                break
            else:
                print("Başarısız giriş, '%s' hakkın kaldı" % (r-1))
                v = 0
            db.commit()
        except:
            db.rollback()
    if v == 0:
        print("misafir olarak giriş yapılıyor.")
    else:
        print("Logged in")
    return v


def wrongchoice():
    print("Yanlış bir giriş yaptın tekrar dene.\n")


def buy(valid):
    if valid == 1:
        x = int(input("Satın almak istediğiniz ürünü seçin.\n"))
    else:
        print("Satın almak için lütfen giriş yapın.")


def shopping(valid):
    choice3 = int(input("1:Bilgisayar\n2:Beyaz Eşya\n3:Diğer Elektronik\n"))
    if choice3 == 1:
        choiceC = int(input("1:Dizüstü bilgisayar.\n2:Masaüstü bilgisayar.\n"))
        if choiceC == 1:
            print("1:ASUS S430FN CORE İ7 8565U 1.8GHZ-8GB RAM-256GB SSD-14\"-MX150 2GB-W10 Fiyat:7.519 TL")
            print(
                "2:OMEN BY HP17-AN109NT CORE İ7 8750H 2.2GHZ-16GB-2TB+256SSD-17.3''GTX1050Ti4GB-W10 Fiyat:10.299 TL")
            print("3:DELL INSPIRON 15 3580 CORE İ5 8265U 1.6GHZ-8GB RAM-256GB SSD-2GB-15.6\"W10 Fiyat:4.726 TL")
            print(
                "4:HP PAVILION15-CX0032NT COREİ7 8750H 2.2GHZ-16GB-1TB+256GBSSD-15.6\"-GTX1050Ti-W10 Fiyat:8.999 TL")
            print("5:ACER A114 CELERON N4000 1.1GHZ-4GB RAM-32GB EMMC-14\"-INT-W10 NOTEBOOK Fiyat:1.598 TL")
            buy(valid)
        elif choiceC == 2:
            print("1:MSI PRO 24X CORE İ5 7200U 2.5GHZ 8GB+16GB OPTANE 1TB INTEL HD 620 WIN10 23.8\" Fiyat:6.012 TL")
            print("2:EXPER G23-561 INTEL CORE İ5 7400 3 GHZ 4 GB 1TB INTEL HD 630 WIN10 23\" Fiyat:4.881 TL")
            print("3:ASUS GL12CX-TR005T İ9 9900K 3.6 GHZ 32 GB 1TB+256SSD 8 GB NVIDIA RTX2080 WIN10 Fiyat:25.293 TL")
            print("4:ASUS GL12CX-TR006T İ7 9700K 3.6 GHZ 16 GB 1TB+128SSD 8 GB NVIDIA RTX2070 WIN10 Fiyat:19.196 TL")
            print("5:EXPER ACTIVE DEX321W INTEL CELERON J3355 2GHZ 4GB 500GB INTEL HD GRAPHICS WIN10 Fiyat:1.799 TL")
            buy(valid)
        else:
            wrongchoice()
    elif choice3 == 2:
        choiceB = int(input("1:Çamaşır Makineleri\n2:Çay Makineleri\n3:Bulaşık Makineleri\n4:Su\n"))
        if choiceB == 1:
            print("1:Vestfrost VF ÇM 5800 A++ 5 kg 800 Devir Çamaşır Makinesi Fiyat:999 TL")
            print("2:Vestfrost VWM 9122/9120 A++ 9 kg 1200 Devir Çamaşır Makinesi Fiyat: 1.299 TL")
            print("3:Vestel CM 5608 A++ Çamaşır Makinesi Fiyat:1.267 TL")
            buy(valid)
        elif choiceB == 2:
            print("1:Sinbo Stm-5812 Elektrikli Çay Makinesi Fiyat:79 TL")
            print("2:Aldente Semaver Çaycı Elektrikli Çay Makinesi Kettle Çaydanlık Çay Fiyat:99 TL")
            print("3:Sunny Lateafe Elektrikli Çaycı Lüx Çay Makinesi Fiyat:97 TL")
            buy(valid)
        elif choiceB == 3:
            print("1:Arçelik 6344 A Bulaşık Makinesi Fiyat:2.028 TL")
            print("2:Profilo BM4226EG Bulaşık Makinesi Fiyat:1.350 TL")
            print(
                "3:Electrolux ESF2300OW Compact A Enerji Sınıfı 6 Programlı Tezgahüstü Bulaşık Makinesi Fiyat:1390 TL")
            buy(valid)
        elif choiceB == 4:
            print("1:Vestel SP 120 Normal&Soğuk Su Sebili Beyaz Fiyat:299 TL")
            print("2:Bosch Rdw1570 Gizli Damacanalı Gri Su Sebili Fiyat:1.219 TL")
            print("3:Simfer Sb 2604 Dijital Ekranlı Sıcak-soğuk Su Sebili Fiyat:688 TL")
            buy(valid)
        else:
            wrongchoice()
    elif choice3 == 3:
        choiceE = int(input("1:Cep Telefonu\n2:Televizyon\n"))
        if choiceE == 1:
            print("1:Sony Xperia Z (c6603) Cep Telefonu Fiyat:599 TL")
            print("2:Huawei Mate 20 Pro Twilight Cep Telefonu Fiyat:6.499 TL")
            print("3:Xiaomi Redmi 6 Pro 4 GB 32 GB Cep Telefonu Snapdragon 625 Octa Fiyat:996 TL")
            print("4:XİAOMİ Mİ A2 LİTE 64 GB 4GB RAM CEP TELEFONU Fiyat:1.299 TL")
            print("5:Samsung Galaxy M20 32GB SM-M205F Fiyat:1.599 TL")
            buy(valid)
        elif choiceE == 2:
            print("1:Vestel Finlux 43\"(110cm) Ultrahd 4k Smart Wifi 1200hz Led Tv Fiyat:2.000 TL")
            print("2:Arçelik A32L 6850 5B Smart TV Fiyat:1.299 TL")
            print("3:Samsung Ue-55nu7300 Curved 4k Uydu Alıcılı Smart Led Televizyon Fiyat:4.599 TL")
            buy(valid)
        else:
            wrongchoice()
    else:
        wrongchoice()


validation = 0
while validation == 0:
    choice = int(input("1:Alışveriş yapmak istiyorum.\n2:Sadece gezinmek istiyorum.\n3:Çıkmak istiyorum.\n"))
    if choice == 1:
        print("Lütfen kayıt olun.\n")
        choice2 = int(input("1:Kayıt olmak istiyorum.\n2:Mevcut hesabıma giriş yapmak istiyorum.\n"))
        if choice2 == 1:
            signup()
            validation = login()
        elif choice2 == 2:
            validation = login()
        else:
            wrongchoice()
    elif choice == 2:
        print("Gezindin")
        shopping(validation)
    elif choice == 3:
        break
    else:
        wrongchoice()
while validation == 1:
    # print("Başarılı.")
    shopping(validation)
    break

db.close()
