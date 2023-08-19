# Custom Functions and Utilities

This folder contains a collection of custom Python functions and utility classes that you've created to enhance your programming tasks.

## Contents

- [new_range_generator.py](./new_range_generator.py): A sequence generator function similar to the built-in `range()` function. Generates a sequence of values with customizable start, end, and step.

<!-- Other Functions will coming Soon -->

## Usage

### new_range_generator.py

The `new_range` function generates a sequence of values similar to the built-in `range()` function.

```python
from new_range_generator import new_range

# Generate a sequence from 1 to 10 with a step of 2
for num in new_range(1, 10, 2):
    print(num)
