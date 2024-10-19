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

