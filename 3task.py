
file_paths = ['1.txt', '2.txt', '3.txt']
file_data = {}

for file_path in file_paths:
    with open(file_path, encoding='utf-8') as f:
        lines = f.readlines()
        file_name = file_path
        line_count = len(lines)
        file_data[file_path] = {'name': file_name, 'lines': line_count, 'content': lines}


sorted_files = sorted(file_data.items(), key=lambda x: x[1]['lines'])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, file_info in sorted_files:
        result_file.write(file_info['name'] + '\n')
        result_file.write(str(file_info['lines']) + '\n')
        result_file.writelines(file_info['content'])
        result_file.write('\n')

print("Готово. Результат записан в файл 'result.txt'.")
