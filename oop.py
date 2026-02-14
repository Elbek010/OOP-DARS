# 1 - misol
# class avto:
#     def __init__(self,nomi, narxi, yili, rangi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.yili = yili
#         self.rangi = rangi
#     def get_info(self):
#         return f"Mashina nomi {self.nomi}\nMashina natxi {self.narxi}\nMashina isjlab chiqqan yili {self.yili}\nMashina rangi {self.rangi}"
#     def get_price(self):
#         return self.narxi
# if __name__ == "mashinalar":
#     avto1 = avto("BMW m 5", 20000, 2020, "qora")
#     print(avto1.get_info())
#     print("Narxi:", avto1.get_price())
#     avto2 = avto("AUDI S 9", 18000, 2019, "Ko'k")
#     print(avto2.get_info())
#     print("Narxi:", avto2.get_price())
# class mashina:
#     def get_info(self):
#         return f"Mashina nomi {self.nomi}\nMashina narxi {self.narxi}\nMashina ishlab chiqilgan yili {self.yili}\nMashina rangi {self.rangi}"
#     def get_price(self, current_year , prestage_of_color):
#         count_year  = current_year - self.year     
#         if count_year >= 5:
#             self.narxi = self.narxi - (self.narxi * 0.1)
#         if prestage_of_color == "qora":
#             self.narxi = self.narxi - (self.narxi * 0.05)
#         return self.narxi

#     def __init__(self, nomi, narxi, yili, rangi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.year = yili
#         self.rangi = rangi

# if __name__ == "__main__":
#     avto1 = mashina("BMW m 5", 20000, 2020, "qora")
#     print(avto1.get_info())
#     print("Narxi:", avto1.get_price(2024, "qora"))
#     avto2 = mashina("AUDI S 9", 18000, 2019, "Ko'k")
#     print(avto2.get_info())
#     print("Narxi:", avto2.get_price(2024, "Ko'k"))


# class mahsulot:
#     def __init__(self,mahsulot_nomi,mahsulot_narxi,mahsulot_turi):
#         self.name = mahsulot_nomi
#         self.price = mahsulot_narxi
#         self.turi = mahsulot_turi


#     def get_info(self):
#         return f"Mahsulot nomi : {self.name}\nMahsulot narxi : {self.price}\nMahsulot turi : {self.turi}"
    
#     def get_price(self):
#         return self.price

# class sut(mahsulot):
#     def __init__(self, mahsulot_nomi, mahsulot_narxi, mahsulot_turi):
#         super().__init__(mahsulot_nomi, mahsulot_narxi, mahsulot_turi)




        
# mahsulot1 = mahsulot("olma", 5000, "meva")
# print(mahsulot1.get_info())
# print("Narxi:", mahsulot1.get_price())
# mahsulot2 = mahsulot("banan", 4000, "meva")
# print(mahsulot2.get_info())
# print("Narxi:", mahsulot2.get_price())






# 1 - misol done

# class avto:
#     def __init__(self, nomi, narxi, yili, rangi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.yili = yili
#         self.rangi = rangi

#     def get_info(self):
#         return f"Mashina nomi {self.nomi}\nMashina narxi {self.narxi}\nMashina ishlab chiqilgan yili {self.yili}\nMashina rangi {self.rangi}"

#     def get_price(self):
#         return self.narxi
    
#     class BMW:
#                 model_name = "BMW"
#     def get_model(self):
#         return f"Model: {self.model_name}"
    
# best1 = avto("bmw m5",130000, 2026, "qora")
# print(best1.get_info())

# class audi(avto):
#      def __init__(self, nomi, narxi, yili, rangi, tezlik , classika):
#           super().__init__(nomi, narxi, yili, rangi)

#           self.tezlik = tezlik
#           self.classika = classika
#      def get_info(self):
#           return f"Mashina nomi {self.nomi}\nMashina narxi {self.narxi}\nMashina ishlab chiqilgan yili {self.yili}\nMashina rangi {self.rangi}\nTezlik {self.tezlik}\nClassika {self.classika}"
#      def get_price(self):
#           return self.narxi
# best2 = audi("audi S9", 140000, 2027, "to'q qora", 300, "classik")
# print(best2.get_info())




# 2 - misol
# class ota:
#     def __init__(self,ism,yosh):
#         self.ism = ism 
#         self.yosh = yosh

