
import os
from StringIO import StringIO

import common
common.prepare(use_proxy=False)


root = "http://m.gulongbbs.com"

if os.path.exists("book.htm"):
    lst = open("book.htm").read()
else:
    lst = common.simple_read(open("book.txt").read().strip())

beg = lst.index("<title>") + 7
end = lst.index('_', beg)
book_title = lst[beg:end]

beg = lst.index('table width="100%"', beg)
end = lst.index("</table>", beg)
lst = lst[beg:end]

chapters = []
beg = 0

while True:
    beg = lst.find("href", beg)
    if beg == -1:
        break

    beg += 6
    end = lst.index('"', beg)
    url = lst[beg:end]

    beg = lst.index("title", end) + 7
    end = lst.index('"', beg)
    title = lst[beg:end]

    chapters.append((title, root + url))

    beg = end

txt = book_title + "\n\n"

for title, url in chapters:
    raw = common.simple_read(url)

    beg = raw.index("<!--HTMLBUILERPART0-->") + 22
    end = raw.index("</span>", beg)

    txt += title + "\n\n"

    sio = StringIO(raw[beg:end].replace("<BR>", ""))
    for line in sio:
        txt += line.strip() + '\n'

    txt += '\n'

    print "Done crawling", title
    common.random_sleep(2)

with open(book_title + ".txt", "w") as outf:
    outf.write(txt)
