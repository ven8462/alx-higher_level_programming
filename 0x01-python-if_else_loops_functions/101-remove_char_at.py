#!/usr/bin/python3

def remove_char_at(s, n):
    return "".join(s[i] for i in range(len(s)) if i != n)
