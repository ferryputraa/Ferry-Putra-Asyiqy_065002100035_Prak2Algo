from math import sqrt
rumus = input("Sisi mana yang ingin anda hitung? (a, b, c) : ")

if rumus == 'c' :
    A = int(input("Masukkan panjang a : "))
    B = int(input("Masukkan panjang b : "))
    C = sqrt(A*A + B*B)
    print("Panjang sisi c adalah : ",C)

elif rumus == 'a' :
    B = int(input("Masukkan panjang b : "))
    C = int(input("Masukkan panjang c : "))
    if (C<B) :
        print("Panjang c tidak valid! ")
        C = int(input("Masukkan panjang c : "))
        A = sqrt(C*C - B*B)
        print("Panjang sisi a adalah : ",A)

elif rumus == "b" :
    A = int(input("Masukkan panjang a : "))
    C = int(input("Masukkan panjang c : "))
    if (C<A) :
        print("Panjang c tidak valid! ")
        C = int(input("Masukkan panjang c : "))
        B = sqrt(C*C - A*A)
        print("Panjang sisi b adalah : ",B)
