

print("-----------HOŞGELDİNİZ----------" "\n")

print("-------------------------------------")

isminiz = input("isminizi giriniz = ")

print("-------------------------------------")

faiz_orani = float(input("Senelik Faiz Oranini Giriniz = "))

print("-------------------------------------")

kredi_miktari = float(input("Kredi Miktarini Giriniz = "))

print("-------------------------------------")

maksimum_yil = int(input("Maksimum Yili Giriniz = "))

print("-------------------------------------")

maksimum_ay = int(input("Maksimum Ayi Giriniz = "))

print("-------------------------------------")

yineleme = int(input("Yineleme Araliğini Giriniz = "))

print("-------------------------------------")



def print_duration(maksimum_ay):
    koyulacak_yil = int(maksimum_ay/12)
    kalacak_ay = int(maksimum_ay%12)
    print("ay", kalacak_ay,"yil", koyulacak_yil)
         
#YIL OLARAK GİRDİĞİMİZ DEĞERİ AY CİNSİNDEN YAZDIRIYORUZ.


def print_money(kredi_miktari):
    print(format(kredi_miktari , ".1f"), "$")
   
#DOLAR İŞARETİ EKLİYORUZ VE VİRGÜLDEN SONRA BİR BASAMAK OLMASINI AYARLIYORUZ.

    
def print_entry(kredi, yillik_oran, ay):
    toplam_faiz = (kredi)/100 * ay * (yillik_oran/12)
    print("toplam odeme:")
    print_money(kredi + toplam_faiz)
    print("aylik odeme:")
    print_money((kredi+toplam_faiz)/ay)

#İLK İKİ FONKSİYONDAKİ DEĞERLERİ ÇAĞIRIP BİRLİKTE YAZDIRIYORUZ.   


def print_full_report(kredi_miktari, maksimum_yil, maksimum_ay, yineleme, faiz_orani): 
    a= yineleme
    while(a<= maksimum_ay + (maksimum_yil * 12)):
         print_duration(a)  
         print_entry(kredi_miktari, faiz_orani, yineleme)
         a+=yineleme
   
#KULLANICIDAN ÇAĞIRILAN GİRDİLERİN EKRANDA KAÇ KEZ YİNELENECEĞİNİ AYARLIYORUZ  
   
print_full_report(kredi_miktari, maksimum_yil, maksimum_ay, yineleme, faiz_orani)
