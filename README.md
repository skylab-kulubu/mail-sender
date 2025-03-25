# **Toplu E-Posta Gönderim Aracı - SKY LAB Readme**

Bu Python betiği, bir Excel dosyasındaki alıcı listesine **toplu e-posta göndermek** için tasarlanmıştır. **SMTP protokolü** kullanılarak Outlook (Office 365) veya Gmail üzerinden e-posta gönderimi yapılabilir.

---

## **📋 Kullanım Talimatları**

### **1. Gereksinimler**
- Python 3.x yüklü olmalıdır.
- Gerekli kütüphaneler (`pandas`, `smtplib`) kurulmalıdır.

#### **Kütüphanelerin Kurulumu**
```bash
pip install pandas
```

---

### **2. Excel Dosyası Hazırlama**
- **`sky-lab-test-list.xlsx`** dosyasına gönderilecek kişilerin bilgileri eklenmelidir.
- **Zorunlu Sütunlar:**
  - `Name` (Ad)
  - `LastName` (Soyad)
  - `Email` (E-posta adresi)

**Örnek Excel Yapısı:**

| Name  | LastName | Email             |
|-------|----------|-------------------|
| Ahmet | Yılmaz   | ahmet@example.com |
| Ayşe  | Demir    | ayse@example.com  |

---

### **3. SMTP Ayarları**
#### **Outlook (Office 365) için:**
```python
smtp_server = "smtp.office365.com"
smtp_port = 587
gonderici_email = "outlook@hotmail.com"  # Gönderici e-posta
gonderici_sifre = "uygulama_sifresi"    # Uygulama şifresi (normal şifre değil)
```

#### **Gmail için:**
```python
smtp_server = "smtp.gmail.com"
smtp_port = 587
gonderici_email = "example@gmail.com"   # Gönderici e-posta
gonderici_sifre = "uygulama_sifresi"    # Uygulama şifresi (normal şifre değil)
```

> **⚠️ Önemli:**  
> - Gmail veya Outlook için **"Uygulama Şifresi"** kullanılmalıdır.  
> - **2 Adımlı Doğrulama** açık olmalıdır.  
> - Uygulama şifresi oluşturmak için video rehberler:  
>   - **Outlook/Hotmail:** [Hotmail'de Uygulama Şifresi Alma Rehberi](https://www.youtube.com/watch?v=fqimk_W1cgQ)  
>   - **Gmail:** [Gmail'de Uygulama Şifresi Alma Rehberi](https://www.youtube.com/watch?v=MkLX85XU5rU)  
> - Metin rehberler:  
>   - **Gmail:** [Google Hesap Güvenlik](https://myaccount.google.com/apppasswords)  
>   - **Outlook:** [Microsoft Güvenlik](https://mysignins.microsoft.com/security-info)  

---

### **4. E-Posta İçeriğini Düzenleme**
- **Konu:** `msg['Subject']` kısmından değiştirilebilir.
- **Mesaj İçeriği:** `body` değişkeni içine yazılmalıdır.

**Örnek:**
```python
body = f"""
Sayın {row['Name']} {row['LastName']},

Bu bir test mesajıdır. SKY LAB Toplu e-posta gönderim aracını kullandığınız için teşekkür ederiz.

Saygılarımızla,
SKY LAB KULÜBÜ
"""
```

---

### **5. Betiği Çalıştırma**
Terminal veya komut istemcisinde:
```bash
python mail_gonder.py
```

#### **Beklenen Çıktı:**
```
ahmet@example.com adresine gönderildi.
ayse@example.com adresine gönderildi.
```

---

## **🚨 Hata Durumunda Yapılacaklar**
- **SMTP Bağlantı Hatası:**  
  - Güvenlik duvarı veya antivirüs engelleyebilir.  
  - SMTP ayarlarını kontrol edin (port, sunucu adı).  
- **Kimlik Doğrulama Hatası:**  
  - E-posta veya şifre yanlış olabilir.  
  - **Uygulama şifresi kullanıldığından emin olun.**  
- **Excel Dosyası Bulunamadı:**  
  - Dosya adını ve konumunu kontrol edin.  

---

---

**SKY LAB: Bilgisayar Bilimleri Kulübü**  
📧 info@yildizskylab.com  
🌐 [yildizskylab.com](https://yildizskylab.com)  

---
