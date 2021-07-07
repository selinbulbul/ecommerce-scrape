f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/s?k=headphones&i=electronics&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')


for i in range(2,75):
    url = 'https://www.amazon.de/-/en/s?k=headphones&i=electronics&page=' + str(i) + '&qid=1625672410&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')
f.close()
