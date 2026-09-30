#Code to create a table was made by ChatGPT given a prompt telling it the file name, structure, and desired info in the table.

import glob
import re

results = []

files = glob.glob("jaccard_mut*.txt")

for filename in files:
    # Get just the filename, without .txt
    name = filename[:-4]

    # Example: jaccard_mut0.01_s1
    match = re.fullmatch(r"jaccard_mut([0-9]+\.[0-9]+)_(s[0-9]+)", name)

    if match is None:
        print("Skipping:", filename)
        continue

    mutation_proportion = float(match.group(1))

    # Read file
    with open(filename, "r") as f:
        lines = f.readlines()

    # Extract values from the three lines
    jaccard = float(lines[0].split()[-1].rstrip("."))
    ani_exact = float(lines[1].split()[-1].rstrip("."))
    ani_approx = float(lines[2].split()[-1].rstrip("."))

    results.append([
        filename,
        mutation_proportion,
        jaccard,
        ani_exact,
        ani_approx
    ])

# Sort by mutation proportion, then filename
results.sort(key=lambda x: (x[1], x[0]))

# Display a Markdown table
print("| Filename | Expected Mutation Proportion | Jaccard Coefficient | ANI Exact | ANI Approximate |")
print("|---|---:|---:|---:|---:|")

for filename, mutation_proportion, jaccard, ani_exact, ani_approx in results:
    print(
        f"| {filename} | "
        f"{mutation_proportion:.4f} | "
        f"{jaccard:.6f} | "
        f"{ani_exact:.6f} | "
        f"{ani_approx:.6f} |"
    )

print(f"\nProcessed {len(results)} files.")