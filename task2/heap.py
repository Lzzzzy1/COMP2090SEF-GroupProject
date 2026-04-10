import random
import time

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def heap_sort(self):
        print("Original array (first 10):", self.heap[:10], "...")
        result = []
        temp = self.heap[:]
        step = 1
        
        while temp:
            self._heapify_down(0, temp)
            max_val = temp.pop(0)
            result.append(max_val)
            
            if step % 3 == 0 or len(temp) <= 8:
                print(f"Step {step:2d} | Extracted max: {max_val:3d} | Remaining: {len(temp):2d} | Last 5 sorted: {result[-5:]}")
                time.sleep(0.5)
            
            step += 1
        
        print("\n=== Sorting Completed! ===")
        print("Final sorted result (first 20):", result[:20])
        print("Final sorted result (last 20):", result[-20:])
        return result

    def _heapify_down(self, i, arr):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(arr)
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right
        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self._heapify_down(smallest, arr)

if __name__ == "__main__":
    print("=== Task 2: Heap Sort Visualization Demo (50 Random Numbers) ===\n")
    
    random.seed(42)
    data = [random.randint(1, 100) for _ in range(50)]
    
    print("Generated 50 random numbers:", data)
    print("-" * 70)
    
    h = Heap()
    for num in data:
        h.insert(num)
    
    h.heap_sort()
    
    print("\nHeap Sort demonstration completed!")
    input("\nPress Enter to exit...")
