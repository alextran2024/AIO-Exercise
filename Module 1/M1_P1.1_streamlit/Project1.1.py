# Word correction

# mở và lấy từ vựng từ đường dẫn trên máy:

import streamlit as st


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(
    file_path='/Users/trantrang/Desktop/GIT-AIO/AIO-Exercise/Module 1/source/data/vocab.txt')

# tính khoảng cách levenshtein:

# định nghĩa khoảng cách ban đầu


def initialize_distances(len1, len2):
    distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for t1 in range(len1 + 1):
        distances[t1][0] = t1
    for t2 in range(len2 + 1):
        distances[0][t2] = t2
    return distances

# tinh chi phi giữa 2 khoảng cách khi chỉnh sửa


def calculate_cost(token1, token2, t1, t2):
    return 0 if token1[t1 - 1] == token2[t2 - 1] else 1


def update_distances(distances, token1, token2):
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            cost = calculate_cost(token1, token2, t1, t2)
            distances[t1][t2] = min(distances[t1 - 1][t2] + 1,       # Deletion
                                    distances[t1][t2 - 1] + \
                                    1,       # Insertion
                                    distances[t1 - 1][t2 - 1] + cost)  # Substitution
    return distances


def distance(token1, token2):
    distances = initialize_distances(len(token1), len(token2))
    distances = update_distances(distances, token1, token2)
    return distances[-1][-1]


# sử dụng streamlit


def main():
    st.title("Word correction using Levenshtein Distance")
    word = st.text_input("Word:")
    if st.button("Correct"):

        # tinh khoang cach:
        distances = {vocab: distance(word, vocab) for vocab in vocabs}

        # sắp xếp lại khoảng cách:
        sorted_distances = dict(
            sorted(distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write("Correct word: ", correct_word)

        col1, col2 = st.columns(2)
        col1.write("Vocabulary: ")
        col1.write(vocabs)
        col2.write("Distance")
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
