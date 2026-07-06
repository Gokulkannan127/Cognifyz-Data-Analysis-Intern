"""
Cognifyz Technologies - Data Analysis Internship
LEVEL 3
Task 1: Restaurant Reviews (adapted - see note below)
Task 2: Votes Analysis
Task 3: Price Range vs. Online Delivery and Table Booking

NOTE on Task 1: The provided dataset (Dataset_.csv) does not contain a raw
text-review column (e.g. individual customer review text). It does contain
'Rating text' (Excellent/Very Good/Good/Average/Poor/Not rated), which is the
closest available proxy for review sentiment. This script analyzes the
sentiment-category distribution and its relationship with Votes (used here as
a proxy for review volume/engagement, since actual review length is not
present in the data) so that the spirit of the task -- linking review
sentiment to restaurant performance -- is still addressed with the data on hand.
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 120
DATA_PATH = "Dataset.csv"
OUT_DIR = "."

df = pd.read_csv(DATA_PATH)
total_restaurants = len(df)

report_lines = []
def log(msg):
    print(msg)
    report_lines.append(msg)

log("=" * 60)
log("LEVEL 3 - DATA ANALYSIS REPORT")
log("=" * 60)

# ---------------------------------------------------------------
# TASK 1: RESTAURANT REVIEWS (adapted, see module docstring)
# ---------------------------------------------------------------
log("\n--- Task 1: Restaurant Reviews (adapted) ---\n")
log("NOTE: Dataset_.csv has no raw review-text column. Using 'Rating text' "
    "(Excellent/Very Good/Good/Average/Poor/Not rated) as the closest sentiment "
    "proxy, and 'Votes' as a proxy for review engagement/volume.\n")

positive_categories = ['Excellent', 'Very Good', 'Good']
negative_categories = ['Poor']
neutral_categories = ['Average', 'Not rated']

sentiment_counts = df['Rating text'].value_counts()
log("Rating-text ('sentiment') category counts:")
for cat, count in sentiment_counts.items():
    log(f"  {cat}: {count}")

pos_count = df['Rating text'].isin(positive_categories).sum()
neg_count = df['Rating text'].isin(negative_categories).sum()
log(f"\nPositive-leaning restaurants (Good/Very Good/Excellent): {pos_count} "
    f"({pos_count/total_restaurants*100:.2f}%)")
log(f"Negative-leaning restaurants (Poor): {neg_count} "
    f"({neg_count/total_restaurants*100:.2f}%)")

avg_votes_by_sentiment = df.groupby('Rating text')['Votes'].mean().sort_values(ascending=False)
log("\nAverage votes (engagement proxy) by rating category:")
for cat, avg in avg_votes_by_sentiment.items():
    log(f"  {cat}: {avg:.1f} avg votes")

corr_votes_rating = df['Votes'].corr(df['Aggregate rating'])
log(f"\nCorrelation between Votes and Aggregate Rating: {corr_votes_rating:.3f}")
log("(A positive correlation suggests that restaurants with more customer "
    "engagement/votes tend to also have higher ratings.)")

fig, ax = plt.subplots(figsize=(7, 5))
order = avg_votes_by_sentiment.index
ax.bar(order, avg_votes_by_sentiment.values, color="#4C72B0")
ax.set_ylabel("Average Votes")
ax.set_xlabel("Rating Category")
ax.set_title("Average Votes by Rating Category (Engagement vs Sentiment)")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task1_votes_by_sentiment.png")
plt.close()

# ---------------------------------------------------------------
# TASK 2: VOTES ANALYSIS
# ---------------------------------------------------------------
log("\n--- Task 2: Votes Analysis ---\n")

top_voted = df.nlargest(5, 'Votes')[['Restaurant Name', 'City', 'Votes', 'Aggregate rating']]
bottom_voted = df.nsmallest(5, 'Votes')[['Restaurant Name', 'City', 'Votes', 'Aggregate rating']]

log("Top 5 restaurants with the HIGHEST number of votes:")
for _, row in top_voted.iterrows():
    log(f"  {row['Restaurant Name']} ({row['City']}): {row['Votes']} votes, rating {row['Aggregate rating']}")

log("\n5 restaurants with the LOWEST number of votes:")
for _, row in bottom_voted.iterrows():
    log(f"  {row['Restaurant Name']} ({row['City']}): {row['Votes']} votes, rating {row['Aggregate rating']}")

correlation = df['Votes'].corr(df['Aggregate rating'])
log(f"\nCorrelation coefficient between Votes and Aggregate Rating: {correlation:.3f}")
if correlation > 0.3:
    strength = "a moderate-to-strong positive"
elif correlation > 0.1:
    strength = "a weak positive"
else:
    strength = "a very weak or negligible"
log(f"This indicates {strength} relationship: restaurants with higher ratings "
    "tend to receive somewhat more votes, though rating is far from the only "
    "driver of vote volume.")

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(df['Aggregate rating'], df['Votes'], alpha=0.3, s=15, color="#C44E52")
ax.set_xlabel("Aggregate Rating")
ax.set_ylabel("Votes")
ax.set_title(f"Votes vs Aggregate Rating (corr = {correlation:.2f})")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task2_votes_vs_rating.png")
plt.close()

# ---------------------------------------------------------------
# TASK 3: PRICE RANGE vs ONLINE DELIVERY & TABLE BOOKING
# ---------------------------------------------------------------
log("\n--- Task 3: Price Range vs. Online Delivery and Table Booking ---\n")

delivery_by_price = pd.crosstab(df['Price range'], df['Has Online delivery'], normalize='index') * 100
booking_by_price = pd.crosstab(df['Price range'], df['Has Table booking'], normalize='index') * 100

log("Percentage of restaurants offering ONLINE DELIVERY, by price range:")
for price, row in delivery_by_price.iterrows():
    log(f"  Price range {price}: {row.get('Yes', 0):.2f}% offer online delivery")

log("\nPercentage of restaurants offering TABLE BOOKING, by price range:")
for price, row in booking_by_price.iterrows():
    log(f"  Price range {price}: {row.get('Yes', 0):.2f}% offer table booking")

log("\nObservation: Table booking availability tends to rise sharply with price "
    "range (higher-end restaurants offer it far more often), while online "
    "delivery shows a different, often non-monotonic pattern -- it's most "
    "common among the mid-range restaurants and less common at the very top "
    "price tier, where fine-dining establishments are less likely to offer delivery.")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
delivery_by_price['Yes'].plot(kind='bar', ax=axes[0], color="#55A868")
axes[0].set_title("Online Delivery Availability by Price Range")
axes[0].set_ylabel("% Offering Online Delivery")
axes[0].set_xlabel("Price Range")
axes[0].tick_params(axis='x', rotation=0)

booking_by_price['Yes'].plot(kind='bar', ax=axes[1], color="#8172B2")
axes[1].set_title("Table Booking Availability by Price Range")
axes[1].set_ylabel("% Offering Table Booking")
axes[1].set_xlabel("Price Range")
axes[1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig(f"{OUT_DIR}/task3_price_vs_services.png")
plt.close()

with open(f"{OUT_DIR}/Level3_Report.txt", "w") as f:
    f.write("\n".join(report_lines))

print("\nLevel 3 analysis complete. Charts and report saved to:", OUT_DIR)
