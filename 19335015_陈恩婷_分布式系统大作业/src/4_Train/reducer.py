import sys

current_label = None
curr_count = 0
curr_tf_idf = 0
label = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    label, tf_idf = line.strip().split('\t', 1)
    tf_idf = float(tf_idf)
    label = int(label)

    dim = len(tf_idf)
    if current_label != label:
        if current_label is not None:
            # write result to STDOUT
            print(f'{current_label}\t{[curr_tf_idf[i] / curr_count for i in range(dim)]}')
        current_label = label
        curr_count = 0
        curr_tf_idf = [0] * dim
    
    # update current_label and current_count
    curr_count += 1
    curr_tf_idf = [curr_tf_idf[i] + tf_idf[i] for i in range(dim)]

# do not forget to output the last word if needed!
if current_label == label:
    # write result to STDOUT
    print(f'{current_label}\t{[curr_tf_idf[i] / curr_count for i in range(dim)]}')