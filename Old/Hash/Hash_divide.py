def hash(object, returnstr=False):
    res = [0 for i in range(len(object))]
    for i in range(len(object)):
        res[i] = object[i] % len(object)

    return ''.join(map(lambda d: str(d), res)) if returnstr else res


a = [11, 122, 123, 154, 15, 217, 1, 1, 1, 1, 1]

if __name__ == '__main__':
    print(hash(a,returnstr=False))
