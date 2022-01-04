def find_words_by_mask(path, mask):

    with open(path, encoding='utf-8') as f:
        words = f.read().replace('\n', '').split(' ')
        lengths = list(map(lambda x : len(x), words))

        matching_indexes = [x for x in range(len(lengths)) if lengths[x:x+len(mask)] == mask]


        return words[matching_indexes[0]:matching_indexes[0] + len(mask)] if len(matching_indexes) > 0 else []
