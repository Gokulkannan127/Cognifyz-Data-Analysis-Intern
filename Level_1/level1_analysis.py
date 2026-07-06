"""
Cognifyz Technologies - Data Analysis Internship
LEVEL 1
Task 1: Top Cuisines
Task 2: City Analysis
Task 3: Price Range Distribution
Task 4: Online Delivery
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 120
DATA_PATH = "Dataset .csv"
OUT_DIR = "."

df = pd.read_csv(DATA_PATH)

report_lines = []
def log(msg):
    print(msg)
    report_lines.append(msg)

log("=" * 60)
log("LEVEL 1 - DATA ANALYSIS REPORT")
log("=" * 60)

# ---------------------------------------------------------------
# TASK 1: TOP CUISINES
# ---------------------------------------------------------------
log("\n--- Task 1: Top Cuisines ---\n")

cuisines_split = df['Cuisines'].dropna().str.split(', ')
all_cuisines = cuisines_split.explode()
cuisine_counts = all_cuisines.value_counts()
top3_cuisines = cuisine_counts.head(3)

total_restaurants = len(df)
log("Top 3 most common cuisines:")
for cuisine, count in top3_cuisines.items():
    pct = (count / total_restaurants) * 100
    log(f"  {cuisine}: {count} restaurants ({pct:.2f}% of all restaurants)")

fig, ax = plt.subplots(figsize=(7, 5))
top10 = cuisine_counts.head(10)
ax.barh(top10.index[::-1], top10.values[::-1], color="#4C72B0")
ax.set_xlabel("Number of Restaurants")
ax.set_title("Top 10 Most Common Cuisines")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task1_top_cuisines.png")
plt.close()

# ---------------------------------------------------------------
# TASK 2: CITY ANALYSIS
# ---------------------------------------------------------------
log("\n--- Task 2: City Analysis ---\n")

city_counts = df['City'].value_counts()
city_with_most = city_counts.idxmax()
log(f"City with the highest number of restaurants: {city_with_most} ({city_counts.max()} restaurants)")

city_avg_rating = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)
# Only consider cities with a meaningful number of restaurants to avoid noise from 1-restaurant cities
city_avg_rating_filtered = df.groupby('City').filter(lambda x: len(x) >= 5).groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

log(f"\nCity with highest average rating (all cities): {city_avg_rating.idxmax()} ({city_avg_rating.max():.2f})")
log(f"City with highest average rating (min. 5 restaurants): {city_avg_rating_filtered.idxmax()} ({city_avg_rating_filtered.max():.2f})")
log("\nTop 5 cities by average rating (min. 5 restaurants):")
for city, rating in city_avg_rating_filtered.head(5).items():
    log(f"  {city}: {rating:.2f}")

fig, ax = plt.subplots(figsize=(7, 5))
top10_cities = city_counts.head(10)
ax.barh(top10_cities.index[::-1], top10_cities.values[::-1], color="#55A868")
ax.set_xlabel("Number of Restaurants")
ax.set_title("Top 10 Cities by Restaurant Count")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task2_city_restaurant_count.png")
plt.close()

# ---------------------------------------------------------------
# TASK 3: PRICE RANGE DISTRIBUTION
# ---------------------------------------------------------------
log("\n--- Task 3: Price Range Distribution ---\n")

price_counts = df['Price range'].value_counts().sort_index()
price_pct = (price_counts / total_restaurants * 100).round(2)

log("Restaurant count and percentage by price range:")
for price, count in price_counts.items():
    log(f"  Price range {price}: {count} restaurants ({price_pct[price]}%)")

fig, ax = plt.subplots(figsize=(6, 5))
ax.bar(price_counts.index.astype(str), price_counts.values, color="#C44E52")
ax.set_xlabel("Price Range")
ax.set_ylabel("Number of Restaurants")
ax.set_title("Distribution of Price Ranges")
for i, v in enumerate(price_counts.values):
    ax.text(i, v + 30, str(v), ha='center')
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task3_price_range_distribution.png")
plt.close()

# ---------------------------------------------------------------
# TASK 4: ONLINE DELIVERY
# ---------------------------------------------------------------
log("\n--- Task 4: Online Delivery ---\n")

delivery_counts = df['Has Online delivery'].value_counts()
delivery_pct = (delivery_counts / total_restaurants * 100).round(2)
log("Percentage of restaurants offering online delivery:")
for val, count in delivery_counts.items():
    log(f"  {val}: {count} restaurants ({delivery_pct[val]}%)")

avg_rating_by_delivery = df.groupby('Has Online delivery')['Aggregate rating'].mean()
log("\nAverage rating comparison:")
for val, rating in avg_rating_by_delivery.items():
    log(f"  Online delivery = {val}: average rating = {rating:.2f}")

fig, ax = plt.subplots(figsize=(6, 5))
ax.bar(avg_rating_by_delivery.index, avg_rating_by_delivery.values, color=["#8172B2", "#CCB974"])
ax.set_ylabel("Average Aggregate Rating")
ax.set_title("Average Rating: With vs Without Online Delivery")
for i, v in enumerate(avg_rating_by_delivery.values):
    ax.text(i, v + 0.03, f"{v:.2f}", ha='center')
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task4_online_delivery_ratings.png")
plt.close()

# Save text report
with open(f"{OUT_DIR}/Level1_Report.txt", "w") as f:
    f.write("\n".join(report_lines))

print("\nLevel 1 analysis complete. Charts and report saved to:", OUT_DIR)
