import numpy as np 

labels = [
    'comp:apis',
    'comp:autograph',
    'comp:cloud',
    'comp:core',
    'comp:signal',
    'comp:tensorboard',
    'comp:tf.function',
    'comp:tfdbg',
    'comp:tpus',
    'comp:xla'
    ]

for i in range(len(labels)):
    label_dict = {
        labels[i] : i
    }

word_index_dict = {}
word_count_dict = {}
word_list = []
with open("part-00000",'r') as fp:
    for i, line in enumerate(fp.readlines()):
        word, count = line.strip().split('\t', 1)
        word_count_dict[word] = int(count)
        word_index_dict[word] = i        
        word_list.append(word)

dataset = {x:[] for x in range(len(labels))}

with open('issue_titles-1.txt', 'r') as fp:
    lines = fp.readlines()
    
    idf = np.zeros(len(word_list))

    for i in range(len(word_list)):
        idf[i] = np.log2(len(lines) / (word_count_dict[word_list[i]] + 1))

    for i, line in enumerate(lines):
        tf = np.zeros(len(word_list))
        # print(line)
        label, sentence = line.strip().split('\t', 1)
        words = sentence.split()

        for word in words:
            tf[word_index_dict[word]] += 1
        
        tf /= len(words)

        dataset[label_dict[label]].append((tf*idf, sentence))

with open('TF-IDF_train', 'w') as fp:
    for label, sentences in dataset.items():
        for x in sentences:
            fp.write(f'{label}\t{x[0].tolist()}\n')

with open('TF-IDF_test', 'w') as fp:
    for label, sentences in dataset.items():
        for x in sentences:
            fp.write(f'{label}\t{x[0].tolist()}\t{x[1]}\n')
