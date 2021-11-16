print("\n======  Kosan Putri  =======")
print("Menyediakan Kosan Khusus Putri")

kp= input("Silahkan Masukkan nama anda : ")
print("Nama Penyewa = ", kp)

Jelas = 'iya'
While(true):


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
    
print("\n======== T E R I M A   K A S I H =========")

Jelas=input(" Apakah anda ingin menambahkan kamar") 
if jelas == 'tidak':
    break
