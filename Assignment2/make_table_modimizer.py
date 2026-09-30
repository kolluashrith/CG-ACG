import glob
import re
from pathlib import Path

results = []

# Look for files such as: modimizers_mut0.01_s1_m1000.txt
files = glob.glob("modimizers_mut*.txt")

for filename in files:
    # Get only the filename without its extension
    name = Path(filename).stem

    # Expected format:
    # modimizers_mut0.01_s1_m1000
    match = re.fullmatch(
        r"modimizers_mut([0-9]+(?:\.[0-9]+)?)_(s[0-9]+)_m([0-9]+)",
        name
    )

    if match is None:
        print("Skipping:", filename)
        continue

    mutation_proportion = float(match.group(1))
    seed = match.group(2)
    m_value = int(match.group(3))

    with open(filename, "r") as f:
        lines = f.readlines()

    if len(lines) < 4:
        print("Skipping incomplete file:", filename)
        continue

    # Extract values from the first three lines
    jaccard = float(lines[0].split()[-1].rstrip("."))
    ani_exact = float(lines[1].split()[-1].rstrip("."))
    ani_approx = float(lines[2].split()[-1].rstrip("."))

    # Extract modimizer counts from the fourth line
    modimizer_match = re.search(
        r"sequence 1 is (\d+) and the number found in sequence 2 is (\d+)",
        lines[3]
    )

    if modimizer_match is None:
        print("Could not extract modimizer counts from:", filename)
        continue

    modimizers_sequence_1 = int(modimizer_match.group(1))
    modimizers_sequence_2 = int(modimizer_match.group(2))

    results.append([
        filename,
        mutation_proportion,
        seed,
        m_value,
        jaccard,
        ani_exact,
        ani_approx,
        modimizers_sequence_1,
        modimizers_sequence_2
    ])

# Sort by mutation proportion, then m value, then filename
results.sort(key=lambda x: (x[1], x[3], x[0]))

# Print Markdown table
print(
    "| Filename | Expected Mutation Proportion | Seed | m | "
    "Jaccard Coefficient | ANI Exact | ANI Approximate | "
    "Modimizers in Sequence 1 | Modimizers in Sequence 2 |"
)
print("|---|---:|---|---:|---:|---:|---:|---:|---:|")

for (
    filename,
    mutation_proportion,
    seed,
    m_value,
    jaccard,
    ani_exact,
    ani_approx,
    modimizers_sequence_1,
    modimizers_sequence_2
) in results:
    print(
        f"| {filename} | "
        f"{mutation_proportion:.4f} | "
        f"{seed} | "
        f"{m_value} | "
        f"{jaccard:.6f} | "
        f"{ani_exact:.6f} | "
        f"{ani_approx:.6f} | "
        f"{modimizers_sequence_1} | "
        f"{modimizers_sequence_2} |"
    )

print(f"\nProcessed {len(results)} files.")