#1
import threading

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Thread function to check for primes in a subrange
def check_primes_in_range(start, end, result):
    for number in range(start, end):
        if is_prime(number):
            result.append(number)

# Main program
def main():
    start_range = 1
    end_range = 100
    num_threads = 4  # You can increase this to make it faster
    
    # Shared list to store results
    result = []

    # Create threads
    threads = []
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        # Calculate the start and end for each thread
        thread_start = start_range + i * step
        thread_end = start_range + (i + 1) * step if i != num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes_in_range, args=(thread_start, thread_end, result))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Sort and print the results
    result.sort()
    print("Prime numbers in range:", result)

main()

#2 
import threading
from collections import Counter
import os

# Function that counts words in a chunk of lines
def count_words(lines, counter, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().lower().split()
        local_counter.update(words)
    
    # Safely update the shared counter
    with lock:
        counter.update(local_counter)

def main():
    filename = "large_text_file.txt"  # Change to your actual file name
    num_threads = 4

    # Read all lines from the file
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Split lines into chunks for each thread
    chunk_size = len(lines) // num_threads
    threads = []
    counter = Counter()
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        thread_lines = lines[start:end]

        thread = threading.Thread(target=count_words, args=(thread_lines, counter, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Display results
    print("\n--- Word Count Summary ---")
    for word, count in counter.most_common(20):  # Show top 20 words
        print(f"{word}: {count}")  

if __name__ == "__main__":
    main()
