import csv
import os

print("-" * 50)

with open("Predictions/solution.csv") as f:
    reader = csv.reader(f)
    next(reader)
    solution = list(reader)

results = []

# Iterate over all csv files in the Predictions folder
for file in os.listdir("Predictions"):
    if file == "solution.csv":
        continue

    with open("Predictions/" + file) as f:
        reader = csv.reader(f)
        next(reader)
        prediction = list(reader)

    if len(solution) != len(prediction):
        print(f"Prediction file {file}has wrong number of lines")
        continue

    correct = 0

    for i in range(len(solution)):
        if solution[i][1] == prediction[i][1]:
            correct += 1

    print(f"[{file}] Correct: {correct}/{len(solution)} ({correct / len(solution) * 100:.2f}%)")
    results.append((file, correct / len(solution)))

results.sort(key=lambda x: x[1], reverse=True)

print("-" * 50)
print("\nBest predictions:")
print("\n".join([f"{x[0]}: {x[1] * 100:.2f}%" for x in results[:5]]))
print("-" * 50)


