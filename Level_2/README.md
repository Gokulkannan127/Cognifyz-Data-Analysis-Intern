# Level 2 - Data Analysis Internship (Cognifyz Technologies)

## Contents
- `level2_analysis.py` — Python script for all Level 2 tasks
- `Level2_Report.txt` — Text output of all findings
- `task1_rating_distribution.png`, `task1_rating_category_counts.png`
- `task2_top_cuisine_combinations.png`
- `task3_geographic_scatter.png`, `task3_geographic_india_zoom.png`
- `task4_top_restaurant_chains.png`

## Key Findings

**Task 1 — Restaurant Ratings**
- Most common rating category: "Average" (3,737 restaurants)
- Average votes per restaurant: 156.91

**Task 2 — Cuisine Combinations**
- Most common combo: North Indian + Chinese (511 restaurants)
- Highest-rated combos (min. 10 restaurants): Modern Indian (4.35), Indian (4.25), Seafood (4.11)

**Task 3 — Geographic Analysis**
- Restaurants are heavily clustered in the Delhi-NCR region (India), with smaller
  clusters across the US, UK, UAE, and other represented countries
- See scatter plots for full global distribution and a zoomed-in India cluster view

**Task 4 — Restaurant Chains**
- 734 restaurant names appear more than once (2,839 total outlets)
- Largest chain: Cafe Coffee Day (83 outlets)
- Best-rated major chain: Barbeque Nation (4.35 avg rating, 28,142 total votes across 26 outlets)

## How to Run
```
pip install pandas matplotlib
python level2_analysis.py
```
