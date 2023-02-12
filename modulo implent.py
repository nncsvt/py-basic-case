
'Jika hari senin adalah tanggal 1 pada bulan tersebu. Tentukan hari pada tanggal yang dimasukkan user'

tgl = int(input("masukkan tgl = "))
print("Hari pada tanggal " + str(tgl) + " adalah : ", end = '') #deliminator in python
#nested if
if 0 < tgl <= 30:
  if tgl % 7 == 1 :
    print("senin")
  elif tgl % 7 == 2 :
    print("selasa")
  elif tgl % 7 == 3 :
    print("rabu")
  elif tgl % 7 == 4 :
    print("kamis")
  elif tgl % 7 == 5 :
    print("jumat")
  elif tgl % 7 == 6 :
    print("sabtu")
  else :
    print("minggu")
else:
  print("angka yang dimasukkan tidak sesuai")