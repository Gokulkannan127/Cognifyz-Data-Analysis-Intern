# Level 1 - Data Analysis Internship (Cognifyz Technologies)

## Contents
- `level1_analysis.py` — Python script (pandas + matplotlib) that performs all Level 1 tasks
- `Level1_Report.txt` — Text output of all findings
- `task1_top_cuisines.png` — Top 10 cuisines chart
- `task2_city_restaurant_count.png` — Top 10 cities by restaurant count
- `task3_price_range_distribution.png` — Price range distribution
- `task4_online_delivery_ratings.png` — Rating comparison by delivery availability

## Key Findings

**Task 1 — Top Cuisines**
- Top 3 cuisines: North Indian (41.46%), Chinese (28.64%), Fast Food (20.79%)

**Task 2 — City Analysis**
- Most restaurants: New Delhi (5,473)
- Highest average rating (min. 5 restaurants per city): London (4.54)

**Task 3 — Price Range Distribution**
- Price range 1 (budget): 46.53% of restaurants
- Price range 4 (premium): 6.14% of restaurants

**Task 4 — Online Delivery**
- 25.66% of restaurants offer online delivery
- Restaurants with delivery average a 3.25 rating vs. 2.47 without

## How to Run
```
pip install pandas matplotlib
python level1_analysis.py
```
Update `DATA_PATH` at the top of the script if the dataset location changes.
