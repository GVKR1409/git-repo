import argparse

def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) <= width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word) + 1
    
    if current_line:
        lines.append(' '.join(current_line))

    justified_text = '\n'.join(lines)
    return justified_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Justify text to a specific width')
    parser.add_argument('text', nargs='?', type=str, help='Text to justify')
    parser.add_argument('width', nargs='?', type=int, help='Width to justify the text to')
    args = parser.parse_args()

    if not args.text or not args.width:
        text = input("Enter the text to justify: ")
        width = int(input("Enter the width: "))
    else:
        text = args.text
        width = args.width

    justified_text = justify_text(text, width)
    print(justified_text)
