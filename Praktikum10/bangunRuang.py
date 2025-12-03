import math

# Rumus Kubus
def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

# Rumus Balok 
def balok(p,l,t):
    hasil = p * l * t
    return hasil

# Rumus Prisma Segitiga
def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

#  Rumus Tabung
def tabung(jari_jari, tinggi):
    alas = 22/7 * jari_jari **2
    hasil = alas * tinggi
    return hasil

# Rumus Kerucut
def kerucut(radius, tinggi):
    hasil = 1/3 * 22/7 * pow(radius,2) * tinggi
    return hasil

print(kubus(3))
print(balok(3,3,3))
print(prisma(3,3,3))
print(tabung(7,10))
print(kerucut(7,10))