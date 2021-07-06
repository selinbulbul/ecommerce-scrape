f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/s?k=DSLR+Cameras'
f.write(url)
f.write('\n')


for i in range(2,21):
    url = 'https://www.amazon.de/-/en/s?k=DSLR+Cameras&page=' + str(i) + '&qid=1625555168&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()