import tkinter as tk#tkinter modülünü import eder.
from tkinter import ttk, messagebox#ttk tkinterın gelişmiş widgetlarınısağlar
import re#re modülü düzenli ifadelerle metin üzerinde arama ve bulma yapar
from VT_Sorgulari import Uye#veri tabanı sorgusundaki üyeleri import eder

class MainApp: #uygulamanın ana arayüz bileşenlerini tanımlar.
    def __init__(self, root):
        self.root = root
        self.root.title("Üye Yönetim Sistemi Görsel Programlama")#arayüz penceresi başlık
        self.root.geometry('1300x600')#Arayüz penceresi boyutlandırma
        self.root.configure(bg="#f4f4f4")#arkaplan renk

        #Üye Bilgi Çerçevesi
        frame_ust = ttk.LabelFrame(root, text="Üye Bilgileri", padding=(10, 10))
        frame_ust.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        #Giiriş Alanları Oluşturuyoruz.(Ad,Soyad,Meslek,Ceptel,Eposta,Adres)
        ttk.Label(frame_ust, text="TCKimlikNo:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.tckimlik_entry = ttk.Entry(frame_ust)#tckimlik girişi
        self.tckimlik_entry.grid(row=0, column=1, padx=5, pady=5)#gridde konumlandırma.

        ttk.Label(frame_ust, text="Ad:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.ad_entry = ttk.Entry(frame_ust) #isim giriş
        self.ad_entry.grid(row=1, column=1, padx=5, pady=5) #gridle konumlandırma textbox

        ttk.Label(frame_ust, text="Soyad:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.soyad_entry = ttk.Entry(frame_ust)# soyisim giriş
        self.soyad_entry.grid(row=2, column=1, padx=5, pady=5)#gridle konumlandırma textbox

        ttk.Label(frame_ust, text="CepTel").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.ceptel_entry = ttk.Entry(frame_ust) #telefon giriş
        self.ceptel_entry.grid(row=4, column=1, padx=5, pady=5)#gridle konumlandırma textbox

        ttk.Label(frame_ust, text="Eposta:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.eposta_entry = ttk.Entry(frame_ust)#e posta giriş alanı
        self.eposta_entry.grid(row=5, column=1, padx=5, pady=5)#gridle konumlandırma textbox

        ttk.Label(frame_ust, text="Meslek:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.meslek_entry = ttk.Entry(frame_ust) #meslek girişi
        self.meslek_entry.grid(row=3, column=1, padx=5, pady=5)#gridle konumlandırma textbox

        ttk.Label(frame_ust, text="Adres:").grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.adres_entry = ttk.Entry(frame_ust) #adres girişi
        self.adres_entry.grid(row=6, column=1, padx=5, pady=5)#gridle konumlandırma textbox

        #İşlem Butonları(Ekle,Bul,Güncelle,Sil,Listele
        frame_butonlar = ttk.Frame(root, padding=(10, 10))
        frame_butonlar.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        ttk.Button(frame_butonlar, text="Ekle", command=self.ekle).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(frame_butonlar, text="Bul", command=self.bul).grid(row=0, column=1, padx=10, pady=10)
        self.guncelle_btn = ttk.Button(frame_butonlar, text="Güncelle", command=self.guncelle, state="disabled")
        self.guncelle_btn.grid(row=0, column=2, padx=10, pady=10)
        self.sil_btn = ttk.Button(frame_butonlar, text="Sil", command=self.sil, state="disabled")
        self.sil_btn.grid(row=0, column=3, padx=10, pady=10)
        ttk.Button(frame_butonlar, text="Listele", command=self.listele).grid(row=0, column=4, padx=10, pady=10)

        #Listeleme Alanı(treeview)
        frame_liste = ttk.LabelFrame(root, text="Üye Listesi", padding=(10, 10))
        frame_liste.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.tree = ttk.Treeview(frame_liste,
                                 columns=("UyeID", "TCKimlikNo", "Ad", "Soyad", "Meslek", "CepTel", "EPosta", "Adres"),
                                 show="headings")
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        scrollbar = ttk.Scrollbar(frame_liste, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        #Treeview Sütun Başlıkları
        self.tree.heading("UyeID", text="Uye ID")
        self.tree.heading("TCKimlikNo", text="T.C. Kimlik No")
        self.tree.heading("Ad", text="Ad")
        self.tree.heading("Soyad", text="Soyad")
        self.tree.heading("Meslek", text="Meslek")
        self.tree.heading("CepTel", text="Telefon")
        self.tree.heading("EPosta", text="E-Posta")
        self.tree.heading("Adres", text="Adres")

        #Treeview sütun Genişliklerini ayarlama
        self.tree.column("UyeID", width=100, anchor="center")
        self.tree.column("TCKimlikNo", width=150, anchor="center")
        self.tree.column("Ad", width=150, anchor="center")
        self.tree.column("Soyad", width=150, anchor="center")
        self.tree.column("Meslek", width=150, anchor="center")
        self.tree.column("CepTel", width=150, anchor="center")
        self.tree.column("EPosta", width=150, anchor="center")
        self.tree.column("Adres", width=150, anchor="center")

        root.grid_rowconfigure(2, weight=1)#Listeleme Alanı için genişlik sağlıyoruz.
        root.grid_columnconfigure(0, weight=1)#Listeleme Alanı için genişlik sağlıyoruz.
        frame_liste.grid_rowconfigure(0, weight=1)#Treeview Alanı için esneklik sağlıyoruz.
        frame_liste.grid_columnconfigure(0, weight=1)#Treeview Alanı için esneklik sağlıyoruz.

        self.tree.bind("<<TreeviewSelect>>", self.kayit_secildi)#Treeview seçim onayı

    def ekle(self):#yeni üye ekler.
        tckimlik = self.tckimlik_entry.get() #tckimlik bilgilerini alır
        ad = self.ad_entry.get() #ad bilgisi alınır
        soyad = self.soyad_entry.get() #soyad bilgisi alınır
        ceptel = self.ceptel_entry.get() #ceptel bilgisi alınır
        eposta = self.eposta_entry.get() #eposta bilgisi alınır
        adres = self.adres_entry.get() #adres bilgisi alır
        meslek = self.meslek_entry.get() #meslek bilgisi alır.

        if not self.gecerli_tckimlik(tckimlik):#tckimlik kontrolü yapar
            messagebox.showerror("Hata", "Geçersiz TC Kimlik Numarası. 11 hane olmalıdır.")
            return
        if not self.gecerli_ceptel(ceptel):#telefon kontrolü yapar
            messagebox.showerror("Hata", "Geçersiz cep telefonu giridiniz +90 ile başlayan 10 haneli olmalıdır.")
            return
        try:
            Uye.ekle(tckimlik, ad, soyad, ceptel, eposta, meslek, adres)#Veritabanına ekleme işlemi
            messagebox.showinfo("Başarılı", "Üye başarıyla eklendi.")
            self.temizle()
            self.listele()
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

    def gecerli_tckimlik(self, tckimlik):#tc kimlik geçerli mi diye kontrol eder.
        return tckimlik.isdigit() and len(tckimlik) == 11#TcKimlik durumu 11 haneli olacak şekilde kontrol eder.

    def gecerli_ceptel(self, ceptel):#cep telefonu geçerli mi diye kontrol eder.
        return bool(re.match(r"^\+90\s?\d{10}$", ceptel))

    def gecerli_eposta(self,eposta):#
        return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',eposta))#E-Posta Durumunu Kontrol eder

    def bul(self): #seçili üyenin bilgileri burada getirilir
        tckimlik = self.tckimlik_entry.get()
        if not tckimlik:
            messagebox.showwarning("Uyarı", "Lütfen TC Kimlik Numarasını girin.")
            return
        uye = Uye.bul(tckimlik)#Tc kimlik numa göre arar
        if uye: #giriş alanlarını bulduğumuz üye bilgileri ile dolduruyoruz.
            self.ad_entry.delete(0, tk.END)
            self.ad_entry.insert(0, uye[2])
            self.soyad_entry.delete(0, tk.END)
            self.soyad_entry.insert(0, uye[3])
            self.ceptel_entry.delete(0, tk.END)
            self.ceptel_entry.insert(0, uye[4])
            self.eposta_entry.delete(0, tk.END)
            self.eposta_entry.insert(0, uye[5])
            self.meslek_entry.delete(0, tk.END)
            self.meslek_entry.insert(0, uye[6])
            self.adres_entry.delete(0, tk.END)
            self.adres_entry.insert(0, uye[7])
            self.guncelle_btn.config(state="normal")
            self.sil_btn.config(state="normal")
        else:
            messagebox.showinfo("Bilgi", "Üye Bulunamadı.")

    def guncelle(self): #üye güncelleme işlemi
        eski_tckimlik = self.selected_tckimlik
        yeni_tckimlik = self.tckimlik_entry.get()
        eposta=self.eposta_entry.get()
        ceptel=self.ceptel_entry.get()

        if not self.gecerli_tckimlik(yeni_tckimlik):
            messagebox.showerror("Hata", "Geçersiz TC Kimlik Numarası. 11 hane olmalıdır.")
            return
        if not self.gecerli_eposta(eposta):
            messagebox.showerror("Hata", "Geçersiz Eposta.")
            return
        if not self.gecerli_ceptel(ceptel):
            messagebox.showerror("Hata", "Geçersiz Telefon Numarası.")
            return

        try: #veritabanında güncelleme işlemi
            Uye.guncelle(
                eski_tckimlik,
                yeni_tckimlik,
                self.ad_entry.get(),
                self.soyad_entry.get(),
                self.ceptel_entry.get(),
                self.eposta_entry.get(),
                self.meslek_entry.get(),
                self.adres_entry.get()
            )
            messagebox.showinfo("Başarı", "Üye Başarıyla Güncellendi")
            self.temizle()
            self.listele()
        except Exception as e:
            messagebox.showerror("Hata", f"Güncelleme başarısız: {e}")

    def sil(self): #seçili üyeyi silme işlemi kodları
        try:
            Uye.sil(self.tckimlik_entry.get())
            messagebox.showinfo("Başarı", "Üye başarıyla silindi.")
            self.temizle()
            self.listele()
        except Exception as e:
            messagebox.showerror("Hata", f"Silme işlemi başarısız: {e}")

    def listele(self): #Bilgiler buradaki kodlar sayesinde listelenir.
        for row in self.tree.get_children():
            self.tree.delete(row)
        for uye in Uye.listele():
            self.tree.insert("", tk.END,
                             values=(
                                 uye[0], uye[1], uye[2], uye[3], uye[6], uye[4], uye[5], uye[7]))

    def temizle(self): #seçilen öge temizlenir
        self.tckimlik_entry.delete(0, tk.END)
        self.ad_entry.delete(0, tk.END)
        self.soyad_entry.delete(0, tk.END)
        self.ceptel_entry.delete(0, tk.END)
        self.eposta_entry.delete(0, tk.END)
        self.meslek_entry.delete(0, tk.END)
        self.adres_entry.delete(0, tk.END)
        self.guncelle_btn.config(state="disabled")
        self.sil_btn.config(state="disabled")

    def kayit_secildi(self, event):
        selected_items = self.tree.selection()
        if not selected_items:
            return

        selected_item = selected_items[0] #Tüm giriş alanlarını temizler ve butonları devre dışı bırakır
        selected_data = self.tree.item(selected_item, "values")
        self.selected_tckimlik = selected_data[1]

        self.tckimlik_entry.delete(0, tk.END) #tckimlik ekleme silme ayarları
        self.tckimlik_entry.insert(0, selected_data[1])

        self.ad_entry.delete(0, tk.END)#ad ekleme silme ayarları
        self.ad_entry.insert(0, selected_data[2])

        self.soyad_entry.delete(0, tk.END)#soyad ekleme silme ayarları
        self.soyad_entry.insert(0, selected_data[3])

        self.ceptel_entry.delete(0, tk.END)#ceptel ekleme silme ayarları
        self.ceptel_entry.insert(0, selected_data[5])

        self.eposta_entry.delete(0, tk.END)#eposta ekleme silme ayarları
        self.eposta_entry.insert(0, selected_data[6])

        self.meslek_entry.delete(0, tk.END)#meslekekleme silme ayarları
        self.meslek_entry.insert(0, selected_data[4])

        self.adres_entry.delete(0, tk.END)#adres ekleme silme ayarları
        self.adres_entry.insert(0, selected_data[7])

        self.guncelle_btn.config(state="normal")
        self.sil_btn.config(state="normal")

# Tkinter penceresini oluştur
root = tk.Tk()
app = MainApp(root)
root.mainloop()