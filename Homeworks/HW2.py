# Kişi bilgileri https://random-name-generator.com/turkey adresinden oluşturulmuştur.
# Gerçek kişileri temsil etmemektedir.

CV1 = {"name" :"Koray", "sname":"Adıvar", "mail":"korayvar@mail.com", "age":25, "address":"İnegöl/Bursa", "title":"Kimya Mühendisi", "experience":"2 yıl.","languages" : "İngilizce, Almanca","IT" : "Python, Java, C"}
CV2 = {"name":"Sinem", "sname":"Orbay", "mail":"sinbay@mail.com", "age":19, "address":"Armutlu/Yalova", "title":"Öğrenci", "experience":"Yok", "languages" : "İngilizce", "IT" : "HTML, CSS"}
CV3 = {"name":"Ece", "sname":"Durak", "mail":"ecedrak@mail.com", "age":34, "address":"Edremit/Balıkesir", "title":"Kimya Teknikeri", "experience":"9 yıl", "languages" : "İngilizce", "IT" : "Chemcad, Matlab"}
CV4 = {"name":"Armağan", "sname":"Akyüz", "mail":"armayuz@kmail.com", "age":28, "address":"Gemlik/Bursa", "title":"Metalurji Mühendisi", "experience":"5 yıl", "languages" : "İngilizce, Rusça", "IT" : "Python, C#"}
CV5 = {"name":"Ebru", "sname":"Ozansoy", "mail":"ebrusoy@mail.com", "age":23, "address":"Bozcaada/Çanakkale", "title":"Kimyager", "experience":"6 ay", "languages" : "Yok", "IT" : "MS Office"}

def CVprint(ad, soyad, email, yas, adres, unvan, deneyim, ydil, bilisim):
    print("Ad               : ", ad)
    print("Soyad            : ", soyad)
    print("E-mail           : ", email)
    print("Yaş              : ", yas)
    print("Adres            : ", adres)
    print("Unvan            : ", unvan)
    print("Deneyim          : ", deneyim)
    print("Yabancı Dil      : ", ydil)
    print("IT yetkinlikleri : ", bilisim)
    print("-"*40)
    
CVprint(CV1.get("name"), CV1.get("sname"), CV1.get("mail"), CV1.get("age"), CV1.get("address"), CV1.get("title"), CV1.get("experience"), CV1.get("languages"), CV1.get("IT"))
CVprint(CV2.get("name"), CV2.get("sname"), CV2.get("mail"), CV2.get("age"), CV2.get("address"), CV2.get("title"), CV2.get("experience"), CV2.get("languages"), CV2.get("IT"))
CVprint(CV3.get("name"), CV3.get("sname"), CV3.get("mail"), CV3.get("age"), CV3.get("address"), CV3.get("title"), CV3.get("experience"), CV3.get("languages"), CV3.get("IT"))
CVprint(CV4.get("name"), CV4.get("sname"), CV4.get("mail"), CV4.get("age"), CV4.get("address"), CV4.get("title"), CV4.get("experience"), CV4.get("languages"), CV4.get("IT"))
CVprint(CV5.get("name"), CV5.get("sname"), CV5.get("mail"), CV5.get("age"), CV5.get("address"), CV5.get("title"), CV5.get("experience"), CV5.get("languages"), CV5.get("IT"))
