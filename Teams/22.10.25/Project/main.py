# ---

""" static type annotation
var_int: int = 0
var_float: float = 0.11
var_string: str = 'string'
var_bool: bool = True
var_tuple: tuple[int, float, str, bool] = (var_int, var_float, var_string, var_bool)
var_list: list[int, float, str, bool] = [var_int, var_float, var_string, var_bool]
var_set: set[int, float, str, bool] = {var_int, var_float, var_string, var_bool}
"""

# ---

""" print functionality w/ sep=,  // .join() method
print(f"{22} Жовтня {2025}р. // Середа")
print(22, 10, 25, sep='.', end='р. \n')
print('Перша мова - Python')

temp_var: str = 'test'
print('.'.join(temp_var))

temp_list: list[int, float, str, bool] = [var_int, var_float, var_string, var_bool]
temp_list = [str(item) for item in temp_list]
print(' // '.join(temp_list))

print('Чудово')
"""

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

""" print with a custom separator
print('Python', end=f'\n{'='*6}\n') # Варіант 1 (end)
print('Python\n', '='*6, sep='') # Варіант 2 (sep)
"""

# ---

"""task template
Nothing will work unless you do
"""

"""
print('Nothing', 'will', 'work - ', sep='*', end='')
print('unless', 'you', 'do', sep='_')
"""

# ---

"""
print('Колір\n' + '\033[33m+'*5)
print('\033[0m') # reset color to defaults
print('Колір\n' + '\033[43m+'*5, end='')
print('\033[0m') # reset color to defaults
"""

# ---

# print(
# """
# |\   \\\\__     \033[34mo\033[0m
# | \_/    \033[32mo\033[0m \    \033[34mo\033[0m
# > _   (( <_  \033[34moo\033[0m
# | / \__+___/
# |/     |/
# """)

class Color:
    def __init__(self):
        self.green = '\033[32m'
        self.blue = '\033[34m'
        self.close_symbol = '\033[0m'

    def color_text(self, color, text):
        return f'{color}{text}{self.close_symbol}'

color = Color()

print(
fr"""
|\   \\\\__     {color.color_text(color.blue, 'o')}
| \_/    {color.color_text(color.green, 'o')} \    {color.color_text(color.blue, 'o')}
> _   (( <_  {color.color_text(color.blue, 'o')}
| / \__+___/
|/     |/
""")

# ---

