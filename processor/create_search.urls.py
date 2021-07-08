f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/s?k=processor&i=computers&ref=nb_sb_noss_2'
f.write(url)
f.write('\n')


for i in range(2,72):
    url = 'https://www.amazon.de/-/en/s?k=processor&i=computers&page=' + str(i) + '&qid=1625731797&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')
f.close()
