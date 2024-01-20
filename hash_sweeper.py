import os
import sys

def get_file_names(path):
    try:
        file_names = os.listdir(path)
        return [os.path.join(path, file_name) for file_name in file_names]
    except OSError as e:
        print(f"Error {e}")
        return []
        
def get_bad_hashes(path):
    bad_hashes = set()

    try:
        with open(path, 'r') as file:
            for line in file:
                hash_value = line.strip()
                bad_hashes.add(hash_value)
    except FileNotFoundError:
        print(f"File {path} not found")
    except Exception as e:
        print(f"Error {e}")

    return bad_hashes

def count_bad_hashes(files, bad_hashes):
    file_ioc_count = {}

    # Initialise ioc count to 0 for each file
    for file in files:
        file_ioc_count[file] = 0

    for bad_hash in bad_hashes:
        for file in files:
            if bad_hash in open(file).read():
                file_ioc_count[file] += 1

    # Sort before returning results
    return dict(sorted(file_ioc_count.items(), key=lambda item: item[1], reverse=True))

def display_results(ioc_counts):
    for file, count in ioc_counts.items():
        print(f"File: {file} | IOC count: {count}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_sweeper.py <directory> <hash_file>")
        sys.exit(1)

    files = get_file_names(sys.argv[1])
    bad_hashes = get_bad_hashes(sys.argv[2])
    ioc_counts = count_bad_hashes(files, bad_hashes)
    display_results(ioc_counts)

if __name__ == "__main__":
    main()
