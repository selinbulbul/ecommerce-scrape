f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/-/en/s?k=headphones&qid=1625650428&ref=sr_pg_1'
f.write(url)
f.write('\n')


for i in range(2,21):
    url = 'https://www.amazon.de/-/en/s?k=headphones&page=' + str(i) + '&qid=1625650460&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')
f.close()
