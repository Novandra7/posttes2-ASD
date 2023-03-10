# NAMA : Awang Muhammad Novandra Arissaputra
# NIM : 2209116040
# KELAS : Sistem Informasi A 2022

arr = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
def linearsearch(arr,x):
    for l in range(len(arr)):
        if type(arr[l]) == list:
            hasil_x = linearsearch(arr[l],x)
            if hasil_x == -1:
                return -1
            else:
                return(f'{x} ditemukan pada indeks {l}, kolom {hasil_x}')
                
        elif arr[l] == x:
            return (f'{x} ditemukan pada indeks {l}')
    return -1
while True:   
    nama = input("masukkan nama yang ingin dicari : ").capitalize()
    print(linearsearch(arr,nama))
    lanjut = input("apakah ingin lanjut mencari (y/t) : ")
    if lanjut == "y":
        pass
    else:
        break