#     def get_info(self):
#         return f"Ismi {self.ism}\nYoshi{self.yosh}"
    
# class bola(ota):
#     def __init__(self, ism, yosh,mahtab_nomi):
#         super().__init__(ism, yosh)
        

#         self.maktab_nomi = mahtab_nomi

#     def get_info(self):
#         return f"Ismi{self.ism}\nYoshi{self.yosh}\nMaktabi{self.maktab_nomi}"
# family = bola("Elbek", 16, "20 maktab")
# print(family.get_info())
    
    

# 3-misol
# class hayvon:
#     def __init__(self, nomi, yoshi):
#         self.nomi = nomi
#         self.yoshi = yoshi

#     def get_info(self):
#         return f"Hayvon nomi {self.nomi}\nHayvon yoshi {self.yoshi}"
# class it(hayvon):
#     def __init__(self, nomi, yoshi, rangi):
#         super().__init__(nomi, yoshi)
#         self.rangi = rangi

#     def get_info(self):
#         return f"Hayvon nomi {self.nomi}\nHayvon yoshi {self.yoshi}\nHayvon rangi {self.rangi}"
# class mushuk(hayvon):
#     def __init__(self, nomi, yoshi, turi):
#         super().__init__(nomi, yoshi)
#         self.turi = turi

#     def get_info(self):
#         return f"Hayvon nomi {self.nomi}\nHayvon yoshi {self.yoshi}\nHayvon turi {self.turi}"
    
# dogs = it("ko'ppak", 2.5, "qora")
# print(dogs.get_info())
    
# 4-misol
# class avto:
#     def __init__(self,nomi,tezlik,dizayn):
#         self.namae = nomi
#         self.speed = tezlik
#         self.dizayn = dizayn


#     def get_info(self):
#         return f"Nomi:{self.namae}\nTezligi:{self.speed}\nDizayni:{self.dizayn}"
#     def get_speed(self):
#         return self.speed
# class sportcar(avto):
#     def __init__(self, nomi, tezlik, dizayn, turbo):
#         super().__init__(nomi, tezlik, dizayn)
#         self.turbo = turbo

#     def get_info(self):
#         return f"Nomi:{self.namae}\nTezligi:{self.speed}\nDizayni:{self.dizayn}\nTurbo:{self.turbo}"
#     def get_speed(self):
#         return self.speed + 50
# sport = sportcar("Lamborgini", 300, "sport dizayn", "bor")
# print(sport.get_info())
    
        
# 5-misol

# class talaba:
#     def __init__(self,ism, yosh, fakultet):
#         self.ism = ism
#         self.yosh = yosh
#         self.fakultet = fakultet
#     def get_info(self):
#         return f"Ismi:{self.ism}\nYoshi:{self.yosh}\nFakulteti:{self.fakultet}"
# class bacalavr(talaba):
#     def __init__(self, ism, yosh, fakultet,daraja):
#         super().__init__(ism, yosh, fakultet)

#         self.degri = daraja
#     def info(self):
#         return f"{self.get_info()}\nTalabaning darajasi:{self.degri}"
    


    
# talaba1 = bacalavr("Laizbek",16,"Toshkent","B1")
# print(talaba1.info())
    

# 6-misol

# class ustoz:
#     def __init__(self,maktabi,ismi,fani):
#         self.maktabi = maktabi
#         self.ismi = ismi
#         self.fani = fani


#     def info(self):
#         return f"Ismi:{self.ismi}\nFani:{self.fani}\nMaktab nomi:{self.maktabi}"
    
# class informatika(ustoz):
#     def __init__(self, maktabi, ismi, fani,kampyuter):
#         super().__init__(maktabi, ismi, fani)

#         self.kamtyuter = kampyuter

#     def info(self):
#         return f"{self.ismi}ning fani {self.fani}\nMaktabi {self.maktabi}\nKompyuteri {self.kamtyuter}"
# informatika_ustoz = informatika("20-maktab","Sarvar","Informatika","Bor")
# print(informatika_ustoz.info())


# 7-misol

# class texnika():
#     def __init__(self,qulaylik,mator,taymer):
#         self.qulaylik = qulaylik
#         self.mator = mator
#         self.taymer = taymer


#     def info(self):
#         return f"Qulayliklari:{self.qulaylik}\nMator turi:{self.mator}\nTaymeri:{self.taymer}"        
        

