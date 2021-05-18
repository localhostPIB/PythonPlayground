def split_in_halves(l):
    middle = int(len(l) / 2)
    left_half = l[:middle]
    right_half = l[middle:]
    return left_half, right_half


left, right = split_in_halves([1, 2, 3, 4, 5, 6, 7])
print("links: ", left, "rechts: ", right)


# ******
n=50
test = bin(n)[2:]

len([int(x) for x in str(bin(n)[2:])])

def countBits(n):
    return a(n)()

def a(n):
    return len([int(x) for x in str(bin(n)[2:])])