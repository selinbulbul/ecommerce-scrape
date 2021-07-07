f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/s?k=DSLR&i=electronics&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')


for i in range(2,70):
    url = 'https://www.amazon.de/-/en/s?k=DSLR&i=electronics&page=' + str(i) + '&qid=1625668687&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()