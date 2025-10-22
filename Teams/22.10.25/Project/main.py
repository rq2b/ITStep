# ---


var_int: int = 0
var_float: float = 0.11
var_string: str = 'string'
var_bool: bool = True
var_tuple: tuple[int, float, str, bool] = (var_int, var_float, var_string, var_bool)
var_list: list[int, float, str, bool] = [var_int, var_float, var_string, var_bool]
var_set: set[int, float, str, bool] = {var_int, var_float, var_string, var_bool}


# ---


print(f"{22} Жовтня {2025}р. // Середа")
print(22, 10, 25, sep='.', end='р. \n')
print('Перша мова - Python')

temp_var: str = 'test'
print('.'.join(temp_var))

temp_list: list[int, float, str, bool] = [var_int, var_float, var_string, var_bool]
temp_list = [str(item) for item in temp_list]
print(' // '.join(temp_list))

print('Чудово')


# ---

""" to be or not to be variations
print("To be\nor not\nto be.") # variant #1
print("To be", "or not", "to be.", sep='\n')  # variant #2
print('\n'.join(f"{item}" for item in ["To be", "or not", "to be."]))  # variant #3
"""

# ---
""" \r character example
print("Python.\r012")

Надрукувало Python, далі \r перейшов назад до 
початку строки й переписав її початок на 012.
Результат: 012hon.
"""

# ---

""" char definitions
\t - tab
\f - diagonal offset to the right from the previous line
\n - next line
\r - move the carriage to the start of the line
"""

# ---

""" task template
Life is what happens when you're busy making other plans. 
John Lennon
"""

# print("\t\"Life is what happens\fwhen\fyou're busy making other plans\"\fJohn Lennon")

# ---