def buble_sort(arr):
    #mengukur data/array
    n=len(arr)
    #melakukan perulangan
    for i in range(n-1):
        #melakukan perbandingan
        for j in range(n - 1 - i):
            #melakukan perbandingan data
            if arr[j] > arr[j+1]:
                #menukar posisi
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)

arr = [64, 34, 25, 12, 22, 11, 90]
print("Data yang belum di buble sort :", arr)
buble_sort(arr)
print("Data yang sudah di buble sort :", arr)
