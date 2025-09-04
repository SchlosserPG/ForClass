##This file has a lot of chart objects used in the Data Reasoning Slide Deck. 

import matplotlib.pyplot as plt
import numpy as np


# Create a 2x2 subplot layout
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Chart (a): Simple blue bar chart
categories_a = ['A', 'B', 'C']
values_a = [3, 5, 4]
axs[0, 0].bar(categories_a, values_a, color='blue')
axs[0, 0].set_ylabel('value')
axs[0, 0].set_title('(a)')

# Chart (b): Yellow, cyan, and magenta bars with title 'ugly'
colors_b = ['yellow', 'cyan', 'magenta']
values_b = [3, 5, 4]
axs[0, 1].bar(categories_a, values_b, color=colors_b)
axs[0, 1].set_ylabel('value')
axs[0, 1].set_title('(b) ugly')

# Chart (c): Two sets of bars with title 'bad'
values_c1 = [3, 5, 0]
values_c2 = [0, 0, 4]
x = range(len(categories_a))
axs[1, 0].bar(x, values_c1, color='blue', label='Set 1')
axs[1, 0].bar(x, values_c2, color='red', label='Set 2', bottom=values_c1)
axs[1, 0].set_xticks(x)
axs[1, 0].set_xticklabels(categories_a)
axs[1, 0].set_ylabel('value')
axs[1, 0].set_title('(c) bad')

# Chart (d): Blue bars with title 'wrong'
values_d = [1, 5, 3]
axs[1, 1].bar(categories_a, values_d, color='blue')
axs[1, 1].set_ylabel('value')
axs[1, 1].set_title('(d) wrong')

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('grouped_bar_charts.png')
plt.show()


#############################################################
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Create a 3x2 grid of subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 10))

# Line Width
line_widths = [2, 4, 6, 8]
for i, lw in enumerate(line_widths):
    axs[0, 0].plot([0, 1], [i, i], linewidth=lw, color='black')
axs[0, 0].set_title('Line Width')
axs[0, 0].axis('off')

# Line Type
linestyles = ['solid', 'dashed', 'dotted', 'dashdot']
for i, ls in enumerate(linestyles):
    axs[0, 1].plot([0, 1], [i, i], linestyle=ls, linewidth=2, color='black')
axs[0, 1].set_title('Line Type')
axs[0, 1].axis('off')

# Shape
shapes = ['o', 's', 'D', '^']
for i, shape in enumerate(shapes):
    axs[1, 0].scatter(i, 0, marker=shape, s=200, color='black')
axs[1, 0].set_title('Shape')
axs[1, 0].axis('off')

# Size
sizes = [50, 100, 150, 200]
for i, size in enumerate(sizes):
    axs[1, 1].scatter(i, 0, s=size, color='black')
axs[1, 1].set_title('Size')
axs[1, 1].axis('off')

# Color
colors = ['orange', 'skyblue', 'green', 'yellow']
for i, color in enumerate(colors):
    axs[2, 0].bar(i, 1, color=color)
axs[2, 0].set_title('Color')
axs[2, 0].axis('off')

