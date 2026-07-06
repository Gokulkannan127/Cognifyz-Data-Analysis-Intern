"""
Cognifyz Technologies - Data Analysis Internship
LEVEL 2
Task 1: Restaurant Ratings
Task 2: Cuisine Combination
Task 3: Geographic Analysis
Task 4: Restaurant Chains
"""

import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

plt.rcParams['figure.dpi'] = 120
DATA_PATH = "Dataset.csv"
OUT_DIR = "."
df = pd.read_csv(DATA_PATH)

report_lines = []
def log(msg):
    print(msg)
    report_lines.append(msg)

log("=" * 60)
log("LEVEL 2 - DATA ANALYSIS REPORT")
log("=" * 60)

# ---------------------------------------------------------------
# TASK 1: RESTAURANT RATINGS
# ---------------------------------------------------------------
log("\n--- Task 1: Restaurant Ratings ---\n")

rating_text_counts = df['Rating text'].value_counts()
log("Distribution of aggregate ratings (by rating category):")
for cat, count in rating_text_counts.items():
    log(f"  {cat}: {count} restaurants")

most_common_range = rating_text_counts.idxmax()
log(f"\nMost common rating range/category: {most_common_range} ({rating_text_counts.max()} restaurants)")

avg_votes = df['Votes'].mean()
log(f"\nAverage number of votes received by restaurants: {avg_votes:.2f}")

fig, ax = plt.subplots(figsize=(7, 5))
ax.hist(df['Aggregate rating'], bins=20, color="#4C72B0", edgecolor='white')
ax.set_xlabel("Aggregate Rating")
ax.set_ylabel("Number of Restaurants")
ax.set_title("Distribution of Aggregate Ratings")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task1_rating_distribution.png")
plt.close()

fig, ax = plt.subplots(figsize=(7, 5))
order = rating_text_counts.index
ax.bar(order, rating_text_counts.values, color="#55A868")
ax.set_xlabel("Rating Text Category")
ax.set_ylabel("Number of Restaurants")
ax.set_title("Restaurant Count by Rating Category")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task1_rating_category_counts.png")
plt.close()

# ---------------------------------------------------------------
# TASK 2: CUISINE COMBINATIONS
# ---------------------------------------------------------------
log("\n--- Task 2: Cuisine Combination ---\n")

cuisines_lists = df['Cuisines'].dropna().str.split(', ')
# Only consider actual multi-cuisine combos as they appear (exact combo strings)
combo_counts = df['Cuisines'].dropna().value_counts()
multi_combo_counts = combo_counts[combo_counts.index.str.contains(',')]

log("Top 10 most common cuisine combinations:")
for combo, count in multi_combo_counts.head(10).items():
    log(f"  {combo}: {count} restaurants")

# Average rating per combination (for combos with a reasonable sample size)
df_valid = df.dropna(subset=['Cuisines'])
combo_avg_rating = df_valid.groupby('Cuisines')['Aggregate rating'].agg(['mean', 'count'])
combo_avg_rating = combo_avg_rating[combo_avg_rating['count'] >= 10].sort_values('mean', ascending=False)

log("\nTop 10 cuisine combinations (min. 10 restaurants) by average rating:")
for combo, row in combo_avg_rating.head(10).iterrows():
    log(f"  {combo}: avg rating {row['mean']:.2f} (n={int(row['count'])})")

fig, ax = plt.subplots(figsize=(8, 5))
top10combo = multi_combo_counts.head(10)
ax.barh(top10combo.index[::-1], top10combo.values[::-1], color="#C44E52")
ax.set_xlabel("Number of Restaurants")
ax.set_title("Top 10 Most Common Cuisine Combinations")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task2_top_cuisine_combinations.png")
plt.close()

# ---------------------------------------------------------------
# TASK 3: GEOGRAPHIC ANALYSIS
# ---------------------------------------------------------------
log("\n--- Task 3: Geographic Analysis ---\n")

log(f"Longitude range: {df['Longitude'].min():.4f} to {df['Longitude'].max():.4f}")
log(f"Latitude range: {df['Latitude'].min():.4f} to {df['Latitude'].max():.4f}")
log("\nRestaurants are heavily clustered around a few major hubs, dominated by New Delhi "
    "and other Indian NCR cities, with smaller clusters in the US, UK, UAE, and other "
    "countries represented in the dataset (see scatter plot).")

fig, ax = plt.subplots(figsize=(9, 6))
scatter = ax.scatter(df['Longitude'], df['Latitude'], s=5, alpha=0.4, c=df['Aggregate rating'], cmap='viridis')
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Restaurant Locations (colored by Aggregate Rating)")
plt.colorbar(scatter, label="Aggregate Rating")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task3_geographic_scatter.png")
plt.close()

# Zoomed-in view on the densest cluster (India / NCR region)
india_df = df[(df['Longitude'].between(70, 90)) & (df['Latitude'].between(8, 32))]
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(india_df['Longitude'], india_df['Latitude'], s=5, alpha=0.4, color="#4C72B0")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_title("Restaurant Cluster - India Region (Zoomed In)")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task3_geographic_india_zoom.png")
plt.close()

# ---------------------------------------------------------------
# TASK 4: RESTAURANT CHAINS
# ---------------------------------------------------------------
log("\n--- Task 4: Restaurant Chains ---\n")

name_counts = df['Restaurant Name'].value_counts()
chains = name_counts[name_counts > 1]
log(f"Number of restaurant names appearing more than once (potential chains): {len(chains)}")
log(f"Total outlets belonging to chains: {chains.sum()} out of {total_restaurants if (total_restaurants:=len(df)) else len(df)} restaurants")

log("\nTop 10 restaurant chains by number of outlets:")
for name, count in chains.head(10).items():
    log(f"  {name}: {count} outlets")

chain_stats = df[df['Restaurant Name'].isin(chains.index)].groupby('Restaurant Name').agg(
    outlets=('Restaurant Name', 'count'),
    avg_rating=('Aggregate rating', 'mean'),
    total_votes=('Votes', 'sum')
).sort_values('outlets', ascending=False)

log("\nTop 10 chains - ratings & popularity (total votes):")
for name, row in chain_stats.head(10).iterrows():
    log(f"  {name}: {int(row['outlets'])} outlets, avg rating {row['avg_rating']:.2f}, total votes {int(row['total_votes'])}")

fig, ax = plt.subplots(figsize=(8, 5))
top10chains = chains.head(10)
ax.barh(top10chains.index[::-1], top10chains.values[::-1], color="#8172B2")
ax.set_xlabel("Number of Outlets")
ax.set_title("Top 10 Restaurant Chains by Outlet Count")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task4_top_restaurant_chains.png")
plt.close()

with open(f"{OUT_DIR}/Level2_Report.txt", "w") as f:
    f.write("\n".join(report_lines))

print("\nLevel 2 analysis complete. Charts and report saved to:", OUT_DIR)
