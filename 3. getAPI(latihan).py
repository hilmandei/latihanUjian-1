#membuat GET API - input pemain - result (Nama team)


import requests
import json

while True:
    print('Selamat datang, mau tahu berita apa hari ini?\n'
          '[1] Berita seputar teknologi\n'
          '[2] Berita seputar bisnis\n'
          '[3] Berita seputar olahraga\n'
          '[4] Berita seputar kesehatan\n'
          '[5] Berita seputar science')

    nama = input('Ketik pilihan Anda [1/2/3/4/5] : ')
    nama1 = ''

    if int(nama) in range(6):
        if nama == '1':
            nama1 = 'technology'

        elif nama == '2':
            nama1 = 'business'

        elif nama == '3':
            nama1 = 'sports'

        elif nama == '4':
            nama1 = 'health'

        elif nama == '5':
            nama1 = 'science'
    else:
        print('Tidak ada pada pilihan \n')
        continue

    print(nama1)

    url = 'https://newsapi.org/v2/top-headlines?country=id&category=' + nama1 + '&apiKey=dc26aae874584efe9fd74b443d2e25c8'
    tekno = requests.get(url)
    teknoxx = tekno.json()['articles']


    # print(teknoxx)
    # print(type(teknoxx))
    print()
    cc = 1
    for x in teknoxx:
        if cc <= 5:
            print(cc, x['title'])

        cc = cc + 1

    print('\n---------------------------------------------------------------------------\n')








