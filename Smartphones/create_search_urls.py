f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/s?k=smartphones&i=electronics&ref=nb_sb_noss'
f.write(url)
f.write('\n')


for i in range(2,77):
    url = 'https://www.amazon.de/-/en/s?k=smartphones&i=electronics&page=' + str(i) + '&qid=1625656650&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()