# Position with increased spacing for text
axs[2, 1].arrow(0.1, 0.1, 0.3, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')
axs[2, 1].arrow(0.1, 0.1, 0, 0.3, head_width=0.05, head_length=0.05, fc='black', ec='black')
axs[2, 1].text(-0.2, 0.6, 'Position', fontsize=12)
axs[2, 1].text(0.6, 0.05, 'x', fontsize=12)
axs[2, 1].text(0.05, 0.6, 'y', fontsize=12)
axs[2, 1].set_xlim(0, 1)
axs[2, 1].set_ylim(0, 1)
axs[2, 1].set_title('Position')
axs[2, 1].axis('off')

# Add a visible box around all subplots
fig.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
rect = patches.Rectangle((0, 0), 1, 1, transform=fig.transFigure,
                         fill=False, color='black', linewidth=2)
fig.patches.append(rect)

# Display the figure
plt.tight_layout()
plt.show()
#############################################################


# Sample data: daily temperature normals for Houston, TX
days = np.linspace(1, 365, 365)
temperature = 70 + 20 * np.sin((days - 80) * np.pi / 180)

# Create a figure with 3 subplots: 2 on top, 1 on bottom
fig = plt.figure(figsize=(12, 8))

# Top left (a)
ax1 = plt.subplot(2, 2, 1)
ax1.plot(days, temperature)
ax1.set_title('(a)')
ax1.set_xlabel('Day of Year')
ax1.set_ylabel('Temperature (°F)')
ax1.set_aspect('auto')

# Top right (b)
ax2 = plt.subplot(2, 2, 2)
ax2.plot(days, temperature)
ax2.set_title('(b)')
ax2.set_xlabel('Day of Year')
ax2.set_ylabel('Temperature (°F)')
ax2.set_aspect(0.5)  # More vertical stretch

# Bottom full-width (c)
ax3 = plt.subplot(2, 1, 2)
ax3.plot(days, temperature)
ax3.set_title('(c)')
ax3.set_xlabel('Day of Year')
ax3.set_ylabel('Temperature (°F)')
ax3.set_aspect('auto')

plt.tight_layout()
plt.show()

########################################################
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Southeast states
states = [
    "Alabama", "Florida", "Georgia", "Kentucky", "Mississippi",
    "North Carolina", "South Carolina", "Tennessee", "Virginia", "West Virginia"
]

# Assign regions (arbitrary grouping for sales reps)
regions = [
    "Region 1", "Region 1", "Region 1",    # AL, FL, GA
    "Region 2", "Region 2", "Region 2",    # KY, MS, NC
    "Region 3", "Region 3", "Region 3", "Region 3"  # SC, TN, VA, WV
]

# Fake "sales" data
np.random.seed(42)
sales = np.random.randint(100, 1000, len(states))  # in thousands $

df = pd.DataFrame({"State": states, "Region": regions, "Sales": sales})

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# --- Chart 1: Distinguish groups (Regions + legend) ---
region_colors = {
    "Region 1": "skyblue",
    "Region 2": "lightgreen",
    "Region 3": "orange"
}
df["Color"] = df["Region"].map(region_colors)

bars = ax[0].bar(df["State"], df["Sales"], color=df["Color"], edgecolor="black")
ax[0].set_title("Distinguish Groups (Regions)")
ax[0].tick_params(axis='x', rotation=45)

# Add legend for regions
handles = [plt.Rectangle((0,0),1,1, color=region_colors[r], edgecolor="black") for r in region_colors]
ax[0].legend(handles, region_colors.keys(), title="Region")

# --- Chart 2: Represent values (sorted + colormap) ---
df_sorted = df.sort_values("Sales", ascending=True)
colors = plt.cm.Greens(
    (df_sorted["Sales"] - df_sorted["Sales"].min()) /
    (df_sorted["Sales"].max() - df_sorted["Sales"].min())
)
ax[1].bar(df_sorted["State"], df_sorted["Sales"], color=colors, edgecolor="black")
ax[1].set_title("Represent Values (Sales Sorted by Size)")
ax[1].tick_params(axis='x', rotation=45)

# --- Chart 3: Highlight high + low ---
max_state = df.loc[df["Sales"].idxmax(), "State"]
min_state = df.loc[df["Sales"].idxmin(), "State"]

highlight_colors = [
    "red" if s == max_state else
    "blue" if s == min_state else
    "lightgrey" for s in df["State"]
]

ax[2].bar(df["State"], df["Sales"], color=highlight_colors, edgecolor="black")
ax[2].set_title(f"Highlight High ({max_state}) & Low ({min_state})")
ax[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
########################################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Make reproducible
np.random.seed(42)

# Fake data
categories = ["A", "B", "C", "D"]
amounts = np.random.randint(10, 100, size=4)
dist_data = np.random.normal(0, 1, 200)
dist_data2 = np.random.normal(1, 1.2, 200)
proportions = [0.3, 0.5, 0.2]
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, size=100)

fig, axes = plt.subplots(4, 3, figsize=(15, 12))
axes = axes.flatten()

# Amounts (bar + dot)
axes[0].bar(categories, amounts, color="skyblue", edgecolor="black")
axes[0].set_title("Amounts: Bar Chart")

axes[1].scatter(categories, amounts, color="red", s=60)
axes[1].set_title("Amounts: Dot Plot")

axes[2].bar(categories, [a*0.8 for a in amounts], color="orange", edgecolor="black")
axes[2].bar(categories, [a*0.2 for a in amounts], bottom=[a*0.8 for a in amounts], 
            color="green", edgecolor="black")
axes[2].set_title("Amounts: Stacked Bars")

# Distributions
axes[3].hist(dist_data, bins=15, color="steelblue", edgecolor="black")
axes[3].set_title("Distribution: Histogram")

sns.kdeplot(dist_data, fill=True, ax=axes[4], color="purple")
sns.kdeplot(dist_data2, fill=True, ax=axes[4], color="orange", alpha=0.5)
axes[4].set_title("Distribution: Densities")

sns.boxplot(data=[dist_data, dist_data2], ax=axes[5], palette="Set2")
axes[5].set_title("Distribution: Boxplots")

# Proportions
axes[6].pie(proportions, labels=["X","Y","Z"], autopct="%1.0f%%", colors=["red","blue","green"])
axes[6].set_title("Proportions: Pie Chart")

axes[7].bar(["X","Y","Z"], proportions, color=["red","blue","green"], edgecolor="black")
axes[7].set_title("Proportions: Bars")

axes[8].bar(["X","Y","Z"], proportions, bottom=0, color=["red","blue","green"], edgecolor="black")
axes[8].set_title("Proportions: Stacked Bars")

# X–Y Relationships
axes[9].scatter(x, y, color="teal", alpha=0.7)
axes[9].set_title("x–y: Scatterplot")

axes[10].plot(x, y, color="navy")
axes[10].set_title("x–y: Line Plot")

sns.heatmap(np.random.rand(5,5), ax=axes[11], cmap="YlGnBu", cbar=False, annot=False)
axes[11].set_title("x–y: Heatmap")

# Turn off axes for a clean look
for ax in axes:
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

plt.tight_layout()
plt.show()

#########################################################   
import matplotlib.pyplot as plt
import pandas as pd

# Sales data for each month
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [120, 130, 90, 150, 80, 70, 200, 210, 180, 160, 140, 100]

data = pd.DataFrame({"Month": months, "Sales": sales})

fig, ax = plt.subplots(1, 3, figsize=(18, 5))

# --- Chart 1: Full dataset ---
ax[0].plot(data["Month"], data["Sales"], marker="o", color="steelblue")
ax[0].set_title("Full Data (All 12 Months)")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Sales")

# --- Chart 2: Cherry-picked data points (peak months only) ---
cherry_points = data[data["Month"].isin(["Jan", "Aug", "May"])]
ax[1].plot(cherry_points["Month"], cherry_points["Sales"], marker="o", color="red")
ax[1].set_title("Cherry-Picked Data Points (Selcting Certain Months)")
ax[1].set_xlabel("Month")
ax[1].set_ylabel("Sales")

# --- Chart 3: Cherry-picked time frame (Jun–Sep) ---
subset = data[data["Month"].isin(["Jun", "Jul", "Aug", "Sep"])]
ax[2].plot(subset["Month"], subset["Sales"], marker="o", color="orange")
ax[2].set_title("Cherry-Picked Time Frame (Jun–Sep)")
ax[2].set_xlabel("Month")
ax[2].set_ylabel("Sales")

plt.tight_layout()
plt.show()

######################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1) Simulate some daily data
# -----------------------------
np.random.seed(42)
n_days = 180
dates = pd.date_range("2024-01-01", periods=n_days, freq="D")

# Baseline with a gentle seasonal pattern + noise (e.g., site visits, defects, cases)
baseline = 70 + 5*np.sin(np.linspace(0, 10*np.pi, n_days))
noise = np.random.normal(0, 8, size=n_days)
y = baseline + noise

df = pd.DataFrame({"date": dates, "value": y}).set_index("date")

# -----------------------------------------
# 2) Pick an arbitrary (unjustified) cutoff
# -----------------------------------------
# This could be chosen to make a point (e.g., too low) without any rationale.
arbitrary_threshold = 72  # <- arbitrary and not justified by the data
pct_above_arbitrary = (df["value"] > arbitrary_threshold).mean() * 100

# ----------------------------------------------------
# 3) Compute data-driven thresholds for comparison
# ----------------------------------------------------
p95 = df["value"].quantile(0.95)         # 95th percentile
mean_plus_2sd = df["value"].mean() + 2*df["value"].std()

pct_above_p95 = (df["value"] > p95).mean() * 100
pct_above_mean2sd = (df["value"] > mean_plus_2sd).mean() * 100

print(f"Arbitrary threshold = {arbitrary_threshold:.1f}  -> {pct_above_arbitrary:.1f}% of days above")
print(f"95th percentile     = {p95:.1f}  -> {pct_above_p95:.1f}% of days above")
print(f"Mean + 2σ           = {mean_plus_2sd:.1f}  -> {pct_above_mean2sd:.1f}% of days above")

# --------------------------------------
# 4) Plot misleading vs. better practice
# --------------------------------------
fig, axes = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

# (A) Misleading view with an arbitrary threshold
ax = axes[0]
ax.plot(df.index, df["value"], color="#3a78b7", lw=1.5)
ax.axhline(arbitrary_threshold, color="#d62728", ls="--", lw=2, label=f"Arbitrary = {arbitrary_threshold:.1f}")
ax.fill_between(df.index, df["value"], arbitrary_threshold,
                where=(df["value"] > arbitrary_threshold),
                color="#d62728", alpha=0.15)
ax.set_title("Misleading: Arbitrary Threshold (chosen without justification)")
ax.legend(loc="upper right")
ax.set_ylabel("Value")
ax.text(0.01, 0.9,
        f"{pct_above_arbitrary:.1f}% of days \"above the limit\"",
        transform=ax.transAxes, fontsize=10, color="#d62728")

# (B) Better practice with data-driven thresholds
ax = axes[1]
ax.plot(df.index, df["value"], color="#3a78b7", lw=1.5, label="Daily value")
ax.axhline(p95, color="#2ca02c", ls="--", lw=2, label=f"95th percentile = {p95:.1f}")
ax.axhline(mean_plus_2sd, color="#9467bd", ls=":", lw=2, label=f"Mean + 2σ = {mean_plus_2sd:.1f}")
ax.fill_between(df.index, df["value"], p95,
                where=(df["value"] > p95),
                color="#2ca02c", alpha=0.12)
ax.set_title("Better: Data‑Driven Thresholds (95th percentile, mean + 2σ)")
ax.legend(loc="upper right")
ax.set_ylabel("Value")

plt.suptitle("How Arbitrary Thresholds Can Mislead", y=0.98, fontsize=13)
plt.tight_layout()
plt.show()
