def fpb(angka1, angka2):
    listfpb = []
    listfpb2 = []

    for x in range(1, (int(angka1) + 1)):
        if int(angka1) % x == 0:
            listfpb.append(x)

    for y in range(1, (int(angka2) + 1)):
        if int(angka2) % y == 0:
            listfpb2.append(y)

    fpb1 = max(set(listfpb) & set(listfpb2))
    return fpb1


def kpk(angka1, angka2):
    aa = 0
    bb = 0
    x = 1
    y = 1
    listkpk1 = []
    listkpk2 = []

    while aa < (int(angka1) * int(angka2)):
        aa = int(angka1) * x
        x = x + 1
        listkpk1.append(aa)

    while bb < (int(angka1) * int(angka2)):
        bb = int(angka2) * y
        y = y + 1
        listkpk2.append(bb)

    kpk1 = min(set(listkpk1) & set(listkpk2))
    return kpk1


n = 'y'
while n == 'y':

    ang1 = input('1. Masukkan angka pertama : ')
    while not ang1.isnumeric() or int(ang1) == 0:
        print('Maaf, anda salah input, angka > 0')
        ang1 = input('1. Masukkan angka pertama : ')

    ang2 = input('2. Masukkan angka kedua : ')
    while not ang2.isnumeric() or int(ang2) == 0:
        print('Maaf, anda salah input, angka > 0')
        ang2 = input('2. Masukkan angka kedua : ')

    print('nilai FPB dari %s dan %s adalah : %s' % (ang1, ang2, fpb(ang1, ang2)))
    print('nilai KPK dari %s dan %s adalah : %s' % (ang1, ang2, kpk(ang1, ang2)))

    n = input('ketik (y) untuk lanjut, ketik (x) untuk keluar : ')

    if n.lower() == 'y':
        print('\n============= isi kembali angka anda =============: \n')
        pass

    elif n.lower() == 'x':
        print('\n============Selesai, sampai jumpa1=================')
        break

    else:
        while n.lower() != 'x':
            n = input('keyword anda salah, ketik (y) atau (x): ')
            if n.lower() == 'y':
                print('\n============= isi kembali angka anda =============: \n')
                break
        else:
            print('\n============Selesai, sampai jumpa2=================')
            break