# class kompyuter(texnika):
#     def __init__(self, qulaylik, mator, taymer, operatsion_tizim):
#         super().__init__(qulaylik, mator, taymer)

#         self.operatsion_tizim = operatsion_tizim

#     def info(self):
#         return f"{self.get_info()}\nOperatsion tizimi:{self.operatsion_tizim}"
# kompyuter1 = kompyuter("Yuqori qulaylik","Kuchli mator","5 sekund", "Windows 11")
# print(kompyuter1.info())

# 8-misol
# class odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def get_info(self):
#         return f"Ismi: {self.ism}\nYoshi: {self.yosh}"
# class ishchi(odam):
#     def __init__(self, ism, yosh, kasbi):
#         super().__init__(ism, yosh)
#         self.kasbi = kasbi

#     def get_info(self):
#         return f"{super().get_info()}\nKasbi: {self.kasbi}"
# ishchi1 = ishchi("Vali", 15, "farrosh")
# print(ishchi1.get_info())
        
# 9-misol

# class shaxs:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def get_info(self):
#         return f"Ismi: {self.ism}\nYoshi: {self.yosh}"
# class oqituvchi(shaxs):
#     def __init__(self, ism, yosh, fan):
#         super().__init__(ism, yosh)
#         self.fan = fan

#     def get_info(self):
#         return f"{super().get_info()}\nFani: {self.fan}"
# oqituvchi1 = oqituvchi("Olim", 30, "Matematika")
# print(oqituvchi1.get_info())

# 10-misol

# class Mashina:
#     def __init__(self, nomi, narxi, yili, rangi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.yili = yili
#         self.rangi = rangi

#     def get_info(self):
#         return f"Mashina nomi: {self.nomi}\nMashina narxi: {self.narxi}\nMashina yili: {self.yili}\nMashina rangi: {self.rangi}"
# class YukMashina(Mashina):
#     def __init__(self, nomi, narxi, yili, rangi, yuk_kap):
#         super().__init__(nomi, narxi, yili, rangi)
#         self.yuk_kap = yuk_kap

#     def get_info(self):
#         return f"{super().get_info()}\nYuk ko'tarish qobiliyati: {self.yuk_kap} tonna"
# yuk_mashina1 = YukMashina("Kamaz", 50000, 2015, "Oq", 10)
# print(yuk_mashina1.get_info())

# 11-misol

# class Uchuvchi:
#     def __init__(self, nomi, tezligi, balandligi):
#         self.nomi = nomi
#         self.tezligi = tezligi
#         self.balandligi = balandligi

#     def get_info(self):
#         return f"Uchuvchi nomi: {self.nomi}\nTezligi: {self.tezligi} km/soat\nBalandligi: {self.balandligi} metr"
# class HarbiyUchuvchi(Uchuvchi):
#     def __init__(self, nomi, tezligi, balandligi, qurol_turi):
#         super().__init__(nomi, tezligi, balandligi)
#         self.qurol_turi = qurol_turi

#     def get_info(self):
#         return f"{super().get_info()}\nQurol turi: {self.qurol_turi}"
# harbiy_uchuvchi1 = HarbiyUchuvchi("Qruvchi samalyot f-16", 2400, 15000, "Turbo")
# print(harbiy_uchuvchi1.get_info())


# 12-misol

# class kitob:
#     def __init__(self,bet,bob,mavzu,nomi):
#         self.nomi = nomi
#         self.bet = bet
#         self.bob = bob
#         self.mavzu = mavzu

#     def get_info(self):
#         return f"Kitob nomi :{self.nomi}\nSahifalar soni :{self.bet}\nBoblar soni :{self.bob}\nMavzular soni :{self.mavzu}"
    
# class darslik(kitob):
#     def __init__(self, nomi, bob, mavzu, bet,munda_reja):
#         super().__init__(bet, bob, mavzu, nomi)

        
#         self.munda_reja = munda_reja


#     def info(self):
#         return f"Kitob nomi :{self.nomi}\nBoblar soni :{self.bob}\nSahifalar soni :{self.bet}\nMavzu :{self.mavzu}\nMunda reja :{self.munda_reja}"
    
# darslik1 = darslik("Hisob kitob",12,24,"48 bet","50 ta")
# print(darslik1.info())

# 13-misol

