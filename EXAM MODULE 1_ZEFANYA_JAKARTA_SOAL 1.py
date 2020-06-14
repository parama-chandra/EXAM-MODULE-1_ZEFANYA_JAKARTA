def Hashtag (a):

    if a == "":
        return False #untuk return False saat inputnya empty string
    else:
        sentence = a.split()
        hasil = "#" #untuk mulai dengan hashtag
        for b in sentence :
            capital = str(b).capitalize() #untuk setiap kata mulai dengan huruf kapital
            hasil += capital 
    if len(hasil) > 140: #untuk return False saat jumlah char lebih dari 140
        return False
    else :
        return hasil

kalimat = input("Masukkan kalimatnya disini : ")
print(Hashtag(kalimat))