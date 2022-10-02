import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    word, count = line.strip().split('\t', 1)

    # convert count (currently a string) to int
    count = int(count)
    # this IF-switch only works because Hadoop sorts map output
    if current_word != word:
        # write result to STDOUT
        if current_word is not None:
            print(f'{current_word}\t{current_count}')
        # start over
        current_word = word
        current_count = 0
    # update current_word and current_count
    current_count += count

# do not forget to output the last word if needed!
if current_word == word:
    print(f'{current_word}\t{current_count}')