# class hayvon:
#     def __init__(self, nomi):
#         self.nomi = nomi

#     def ovoz(self):
#         return f"{self.nomi} ovoz chiqaradi"
# class it(hayvon):
#     def ovoz(self):
#         return f"{self.nomi} havlaydi"
# class mushuk(hayvon):
#     def ovoz(self):
#         return f"{self.nomi} miyovlaydi"
# it1 = it("Kuchuk")
# print(it1.ovoz())
# mushuk1 = mushuk("Mushuk")
# print(mushuk1.ovoz())

# 14-misol
# class qurilma:
#     def __init__(self,nomi,fresh_rate,pratsetsor,batareya):
#         self.nomi = nomi
#         self.protsetsor = pratsetsor
#         self.batareya = batareya

#     def info(self):
#         return f"qurilma nomi {self.nomi}\n Protsetsori :{self.protsetsor}\nBatreyasi :{self.batareya}"
# class telefon(qurilma):
#     def __init__(self, nomi, fresh_rate, pratsetsor, batareya,narxi,qamera):
#         super().__init__(nomi, fresh_rate, pratsetsor, batareya)
#         self.narxi = narxi
#         self.qamera = qamera
#     def get_info(self):
#         return f"qurilma nomi {self.nomi}\n Protsetsori :{self.protsetsor}\nBatreyasi :{self.batareya}\nQurilam narxi :{self.narxi}\nQurilma Kamerai :{self.qamera}"
# qurilam1 = qurilma("Xiomi 11t",120,"sanp dragon g1",7000)

        

# 15-misol

# class kompaniya:
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.ishchilar = []
#         self.ishchilar_soni = 0
#     def ishchi_qoshish(self,ishchi):
#         self.ishchilar.append(ishchi)
#         self.ishchilar_soni += 1
#     def kompaniya_info(self):
#         return f"Kompaniya nomi: {self.nomi}\nIshchilar soni: {self.ishchilar_soni}"
# class ishchi(kompaniya):
#     def __init__(self, nomi, ish_joyi):
#         super().__init__(nomi)
#         self.ish_joyi = ish_joyi
#     def get_info(self):
#         return f"Ishchi nomi: {self.nomi}\nIsh joyi: {self.ish_joyi}"
# kompaniya1 = kompaniya("Tech Solutions")
# ishchi1 = ishchi("Elbek", "Dasturchi")
# kompaniya1.ishchi_qoshish(ishchi1)
# print(kompaniya1.kompaniya_info())

# 16-misol

# class ota:
#     def __init__(self,ism,yosh,kasbi):
#         self.ism = ism 
#         self.yosh = yosh
#         self.kasbi = kasbi

#     def get_info(self):
#         return f"Ismi {self.ism}\nYoshi{self.yosh}\nKasbi{self.kasbi}"
    
# class bola(ota):
#     def __init__(self, ism, yosh, kasbi, talaba_yili, oqish_joyi):
#         super().__init__(ism, yosh, kasbi)
#         self.talaba_yili = talaba_yili
#         self.oqish_joyi = oqish_joyi

#     def get_info(self):
#         return f"{super().get_info()}\nTalaba yili: {self.talaba_yili}\nO'qish joyi: {self.oqish_joyi}"
    
# bola1 = bola("Elbek", 20, "Dasturchi", 2, "It park")
# print(bola1.get_info())

# 17-misol

# class transport:
#     def __init__(self, nomi, tezlik):
#         self.nomi = nomi
#         self.tezlik = tezlik
#     def get_info(self):
#         return f"Transport nomi: {self.nomi}\nTezligi: {self.tezlik} km/soat"
# class avtobus(transport):
#     def __init__(self, nomi, tezlik, yolovchi_kap):
#         super().__init__(nomi, tezlik)
#         self.yolovchi_kap = yolovchi_kap
#     def get_info(self):
#         return f"{super().get_info()}\nYo'lovchi sig'imi: {self.yolovchi_kap} kishi"
# class poyezd(transport):
#     def __init__(self, nomi, tezlik, vagon_soni):
#         super().__init__(nomi, tezlik)
#         self.vagon_soni = vagon_soni
#     def get_info(self):
#         return f"{super().get_info()}\nVagon soni: {self.vagon_soni}"
# avtobus1 = avtobus("Mercedes", 120, 50)
# print(avtobus1.get_info())

