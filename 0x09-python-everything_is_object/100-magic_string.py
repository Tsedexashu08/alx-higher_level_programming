#!/usr/bin/python3
# 100-magic_string.py
# Tsedalu Ashenafi <Tsedexashu08@github.com>

def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("Holberton, " * (magic_string.n - 1) + "Holberton")
