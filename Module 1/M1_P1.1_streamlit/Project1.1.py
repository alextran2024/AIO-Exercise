# Word correction

# mở và lấy từ vựng từ đường dẫn trên máy:

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readline()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(
    file_path='/Users/trantrang/Desktop/GIT-AIO/AIO-Exercise/Module 1/source/data/vocab.txt')

# tính khoảng cách levenshtein:


def initialize_distances(len1, len2):
    distances = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for t1 in range(len1 + 1):
        distances[t1][0] = t1
    for t2 in range(len2 + 1):
        distances[0][t2] = t2
    return distances


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


# Test case
token1 = "kitten"
token2 = "sitting"
distance = distance(token1, token2)
print(
    f"The Levenshtein distance between '{token1}' and '{token2}' is {distance}")
