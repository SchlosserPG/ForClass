import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo

##retrieved the data from the ucimlrepo, which means you need to have that library installed to access

# fetch dataset
pittsburgh_bridges = fetch_ucirepo(id=18)

# data
X = pittsburgh_bridges.data.features
print(X.head())


# get the counts by construction material and period of construction
material_counts = X['MATERIAL'].value_counts(normalize=True) * 100
period_counts   = X['ERECTED'].value_counts(normalize=True) * 100

# combine them (bad practice — overlaps!)
bad_counts = {
    'steel':  X['MATERIAL'].value_counts(normalize=True).get('STEEL', 0) * 100,
    'wood':   X['MATERIAL'].value_counts(normalize=True).get('WOOD', 0) * 100,
    'iron':   X['MATERIAL'].value_counts(normalize=True).get('IRON', 0) * 100,
    'modern': X['ERECTED'].value_counts(normalize=True).get('MODERN', 0) * 100,
    'crafts': X['ERECTED'].value_counts(normalize=True).get('CRAFTS', 0) * 100
}

values = list(bad_counts.values())
labels = list(bad_counts.keys())
total_shown = sum(values)

def raw_label(pct):
    # pct is the fraction of the wedge out of 100 (matplotlib normalizes),
    # but we want to show our misleading raw value instead
    index = raw_label.idx
    value = values[index]
    raw_label.idx += 1
    return f"{value:.1f}%"

raw_label.idx = 0

plt.pie(
    values,
    labels=labels,
    autopct=raw_label,   # put raw % labels inside slices
    startangle=90
)
plt.title(f"Bad Pie: Labels total {total_shown:.1f}% (>100%)")
plt.show()

#####################################################
# make a misleading bar chart
plt.figure(figsize=(7,4))
plt.bar(bad_counts.keys(), bad_counts.values(),
        color=['#1f77b4','#2ca02c','#ff7f0e','#17becf','#bcbd22'])
for i, v in enumerate(values):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center', va='bottom', fontsize=9)
plt.ylabel("proportion of bridges (%)")
plt.title(f"Breakdown of Pittsburgh Bridges (Labels total {total_shown:.1f}% — misleading)")
plt.tight_layout()
plt.show()


