import csv
import math

def distance_metric(a, b, r):
    total = sum(abs(x - y) ** r for x, y in zip(a, b))
    return total ** (1 / r)

def load_data(filename):
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            # Start index at 1 to match CSV row number
            for i, row in enumerate(reader, 1):
                features = list(map(float, row[:-1]))
                label = row[-1]
                data.append((features, label, i))
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def normalize(data):
    feature_count = len(data[0][0])
    mins = [min(row[0][i] for row in data) for i in range(feature_count)]
    maxs = [max(row[0][i] for row in data) for i in range(feature_count)]

    normalized_list = []
    for features, label, csv_row in data:
        norm_features = []
        for i in range(feature_count):
            if maxs[i] != mins[i]:
                norm_features.append((features[i] - mins[i]) / (maxs[i] - mins[i]))
            else:
                norm_features.append(0.0)
        normalized_list.append((features, norm_features, label, csv_row))

    return normalized_list, mins, maxs

def vote(neighbors, voting_type):
    if voting_type == "1":
        counts = {}
        for _, _, _, label, _ in neighbors:
            counts[label] = counts.get(label, 0) + 1
        print("\n--- Unweighted Voting ---")
        print(f"Frequency Count: {counts}")
        return max(counts, key=counts.get)
    else:
        weighted_scores = {}
        for _, _, dist, label, _ in neighbors:
            weight = 1 / (dist + 1e-9)
            weighted_scores[label] = weighted_scores.get(label, 0) + weight
        print("\n--- Weighted Voting ---")
        print(f"Weighted Scores: { {k: round(v,4) for k,v in weighted_scores.items()} }")
        return max(weighted_scores, key=weighted_scores.get)

def knn(data, query, k, r_value, voting_type, is_normalized):
    results = []

    # Calculate distances (keep CSV order)
    for original, normalized, label, csv_row in data:
        compare_point = normalized if is_normalized else original
        d = distance_metric(compare_point, query, r_value)
        results.append((original, normalized, d, label, csv_row))

    # Sort only for ranking and selecting top K
    sorted_by_distance = sorted(results, key=lambda x: x[2])

    # Assign ranks without changing CSV order
    rank_map = {}
    for rank, item in enumerate(sorted_by_distance, 1):
        rank_map[item[4]] = rank  # csv_row  rank

    # ---- DISPLAY TABLE (CSV ORDER) ----
    print(f"\n{'CSV Row':<8} | {'Data Point':<30} | {'Distance':<10} | {'Class':<10} | {'Rank':<5}")
    print("-" * 85)

    for original, _, d, label, csv_row in results:
        print(f"{csv_row:<8} | {str(original):<30} | {d:.4f}     | {label:<10} | {rank_map[csv_row]:<5}")

    # Select Top K neighbors
    neighbors = sorted_by_distance[:k]

    print(f"\nTop K ({k}) Neighbors Selected (Sorted by Proximity):")
    print(f"{'Rank':<5} | {'CSV Row':<8} | {'Distance':<10} | {'Class':<10}")
    print("-" * 50)

    for i, (_, _, d, label, csv_row) in enumerate(neighbors, 1):
        print(f"{i:<5} | {csv_row:<8} | {d:.4f}     | {label:<10}")

    return vote(neighbors, voting_type)

def main():
    print("KNN Classifier")
    data = load_data("data.csv")
    if not data:
        return

    # Check if normalization needed
    needs_norm = False
    for features, _, _ in data:
        if any(val > 100.0 or val < 0.0 for val in features):
            needs_norm = True
            break

    if needs_norm:
        print("Large values detected. Normalizing...")
        processed_data, mins, maxs = normalize(data)
    else:
        print("Normalization Skipped!")
        processed_data = [(f, f, l, r) for f, l, r in data]
        mins, maxs = [], []

    while True:
        print("\n1. Predict\n2. Exit")
        ch = input("Choice: ")

        if ch == "2":
            break

        if ch == "1":
            try:
                num_features = len(data[0][0])
                query = [float(input(f"x{i+1}: ")) for i in range(num_features)]

                final_query = query
                if needs_norm:
                    final_query = [
                        (query[i] - mins[i]) / (maxs[i] - mins[i]) if maxs[i] != mins[i] else 0
                        for i in range(len(query))
                    ]

                k = int(input("Enter K: "))

                print("\nDistance Metric: 1. Euclidean (r=2), 2. Manhattan (r=1)")
                r_val = 2 if input("Choice: ") == "1" else 1

                print("\nVoting: 1. Unweighted, 2. Weighted")
                v_choice = input("Choice: ")

                result = knn(processed_data, final_query, k, r_val, v_choice, needs_norm)
                print("\nFinal Predicted Class:", result)

            except ValueError:
                print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
