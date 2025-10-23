"""
Додаткові виконані завдання (окрім основних): 
- створив допоміжну функцію для розділення завдань;
- створив змінні для зручного викорстання кольорів через форматовані рядки
- додав кольори й форматування у завдання
- використав type annotation для більш зручного й зрозумілого читання коду
- вирівняв значення у таблиці завдяки < й > (right & left align)
"""

def separate_tasks():
    print('-'*32)

# стилі
reset: str = '\033[0m'
bold: str = '\033[1m'
dim: str = '\033[2m'
italic: str = '\033[3m'
underline: str = '\033[4m'
blink: str = '\033[5m'
inverse: str = '\033[7m'
hidden: str = '\033[8m'

# кольори
black: str = '\033[30m'
red: str = '\033[31m'
green: str = '\033[32m'
yellow: str = '\033[33m'
blue: str = '\033[34m'
magenta: str = '\033[35m'
cyan: str = '\033[36m'
white: str = '\033[37m'

# --- Завдання 1
separate_tasks()

print(f"""
To be, {red}or not{reset} to be: that is the question:
{italic}Whether {yellow}'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them?
{bold}William Shakespeare{reset}
""")

# Додатково: зробив додаткові форматування текстів (italic, bold)

# --- Завдання 2
separate_tasks()

breed: str = 'ротвейлер'
phone: str = '123-456-78-90'
items: dict[str, int] = {
    'Маська (7 місяці)': 2720,
    'Буся (3 роки)': 950,
    'Аля (5 місяців)': 1950,
    'Туля (4 роки 2 місяці)': 1960
}

print(f"""
{bold}Продам цуценят.{reset}
Порода: {yellow}{breed}{reset}
{'.'*12}
{underline}Тел.: {phone}{reset}

{"\n".join(f"| {italic}{name:<25}{reset} |{yellow}{price:>6} грн.{reset} |" for name, price in items.items())}
""")

"""
Тут трохи не зрозумів початкове завдання, тож виконав творче.
Додатково: зробив повне налаштування породи, номеру телефону, цін, 
  товарів (таблиця), автоматичне вирівняння таблиці завдяки 
  < (left-align) та > (right-align), додав кольори, тощо.
"""

# --- Завдання 3
separate_tasks()

print(f'\n{red}a', 'b', f'c{reset}', sep='*')

print(f'{green}d', 'e', f'f{reset}', sep='**', end='')
print(f'{green}g', 'h', f'i{reset}', sep='+', end='%')
print(f'{green}j', 'k', f'l{reset}', sep='-')

print(f'{yellow}m', 'n', f'o{reset}', sep='/', end='!')
print(f'{yellow}p', 'q', f'r{reset}', sep='1', end='%')
print(f'{yellow}s', 't', f'u{reset}', sep='&')

print(f'{blue}v', 'w', f'x{reset}', sep='%')

print(f'{magenta}y', f'z{reset}', sep='/', end='!\n\n')

# Додатково: кожен рядок (окрім сепараторів) має свій кольор

# ---
separate_tasks()