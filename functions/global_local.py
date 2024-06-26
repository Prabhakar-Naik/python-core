

def local_scope():
    x = 10  # Local variable
    print(f"Inside function: {x}")


local_scope()


x = 20  # Global variable

def global_scope():
    print(f"Inside function: {x}")

global_scope()
print(f"Outside function: {x}")

