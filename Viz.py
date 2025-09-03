import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
file_path = "data/livedata-weekly-job-changes-2025-07-23.csv"
df = pd.read_csv(file_path)


# Convert date columns to datetime
df['current_job.started_at'] = pd.to_datetime(df['current_job.started_at'], errors='coerce')
df['previous_job.ended_at'] = pd.to_datetime(df['previous_job.ended_at'], errors='coerce')


# Create a 'month' column directly for arrivals vs departures
df['month'] = df.apply(
    lambda row: row['current_job.started_at'] 
    if row['arrival/departure'] == 'arrival' else row['previous_job.ended_at'],
    axis=1
).dt.tz_localize(None).dt.to_period('M').dt.start_time # Normalize to start of month and remove timezone

# Filter to only 2025
df_2025 = df[df['month'].dt.year == 2025].copy() # work on a copy to avoid warning

# Count arrivals and departures by month
monthly_counts = (df_2025.groupby(['month', 'arrival/departure'])
           .size() # count occurrences
           .reset_index(name='count') # reset index to turn groupby object into DataFrame
)

# Pivot to arrivals/departures columns
pivot_monthly = monthly_counts.pivot(index='month', columns='arrival/departure', values='count').fillna(0)
# Ensure all months in 2025 are represented

# Format x-axis labels as "Mon"
pivot_monthly.index = pivot_monthly.index.strftime("%b") # Format as "Jan", "Feb", etc.

# Plot monthly bars
pivot_monthly.plot(kind='bar', stacked=False, color=["#382261", "#D4A421"])

plt.title("Monthly Job Arrivals vs. Departures (2025)")
plt.ylabel("Number of Changes")
plt.xlabel("Month") 
plt.xticks(rotation=45, ha="right") # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent clipping
plt.show()


#############################################

# Filter for departures
departures = df[df['arrival/departure'] == 'departure']

# Get top 10 companies with the most departures
top_departure_companies = departures['previous_job.company.name'].value_counts().nlargest(10) 

# Top Companies by Number of Departures
sns.barplot(
    x=top_departure_companies.values, # use values for x-axis
    y=top_departure_companies.index, # use index for y-axis
    hue=top_departure_companies.index,   # map palette to the y-axis categories
    dodge=False, 
    legend=False,
    palette="coolwarm"
)
plt.title("Top Companies by Number of Departures")
plt.xlabel("Number of Departures")
plt.ylabel("Company")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()


##############################################

##Plot Top 10 Job Functions by Number of Departures
# Get top 10 job functions
departures_by_function = (departures['previous_job.function']     # look at the job function people
    .value_counts()                         # count how many departures per function
    .nlargest(10)                           # keep the top 10
    .reset_index()                          # make it a DataFrame for plotting
)

# Rename columns for clarity
departures_by_function.columns = ['previous_job.function', 'count'] 

# Barplot with function as hue for distinct colors
sns.barplot(
    data=departures_by_function,
    x="count",
    y="previous_job.function",
    hue="previous_job.function",
    palette="Reds_r",
    legend=False
)

plt.title("Top 10 Job Functions by Number of Departures")
plt.xlabel("Number of Departures")
plt.ylabel("Job Function")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.show()





