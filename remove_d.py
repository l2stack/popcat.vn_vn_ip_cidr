def remove_duplicates(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        unique_lines = list(dict.fromkeys(line.strip() for line in lines))  # Loại bỏ trùng lặp và giữ thứ tự
    with open(input_file, 'w') as f:
        for line in unique_lines:
            f.write(line + '\n')
input_file = 'ipv4.cidr'
remove_duplicates(input_file)