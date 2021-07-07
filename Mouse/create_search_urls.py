f = open('search_urls.txt', 'w+')
url = 'https://www.amazon.de/s?k=mouse+pc&i=computers&crid=1HAHDV24TKVYT&sprefix=mouse+pc%2Ccomputers%2C197&ref=nb_sb_ss_ts-doa-p_1_8'
f.write(url)
f.write('\n')


for i in range(2,73):
    url = 'https://www.amazon.de/-/en/s?k=mouse+pc&i=computers&page=' + str(i) + '&crid=1HAHDV24TKVYT&qid=1625656402&sprefix=mouse+pc%2Ccomputers%2C197&ref=sr_pg_' + str(i)
    f.write(url)
    f.write('\n')

f.close()