

def luas_segitiga_siku():
	bidang_datar = 'segitiga siku'
	
	alas = int(input('masukkan alas: '))
	tinggi = int(input('masukkan tinggi: '))
	luas_segitiga_siku = 0.5 * alas * tinggi
	
	return bidang_datar, luas_segitiga_siku
	
	
def luas_persegi():
	bidang_datar = 'persegi'
	sisi = int(input('masukkan sisi: '))
	luas = sisi * sisi
	
	return bidang_datar, luas

def luas_lingkaran():
	bidang_datar = 'lingkaran'
	jari_jari = int(input('masukkan jari_jari: '))
	luas_lingkaran = 3.14 * jari_jari**2
	
	return bidang_datar, luas_lingkaran
				
while True:
	print("1. Luas segitiga siku")
	print("2. Luas persegi")
	print("3. Luas lingkaran")
	print("4. keluar")
	
	pilih_menu = int(input("pilih menu: "))
	
	if pilih_menu == 1:
		hasil = luas_segitiga_siku()
	elif pilih_menu == 2:
		hasil = luas_persegi()
	elif pilih_menu == 3:
		hasil = luas_lingkaran()
	elif pilih_menu == 4:
		break
		
	print('luas {} adalah {}'.format(hasil[0], hasil[1]))
	
