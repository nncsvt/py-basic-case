#Program cek kepemilikan KTP
#penggunaan nested if, len, and lower function

nama = input("Nama            : ")
umur = int(input("Umur            : "))
if umur >= 17:
  ktp = input("Punya KTP (y/t) : ")
  if ktp.lower() == 'y': ##identifier python library
    NIK = int(input("NIK             : "))
    if len(str(NIK)) != 16: ##check 16 digit 999999999999
      print("NIK yang anda masukkan tidak valid")
  elif ktp.lower() == 't':
    ktp = input("Apakah anda ingin membuat KTP?(y/t) ")
    if ktp.lower() == 'y':
      print("Silahkan lanjutkan ke layanan pembuatan KTP")
  else:
    print("Input status KTP anda tidak tepat")
  print("Terima kasih sudah menggunakan layanan kami")
elif umur < 17:
  print("Layanan ini hanya untuk orang yang berurmur 17 tahun keatas")