f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/s?k=laptops&i=computers&ref=nb_sb_noss_1'
f.write(url)
f.write('\n')


for i in range(2,68):
    url = 'https://www.amazon.de/-/en/s?k=laptops&i=computers&page=' + str(i) + '2&qid=1625648739&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()