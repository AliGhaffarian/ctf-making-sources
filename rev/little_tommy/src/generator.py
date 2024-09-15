flag="CTM{https://open.spotify.com/track/6Nx2v8RqzBZZicfvZStGep?si=8d60cb474c564139}"
read_fd=0
buffer_name="buff"
c_read_left=f"read({read_fd}, {buffer_name}, "
c_read_right=");"

for c in flag:
    print(c_read_left + str(ord(c)) + c_read_right)

    print("write(0, \"tommy: \", 7);" )
    print("write(1, buff, 2048);")
    print("write(1, \"\\n\", 1);")
    print("memset(buff, 0, 2048);")


