immutable_var = ('home', 2025, True)
print(immutable_var)
# immutable_var[1] = 2026 # в кортежах нельзя изменять элементы списка.
                          # Однако можно изменить содержимое элемента (если он содержит изменяемый объект)
mutable_list = [13, 9, 1987, 'sun']
mutable_list[0 : 4] = 21, 2, 1952, 'moon'
print(mutable_list)