
# coding: utf-8


import httplib2

def test():
    resp, content = httplib2.Http().request("http://localhost:7474/db/data/")
    print resp, content
    return

test()

