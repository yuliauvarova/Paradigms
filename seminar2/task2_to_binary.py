def to_binary(number):
    str_bin_res = ""
    while number >= 1:
        bin_res = int(number % 2)
        number = number / 2
        str_bin_res += str(bin_res)
    return str_bin_res[::-1]


print(to_binary(6))


