def xor(a, b):
    res = ""
    for i in range(len(a)):
        res += hex(int(a[i], 16) ^ int(b[i], 16))[2:]
    return res


a = input().strip()
b = input().strip()
c = input().strip()


result = xor(xor(a, b), c)
decoded_result = bytes.fromhex(result).decode('utf-8')

print(decoded_result)