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

class_proto = {}
with open("part-00000") as fp:
    lines = fp.readlines()
    for line in lines:
        label, proto = line.strip().split('\t', 1)
        class_proto[int(label)] = np.array(eval(proto))

# (total, accuracy)
result = {x : [0,0] for x in labels}
with open("TF-IDF_test") as fp:
    for line in fp.readlines():
        label_idx, test_vec, sentence = line.strip().split('\t', 2)
        label_idx, test_vec = int(label_idx), np.array(eval(test_vec))

        dist = []
        max_dist, max_label = -np.inf, None
        for u, v in class_proto.items():
            cosine = np.dot(test_vec, v)/(np.linalg.norm(test_vec)*(np.linalg.norm(v)))
            dist.append(cosine)
            
            if cosine > max_dist:
                max_dist, max_label = cosine, u

        label = labels[label_idx]
        # 判断测试是否正确
        if max_label == label_idx:
            result[label][1] += 1
        # print(label)
        # print(dist[label_idx])
        # print(labels[max_label])
        # print(dist[max_label])
        # print(sentence)
        # print(f'{label} {dist[label_idx]} | {labels[max_label]} {dist[max_label]} | {sentence}')
        result[label][0] += 1

for u, v in result.items():
    print(f'{u} | Total: {v[0]} | Correct: {v[1]} | Accuracy: {v[1] / v[0]}')
