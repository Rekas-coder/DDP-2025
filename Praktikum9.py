#celcius_to_fahrenheit
def celcius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celcius_to_fahrenheit(100))

def celcius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celcius_to_fahrenheit(0))

#is_genap
def is_genap(angka):
  if angka % 2 == 0:
    return True
  else:
    return False
print(is_genap(10))

def is_genap(angka):
  if angka % 2 == 0:
    return True
  else:
    return False
print(is_genap(7))

#keterangan_lulus
def keterangan_lulus(nilai):
  if nilai >= 60:
    return "lulus"
  else:
    return "tidak lulus"
print(keterangan_lulus(70))

def keterangan_lulus(nilai):
  if nilai >= 60:
    return "lulus"
  else:
    return "tidak lulus"
print(keterangan_lulus(50))

#menampilkan_bilangan_ganjil
def bilangan(angka):
  for i in range(1, angka):
    if i % 2 != 0:
      print(i, end=', ')

bilangan(20)      