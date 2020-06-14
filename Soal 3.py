
def asc(gjl):
    '''
    mengurutkan angka ganjil kecil ke besar dengan bubble sort
    '''
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(len(gjl)-1):
            if gjl[i] > gjl [i+1]:
                swap += 1
                gjl[i],gjl[i+1]=gjl[i+1],gjl[i]
    return gjl

def dsc(gnp):
    '''
    mengurutkan angka genap besar ke kecil dengan bubble sort
    '''
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(len(gnp)-1):
            if gnp[i] < gnp [i+1]:
                swap += 1
                gnp[i],gnp[i+1]=gnp[i+1],gnp[i]
    return gnp

def sort_odd_even(inputan):
    if inputan == []:
        return f"Input list kosong {inputan}" # return list kosong bila diinput list kosong
    else:
        pos = []
        odd = []
        even = []
        for s in range(len(inputan)):
            if inputan[s]=="":
                inputan[s]="0"  #error handling apabila saat penginputan ada empty string
        for b in range(len(inputan)):
            if int(inputan[b])%2==0:
                pos.append(1) # mencatat posisi genap
                even.append(inputan[b]) #mengumpulkan angka genap
            else :
                pos.append(0) #mencatat posisi ganjil
                odd.append(inputan[b]) #mengumpulkan angka ganjil
        odd = asc(odd)
        even = dsc(even)
        odd_index = 0
        even_index = 0
        hasil = []
        for k in pos :
            if k == 0:
                hasil.append(odd[odd_index])
                odd_index += 1
            if k == 1:
                hasil.append(even[even_index])
                even_index += 1
        return f"Setelah disort sesuai ketentuan : {hasil}"
    


# cara 1
myList = []
qty = (input("Mau berapa angka ? "))
if qty=="" or int(qty)<1 :
    print (f"Angka yang kamu input adalah {myList}")
    print(f"Input list kosong {myList}")
else:
    qty = int(qty)
    for a in range (1,qty+1):
        myList.append(input(f"Angka ke-{a}= "))
    print (f"Angka yang kamu input adalah {myList}")
    print(f"{sort_odd_even(myList)}")

# cara 2
# myList = [5,3,2,8,1,4]
# sort_odd_even(myList)