# 18-misol


# class shaxs:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh

#     def get_info(self):
#         return f"Ismi: {self.ism}\nYoshi: {self.yosh}"
# class talaba(shaxs):
#     def __init__(self, ism, yosh, fakultet):
#         super().__init__(ism, yosh)
#         self.fakultet = fakultet

#     def get_info(self):
#         return f"{super().get_info()}\nFakulteti: {self.fakultet}"
# class oqituvchi(shaxs):
#     def __init__(self, ism, yosh, fan):
#         super().__init__(ism, yosh)
#         self.fan = fan

#     def get_info(self):
#         return f"{super().get_info()}\nFani: {self.fan}"
# talaba1 = talaba("Elbek", 20, "Informatika")
# print(talaba1.get_info())
# oqituvchi1 = oqituvchi("Sarvar", 35, "Matematika")
# print(oqituvchi1.get_info())

# 19-misol

# class maxsulot:
#     def __init__(self, nomi, narxi, turi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.turi = turi

#     def get_info(self):
#         return f"Maxsulot nomi: {self.nomi}\nMaxsulot narxi: {self.narxi}\nMaxsulot turi: {self.turi}"
# class meva(maxsulot):
#     def __init__(self, nomi, narxi, turi, rang):
#         super().__init__(nomi, narxi, turi)
#         self.rang = rang

#     def get_info(self):
#         return f"{super().get_info()}\nMeva rangi: {self.rang}"
# meva1 = meva("Olma", 5000, "Meva", "Qizil")
# print(meva1.get_info())

# 20-misol

# class bino:
#     def __init__(self, nomi, qavat_soni):
#         self.nomi = nomi
#         self.qavat_soni = qavat_soni

#     def get_info(self):
#         return f"Bino nomi: {self.nomi}\nQavat soni: {self.qavat_soni}"
# class uy(bino):
#     def __init__(self, nomi, qavat_soni, xona_soni):
#         super().__init__(nomi, qavat_soni)
#         self.xona_soni = xona_soni

#     def get_info(self):
#         return f"{super().get_info()}\nXona soni: {self.xona_soni}"
# uy1 = uy("Yashnobod", 5, 3)
# print(uy1.get_info())

# 21-misol
# import datetime

# class bank:
#     def __init__(self,bank_nomi):
#         self.bank_nomi = bank_nomi
#         self.pul = 0


#     def pay(self,hisob_raqami):
#         self.hisob_raqami = hisob_raqami
#         self.pul +=1

#         return f"Bank nomi :{self.bank_nomi}\nHisob raqami :{self.hisob_raqami}"
    
# class Uzum_bank(bank):
#     def __init__(self, bank_nomi,foydalanuvchi_soni):
#         super().__init__(bank_nomi)

#         self.foydalanuvch_soni = foydalanuvchi_soni
#     def info(self):
#         return f"Bank nomi :{self.bank_nomi}\nFoydalanuvchilar soni :{self.foydalanuvch_soni}\nHisob raqami :{self.hisob_raqami}"



# bank1 = Uzum_bank("bank",20)
# print(bank1.info())


# 22-misol

# class kitob:
#     def __init__(self,nomi,bet,muqova,muallif,reja):
#         self.nomi = nomi
#         self.bet = bet 
#         self.muqova = muqova
#         self.muallif = muallif
#         self.reja = reja


#     def get_info(self):
#         return f"KItob nomi :{self.nomi}\nMuqovasi :{self.muqova}\nMuallif :{self.muallif}\nBetlar soni :{self.bet}\nMunda reja :{self.reja}"
# class elektronkitob(kitob):
#     def __init__(self, nomi, bet, muqova, muallif, reja,hajmi):
#         super().__init__(nomi, bet, muqova, muallif, reja)
#         self.hajmi = hajmi

#     def info(self):
#         return f""





# 23-misol

# class mashina:
#     def __init__(self,nomi,mator,ot_kuchi):
#         self.nomi = nomi 
#         self.mator = mator
#         self.ot_kichi = ot_kuchi

#     def info(self):
#         return f"Mashia nomi: {self.nomi}\nMashina dvigeteli: {self.mator}\nMashina kuchi: {self.ot_kichi}"
    
# class ElektroAvto(mashina):
#     def __init__(self, nomi, mator, ot_kuchi,zaryadchik,tezlik):
#         super().__init__(nomi, mator, ot_kuchi)

