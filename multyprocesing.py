import multiprocessing


def count_even_numbers(numbers, queue):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    queue.put(count)


if __name__ == '__main__':

    numbers = ['Large list of numbers']

    split_index = len(numbers) // 2
    first_half = numbers[:split_index]
    second_half = numbers[split_index:]

    queue = multiprocessing.Queue()

    process1 = multiprocessing.Process(target=count_even_numbers, args=(first_half, queue))
    process2 = multiprocessing.Process(target=count_even_numbers, args=(second_half, queue))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    result1 = queue.get()
    result2 = queue.get()

    total_count = result1 + result2
    print("Number of even numbers in the list::", total_count)
