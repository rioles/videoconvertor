#!/usr/bin/env python
from os import getenv
def test_en():
    name = getenv('name')
    print(name)
    return f"my name {name}"

if __name__=="__main__":
    print(test_en())
