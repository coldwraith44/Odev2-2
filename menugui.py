from classespy import Gemiler,YolcuGemisi,PetrolTankeri,KonteynerGemisi, Seferler, Limanlar, Kaptanlar, Murettebatlar
import pyodbc
from tkinter import messagebox
import os
import tkinter.messagebox as mb

import tkinter as tk
from tkinter import messagebox


def main():



    db= pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-11DRFE4\SQLEXPRESS;'
                      'Database=liman_veri_tabani;'
                      'Trusted_Connection=yes;')
    cursor=db.cursor()



    def cikis():
        result = messagebox.askyesno("Çıkış", "Çıkış yapmak istediğinizden emin misiniz?")
        if result:
            root.destroy()
    def info_goster():
        mb.showinfo("A1")
    def entry_alma_modülü(x):

        def bitiris():
                giris_penceresi.destroy()
                geri()


        if x=="yolcu_gemisi_ekle":


            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title(" Yolcu Gemisi Ekle")

            entry1_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Yolcu Gemisinin Seri Numarası:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Yolcu Gemisinin Adı:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)

            entry3_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Yolcu Gemisinin Ağırlığı:")
            entry3_label.pack(pady=5)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=25)

            entry4_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Yolcu Gemisinin Yapım Yılı:")
            entry4_label.pack(pady=5)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=25)

            entry5_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Yolcu Gemisinin Kapasitesi:")
            entry5_label.pack(pady=5)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=25)

            def al():
                gemi_no=entry1.get()
                gemi_ad=entry2.get()
                gemi_agirlik=entry3.get()
                gemi_yy=entry4.get()
                gemi_kapasite=entry5.get()

                gemi=YolcuGemisi(gemi_no,gemi_ad,gemi_agirlik,gemi_yy,gemi_kapasite)


                sql_sorgusu = "SELECT * FROM gemi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (gemi.g_s_no,))


                i = cursor.fetchone()

                try:
                    if gemi.g_s_no is None:
                        mb.showerror("Hata", "Null Değer Giremezsiniz!")

                    else:

                        cursor.execute(f"INSERT INTO gemi_tablo (seri_no, adi, agirlik,yapim_yili) VALUES (?, ?, ?, ?)",
                        (gemi.g_s_no, gemi.g_ad, gemi.agirlik, gemi.y_yili))

                        cursor.execute(f"INSERT INTO yolcu_gemisi_tablo (seri_no, yolcu_kapasitesi) VALUES (?, ?)",
                                        (gemi.g_s_no, gemi.kapasite))
                        mb.showinfo("Başarılı","Yolcu Gemisi Eklendi")


                except  pyodbc.IntegrityError:
                        mb.showerror("Hata", "Bu Gemi Zaten Var!")
                except pyodbc.DataError:
                        mb.showerror("Hata", "Geçersiz Değer Girdiniz!")
                finally:
                    db.commit()

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Çıkış", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()


        elif x=="konteyner_gemisi_ekle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title(" Konteyner Gemisi Ekle")

            entry1_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Konteyner Gemisinin Seri Numarası:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Konteyner Gemisinin Adı:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)

            entry3_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Konteyner Gemisinin Ağırlığı:")
            entry3_label.pack(pady=5)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=25)

            entry4_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Konteyner Gemisinin  Yapım Yılı:")
            entry4_label.pack(pady=5)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=25)

            entry5_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Konteyner Gemisinin Konteyner Sayısı Kapasitesi:")
            entry5_label.pack(pady=5)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=25)

            entry6_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Konteyner Gemisinin Maksimum Ağırlık Kapasitesi:")
            entry6_label.pack(pady=5)
            entry6 = tk.Entry(giris_penceresi,width=25)
            entry6.pack(pady=25)
            def al():
                gemi_no=entry1.get()
                gemi_ad=entry2.get()
                gemi_agirlik=entry3.get()
                gemi_yy=entry4.get()
                gemi_konteyner_sayisi=entry5.get()
                gemi_konteyner_agirlik=entry6.get()

                gemi=KonteynerGemisi(gemi_no,gemi_ad,gemi_agirlik,gemi_yy,gemi_konteyner_sayisi,gemi_konteyner_agirlik)


                sql_sorgusu = "SELECT * FROM gemi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (gemi.g_s_no,))


                i = cursor.fetchone()

                try:
                    if gemi.g_s_no is None:
                        mb.showerror("Hata", "Null Değer Giremezsiniz!")

                    else:

                        cursor.execute(f"INSERT INTO gemi_tablo (seri_no, adi, agirlik,yapim_yili) VALUES (?, ?, ?, ?)",
                        (gemi.g_s_no, gemi.g_ad, gemi.agirlik, gemi.y_yili))

                        cursor.execute(f"INSERT INTO konteyner_gemi_tablo (seri_no, konteyner_sayisi, maks_agirlik) VALUES (?, ?,?)",
                                        (gemi.g_s_no, gemi.konteyner_sayisi,gemi.maks_agirlik))
                        mb.showinfo("Başarılı","Yolcu Gemisi Eklendi")


                except  pyodbc.IntegrityError:
                        mb.showerror("Hata", "Bu Gemi Zaten Var!")
                except pyodbc.DataError:
                        mb.showerror("Hata", "Geçersiz Değer Girdiniz!")
                finally:
                    db.commit()

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)

            button = tk.Button(giris_penceresi, text="Çıkış", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()


        elif x== "petrol_tankeri_ekle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Petrol Tankeri Ekle")

            entry1_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Petrol Tankerinin Seri Numarası:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Petrol Tankerinin Adı:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)

            entry3_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Petrol Tankerinin Ağırlığı:")
            entry3_label.pack(pady=5)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=25)

            entry4_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Petrol Tankerinin Yapım Yılı:")
            entry4_label.pack(pady=5)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=25)

            entry5_label = tk.Label(giris_penceresi, text="Eklemek İstediğiniz Petrol Tankerinin Petrol Kapasitesi:")
            entry5_label.pack(pady=5)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=25)

            def al():
                gemi_no=entry1.get()
                gemi_ad=entry2.get()
                gemi_agirlik=entry3.get()
                gemi_yy=entry4.get()
                gemi_petrol_tasima_kapasitesi=entry5.get()

                gemi=PetrolTankeri(gemi_no,gemi_ad,gemi_agirlik,gemi_yy,gemi_petrol_tasima_kapasitesi)


                sql_sorgusu = "SELECT * FROM gemi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (gemi.g_s_no,))


                i = cursor.fetchone()

                try:
                    if gemi.g_s_no is None:
                        mb.showerror("Hata", "Null Değer Giremezsiniz!")

                    else:

                        cursor.execute(f"INSERT INTO gemi_tablo (seri_no, adi, agirlik,yapim_yili) VALUES (?, ?, ?, ?)",
                        (gemi.g_s_no, gemi.g_ad, gemi.agirlik, gemi.y_yili))

                        cursor.execute(f"INSERT INTO petrol_tankeri_tablo (seri_no, petrol_kapasitesi) VALUES (?, ?)",
                                        (gemi.g_s_no, gemi.petrol_tasima_kapasitesi))
                        mb.showinfo("Başarılı","Petrol Tankeri Eklendi")


                except  pyodbc.IntegrityError:
                        mb.showerror("Hata", "Bu Gemi Zaten Var!")
                except pyodbc.DataError:
                        mb.showerror("Hata", "Geçersiz Değer Girdiniz!")
                finally:
                    db.commit()

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Çıkış", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()


        elif x=="yolcu_gemisi_duzenle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title(" Yolcu Gemisi Duzenle")

            entry1_label = tk.Label(giris_penceresi, text="Duzenlemek İstediğiniz Yolcu Gemisinin Seri Numarası:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Duzenlemekİstediğiniz Yolcu Gemisinin Adı:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)

            entry3_label = tk.Label(giris_penceresi, text="Duzenlemek İstediğiniz Yolcu Gemisinin Ağırlığı:")
            entry3_label.pack(pady=5)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=25)

            entry4_label = tk.Label(giris_penceresi, text="Duzenlemek İstediğiniz Yolcu Gemisinin Yapım Yılı:")
            entry4_label.pack(pady=5)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=25)

            entry5_label = tk.Label(giris_penceresi, text="Duzenlemek İstediğiniz Yolcu Gemisinin Kapasitesi:")
            entry5_label.pack(pady=5)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=25)

            def al():
                gemi_no = entry1.get()
                gemi_ad = entry2.get()
                gemi_agirlik = entry3.get()
                gemi_yy = entry4.get()
                gemi_kapasite = entry5.get()

                gemi = YolcuGemisi(gemi_no, gemi_ad, gemi_agirlik, gemi_yy, gemi_kapasite)

                try:
                    if gemi_no is None:
                        mb.showerror("Hata", "Null Değer Giremezsiniz!")
                    else:

                        cursor.execute("UPDATE gemi_tablo SET gemi_ad = ?, agirlik = ?, yapim_yili = ? WHERE seri_no = ?",
                                    (gemi.g_ad, gemi.agirlik, gemi.y_yili, gemi.g_s_no))

                        cursor.execute("INSERT INTO yolcu_gemisi_tablo (seri_no, yolcu_kapasitesi) VALUES (?, ?)",
                                    (gemi.g_s_no, gemi.kapasite))
                        mb.showinfo("Başarılı", "Yolcu Gemisi Eklendi")
                except pyodbc.IntegrityError:
                    mb.showerror("Hata", "Bu Gemi Zaten Var!")
                except pyodbc.DataError:
                    mb.showerror("Hata", "Geçersiz Değer Girdiniz!")
                finally:
                    db.commit()
            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Çıkış", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()


        elif x=="petrol_tankeri_duzenle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Petrol Tankeri Düzenle")

            entry1_label = tk.Label(giris_penceresi, text="Düzenlemek İstediğiniz Petrol Tankerinin Seri Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)


            button = tk.Button(giris_penceresi, text="Düzenlemek İstediğiniz Petrol Tankerinin Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()

        elif x=="yolcu_gemisi_sil":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Yolcu Gemisi Sil")


            entry1_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Yolcu Gemisinin Seri Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)
            def al():
                gemi_no=entry1.get()
                aranan_deger = gemi_no


                sql_sorgusu = "SELECT * FROM yolcu_gemisi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    silinecek_deger = aranan_deger



                    sql_sorgusu = "DELETE FROM gemi_tablo WHERE seri_no = ?"


                    cursor.execute(sql_sorgusu, (silinecek_deger,))

                    sql_sorgusu = "DELETE FROM yolcu_gemisi_tablo WHERE seri_no = ?"


                    cursor.execute(sql_sorgusu, (silinecek_deger,))



                    mb.showinfo("Başarılı","Gemi Silindi")
                else:
                    mb.showerror("Hata", "Böyle Bir Gemi Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Sİlmek İstediğiniz Yolcu Gemisinin Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="konteyner_gemisi_sil":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Konteyner Gemisi Sil")

            entry1_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Konteyner Gemisinin Seri Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)
            def al():
                gemi_no=entry1.get()
                aranan_deger = gemi_no


                sql_sorgusu = "SELECT * FROM konteyner_gemi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    silinecek_deger = aranan_deger




                    sql_sorgusu = "DELETE FROM gemi_tablo WHERE seri_no = ?"


                    cursor.execute(sql_sorgusu, (silinecek_deger,))

                    sql_sorgusu = "DELETE FROM konteyner_gemi_tablo WHERE seri_no = ?"


                    cursor.execute(sql_sorgusu, (silinecek_deger,))
                    mb.showinfo("Başarılı","Gemi Silindi")
                else:
                    mb.showerror("Hata", "Böyle Bir Gemi Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Silmek İstediğiniz Konteyner Gemisinin Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="petrol_tankeri_sil":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Petrol Tankeri Sil")

            entry1_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Petrol Tankerinin Seri Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)
            def al():
                gemi_no=entry1.get()
                aranan_deger = gemi_no


                sql_sorgusu = "SELECT * FROM yolcu_gemisi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    silinecek_deger = aranan_deger


                    sql_sorgusu = "DELETE FROM yolcu_gemisi_tablo WHERE seri_no = ?"


                    cursor.execute(sql_sorgusu, (silinecek_deger,))

                    sql_sorgusu = "DELETE FROM gemi_tablo WHERE seri_no = ?"


                    cursor.execute(sql_sorgusu, (silinecek_deger,))

                    mb.showinfo("Başarılı","Gemi Silindi")
                else:
                    mb.showerror("Hata", "Böyle Bir Gemi Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Silmek İstediğiniz Petrol Tankerinin Veritabanında Olup Olmadığını Kontrol Et")
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="yolcu_gemisi_goruntule":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Yolcu Gemisi Görüntüle")

            entry1_label = tk.Label(giris_penceresi, text="Aramak İstediğiniz Yolcu Gemisinin Seri Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            def al():
                gemi_no=entry1.get()
                aranan_deger = gemi_no


                sql_sorgusu = "SELECT * FROM yolcu_gemisi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    mb.showinfo(gemi_no,i)
                else:
                    mb.showerror("Hata", "Böyle Bir Gemi Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Çıkış",command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="konteyner_gemisi_goruntule":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Konteyner Gemisi Görüntüle")

            entry1_label = tk.Label(giris_penceresi, text="Aramak İstediğiniz Konteyner Gemisinin Seri Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)


            def al():
                gemi_no=entry1.get()
                aranan_deger = gemi_no


                sql_sorgusu = "SELECT * FROM konteyner_gemi_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    mb.showinfo(gemi_no,i)
                else:
                    mb.showerror("Hata", "Böyle Bir Gemi Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Çıkış",command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="petrol_tankeri_goruntule":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Petrol Tankeri Görüntüle")

            entry1_label = tk.Label(giris_penceresi, text="Aramak İstediğiniz Petrol Tankerinin Seri Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            def al():
                gemi_no=entry1.get()
                aranan_deger = gemi_no


                sql_sorgusu = "SELECT * FROM petrol_tankeri_tablo WHERE seri_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    mb.showinfo(gemi_no,i)
                else:
                    mb.showerror("Hata", "Böyle Bir Gemi Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Çıkış",command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="sefer_ekle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Sefer Ekle")

            entry1_label = tk.Label(giris_penceresi, text="Sefer Numarası:")
            entry1_label.pack(pady=3)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=13)

            entry2_label = tk.Label(giris_penceresi, text="Gemi Numarası:")
            entry2_label.pack(pady=3)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=13)

            entry3_label = tk.Label(giris_penceresi, text="Kaptanların Numaraları(Her kaptan numarası arasında virgül kullanınız!):")
            entry3_label.pack(pady=3)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=13)

            entry4_label = tk.Label(giris_penceresi, text="Mürettebatın Numaraları(Her mürettebat numarası arasında virgül kullanınız!):")
            entry4_label.pack(pady=3)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=13)

            entry5_label = tk.Label(giris_penceresi, text="Yola Çıkış Tarihi(Gün/Ay/Yıl şeklinde giriniz):")
            entry5_label.pack(pady=3)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=13)

            entry6_label = tk.Label(giris_penceresi, text="Dönüş Tarihi:(Gün/Ay/Yıl şeklinde giriniz):")
            entry6_label.pack(pady=3)
            entry6 = tk.Entry(giris_penceresi,width=25)
            entry6.pack(pady=13)

            entry7_label = tk.Label(giris_penceresi, text="Yola Çıkış Limanı:")
            entry7_label.pack(pady=3)
            entry7 = tk.Entry(giris_penceresi,width=25)
            entry7.pack(pady=13)

            entry8_label = tk.Label(giris_penceresi, text="Uğranacak Veya Uğranma İhtimali Olan Limanlar(Her liman arasında virgül kullanınız!)")
            entry8_label.pack(pady=3)
            entry8 = tk.Entry(giris_penceresi,width=25)
            entry8.pack(pady=13)

            button = tk.Button(giris_penceresi, text="Sefer Ekle", command=bitiris)
            button.pack(pady=25)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()


        elif x=="sefer_duzenle":
            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Sefer Düzenle")

            entry1_label = tk.Label(giris_penceresi, text="Düzenlemek İstediğiniz Seferin Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)


            button = tk.Button(giris_penceresi, text="Düzenlemek İstediğiniz Seferin Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="sefer_sil":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Sefer Sil")

            entry1_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Seferin Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            button = tk.Button(giris_penceresi, text="Çıkış", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()

        elif x=="sefer_goruntule":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Sefer Görüntüle")

            entry1_label = tk.Label(giris_penceresi, text="Aramak İstediğiniz Seferin Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)


            def al():
                sefer_no=entry1.get()
                aranan_deger = sefer_no


                sql_sorgusu = "SELECT * FROM seferler_tablo WHERE sefer_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    mb.showinfo(sefer_no,i)
                else:
                    mb.showerror("Hata", "Böyle Bir Sefer Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)

            button = tk.Button(giris_penceresi, text="Çıkış", command=bitiris)

            button.pack(pady=35)
            giris_penceresi.geometry("700x700")

            giris_penceresi.mainloop()




        elif x=="liman_ekle":


            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Liman Ekle")

            entry1_label = tk.Label(giris_penceresi, text="Liman Adı:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Limanın Bulunduğu Ülke:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)

            entry3_label = tk.Label(giris_penceresi, text="Limanda Bulunan Gemiler(Gemilerin arasına virgül koyunuz):")
            entry3_label.pack(pady=5)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=25)

            entry4_label = tk.Label(giris_penceresi, text="Limanın Nüfusu:")
            entry4_label.pack(pady=5)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=25)

            entry5_label = tk.Label(giris_penceresi, text="Liman Pasaport İstiyor mu('Evet' veya 'Hayır' şeklinde giriniz):")
            entry5_label.pack(pady=5)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=25)

            entry6_label = tk.Label(giris_penceresi, text="Demirleme Ücreti:")
            entry6_label.pack(pady=5)
            entry6 = tk.Entry(giris_penceresi,width=25)
            entry6.pack(pady=25)


            button = tk.Button(giris_penceresi, text="Liman Ekle", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()



        elif x=="liman_duzenle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Liman Düzenle")

            entry1_label = tk.Label(giris_penceresi, text="Düzenlemek İstediğiniz Limanın Adını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Düzenlemek İstediğiniz Limanın Ülkesini Giriniz:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)


            button = tk.Button(giris_penceresi, text="Düzenlemek İstediğiniz Limanın Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="liman_sil":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Liman Sil")

            entry1_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Limanın Adını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Limanın Ülkesini Giriniz:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)


            button = tk.Button(giris_penceresi, text="Silmek İstediğiniz Limanın Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="liman_goruntule":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Liman Görüntüle")

            entry1_label = tk.Label(giris_penceresi, text="Görüntülemek İstediğiniz Limanın Adını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            entry2_label = tk.Label(giris_penceresi, text="Görüntülemek İstediğiniz Limanın Ülkesini Giriniz:")
            entry2_label.pack(pady=5)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=25)

            def al():
                x=entry1.get()
                x1=entry2.get()
                aranan_deger = x
                aranan_deger2=x1

                sql_sorgusu = "SELECT * FROM limanlar_tablo WHERE liman_adi = ? AND ulke = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,aranan_deger2))


                i = cursor.fetchone()

                if i:
                    mb.showinfo(x+" "+x1,i)
                else:
                    mb.showerror("Hata", "Böyle Bir Liman Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)

            button = tk.Button(giris_penceresi, text="Çıkış", command=bitiris)


            button = tk.Button(giris_penceresi, text="Liman Görüntüle", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()



        elif x=="kaptan_ekle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Kaptan Ekle")

            entry1_label = tk.Label(giris_penceresi, text="Kaptan Numarası:")
            entry1_label.pack(pady=3)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=13)

            entry2_label = tk.Label(giris_penceresi, text="Kaptanın Adı:")
            entry2_label.pack(pady=3)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=13)

            entry3_label = tk.Label(giris_penceresi, text="Kaptanın Soyadı:")
            entry3_label.pack(pady=3)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=13)

            entry4_label = tk.Label(giris_penceresi, text="Kaptanın Adresi:")
            entry4_label.pack(pady=3)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=13)

            entry5_label = tk.Label(giris_penceresi, text="Kaptanın Vatandaşlığı:")
            entry5_label.pack(pady=3)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=13)

            entry6_label = tk.Label(giris_penceresi, text="Kaptanın Doğum Tarihi:(Gün/Ay/Yıl şeklinde giriniz):")
            entry6_label.pack(pady=3)
            entry6 = tk.Entry(giris_penceresi,width=25)
            entry6.pack(pady=13)

            entry7_label = tk.Label(giris_penceresi, text="Kaptanın İşe Giriş Tarihi:(Gün/Ay/Yıl şeklinde giriniz)::")
            entry7_label.pack(pady=3)
            entry7 = tk.Entry(giris_penceresi,width=25)
            entry7.pack(pady=13)

            entry8_label = tk.Label(giris_penceresi, text="Kaptanın Lisansı('Lisans Numarası','Tarih' şeklinde giriniz tarihi girerken Gün/Ay/Yıl şeklinde giriniz")
            entry8_label.pack(pady=3)
            entry8 = tk.Entry(giris_penceresi,width=25)
            entry8.pack(pady=13)

            button = tk.Button(giris_penceresi, text="Kaptan Ekle", command=bitiris)
            button.pack(pady=25)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()


        elif x=="kaptan_duzenle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Kaptan Düzenle")

            entry1_label = tk.Label(giris_penceresi, text="Düzenlemek İstediğiniz Kaptanın Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)


            button = tk.Button(giris_penceresi, text="Düzenlemek İstediğiniz Kaptanın Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="kaptan_sil":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Kaptan Sil")

            entry1_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Kaptanın Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            button = tk.Button(giris_penceresi, text="Silmek İstediğiniz Kaptanın Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()

        elif x=="kaptan_goruntule":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Kaptan Görüntüle")

            entry1_label = tk.Label(giris_penceresi, text="Aramak İstediğiniz Kaptanın Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            def al():
                kaptan_no=entry1.get()
                aranan_deger = kaptan_no


                sql_sorgusu = "SELECT * FROM kaptanlar_tablo WHERE kaptan_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    mb.showinfo(kaptan_no,i)
                else:
                    mb.showerror("Hata", "Böyle Bir Kaptan Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)

            button = tk.Button(giris_penceresi, text="Kaptan Görüntüle")
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="murettebat_ekle":


            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Mürettebat Ekle")

            entry1_label = tk.Label(giris_penceresi, text="Mürettebatın Numarası:")
            entry1_label.pack(pady=3)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=13)

            entry2_label = tk.Label(giris_penceresi, text="Mürettebatın Adı:")
            entry2_label.pack(pady=3)
            entry2 = tk.Entry(giris_penceresi,width=25)
            entry2.pack(pady=13)

            entry3_label = tk.Label(giris_penceresi, text="Mürettebatın Soyadı:")
            entry3_label.pack(pady=3)
            entry3 = tk.Entry(giris_penceresi,width=25)
            entry3.pack(pady=13)

            entry4_label = tk.Label(giris_penceresi, text="Mürettebatın Adresi:")
            entry4_label.pack(pady=3)
            entry4 = tk.Entry(giris_penceresi,width=25)
            entry4.pack(pady=13)

            entry5_label = tk.Label(giris_penceresi, text="Mürettebatın Vatandaşlığı")
            entry5_label.pack(pady=3)
            entry5 = tk.Entry(giris_penceresi,width=25)
            entry5.pack(pady=13)

            entry6_label = tk.Label(giris_penceresi, text="Mürettebatın Doğum Tarihi:(Gün/Ay/Yıl şeklinde giriniz):")
            entry6_label.pack(pady=3)
            entry6 = tk.Entry(giris_penceresi,width=25)
            entry6.pack(pady=13)

            entry7_label = tk.Label(giris_penceresi, text="Mürettebatın İşe Giriş Tarihi:(Gün/Ay/Yıl şeklinde giriniz):")
            entry7_label.pack(pady=3)
            entry7 = tk.Entry(giris_penceresi,width=25)
            entry7.pack(pady=13)

            entry8_label = tk.Label(giris_penceresi, text="Mürettebatın Görevi")
            entry8_label.pack(pady=3)
            entry8 = tk.Entry(giris_penceresi,width=25)
            entry8.pack(pady=13)

            button = tk.Button(giris_penceresi, text="Mürettebat Ekle", command=bitiris)
            button.pack(pady=25)
            giris_penceresi.geometry("1250x900")
            giris_penceresi.mainloop()


        elif x=="murettebat_duzenle":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Mürettebat Düzenle")

            entry1_label = tk.Label(giris_penceresi, text="Düzenlemek İstediğiniz Mürettebatın Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)


            button = tk.Button(giris_penceresi, text="Düzenlemek İstediğiniz Mürettebatın Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()


        elif x=="murettebat_sil":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Mürettebat Sil")

            entry1_label = tk.Label(giris_penceresi, text="Silmek İstediğiniz Mürettebatın Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            button = tk.Button(giris_penceresi, text="Silmek İstediğiniz Mürettebatın Veritabanında Olup Olmadığını Kontrol Et", command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()

        elif x=="murettebat_goruntule":

            giris_penceresi = tk.Toplevel(root)
            giris_penceresi.title("Mürettebat Görüntüle")

            entry1_label = tk.Label(giris_penceresi, text="Aramak İstediğiniz Mürettebatın Numarasını Giriniz:")
            entry1_label.pack(pady=5)
            entry1 = tk.Entry(giris_penceresi,width=25)
            entry1.pack(pady=25)

            def al():
                gemi_no=entry1.get()
                aranan_deger = gemi_no


                sql_sorgusu = "SELECT * FROM murettebat_tablo WHERE murettebat_no = ?"


                cursor.execute(sql_sorgusu, (aranan_deger,))


                i = cursor.fetchone()

                if i:
                    mb.showinfo(gemi_no,i)
                else:
                    mb.showerror("Hata", "Böyle Bir Mürettebat Bulunamadı!")

            buttonx=tk.Button(giris_penceresi, text="Kaydet", command=al)
            buttonx.pack(pady=25)
            button = tk.Button(giris_penceresi, text="Mürettebat Görüntüle",command=bitiris)
            button.pack(pady=50)
            giris_penceresi.geometry("700x700")
            giris_penceresi.mainloop()

        else:

            print()

    def geri(): #Geri dönme mekanizması eklendi

        kaldir_mevcut_butonlar()
        kaldir_mevcut_butonlar_2()


        ekle_button.pack(pady=(50, 25))
        duzenle_button.pack(pady=25)
        sil_button.pack(pady=25)
        goruntule_button.pack(pady=25)
        cikis_button.pack(pady=25)
        geri_button.place_forget()

    def kaldir_mevcut_butonlar():
        ekle_button.pack_forget()
        duzenle_button.pack_forget()
        sil_button.pack_forget()
        goruntule_button.pack_forget()
        cikis_button.pack_forget()

        gemiler_ekle_button.pack_forget()
        gemiler_duzenle_button.pack_forget()
        gemiler_sil_button.pack_forget()
        gemiler_goruntule_button.pack_forget()

        sefer_ekle_button.pack_forget()
        sefer_duzenle_button.pack_forget()
        sefer_sil_button.pack_forget()
        sefer_goruntule_button.pack_forget()

        liman_ekle_button.pack_forget()
        liman_duzenle_button.pack_forget()
        liman_sil_button.pack_forget()
        liman_goruntule_button.pack_forget()

        kaptan_ekle_button.pack_forget()
        kaptan_duzenle_button.pack_forget()
        kaptan_sil_button.pack_forget()
        kaptan_goruntule_button.pack_forget()

        murettebat_ekle_button.pack_forget()
        murettebat_duzenle_button.pack_forget()
        murettebat_sil_button.pack_forget()
        murettebat_goruntule_button.pack_forget()

        geri_button.place_forget()

    def kaldir_mevcut_butonlar_2():
        yolcu_gemisi_ekle_button.pack_forget()
        yolcu_gemisi_duzenle_button.pack_forget()
        yolcu_gemisi_sil_button.pack_forget()
        yolcu_gemisi_goruntule_button.pack_forget()

        konteyner_gemisi_ekle_button.pack_forget()
        konteyner_gemisi_duzenle_button.pack_forget()
        konteyner_gemisi_sil_button.pack_forget()
        konteyner_gemisi_goruntule_button.pack_forget()

        petrol_tankeri_ekle_button.pack_forget()
        petrol_tankeri_duzenle_button.pack_forget()
        petrol_tankeri_sil_button.pack_forget()
        petrol_tankeri_goruntule_button.pack_forget()
    def veri_ekle():    #Gerekli Fonksiyonlar Yazıldı

        kaldir_mevcut_butonlar()        #Butonlar kaldırıldı


        gemiler_ekle_button.pack(pady=(15, 25))     #Yeni butonlar eklendi
        sefer_ekle_button.pack(pady=25)
        liman_ekle_button.pack(pady=25)
        kaptan_ekle_button.pack(pady=25)
        murettebat_ekle_button.pack(pady=25)
        geri_button.place(x=50, y=150)


    def veri_duzenle():
        kaldir_mevcut_butonlar()
        gemiler_duzenle_button.pack(pady=(50, 25))
        sefer_duzenle_button.pack(pady=25)
        liman_duzenle_button.pack(pady=25)
        kaptan_duzenle_button.pack(pady=25)
        murettebat_duzenle_button.pack(pady=25)
        geri_button.place(x=50, y=150)


    def veri_sil():
        kaldir_mevcut_butonlar()
        gemiler_sil_button.pack(pady=(50, 25))
        sefer_sil_button.pack(pady=25)
        liman_sil_button.pack(pady=25)
        kaptan_sil_button.pack(pady=25)
        murettebat_sil_button.pack(pady=25)
        geri_button.place(x=50, y=150)

    def veri_goruntule():
        kaldir_mevcut_butonlar()
        gemiler_goruntule_button.pack(pady=(50, 25))
        sefer_goruntule_button.pack(pady=25)
        liman_goruntule_button.pack(pady=25)
        kaptan_goruntule_button.pack(pady=25)
        murettebat_goruntule_button.pack(pady=25)
        geri_button.place(x=50, y=150)


    def gemi_ekle():
        kaldir_mevcut_butonlar()
        yolcu_gemisi_ekle_button.pack(pady=(50, 25))
        konteyner_gemisi_ekle_button.pack(pady=25)
        petrol_tankeri_ekle_button.pack(pady=25)
        geri_button.place(x=50, y=150)


    def gemi_duzenle():
        kaldir_mevcut_butonlar()
        yolcu_gemisi_duzenle_button.pack(pady=(50, 25))
        konteyner_gemisi_duzenle_button.pack(pady=25)
        petrol_tankeri_duzenle_button.pack(pady=25)
        geri_button.place(x=50, y=150)


    def gemi_sil():
        kaldir_mevcut_butonlar()
        yolcu_gemisi_sil_button.pack(pady=(50, 25))
        konteyner_gemisi_sil_button.pack(pady=25)
        petrol_tankeri_sil_button.pack(pady=25)
        geri_button.place(x=50, y=150)

    def gemi_goruntule():
        kaldir_mevcut_butonlar()
        yolcu_gemisi_goruntule_button.pack(pady=(50, 25))
        konteyner_gemisi_goruntule_button.pack(pady=25)
        petrol_tankeri_goruntule_button.pack(pady=25)
        geri_button.place(x=50, y=150)




    def sefer_ekle():
        x="sefer_ekle"
        entry_alma_modülü(x)

    def sefer_duzenle():
        x="sefer_duzenle"
        entry_alma_modülü(x)


    def sefer_sil():
        x="sefer_sil"
        entry_alma_modülü(x)


    def sefer_goruntule():

        x="sefer_goruntule"

        entry_alma_modülü(x)






    def liman_ekle():
        x="liman_ekle"
        entry_alma_modülü(x)

    def liman_duzenle():
        x="liman_duzenle"
        entry_alma_modülü(x)


    def liman_sil():
        x="liman_sil"
        entry_alma_modülü(x)


    def liman_goruntule():
        x="liman_goruntule"
        entry_alma_modülü(x)



    def kaptan_ekle():
        x="kaptan_ekle"
        entry_alma_modülü(x)


    def kaptan_duzenle():
        x="kaptan_duzenle"
        entry_alma_modülü(x)


    def kaptan_sil():
        x="kaptan_sil"
        entry_alma_modülü(x)


    def kaptan_goruntule():
        x="kaptan_goruntule"
        entry_alma_modülü(x)


    def murettebat_ekle():
        x="murettebat_ekle"
        entry_alma_modülü(x)


    def murettebat_duzenle():
        x="murettebat_duzenle"
        entry_alma_modülü(x)


    def murettebat_sil():
        x="murettebat_sil"
        entry_alma_modülü(x)


    def murettebat_goruntule():
        x="murettebat_goruntule"
        entry_alma_modülü(x)



    def yolcu_gemi_ekle():

        x="yolcu_gemisi_ekle"
        entry_alma_modülü(x)


    def yolcu_gemi_duzenle():

        x="yolcu_gemisi_duzenle"
        entry_alma_modülü(x)


    def yolcu_gemi_sil():


        x="yolcu_gemisi_sil"
        entry_alma_modülü(x)


    def yolcu_gemi_goruntule():
        x="yolcu_gemisi_goruntule"
        entry_alma_modülü(x)


    def konteyner_gemi_ekle():

        x="konteyner_gemisi_ekle"
        entry_alma_modülü(x)



    def konteyner_gemi_duzenle():
        x="konteyner_gemisi_duzenle"
        entry_alma_modülü(x)


    def konteyner_gemi_sil():
        x="konteyner_gemisi_sil"
        entry_alma_modülü(x)


    def konteyner_gemisi_goruntule():
        x="konteyner_gemisi_goruntule"
        entry_alma_modülü(x)


    def petrol_tankeri_ekle():

        x="petrol_tankeri_ekle"
        entry_alma_modülü(x)


    def petrol_tankeri_duzenle():
        x="petrol_tankeri_duzenle"
        entry_alma_modülü(x)

    def petrol_tankeri_sil():
        x="petrol_tankeri_sil"
        entry_alma_modülü(x)


    def petrol_tankeri_goruntule():
        x="petrol_tankeri_goruntule"
        entry_alma_modülü(x)

    def intro_bitir(): #İntro fonksiyonu eklendi

        intro_label.place_forget()

    root = tk.Tk()     #Menü oluşturuldu
    root.title("Liman Veritabanı Yönetim Sistemi")
    root.geometry("1640x960")
    intro_image = tk.PhotoImage(file="intro.png")
    intro_label = tk.Label(root, image=intro_image)

    intro_label.place(relwidth=1, relheight=1)


    root.after(3000, intro_bitir)

    background_image = tk.PhotoImage(file="arka_plan.png")  #Arka plan eklendi
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)



    #Başlıklar ve gerekli butonlar oluşturuldu
    baslik_label = tk.Label(root, text="LİMAN VERİTABANI YÖNETİM SİSTEMLERİ", font=("Helvetica", 34, "bold"), fg="red")

    baslik_label.pack(pady=10)

    ara_baslik=tk.Label(root, text="Yapmak istediğiniz işlemi seçin:", font=("Helvetica", 20))
    ara_baslik.pack(pady=50)

    ekle_button = tk.Button(root, text="Veri Ekle", width=25, height=3, command=veri_ekle)
    ekle_button.pack(pady=(50, 25))

    duzenle_button = tk.Button(root, text="Veri Düzenle", width=25, height=3, command=veri_duzenle)
    duzenle_button.pack(pady=25)

    sil_button = tk.Button(root, text="Veri Sil", width=25, height=3, command=veri_sil)
    sil_button.pack(pady=25)

    goruntule_button = tk.Button(root, text="Veri Görüntüle", width=25, height=3, command=veri_goruntule)
    goruntule_button.pack(pady=25)

    cikis_button = tk.Button(root, text="Çıkış", width=25, height=3, command=cikis)
    cikis_button.pack(pady=25)


    geri_button = tk.Button(root, text="Geri", width=25, height=3, command=geri)


    gemiler_ekle_button = tk.Button(root, text="Gemiler", width=25, height=3,command=gemi_ekle)  # Yeni seçeneklerin butonları oluşturuldu

    gemiler_duzenle_button = tk.Button(root, text="Gemiler", width=25, height=3,command=gemi_duzenle)

    gemiler_sil_button = tk.Button(root, text="Gemiler", width=25, height=3,command=gemi_sil)

    gemiler_goruntule_button = tk.Button(root, text="Gemiler", width=25, height=3,command=gemi_goruntule)

    sefer_ekle_button = tk.Button(root, text="Seferler", width=25, height=3,command= sefer_ekle)

    sefer_duzenle_button = tk.Button(root, text="Seferler", width=25, height=3,command= sefer_duzenle)

    sefer_sil_button = tk.Button(root, text="Seferler", width=25, height=3,command=sefer_sil)

    sefer_goruntule_button = tk.Button(root, text="Seferler", width=25, height=3,command=sefer_goruntule)

    liman_ekle_button = tk.Button(root, text="Limanlar", width=25, height=3,command=liman_ekle)

    liman_duzenle_button = tk.Button(root, text="Limanlar", width=25, height=3,command=liman_duzenle)

    liman_sil_button = tk.Button(root, text="Limanlar", width=25, height=3,command=liman_sil)

    liman_goruntule_button = tk.Button(root, text="Limanlar", width=25, height=3,command=liman_goruntule)

    kaptan_ekle_button = tk.Button(root, text="Kaptanlar", width=25, height=3,command=kaptan_ekle)

    kaptan_duzenle_button = tk.Button(root, text="Kaptanlar", width=25, height=3,command=kaptan_duzenle)

    kaptan_sil_button = tk.Button(root, text="Kaptanlar", width=25, height=3,command=kaptan_sil)

    kaptan_goruntule_button = tk.Button(root, text="Kaptanlar", width=25, height=3,command=kaptan_goruntule)

    murettebat_ekle_button = tk.Button(root, text="Mürettebatlar", width=25, height=3,command=murettebat_ekle)

    murettebat_duzenle_button = tk.Button(root, text="Mürettebatlar", width=25, height=3,command=murettebat_duzenle)

    murettebat_sil_button = tk.Button(root, text="Mürettebatlar", width=25, height=3,command=murettebat_sil)

    murettebat_goruntule_button = tk.Button(root, text="Mürettebatlar", width=25, height=3,command=murettebat_goruntule)



    yolcu_gemisi_ekle_button=tk.Button(root, text="Yolcu Gemisi", width=25, height=3,command=yolcu_gemi_ekle)
    yolcu_gemisi_duzenle_button=tk.Button(root, text="Yolcu Gemisi", width=25, height=3,command=yolcu_gemi_duzenle)
    yolcu_gemisi_sil_button=tk.Button(root, text="Yolcu Gemisi", width=25, height=3,command=yolcu_gemi_sil)
    yolcu_gemisi_goruntule_button=tk.Button(root, text="Yolcu Gemisi", width=25, height=3,command=yolcu_gemi_goruntule)



    konteyner_gemisi_ekle_button=tk.Button(root, text="Konteyner Gemisi", width=25, height=3,command=konteyner_gemi_ekle)
    konteyner_gemisi_duzenle_button=tk.Button(root, text="Konteyner Gemisi", width=25, height=3,command=konteyner_gemi_duzenle)
    konteyner_gemisi_sil_button=tk.Button(root, text="Konteyner Gemisi", width=25, height=3,command=konteyner_gemi_sil)
    konteyner_gemisi_goruntule_button=tk.Button(root, text="Konteyner Gemisi", width=25, height=3,command=konteyner_gemisi_goruntule)



    petrol_tankeri_ekle_button=tk.Button(root, text="Petrol Tankeri", width=25, height=3,command=petrol_tankeri_ekle)
    petrol_tankeri_duzenle_button=tk.Button(root, text="Petrol Tankeri", width=25, height=3,command=petrol_tankeri_duzenle)
    petrol_tankeri_sil_button=tk.Button(root, text="Petrol Tankeri", width=25, height=3,command=petrol_tankeri_sil)
    petrol_tankeri_goruntule_button=tk.Button(root, text="Petrol Tankeri", width=25, height=3,command=petrol_tankeri_goruntule)
    intro_label.lift()

    root.mainloop()

main()
