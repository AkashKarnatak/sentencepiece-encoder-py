import sentencepiece_model_pb2 as spm

model = spm.ModelProto()

with open('../xlnet-base-cased-spiece.model', 'rb') as f:
    model.ParseFromString(f.read())

s = 'today is a great day'
s = '▁' + s.replace(' ', '▁')

scores = [float('inf')] * len(s)
ranges = [(i, i) for i in range(len(s))]

vocab = {x.piece: x.score for x in model.pieces}

# viterbi forward
for eos in range(len(s)):
    for bos in range(eos + 1):
        substr = s[bos:eos+1]
        if substr not in vocab:
            continue

        curr = -vocab[substr]
        if bos > 0:
            curr += scores[bos-1]
        if curr < scores[eos]:
            scores[eos] = curr
            ranges[eos] = (bos, eos)

# viterbi backward
best_split = []
i = len(s) - 1
while i >= 0:
    bos, eos = ranges[i]
    best_split.append(s[bos: eos+1])
    i = bos-1
best_split.reverse()

print(best_split)
