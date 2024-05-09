def justify_paragraph(paragraph, paragraph_width):
    words = paragraph.split()
    lines = []
    current_line = []

    for word in words:
        if len(' '.join(current_line + [word])) <= paragraph_width:
            current_line.append(word)
        else:
            lines.append(current_line)
            current_line = [word]
    
    if current_line:
        lines.append(current_line)

    justified_lines = []
    for line in lines:
        spaces_to_add = paragraph_width - sum(len(word) for word in line)
        num_gaps = len(line) - 1
        if num_gaps > 0:
            spaces_per_gap = spaces_to_add // num_gaps
            extra_spaces = spaces_to_add % num_gaps
            justified_line = ''
            for i, word in enumerate(line):
                justified_line += word
                if i < num_gaps:
                    justified_line += ' ' * spaces_per_gap
                    if extra_spaces > 0:
                        justified_line += ' '
                        extra_spaces -= 1
        else:
            justified_line = line[0] + ' ' * spaces_to_add
        justified_lines.append(justified_line)

    return justified_lines

# Sample input
paragraph = input("Enter paragraph data ")
paragraph_width = int(input("enter paragraph width"))

# Output
print(justify_paragraph(paragraph, paragraph_width))
