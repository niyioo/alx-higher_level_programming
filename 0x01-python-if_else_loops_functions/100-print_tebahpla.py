#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(
        chr(i).lower() if (ord('z') - i) % 2 == 0 else chr(i).upper()),
        end=''
    )
