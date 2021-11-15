# lulus =input("Apakah Kamu lulus")
# if lulus == "Tidak":
#     print("kamu tidak lulus")

# elif lulus == "Iya":
#     print("Kamu Lulus")

print("\n======  Kosan Putri  =======")
print("Menyediakan Kosan Khusus Putri")

ps = input("Silahkan Masukkan nama anda : ")
print("Nama Penyewa = ", ps)

ps2 = input("Apakah anda punya ktp  : ")
i = 0
while i == ps2:
    if ps2 == "Iya":
        print("Silahkan Pilih terlebih dahulu Kamar yang akan disewa",ps)

    elif ps2 == "Tidak" :
        print("Mohon maaf harus ada ktp ")


nama = ["Kamar VIP 1 ", "KamarVIP 2" , "KamarNonVIP 3" , "KamarNonVIP 4"]

for list in nama:
    print("\n==== 1. ", nama[0],"====")
    print("\n==== 2. ", nama[1],"====")
    print("\n==== 3. ", nama[2],"====") 
    print("\n==== 4. ", nama[3],"====") 
    break   


sewa = int(input("Silahkan Pilih Kamar yang akan di sewa : "))
lama = int(input("Berapa Hari : " ))

if sewa == 1:
    biaya1= lama*200000
    print("Kamar VIP 1  Rp : ",biaya1 )

elif sewa == 2:
    biaya2 = lama*150000
    print("Kamar VIP 2 Rp : ", biaya2)

elif sewa == 3:
    biaya3 = lama*100000
    print("KamarNonVIP 3 Rp : ", biaya3)

elif sewa == 4:
    biaya3 = lama*75000
    print("KamarNonVIP 4 Rp : ", biaya3)
