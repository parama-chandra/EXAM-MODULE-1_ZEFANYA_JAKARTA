def create_phone_number(notel):
    hasil="("
    for index in range(0,len(notel)):
        if len(notel[index])!=1:
            return f"ERROR : Inputan ke- {index} tidak sesuai format"
        else:
            if index == 2:
                hasil += notel[index] + ") " #untuk menambah ") " setelah angka ke 3
            elif index == 5:
                hasil += notel[index] + "-" #untuk menambah "-" setelah angka ke 6
            else :
                hasil += notel[index]
    return hasil



myList = []
for a in range (1,11):
    myList.append(input(f"Angka ke-{a} (harus 1 digit)= "))
print (f"Angka yang kamu input adalah {myList}")
print (f"Jadi nomor teleponmu berdasarkan nomor yang kamu input adalah {create_phone_number(myList)}")