# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

# Пример входного файла:
# ab
# c
# dde
# ff

# Пример выходного файла:
# ff
# dde
# c
# ab




with open("dataset_24465_4.txt") as file:
    words_list = file.read().strip()
    words_list = words_list.splitlines()
    words_list.reverse()

with open("dataset_24465_4.txt", "w") as file:
    new_list = "\n".join(words_list)
    file.write(new_list)
