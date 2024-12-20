# 10-lik sanoq sistemasidan 8-likka o'tish
def decimal_to_octal(decimal_number):
    return oct(decimal_number)[2:]

# Test
num = 42
print(f"10-likda: {num}, 8-likda: {decimal_to_octal(num)}")