#         self.quvvatlash= zaryadchik
#         self.tezlik = tezlik


#     def get_info(self):
#         return f"Mashia nomi: {self.nomi}\nMashina dvigeteli: {self.mator}\nMashina ot kuchi: {self.ot_kichi}\nMashinani quvvatlash qurilmasi: {self.quvvatlash}W\nMashina tezligi: {self.tezlik}km/s"

# avto = ElektroAvto("BYD",3,150,260,290)
# print(avto.get_info())

# 24-misol
# class litsey:
#     def __init__(self,nomi,xona_soni,kasb):
#         self.nomi = nomi
#         self.xona_soni = xona_soni
#         self.kasb = kasb

#     def info(self):
#         return f"Litsey nomi: {self.nomi}\nLitsey xonalari soni: {self.xona_soni}\nLitseyda asososiy kasb: {self.kasb}"
# class oqtovchi(litsey):
#     def __init__(self, nomi, xona_soni, kasb,diplomi):
#         super().__init__(nomi, xona_soni, kasb)
#         self.diplom = diplomi

#     def get_info(self):
#         return f"Litsey nomi: {self.nomi}\nLitsey xonalari soni: {self.xona_soni}\nLitseyda asososiy kasb: {self.kasb}\nO'qtuvchi diplomi :{self.diplom}"

# litsey1 = oqtovchi("kasb-hunar",50,"usta","ILTS 8.5")
# print(litsey1.get_info())


# 25-misol

# class hayvon:
#     def __init__(self,teri,oyoq):
#         self.teri = teri
#         self.oyoq = oyoq
#     def get_info(self):
#         return f"Hayvon terisi: {self.teri}\nHayvon oyoqlari soni: {self.oyoq}"
# class qush(hayvon):
#     def __init__(self, teri, oyoq, qanot):
#         super().__init__(teri, oyoq)
#         self.qanot = qanot
#     def uchish(self):
#         return f"{self.get_info()}\nQush qanotlari: {self.qanot}\nQush uchishi mumkin"
# qush1 = qush("Tukli", 2, "Katta")
# print(qush1.uchish())
        
# 26-misol

# class maktab:
#     def __init__(self, nomi, manzili):
#         self.nomi = nomi
#         self.manzili = manzili
#         self.oquvchilar = []
#         self.oquvchilar_soni = 0

#     def oquvchi_qoshish(self, oquvchi):
#         self.oquvchilar.append(oquvchi)
#         self.oquvchilar_soni += 1
#         return f"O'quvchi nomi: {oquvchi.nomi}\nO'quvchi yoshi: {oquvchi.yoshi}\nO'quvchi sinfi: {oquvchi.sinfi}"
# class sinf(maktab):
#     def __init__(self, nomi, manzili, sinf_nomi):
#         super().__init__(nomi, manzili)
#         self.sinf_nomi = sinf_nomi

#     def get_info(self):
#         return f"Maktab nomi: {self.nomi}\nMaktab manzili: {self.manzili}\nSinf nomi: {self.sinf_nomi}\nO'quvchilar soni: {self.oquvchilar_soni}"
# oquvchi1 = sinf("20-maktab", "Toshkent", "10-A")
# print(oquvchi1.get_info())

# 27-misol

# class avto:
#     def __init__(self, nomi, narxi, yili, rangi):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.yili = yili
#         self.rangi = rangi

#     def get_info(self):
#         return f"Mashina nomi: {self.nomi}\nMashina narxi: {self.narxi}\nMashina yili: {self.yili}\nMashina rangi: {self.rangi}"
# class BMW(avto):
#     def __init__(self, nomi, narxi, yili, rangi, model):
#         super().__init__(nomi, narxi, yili, rangi)
#         self.model = model

#     def get_info(self):
#         return f"{super().get_info()}\nModel: {self.model}"
# class chevrolet(avto):  
#     def __init__(self, nomi, narxi, yili, rangi, model):
#         super().__init__(nomi, narxi, yili, rangi)
#         self.model = model

#     def get_info(self):
#         return f"{super().get_info()}\nModel: {self.model}"
# chevrolet1 = chevrolet("Chevrolet Malibu", 15000, 2021, "oq", "Malibu")
# print(chevrolet1.get_info())
# bmw1 = BMW("BMW m5", 20000, 2020, "qora", "M5")
# print(bmw1.get_info())

