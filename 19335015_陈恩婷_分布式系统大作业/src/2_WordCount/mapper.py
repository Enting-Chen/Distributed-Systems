import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    label, sentence = line.strip().split('\t', 1)

    # split the line into words
    words = sentence.split()

    for word in words:
        # write the results to STDOUT (standard output);
        print(f'{word}\t{1}')
