# python-core

A comprehensive repository for learning and practicing core Python concepts — from basics to advanced topics, organized by category.

---

## Project Structure

```
python-core/
├── basic/                      # Python fundamentals
├── operators/                  # All operator types
├── conditions/                 # Conditional statements
├── loops/                      # Loop constructs
├── strings/                    # String operations & algorithms
├── collections/                # Lists, tuples, sets, dicts
├── data_structures/            # Comprehensions, slicing, stacks
├── advance_data_structures/    # deque, defaultdict, namedtuple, JSON/CSV
├── functions/                  # Functions, lambdas, scope
├── control_structures/         # Control flow, exceptions, match
├── exceptions/                 # Exception handling patterns
├── File_handling/              # File I/O operations
├── module_packages/            # Modules and packages
├── numerics/                   # Math and numeric functions
├── dsa/                        # Data structures & algorithms (CSV)
├── json_to_csv/                # JSON to CSV conversion utility
├── password-generator/         # Password generation scripts
├── advance_projects/           # Real-world mini projects
└── projects_mini/              # Fun mini projects (calculator, turtle)
```

---

## Modules

### `basic/`
Covers the very first steps in Python.

| File | Description |
|------|-------------|
| `hello_world.py` | First Python program |
| `declaration.py` | Variable declaration |
| `variables.py` | Variable usage and naming |
| `data_types.py` | int, float, str, bool, None |
| `numbers.py` | Number types and operations |
| `arithematic_operators.py` | Basic arithmetic |
| `fibinocci.py` | Fibonacci sequence |

---

### `operators/`
All Python operator types with examples.

| File | Description |
|------|-------------|
| `arithmetic_operators.py` | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| `comparison_operators.py` | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| `logical_operators.py` | `and`, `or`, `not` |
| `assignment_operators.py` | `=`, `+=`, `-=`, etc. |
| `bitwise_operators.py` | `&`, `\|`, `^`, `~`, `<<`, `>>` |
| `identity_operators.py` | `is`, `is not` |
| `membership_operators.py` | `in`, `not in` |
| `conditional_operators.py` | Ternary / conditional expressions |

---

### `conditions/`
Conditional logic and user input handling.

| File | Description |
|------|-------------|
| `if_conditions.py` | Basic `if` |
| `if_else_conditions.py` | `if-else` |
| `if_elif_else_conditions.py` | `if-elif-else` chains |
| `nested_if_conditions.py` | Nested conditionals |
| `ternary_if_condition.py` | One-liner conditionals |
| `user_input.py` | Reading and validating user input |

---

### `loops/`
Loop constructs in Python.

| File | Description |
|------|-------------|
| `basicloops.py` | Loop fundamentals |
| `forloop.py` | `for` loop with ranges and iterables |
| `whileloop.py` | `while` loop with conditions |

---

### `strings/`
String manipulation, algorithms, and built-in methods.

| File | Description |
|------|-------------|
| `lesson1.py` | String basics |
| `format_string.py` | f-strings and `.format()` |
| `reverse_string.py` | Reverse a string |
| `palindrome.py` | Palindrome check |
| `anagram_string.py` | Anagram detection |
| `capitalize_words.py` | Word capitalization |
| `convert_capital_string.py` | Case conversion |
| `first_non_repeat_char.py` | First non-repeating character |
| `frequent_chat_in_string.py` | Most frequent character |
| `vowels_in_string.py` | Count vowels |
| `remove_punctuation.py` | Strip punctuation |
| `remove_witespace_string.py` | Strip whitespace |
| `replace_sub_string.py` | Substring replacement |
| `split_string.py` | Splitting strings |
| `join_words_in_string.py` | Joining strings |
| `starts_with_ends_with.py` | `startswith` / `endswith` |
| `relate_functions.py` | Common string methods |

---

### `collections/`
Python built-in collection types.

| File | Description |
|------|-------------|
| `lists.py` | List basics |
| `list_program.py` | List programs |
| `tuples.py` | Tuple usage |
| `sets.py` | Set operations |
| `dictionaries.py` | Dictionary usage |

---

### `data_structures/`
Advanced usage of Python data structures.

| File | Description |
|------|-------------|
| `list_comprehence.py` | List comprehensions |
| `dictionary_comprehence.py` | Dict comprehensions |
| `list_functions.py` | `map`, `filter`, `sorted` |
| `list_slicing.py` | Slicing syntax |
| `list_stack.py` | Stack using list |
| `dictionary_methods.py` | Dict methods |
| `set_operations.py` | Union, intersection, difference |
| `tuples.py` | Tuple packing/unpacking |
| `merge_sorted.py` | Merge sorted lists |

