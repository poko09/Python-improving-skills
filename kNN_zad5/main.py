import numpy as np
from numpy import dot
from numpy.linalg import norm

class DistanceMetrics:  # czy zamykanie metryk w jednej klasie jest korzystne?
    def euclidean(self, a, b):
        distance = np.sqrt(np.sum((a-b)**b))  # ten wykładnik mi się nie podoba
        return distance

    def cosine(self, a, b):
        distance = dot(a, b)/(norm(a)*norm(b))  # 1 -
        return distance

    def manhattan_distance(self, a, b):
        distance = sum(abs(value1 - value2) for value1, value2 in zip(a, b))  # nie dałoby się uniknąć tej iteracji?
        return distance

    def max_distance(self, a, b):
        distance = max(abs(value1 - value2) for value1, value2 in zip(a,b))
        return distance

# Not finished:

dm = DistanceMetrics()
def knn(X, y, test_point, k):   # interfejs
    distances = dm.cosine(X, test_point)
    sorted_indices = np.argsort(distances)
    k_nearest_labels = y[sorted_indices[:k]]
    return np.argmax(np.bincount(k_nearest_labels))

X = np.array([[0, 0], [1, 1], [2, 2], [3, 3]])
y = np.array([0, 0, 1, 1])
test_point = np.array([1.5, 1.5])
prediction = knn(X, y, test_point, k=3)
print(prediction)
