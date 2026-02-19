seq_list = ["ATATACGCGTA", "CTTCGGNGA"]

for seq in seq_list:
    print("Последовательность целиком:", seq)
    print("Построчно:")
    for letter in seq:
        print(letter)
    print("-" * 20) 

print("Цикл выполнен")