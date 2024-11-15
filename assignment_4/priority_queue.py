# Creating a class for task
class Task:
    def __init__(self, priority, taskId):
        self.priority = priority
        self.taskId = taskId


# Creating class for priorityqueue
class PriorityQueue:
    def __init__(self):
        # Using an array for the heap
        self.heap = []

    def insert(self, task):
        # adding and bubbling up
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def extract_max(self):
        # returning the max
        if self.is_empty():
            raise IndexError("Heap is empty")
        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        if not self.is_empty():
            self._bubble_down(0)
        return max_task

    def increase_key(self, task_index, new_priority):
        if new_priority <= self.heap[task_index].priority:
            raise ValueError("New priority must be higher")
        self.heap[task_index].priority = new_priority
        self._bubble_up(task_index)

    def is_empty(self):
        return len(self.heap) == 0

    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].priority > self.heap[parent_index].priority:
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )
                index = parent_index
            else:
                break

    def _bubble_down(self, index):
        length = len(self.heap)
        while index < length:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if (
                left_child_index < length
                and self.heap[left_child_index].priority > self.heap[largest].priority
            ):
                largest = left_child_index

            if (
                right_child_index < length
                and self.heap[right_child_index].priority > self.heap[largest].priority
            ):
                largest = right_child_index

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


# Example usage:
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task(priority=5, taskId=1))
    pq.insert(Task(priority=3, taskId=2))
    pq.insert(Task(priority=9, taskId=3))
    pq.insert(Task(priority=4, taskId=4))

    print("Extracted max:", pq.extract_max())
    print("Heap after extraction:", pq.heap)

    # Increase priority of a task
    pq.increase_key(1, 10)  # Increasing the priority of task at index 1 to 10
    print("Heap after increasing key:", pq.heap)

    # Check if the priority queue is empty
    print("Is heap empty?", pq.is_empty())
