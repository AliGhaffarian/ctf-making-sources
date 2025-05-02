# my opinion about the challenge
this challenge was such a good idea, yet the xor key can be bruteforced.  
still a good challenge for one of my firsts  

# the intended solution
the player should use the time that flag.enc was last modified for making the xor key and restore the flag from flag.enc.

```python
timestamp = 1729323140
timestamp = (timestamp // 1000) * 1000
timestamp = timestamp & 0b11111111
flag = open("./flag.enc", "rb").read()

flag = bytearray(flag)
flag.reverse()

for byte in flag:
    ch = byte ^ timestamp
    print(chr(ch), end = "")
print()
print(timestamp)
```
