import math
from collections import Counter

# Function to calculate entropy
def entropy(data):
    labels = [row[-1] for row in data]
    label_counts = Counter(labels)
    total = len(data)

    return -sum((count/total) * math.log2(count/total) for count in label_counts.values())

# Function to split dataset
def split_dataset(data, feature_index, value):
    return [row for row in data if row[feature_index] == value]

# Function to choose the best feature to split on
def choose_best_feature(data):
    num_features = len(data[0]) - 1
    base_entropy = entropy(data)
    best_info_gain = 0
    best_feature = -1

    for i in range(num_features):
        values = set(row[i] for row in data)
        new_entropy = 0

        for value in values:
            subset = split_dataset(data, i, value)
            prob = len(subset) / len(data)
            new_entropy += prob * entropy(subset)

        info_gain = base_entropy - new_entropy

        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i

    return best_feature

# Function to create the decision tree
def build_tree(data, features):
    labels = [row[-1] for row in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]  # Only one class left

    if len(data[0]) == 1:
        return Counter(labels).most_common(1)[0][0]

    best_feat = choose_best_feature(data)
    best_feat_name = features[best_feat]
    tree = {best_feat_name: {}}

    feat_values = set(row[best_feat] for row in data)
    for value in feat_values:
        sub_features = features[:best_feat] + features[best_feat+1:]
        subset = split_dataset(data, best_feat, value)
        sub_data = [row[:best_feat] + row[best_feat+1:] for row in subset]
        tree[best_feat_name][value] = build_tree(sub_data, sub_features)

    return tree

# Example usage
if __name__ == "__main__":
    # Sample dataset: [Outlook, Temperature, Humidity, Wind, PlayTennis]
    dataset = [
        ['Sunny', 'Hot', 'High', 'Weak', 'No'],
        ['Sunny', 'Hot', 'High', 'Strong', 'No'],
        ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
        ['Sunny', 'Mild', 'High', 'Weak', 'No'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
        ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
        ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
        ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
        ['Rain', 'Mild', 'High', 'Strong', 'No'],
    ]

    features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
    
    decision_tree = build_tree(dataset, features)
    
    print("Decision Tree:")
    print(decision_tree)
