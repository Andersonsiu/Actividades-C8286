from concurrent.futures import ThreadPoolExecutor, as_completed

def map_function(log_fragment):
    return [line for line in log_fragment if "ERROR" in line]

def reduce_function(mapped_data):
    return [line for sublist in mapped_data for line in sublist]

def read_log_file(file_path, chunk_size=1024):
    with open(file_path, 'r') as f:
        while True:
            lines = f.readlines(chunk_size)
            if not lines:
                break
            yield lines

def process_logs_in_parallel(log_file_path, num_workers=4):
    log_fragments = read_log_file(log_file_path)
    results = []
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        future_to_fragment = {executor.submit(map_function, fragment): fragment for fragment in log_fragments}
        for future in as_completed(future_to_fragment):
            results.append(future.result())
    combined_results = reduce_function(results)
    return combined_results

if __name__ == "__main__":
    log_file_path = 'large_log_file.log'
    processed_logs = process_logs_in_parallel(log_file_path)
    for log in processed_logs:
        print(log)
