
import re
from HTMLParser import HTMLParser


pattern = re.compile(r"\<[^>]+?\>")
h = HTMLParser()


def strip_tags(html):
    return pattern.sub("", html)


def handle_html_entities(raw):
    return h.unescape(raw)


def format(raw):
    return handle_html_entities(strip_tags(raw))


if __name__ == "__main__":
    import sys
    fpath = sys.argv[1]
    content = open(fpath, "r").read()
    with open(fpath, "w") as outf:
        outf.write(format(content))
