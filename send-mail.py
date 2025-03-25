import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Ayarlar
excel_dosyasi = "sky-lab-test-list.xlsx" # mail gönderilecek kişilerin excel dosyası lütfen kendi excel dosyanızı örnekteki dosyaya bakarak yükleyiniz
smtp_server = "smtp.office365.com" # hotmail için mail sunucusu
#smtp_server = "smtp.gmail.com" # gmail için mail sunucusu
smtp_port = 587
gonderici_email = "test@test.com" # mailin gönderileceği hesap
gonderici_sifre = "uygulama sifresi" # mailin gönderileceği hesabın "uygulama şifresi - normal şifre değil daha fazla detay için readmeye bakınız"


df = pd.read_excel(excel_dosyasi)

# E-posta sunucusuna bağlan
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(gonderici_email, gonderici_sifre)

for index, row in df.iterrows():
    try:
        # E-posta içeriğini hazırla
        msg = MIMEMultipart()
        msg['From'] = gonderici_email
        msg['To'] = row['Email']
        msg['Subject'] = f"{row['Name']} {row['LastName']} - Açıklama Hakkında" # Mailin konusu şuanki durumda Name LastName  - Açıklama Hakkında olarak yazıyor değiştirilebilir
        
        # E-posta gövdesi
        body = f"""
Sayın {row['Name']} {row['LastName']},

MAİL GÖVDESİ İÇERİK DEĞİŞTİRİLEBİLİR
        """ # MAİLİN İÇERİĞİ ÜST KISIMDAKİ ALANA YAZILMALIDIR
        
        msg.attach(MIMEText(body, 'plain'))

        # E-postayı gönder
        server.sendmail(gonderici_email, [msg['To']], msg.as_string())
        print(f"{row['Email']} adresine gönderildi.")

    except Exception as e:
        print(f"{row['Email']} hatası: {str(e)}")


server.quit()


# YUKARIDAKİ MAİL GÖNDERME KODU TAMAMEN SKY LAB KULÜBÜ YILDIZ TEKNİK ÜNİVERSİTESİ BİLGİSAYAR BİLİMLERİ KULÜBÜNE AİTTİR