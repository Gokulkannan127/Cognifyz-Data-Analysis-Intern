# Level 3 - Data Analysis Internship (Cognifyz Technologies)

## Contents
- `level3_analysis.py` — Python script for all Level 3 tasks
- `Level3_Report.txt` — Text output of all findings
- `task1_votes_by_sentiment.png`
- `task2_votes_vs_rating.png`
- `task3_price_vs_services.png`

## Important Note on Task 1 (Restaurant Reviews)
The provided `Dataset_.csv` does not include raw customer review text — only
a `Rating text` field (Excellent / Very Good / Good / Average / Poor / Not
rated). Since text-based keyword extraction requires actual review sentences,
this task was adapted to use `Rating text` as a sentiment proxy and `Votes`
as an engagement/volume proxy, preserving the intent of linking sentiment to
restaurant performance with the data actually available.

## Key Findings

**Task 1 — Restaurant Reviews (adapted)**
- 36.44% of restaurants are positive-leaning (Good/Very Good/Excellent); only 1.95% are "Poor"
- Restaurants rated "Excellent" average 851.8 votes vs. 48.2 for "Average" — engagement rises sharply with sentiment
- Correlation between votes and rating: 0.314 (moderate positive)

**Task 2 — Votes Analysis**
- Highest-voted restaurant: Toit, Bangalore (10,934 votes, 4.8 rating)
- Several restaurants have 0 votes and 0.0 rating (likely newly listed / no reviews yet)
- Votes vs. Rating correlation: 0.314 — more votes weakly-to-moderately associated with higher ratings

**Task 3 — Price Range vs. Online Delivery & Table Booking**
- Table booking rises sharply with price range: 0.02% (range 1) → 46.76% (range 4)
- Online delivery peaks in the mid-range (41.31% at price range 2), dropping to 9.04% at the top tier
- Higher-priced restaurants are far more likely to offer table booking, but not necessarily online delivery

## How to Run
```
pip install pandas matplotlib
python level3_analysis.py
```