---

### `advance_data_structures/`
Python's `collections` module and data handling.

| File | Description |
|------|-------------|
| `defaultdict.py` | `collections.defaultdict` |
| `deque.py` | `collections.deque` |
| `named_tuple.py` | `collections.namedtuple` |
| `data_manipulation.py` | Data transformation techniques |
| `json_parsing.py` | Parsing JSON data |
| `string_parsing_date_handling.py` | String and date parsing |

---

### `functions/`
Function definitions, arguments, and scope.

| File | Description |
|------|-------------|
| `define.py` | Defining and calling functions |
| `function_argument.py` | `*args`, `**kwargs`, defaults |
| `global_local.py` | Global vs local scope |
| `lambda_function.py` | Lambda expressions |

---

### `control_structures/`
Control flow, pattern matching, and exception-integrated I/O.

| File | Description |
|------|-------------|
| `conditions.py` | Conditional control flow |
| `loops.py` | Loop control (`break`, `continue`) |
| `control_flow_mechanisms.py` | Combined control flow |
| `match_statement.py` | Python 3.10+ `match` statement |
| `match_color.py` | `match` with color patterns |
| `exception_file_io.py` | Exceptions in file I/O |
| `exception_https.py` | Exceptions in HTTP requests |
| `exception_userinput.py` | Exceptions in user input |
| `advance_control_structures.py` | Advanced patterns |

---

### `exceptions/`
Exception handling patterns and custom exceptions.

| File | Description |
|------|-------------|
| `try_except_else_finally.py` | Full exception block |
| `multiple_exceptions.py` | Catching multiple exceptions |
| `custom_exceptions.py` | Defining custom exception classes |
| `validate_error_custom_exception.py` | Validation with custom exceptions |
| `file_operations.py` | Exception-safe file operations |

---

### `File_handling/`
Reading, writing, and managing files.

| File | Description |
|------|-------------|
| `open_close.py` | `open()` and `close()` |
| `write_read.py` | Write and read files |
| `appendmode.py` | Append to files |
| `with_statement.py` | Context manager (`with`) |
| `handling_exception.py` | Exception handling in file ops |
| `realtime_file_scenario.py` | Real-world file handling scenario |

---

### `module_packages/`
Creating and using Python modules and packages.

| File | Description |
|------|-------------|
| `greeting.py` | Simple module |
| `greeting_main.py` | Importing and using a module |
| `utils.py` | Utility functions module |
| `my_package/greet.py` | Package module |
| `my_package/greet1.py` | Package module variant |

---

### `numerics/`
Math operations and numeric utilities.

| File | Description |
|------|-------------|
| `math_module_functions.py` | `math` module — `sqrt`, `ceil`, `floor`, etc. |
| `numeric_functions.py` | Built-in numeric functions |

---

### `dsa/`
Data structures and algorithms with file-based data.

| File | Description |
|------|-------------|
| `data.csv` | Sample dataset |
| `data_read.py` | Reading and processing CSV data |

---

### `json_to_csv/`
Utility to convert JSON data to CSV format.

| File | Description |
|------|-------------|
| `input.json` | Sample JSON input |
| `converter.py` | Conversion logic |
| `output.csv` | Generated CSV output |

---

### `password-generator/`
Scripts to generate secure passwords.

| File | Description |
|------|-------------|
| `generate_password.py` | Core password generator |
| `sample_generator.py` | Sample usage |
| `python_console_clean.py` | Console output utilities |

---

### `advance_projects/`
Real-world Python utility scripts.

| File | Description |
|------|-------------|
| `calender-appointment.py` | Calendar and appointment management |
| `hostname_ip_address.py` | Fetch hostname and IP address |

---

### `projects_mini/`
Fun mini projects.

| File | Description |
|------|-------------|
| `calc.py` | Command-line calculator |
| `my_turtle_game.py` | Turtle graphics game |
| `turtle_india_map.py` | Draw India map using turtle |

---

## Requirements

- Python 3.10+ (required for `match` statement)
- No external dependencies for most modules
- `turtle` module — included in Python standard library

---

## Getting Started

```bash
git clone https://github.com/Prabhakar-Naik/python-core.git
cd python-core
python basic/hello_world.py
```

---

## Learning Path

1. `basic/` → `operators/` → `conditions/` → `loops/`
2. `strings/` → `collections/` → `data_structures/`
3. `functions/` → `control_structures/` → `exceptions/`
4. `File_handling/` → `module_packages/` → `advance_data_structures/`
5. `dsa/` → `json_to_csv/` → `advance_projects/` → `projects_mini/`
