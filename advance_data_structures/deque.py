from collections import deque

# Basic usage
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # Output: deque([0, 1, 2, 3, 4])


# advance level
def process_tasks(tasks):
    task_queue = deque(tasks)
    while task_queue:
        task = task_queue.popleft()
        print(f"Processing task: {task}")

tasks = ['task1', 'task2', 'task3']
process_tasks(tasks)  # Output: Processing task: task1, Processing task: task2, Processing task: task3
