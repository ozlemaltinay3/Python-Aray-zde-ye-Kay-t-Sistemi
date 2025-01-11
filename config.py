import pyodbc #pyodbc yi içeri aktarıyoruz.

#veritabanı bağlantı bilgileri
SERVER='DESKTOP-R8OKFF9'
DATABASE='KutuphaneDB'

#veritabanına bağlanmak için bağlantı dizesini döndürür
def get_connection():
    "Veri Tabanına bağlanır ve bağlantı nesnesini döndürür"
    connection=pyodbc.connect(
        f'DRIVER={{SQL Server}};'
        f'SERVER={SERVER};'
        f'DATABASE={DATABASE};'
        'Trusted_Connection=yes;'#Windows kimlik doğrulaması kullanılır.
    )
    return connection