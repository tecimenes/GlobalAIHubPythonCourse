giris = "Merhaba, bilgi yarışmasına hoş geldin! 10 soru ve her sorunun eşit puana sahip olduğu bu yarışmada doğru olduğunu düşündüğün şıkkı veya karşılık geldiği kelimeyi yazabilirsin. Kazanmak için en az 5 soruyu doğru cevaplamalısın. Başarılar!\n"
sorular= ["Pep Guardiola, José Mourinho, Jürgen Klopp hangi spor dalında şampiyonluk kazanmış isimlerdir?\nA:Atletizm \nB:Futbol \nC:Basketbol \nD:Bilardo",
          "Hangisi periyodik tabloda bulunan bir element değildir?\nA:Oksijen\nB:Azot\nC:Su\nD:Kalay",
          "Hangi ülke Asya kıtasındadır?\nA:Somali\nB:Kamboçya\nC:Namibya\nD:Gabon",
          "Bilge Kağan hangi Türk devletinin kurucusudur?\nA:Avarlar\nB:Göktürkler\nC:Karahanlılar\nD:Uygurlar",
          "Hangisi kuvvet birimidir?\nA:Newton\nB:Pascal\nC:Joule\nD:Faraday",
          "Scoville ölçeği hangisini ölçer?\nA:Deniz tuzluluğunu\nB:Çikolata tatlılığını\nC:Limon ekşiliğini\nD:Biber acılığını",
          "Fas'ın başkenti hangi şehirdir?\nA:Kahire\nB:Nairobi\nC:Rabat\nD:Kasablanka",
          "Atatürk'ün yurt gezilerinde (1935-1938) yılları arasında kullandığı trenin adı nedir?\nA:Beyaz Tren\nB:Kara Duman\nC:Demir Türk\nD:Anadolu",
          "Beslenmesinde balık dışında başka ete yer vermeyen kişilere ne denir?\nA:Parnasyen\nB:Peskataryan\nC:Gaseyan\nD:Devoniyen",
          "Türkçede kelimeler en çok hangi harfle başlar?\nA:K harfi\nB:M harfi\nC:R harfi\nD:S harfi"]
cevaplar= ["Futbol", "Su", "Kamboçya", "Uygurlar", "Newton","Biber acılığını", "Rabat", "Beyaz Tren", "Peskataryan", "K harfi"]
cevaplarharf = ["B", "C", "B", "D", "A", "D", "C", "A", "B", "A"]
puan = 0
print(giris)
for i in range(len(sorular)):
    print(sorular[i])
    cevap = str(input("Cevap:"))
    cevap == cevaplar[i] or cevaplarharf[i]
    if cevap.lower() == cevaplar[i].lower() or cevap.lower() == cevaplarharf[i].lower():
        puan += 10
        print("Doğru cevap!!\nŞu anki puanınız: {}\n".format(puan))
    else:
        print("Maalesef! Doğru cevap {}:{} olmalıydı.\nŞu anki puanınız: {}\n".format(cevaplarharf[i], cevaplar[i], puan))

if puan >= 50:
    print("{} soruda {} doğru. Tebrikler!!!".format(len(sorular), int(puan/10)))
else:
    print("{} soruda {} doğru. Tekrar Dene!".format(len(sorular), int(puan/10)))