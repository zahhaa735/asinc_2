import os
import threading


def search_files(extension, directories):
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    print(f"File found: {os.path.join(root, file)}")


def parallel_file_search(extension, directories):
    threads = []
    for directory in directories:
        thread = threading.Thread(target=search_files, args=(extension, [directory]))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


# For example
extension = ".png"
directories = ["/Users/oleksandrsynhaievskiy/Downloads"]
parallel_file_search(extension, directories)
