from collections import namedtuple

# Basic usage
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # Output: 1 2


# advance level
from collections import namedtuple

Employee = namedtuple('Employee', ['id', 'name', 'role'])
e = Employee(1, 'Alice', 'Engineer')
print(e.id, e.name, e.role)  # Output: 1 Alice Engineer
