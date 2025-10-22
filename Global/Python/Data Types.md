```python
# data types

var_int: int = 0
var_float: float = 0.11
var_string: str = 'string'
var_bool: bool = True
var_tuple: tuple[int, float, str] = (var_int, var_float, var_string)
var_list: list[int,  float,  str,  bool] = [var_int, var_float, var_string, var_bool]
var_set: set[int,  float,  str,  bool] = {var_int, var_float, var_string, var_bool}
var_dict: dict[str, Any] = {'num': var_int, 'pi': var_float, 'text': var_string, 'flag': var_bool}
var_frozenset: frozenset[int,  float,  str] = frozenset([var_int, var_float, var_string])
var_bytes: bytes = b'example'
var_bytearray: bytearray = bytearray(b'example')
var_none: None = None
```

There exist many data types & data structures in Python, and the main are:
- integers (_int_) (0, 1, 2..) - whole numbers
- floats (_float_) (0.1, 0.23, 0.445..) - numbers with floating points
- string (_str_) ('string', 'another string', 'text'..) - strings of any text / characters
- booleans (_bool_) (True, False, True..) - values that are either True or False
- tuples (_tuple_) ((0, 0.1, 'text')..) - non-modifiable data structures with fast properties (static)
- lists (_list_) ([0, 0.1, 'text']..) - modifiable data structures, like tuples but slower due to modification properties
- sets (_set_) ({0, 0.1, 'text'}..) - unordered collections of completely unique elements, good for checking the existence of an element
- dictionaries (_dict_) ({'key': 'value', 'another_key': 123}..) - collections of key-value pairs; keys must be unique with any value correspondent to the keys
- frozensets (_frozenset_) (frozenset([0, 1, 2])..) - immutable version of a set; can be used as dictionary keys or set elements
- bytes (_bytes_) (b'example', b'\x00\x01'..) - immutable sequence of bytes; used for binary data
- bytearray (_bytearray_) (bytearray(b'example')..) - mutable sequences of bytes; similar to bytes but modifiable
- NoneType (_None_) - a special type representing the absence of a value

---

Related:
[[Static Type Annotation]]