# 28-misol

# class texnika:
#     def __init__(self, nomi, modeli):
#         self.nomi = nomi
#         self.modeli = modeli

#     def get_info(self):
#         return f"Texnika nomi: {self.nomi}\nTexnika modeli: {self.modeli}"
# class printer(texnika):
#     def __init__(self, nomi, modeli, rang):
#         super().__init__(nomi, modeli)
#         self.rang = rang

#     def get_info(self):
#         return f"{super().get_info()}\nPrinter rangi: {self.rang}"
# class skanner(texnika):
#     def __init__(self, nomi, modeli, tezlik):
#         super().__init__(nomi, modeli)
#         self.tezlik = tezlik

#     def get_info(self):
#         return f"{super().get_info()}\nSkanner tezligi: {self.tezlik} sahifa/dakika"
# printer1 = printer("HP", "LaserJet Pro MFP M227fdw", "Qora")
# print(printer1.get_info())
# skanner1 = skanner("Canon", "CanoScan LiDE 400", 8)
# print(skanner1.get_info())

# 29-misol

# class Sportchi:
#     def __init__(self, ism, yosh, sport_turi):
#         self.ism = ism
#         self.yosh = yosh
#         self.sport_turi = sport_turi

#     def get_info(self):
#         return f"Sportchi nomi: {self.ism}\nYoshi: {self.yosh}\nSport turi: {self.sport_turi}"
# class Futbolchi(Sportchi):
#     def __init__(self, ism, yosh, sport_turi, jamoa):
#         super().__init__(ism, yosh, sport_turi)
#         self.jamoa = jamoa

#     def get_info(self):
#         return f"{super().get_info()}\nJamoasi: {self.jamoa}"
# futbolchi1 = Futbolchi("Ronaldo", 36, "Futbol", "Paris Saint-Germain")
# print(futbolchi1.get_info())


# 30-misol

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_info(self):
#         return f"Student name: {self.name}\nStudent age: {self.age}"
# class Talaba(Student):
#     def __init__(self, name, age, fakultet):
#         super().__init__(name, age)
#         self.fakultet = fakultet

#     def get_info(self):
#         return f"{super().get_info()}\nFakultet: {self.fakultet}"
# talaba1 = Talaba("Elbek", 20, "Informatika")
# print(talaba1.get_info())

# 31-misol

# class mexmonxona:
#     def __init__(self,nomi,xonlar,yulduz):
#         self.nomi = nomi
#         self.xonalar = xonlar
#         self.yulduz = yulduz

#     def info(self):
#         return f"Mexmonxona nomi: {self.nomi}\nXonalari soni: {self.xonalar}\nYulduzlar soni: {self.yulduz}"
# class kafe(mexmonxona):
#     def __init__(self, nomi, xonlar, yulduz,stollar_soni):
#         super().__init__(nomi, xonlar, yulduz)
#         self.stollar_soni = stollar_soni

#     def get_info(self):
#         return f"Kafe nomi: {self.nomi}\nXonalar soni: {self.xonalar}\nYulduzlar soni: {self.yulduz}\nStollar soni: {self.stollar_soni}"
# kafe1 = kafe("Sim-sim","4 ta ","3.5","8 ta")
# print(kafe1.get_info())

# 32-misol

# class Airaport:
#     def __init__(self,nomi,maydon,yolak_soni,haftada_ishlash):
#         self.nomi = nomi
#         self.maydon = maydon
#         self.yolak_soni = yolak_soni
#         self.ishlash_kunlari = haftada_ishlash
#         self.ishchi = []
#         self.ishchi_soni = 0

#     def asistant(self,staf_name):
#         self.ishchi.append(staf_name)

#     def info(self):
#         return f"Airaport nomi: {self.nomi}\nMaydon: {self.maydon} kvadrat metr\nYolak soni: {self.yolak_soni}\nHaftada ishlash kunlari: {self.ishlash_kunlari}\nIshchilar soni: {self.ishchi_soni}"
# class Staf(Airaport):
#     def __init__(self, nomi, maydon, yolak_soni, haftada_ishlash, ishchi_nomi):
#         super().__init__(nomi, maydon, yolak_soni, haftada_ishlash)
#         self.ishchi_nomi = ishchi_nomi
#         self.ishchi_soni += 1

