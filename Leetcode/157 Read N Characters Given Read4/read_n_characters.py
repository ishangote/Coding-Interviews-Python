def read4(buf4):
    pass


def read_n_characters(buf, n):
    characters_read = 0
    read4_characters = 4
    buf4 = [""] * 4

    while characters_read < n and read4_characters == 4:
        read4_characters = read4(buf4)

        for idx in range(read4_characters):
            if characters_read == n:
                return characters_read

            buf[characters_read] = buf4[idx]
            characters_read += 1

    return characters_read
