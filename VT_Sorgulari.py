import pyodbc #pyodbc modülünü içe aktarıyoruz.
from config import get_connection  # config pyden get_connection fonksiyonunu alıyoruz


class Uye:
    @staticmethod
    def connect_db():
        # Veri tabanına bağlanır ve nesneleri döndürür
        connection = get_connection()
        return connection  # bağlantı nesnesini döndürür

    @staticmethod
    def ekle(TCKimlikNo, Ad, Soyad, CepTel, Eposta, Meslek, Adres):
        conn = Uye.connect_db()#bağlantı
        cursor = conn.cursor()#Yarcımcı İmleç
        try:
            # Boşlukları temizle, tırnak işaretlerini çıkar
            TCKimlikNo = TCKimlikNo.strip()
            Ad = Ad.strip()
            Soyad = Soyad.strip()
            CepTel = CepTel.strip()
            Eposta = Eposta.strip()
            Meslek = Meslek.strip()
            Adres = Adres.strip()

            # TC Kimlik No kontrolü
            cursor.execute("SELECT COUNT(*) FROM uye WHERE TCKimlikNo = ?", (TCKimlikNo,))
            count = cursor.fetchone()[0]
            if count > 0:
                raise ValueError("Bu TC Kimlik Numarası zaten kayıtlı.")

            # Eğer Kayıtlı değilse Yeni üye ekleme işlemi yaptırır.
            cursor.execute(
                "INSERT INTO uye (TCKimlikNo, Ad, Soyad, CepTel, Eposta, Meslek, Adres) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (TCKimlikNo, Ad, Soyad, CepTel, Eposta, Meslek, Adres)
            )
            conn.commit()
        except pyodbc.Error as e:
            error_message = str(e)
            if "TCKimlikNo" in error_message:#tc kimlik ile ilgili  kontrol.
                raise ValueError("Tc kimlik numarası geçersiz veya zaten kayıtlı.")
            else:
                raise ValueError(f"Veri Tabanı Hatası: {e}")
        finally:
            conn.close()

    @staticmethod
    def guncelle(eski_tckimlik, yeni_tckimlik, Ad, Soyad, CepTel, Eposta, Meslek, Adres):#Tc Kimlik Numarasına göre üyeleri günceller.
        """
        Güncelleme işlemi
        :param eski_tckimlik: Eski TC Kimlik No
        :param yeni_tckimlik: Yeni TC Kimlik No
        :param Ad:
        :param Soyad:
        :param CepTel:
        :param Eposta:
        :param Meslek:
        :param Adres:
        :return:
        """
        conn = Uye.connect_db()
        cursor = conn.cursor()#yardımcı imleç
        try:
            # Eski TC Kimlik No'nun mevcut olup olmadığını kontrol et.
            cursor.execute("SELECT COUNT(*) FROM uye WHERE TCKimlikNo = ?", (eski_tckimlik,))
            if cursor.fetchone()[0] == 0:
                raise ValueError("Bu TC Kimlik Numarası kayıtlı değil.")

            # Yeni TC Kimlik No'nun zaten var olup olmadığını kontrol et.
            if eski_tckimlik != yeni_tckimlik:
                cursor.execute("SELECT COUNT(*) FROM uye WHERE TCKimlikNo = ?", (yeni_tckimlik,))
                if cursor.fetchone()[0] > 0:
                    raise ValueError("Yeni TC Kimlik Numarası zaten kayıtlı.")

            # Boşlukları ve gereksiz karakterleri temizle
            Ad = Ad.strip()
            Soyad = Soyad.strip()
            CepTel = CepTel.strip()
            Eposta = Eposta.strip()
            Meslek = Meslek.strip()
            Adres = Adres.strip()

            # Güncelleme işlemi
            cursor.execute(
                "UPDATE uye SET TCKimlikNo = ?, Ad = ?, Soyad = ?, CepTel = ?, Eposta = ?, Meslek = ?, Adres = ? WHERE TCKimlikNo = ?",
                (yeni_tckimlik, Ad, Soyad, CepTel, Eposta, Meslek, Adres, eski_tckimlik)
            )
            conn.commit()
        except pyodbc.Error as e:
            raise ValueError(f"Güncelleme hatası: {e}")
        finally:
            conn.close()

    @staticmethod
    def sil(TcKimlikNo):#TC Kimlik Numarasına göre üye siler.
        """
        Silme işlemi
        :param TcKimlikNo:
        :return:
        """
        conn = Uye.connect_db()
        cursor = conn.cursor()
        try:
            # TC Kimlik No'nun mevcut olup olmadığını kontrol etme işlemi gerçekleştirir.
            cursor.execute("SELECT COUNT(*) FROM uye WHERE TCKimlikNo = ?", (TcKimlikNo,))
            if cursor.fetchone()[0] == 0:
                raise ValueError("Bu TC Kimlik Numarası kayıtlı değil.")

            # Silme işlemi burada gerçekleştirilir.
            cursor.execute("DELETE FROM uye WHERE TCKimlikNo = ?", (TcKimlikNo,))
            conn.commit()
        except pyodbc.Error as e:
            raise ValueError(f"Silme hatası: {e}")
        finally:
            conn.close()

    @staticmethod
    def listele():#Tüm Üyeleri Listeler.
        """
        Üye listesini döndürür.
        :return:
        """
        conn = Uye.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM uye")
            return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def bul(TCKimlikNo):#TC Kimlik Numarasına  göre üye arar.
        """
        TC Kimlik Numarasına göre üye bulur.
        :param TCKimlikNo:
        :return:
        """
        conn = Uye.connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM uye WHERE TCKimlikNo = ?", (TCKimlikNo,))
            return cursor.fetchone()#Eğer üye varsa bilgileri döndürür.
        finally:
            conn.close()