#     def get_info(self):
#         return f"Airaport nomi: {self.nomi}\nMaydon: {self.maydon} kvadrat metr\nYolak soni: {self.yolak_soni}\nHaftada ishlash kunlari: {self.ishlash_kunlari}\nIshchi nomi: {self.ishchi_nomi}\nIshchilar soni: {self.ishchi_soni}"
# staf1 = Staf("Toshkent Airaport", 50000, 3, "7 kun", "Ali")
# print(staf1.get_info())

# 33-misol

# class mashina:
#     def __init__(self, nomi, narxi):
#         self.nomi = nomi
#         self.narxi = narxi

#     def get_info(self):
#         return f"Mashina nomi: {self.nomi}\nMashina narxi: {self.narxi}"
# class avto(mashina):
#     def __init__(self, nomi, narxi, modeli):
#         super().__init__(nomi, narxi)
#         self.modeli = modeli

#     def get_info(self):
#         return f"{super().get_info()}\nModel: {self.modeli}"
# class sportcar(mashina):
#     def __init__(self, nomi, narxi, tezlik):
#         super().__init__(nomi, narxi)
#         self.tezlik = tezlik

#     def get_info(self):
#         return f"{super().get_info()}\nTezlik: {self.tezlik} km/s"
# class sportavto(avto, sportcar):
#     def __init__(self, nomi, narxi, modeli, tezlik):
#         avto.__init__(self, nomi, narxi, modeli)
#         sportcar.__init__(self, nomi, narxi, tezlik)

#     def get_info(self):
#         return f"{avto.get_info(self)}\nTezlik: {self.tezlik} km/s"
# sportavto1 = sportavto("Lamborgini", 300000, "Aventador", 350)
# print(sportavto1.get_info())

# 34-misol

# class qush:
#     def __init__(self,nomi,qanot,rang):
#         self.nomi = nomi 
#         self.qanot = qanot
#         self.rang = rang

#     def info(self):
#         return f"Qush nomi: {self.nomi}\nQanot uzunligi: {self.qanot}\nRang: {self.rang}"
# class burgut(qush):
#     def __init__(self, nomi, qanot, rang,tezligi):
#         super().__init__(nomi, qanot, rang)
#         self.tezlik = tezligi

#     def get_info(self):
#         return f"Qush nomi: {self.nomi}\nQanot uzunligi: {self.qanot}\nRang: {self.rang}\nTezligi: {self.tezlik}"

# qush1 = burgut("burgut","2.8 m","oq","87km/h")
# print(qush1.get_info())


# 35-misol

# class hayvon:
#     def __init__(self,nomi,tail,oziga_xos_hususiyat):
#         self.nomi = nomi
#         self.tail = tail
#         self.oziga_xos_hususiyat = oziga_xos_hususiyat
 

#     def info(self):
#         return f"Nomi: {self.nomi}\nDumi: {self.tail}\nO'ziaga hos hususiyati: {self.oziga_xos_hususiyat}"
    

# class mushuk(hayvon):
#     def __init__(self, nomi, tail, oziga_xos_hususiyat,rangi):
#         super().__init__(nomi, tail, oziga_xos_hususiyat)
#         self.rangi = rangi

#     def info_cat(self):
#         return f"Nomi: {self.nomi}\nDumi: {self.tail}\nO'ziaga hos hususiyati: {self.oziga_xos_hususiyat}\nRngi: {self.rangi}"

        
        
# class baliq(hayvon):
#     def __init__(self, nomi, tail, oziga_xos_hususiyat,terisi):
#         super().__init__(nomi, tail, oziga_xos_hususiyat)
    
#         self.terisi = terisi

#     def info_fish(self):
#         return f"Nomi: {self.nomi}\nDumi: {self.tail}\nO'ziaga hos hususiyati: {self.oziga_xos_hususiyat}\nterisi: {self.terisi} bilan qoplangan"

# cat = mushuk("meav","uzun","tez","qora,negr")
# fish  = baliq("sazan","suzgich","suvda nafas oladi","tilla")
# print(cat.info_cat())
# print(fish.info_fish())


# 36-misol

# class kompaniya:
#     def __init__(self,nomi,ishchilar):
#         self.nomi = nomi
#         self.ishchilar = ishchilar
    
#     def 

    
     


        










