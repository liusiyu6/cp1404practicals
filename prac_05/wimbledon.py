"""
Estimated time: 60 minutes
Actual time: 96 minutes
"""
filename = "wimbledon.csv"
data = []
with open(filename, "r", encoding="utf-8-sig") as in_file:
    next(in_file)  # Skip header row
    for line in in_file:
        parts = line.strip().split(',')
        # Handle the case where score contains commas
        if len(parts) > 6:
            score = ','.join(parts[5:])
            data.append(parts[:5] + [score])
        else:
            data.append(parts)

champion_counts = {}
for row in data:
    champion = row[2]  # Champion name is at index 2
    if champion in champion_counts:
        champion_counts[champion] += 1
    else:
        champion_counts[champion] = 1


countries = set()
for row in data:
    countries.add(row[1])  # Champion country is at index 1
countries = sorted(countries)


print("Wimbledon Champions:")
for champion, count in sorted(champion_counts.items()):
    print(f"{champion} {count}")

print(f"\nThese {len(countries)} countries have won Wimbledon:")
print(", ".join(countries))