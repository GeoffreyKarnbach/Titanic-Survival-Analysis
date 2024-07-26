import csv
import os
import tabulate

print("-" * 50)

with open("Predictions/solution.csv") as f:
    reader = csv.reader(f)
    next(reader)
    solution = list(reader)

results = []

output_data = []
output_data.append(["Model", "Correct", "Accuracy"])

# Iterate over all csv files in the Predictions folder
for file in sorted(os.listdir("Predictions")):
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

    output_data.append([file, f"Correct: {correct}/{len(solution)}", f"{correct / len(solution) * 100:.2f}%"])
    results.append((file, correct / len(solution)))

print(tabulate.tabulate(output_data, headers="firstrow"))

with open("evaluation.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Model", "Accuracy"])
    writer.writerows(results)

results.sort(key=lambda x: x[1], reverse=True)

print("-" * 50)
print("Best predictions:\n")
data = [
    ["Rank", "Model", "Accuracy"],
    *[[i + 1, x[0], str(round(x[1] * 100, 2))+"%"] for i, x in enumerate(results[:5])]
]
print(tabulate.tabulate(data, headers="firstrow"))
print("-" * 50)
print("Check out the evaluation.csv file for a complete list of results.")
print("-" * 50)


