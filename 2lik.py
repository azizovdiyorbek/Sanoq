# 10-lik sanoq sistemasidan 2-likka o'tish
def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

# Test
num = 42
print(f"10-likda: {num}, 2-likda: {decimal_to_binary(num)}")
