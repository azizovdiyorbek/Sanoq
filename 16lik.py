# 10-lik sanoq sistemasidan 16-likka o'tish
def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:]

# Test
num = 42
print(f"10-likda: {num}, 16-likda: {decimal_to_hexadecimal(num)}")
