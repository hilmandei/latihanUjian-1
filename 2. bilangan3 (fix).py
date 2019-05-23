def bilangan(angka1):
    try:
        if isinstance(int(angka1), int):
            list1 = []
            angka2 = int(angka1)
            if angka2 <= 0 or angka2 > 0:
                list1.append('Bulat')
                if angka2 >= 0:
                    list1.append('Cacah')
                    if angka2 == 0:
                        list1.append('Nol')
                        list1.append('Genap')
                    elif angka2 > 0:
                        list1.append('Bilangan Asli')
                        if angka2 % 2 != 0 and angka2 > 0:
                            list1.append('Ganjil')
                        elif angka2 % 2 == 0 and angka2 >= 0:
                            list1.append('Genap')

                        list2 = []
                        for x in range(1, angka2 + 1):
                            if angka2 % x == 0 and angka2 > 1:
                                list2.append(x)
                        if len(list2) == 2:
                            list1.append('Prima')
                        elif len(list2) > 2:
                            list1.append('Komposit')

                elif angka2 < 0:
                    list1.append('Negatif')

            return list1

    except ValueError:
        print('------ Maaf, yg anda input salah ------')



n = 'y'

while n == 'y':
    angka = input('Masukkan angka luar while: ')

    while bilangan(angka) is None:
        angka = input('Masukkan angka dlm while: ')

    else:
        print('Jadi %s adalah bilangan : \n%s' % (angka, bilangan(angka)))

    n = input('\nketik (y) untuk lanjut, ketik (x) untuk keluar : ')

    if n.lower() == 'y':
        print('\n============= isi kembali angka anda =============: \n')
        pass

    elif n.lower() == 'x':
        print('\n=============Selesai, Sampai jumpa=================')
        break

    else:
        while n.lower() != 'x':
            n = input('keyword anda salah, ketik (y) atau (x): ')
            if n.lower() == 'y':
                print('\n============= isi kembali angka anda =============: \n')
                break
        else:
            print('\n=============Selesai, Sampai jumpa=================')
            break