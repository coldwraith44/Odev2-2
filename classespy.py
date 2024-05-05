class Gemiler:
    def init(self,g_s_no,g_ad,agirlik,y_yili):
        self.g_s_no=g_s_no
        self.g_ad=g_ad
        self.agirlik=agirlik
        self.y_yili=y_yili

class  YolcuGemisi(Gemiler) :
    def init(self, g_s_no, g_ad, agirlik, y_yili,kapasite):
        super().init(g_s_no, g_ad, agirlik, y_yili)
        self.kapasite=kapasite

class  PetrolTankeri(Gemiler) :
    def init(self, g_s_no, g_ad, agirlik, y_yili,petrol_tasima_kapasitesi):
        super().init(g_s_no, g_ad, agirlik, y_yili)
        self.petrol_tasima_kapasitesi=petrol_tasima_kapasitesi

class  KonteynerGemisi(Gemiler) :
    def init(self, g_s_no, g_ad, agirlik, y_yili,konteyner_sayisi,maks_agirlik):
        super().init(g_s_no, g_ad, agirlik, y_yili)
        self.konteyner_sayisi=konteyner_sayisi
        self.maks_agirlik=maks_agirlik

class Limanlar:
    def init(self, liman_adi, liman_ulkesi,limandaki_gemiler, liman_nufusu, pasaport_kontrol_durumu, demirleme_ucreti):
        self.liman_adi=liman_adi
        self.liman_ulkesi=liman_ulkesi
        self.limandaki_gemiler=limandaki_gemiler
        self.liman_nufusu=liman_nufusu
        self.pasaport_kontrol_durumu=pasaport_kontrol_durumu
        self.demirleme_ucreti=demirleme_ucreti

class Seferler:
    def init(self, sefer_no,gemi_no, kaptanlar, murettebatlar, yola_cikis_tarihi, donus_tarihi, yola_cikis_limani,ugranilan_limanlar):
        self.sefer_no=sefer_no
        self.gemi_no=gemi_no
        self.kaptanlar=kaptanlar
        self.murettebatlar=murettebatlar
        self.yola_cikis_tarihi=yola_cikis_tarihi
        self.donus_tarihi=donus_tarihi
        self.yola_cikis_limani=yola_cikis_limani
        self.ugranilan_limanlar=ugranilan_limanlar

class Kaptanlar:
    def init(self, kaptan_no, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi,lisansi):
        self.kaptan_no=kaptan_no
        self.ad=ad
        self.soyad=soyad
        self.adres=adres
        self.vatandaslik=vatandaslik
        self.dogum_tarihi=dogum_tarihi
        self.ise_giris_tarihi=ise_giris_tarihi
        self.lisansi=lisansi

class Murettebatlar:
    def init(self, murettebat_no, ad, soyad, adres, vatandaslik, dogum_tarihi, ise_giris_tarihi, gorevi):
        self.murettebat_no=murettebat_no
        self.ad=ad
        self.soyad=soyad
        self.adres=adres
        self.vatandaslik=vatandaslik
        self.dogum_tarihi=dogum_tarihi
        self.ise_giris_tarihi=ise_giris_tarihi
        self.gorevi=gorevi
