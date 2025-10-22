```python
# print functionality w/ sep=,  // .join() method

print(f"{22} Жовтня {2025}р. // Середа")
print(22, 10, 25, sep='.', end='р. \n')
print('Перша мова - Python')

temp_var: str = 'test'
print('.'.join(temp_var))

temp_list: list[int, float, str, bool] = [var_int, var_float, var_string, var_bool]
temp_list = [str(item) for item in temp_list]
print(' // '.join(temp_list))

print('Чудово')
```
![[1761147510.png]]

---

```python
# to be or not to be variations

print("To be\nor not\nto be.") # variant #1
print("To be", "or not", "to be.", sep='\n')  # variant #2
print('\n'.join(f"{item}" for item in ["To be", "or not", "to be."]))  # variant #3
```
![[1761147437.png]]

---

```python
# \r character example

print("Python.\r012")

Надрукувало Python, далі \r перейшов назад до 
початку строки й переписав її початок на 012.
Результат: 012hon.
```
![[1761147393.png]]

---

```python
# print with a custom separator

print('Python', end=f'\n{'='*6}\n') # Варіант 1 (end)
print('Python\n', '='*6, sep='') # Варіант 2 (sep)
```
![[1761149170.png]]

---

```python
"""task template
Nothing will work unless you do
"""

# task

print('Nothing', 'will', 'work - ', sep='*', end='')
print('unless', 'you', 'do', sep='_')
```
![[1761149579.png]]

---

Related:
[[Left & Right Align]]
[[Backslash Character Definitions]]
[[Data Types]]
[[Colored & Formatted Output]]
