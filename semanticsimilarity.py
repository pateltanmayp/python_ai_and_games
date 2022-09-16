import numpy as np

def cosine_similarity(vec1, vec2):
    mag1, mag2, dot = 0, 0, 0
    for word, freq in vec1.items():
        mag1 += freq ** 2
    for word, freq in vec2.items():
        mag2 += freq ** 2
        if word in vec1.keys():
            dot += freq * vec1[word]
    return dot / np.sqrt(mag1 * mag2)

# Reduce the complexity (it's less than O(n^2) but still bad)
def build_semantic_descriptors(sentences):
    d = {}
    for sentence in sentences:
        for word in sentence:
            if word not in d.keys():
                d[word] = {}

    for sentence in sentences:
        for word in sentence:
            done = []
            for i in range(len(sentence)):
                if sentence[i] not in done and sentence[i] != word:
                    done.append(sentence[i])
                    d[word].update({sentence[i]:1 + d[word].get(sentence[i], 0)})
    return d

def build_semantic_descriptors2(sentences):
    d = {}
    for sentence in sentences:
        for word in sentence:
            if word not in d.keys():
                d[word] = {}

    for sentence in sentences:
        for word in sentence:
            done = []
            for i in range(len(sentence)):
                if sentence[i] not in done and sentence[i] != word:
                    done.append(sentence[i])
                    d[word].update({sentence[i]:1 + d[word].get(sentence[i], 0)})
    return d

def build_semantic_descriptors_from_files(filenames):
    sentences_ls = []
    for filename in filenames:
        text = open(filename, encoding="latin-1").read()
        sentences = text.replace("?", ".").replace("!", ".").lower().split(".")
        for sentence in sentences:
            temp_sentence = sentence.replace(",", " ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ").replace("\n", " ")
            sentences_ls.append(temp_sentence.split(" "))
    return build_semantic_descriptors(sentences_ls)

# When will it be impossible to compute semantic similarity btwn 2 words?
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    similarities = {}

    # Added if statement to check if [word] exists
    if word not in semantic_descriptors.keys():
        return choices[0]

    for choice in choices:
        # Added if statement to check if [choice] exists
        if choice in semantic_descriptors.keys():
            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
            similarities[choice] = similarity
        else:
            similarities[choice] = -1
    top_similarity = max(similarities.values())
    for choice, similarity in similarities.items():
        if similarity == top_similarity:
            return choice

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    text = open(filename, encoding="latin-1").read().split("\n")
    tot_tests = len(text)
    passed_tests = 0

    for line in text:
        words = line.split(" ")

        # Changed words[1:] to words[2:]...I think this is right, correct me if im wrong
        if most_similar_word(words[0], words[2:], semantic_descriptors, similarity_fn) == words[1]:
            passed_tests += 1
    return (passed_tests / tot_tests) * 100

if __name__ == "__main__":
    sentences = [["a", "bat", "flew"], ["a", "cat", "flew"]]
    print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
    print(build_semantic_descriptors(sentences))
    print("\n----")

    # Update with your paths/text file names
    data_paths = ["sample.txt", "sample2.txt"]
    test_path = "test.txt"
    descriptors = build_semantic_descriptors_from_files(data_paths)
    res = run_similarity_test(test_path, descriptors, cosine_similarity)
    print("Accuracy rate:", res)