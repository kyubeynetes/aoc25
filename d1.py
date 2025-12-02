def get_pw(filename) -> int:
    ptr = 50
    times = 0
    with open(filename) as file:
        for line in file:
            op = line[0]
            num = int(line[1:])
            if op == "R":
                ptr = (ptr + num) % 100
            if op == "L":
                ptr = (ptr - num) % 100
            if ptr == 0:
                times += 1
    return times

def get_pw_spin(filename) -> int:
    ptr = 50
    times = 0
    with open(filename) as file:
        for line in file:
            op = line[0]
            num = int(line[1:])
            if op == "R":
                while num > 0:
                    ptr += 1
                    ptr %= 100
                    if ptr == 0:
                        times += 1
                    num -= 1
            if op == "L":
                while num > 0:
                    ptr -= 1
                    ptr %= 100
                    if ptr == 0:
                        times += 1
                    num -= 1
    return times

if __name__ == "__main__":
    filename = "./d1i.txt"
    pw = get_pw(filename)
    print(pw)
    pw_spin = get_pw_spin(filename)
    print(pw_spin)
