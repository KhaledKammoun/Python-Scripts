import re

def sort_text_file(input_file, output_file):
    # Read lines from the input file
    with open(input_file, 'r') as f:
        lines = f.read()
        lines = re.findall(r'\([^)]+\)', lines)
    # Sort the lines based on the key (assuming key is the first element inside parentheses in each line)
    for i in range(len(lines)) :
        values = lines[i].strip('()').split(',')

        lines[i] = tuple(values)

    
    sorted_lines = sorted(lines, key=lambda line: int(line[0]) if line[0].isdigit() else -1 )
    sorted_lines = [line for line in sorted_lines if line != -1 and "" not in line]

    dic = dict()
    for line in sorted_lines :
        if (len(line) in dic) :
            dic[len(line)]+=1
        else :
            dic[len(line)] = 1
    for key, value in dic.items() :
        print(key, value)
    x_sorted_lines = [line for line in sorted_lines if line != -1]
    # print(len(sorted_lines) - len(x_sorted_lines))
    # print(sorted_lines)
    # Write the sorted lines to the output file
    # with open(output_file, 'w') as f:
    #     f.write(','.join(sorted_lines))

# Example usage:
input_file_path = 'input.txt'  # Path to your input text file
output_file_path = 'sorted_output.txt'  # Path to the sorted output text file

sort_text_file(input_file_path, output_file_path)
