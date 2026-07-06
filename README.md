## 📌 Project Overview

This repository contains my solutions for the Data Analysis Internship. The project focuses on Exploratory Data Analysis (EDA) of a restaurant dataset using Python, with the objective of extracting meaningful insights through data cleaning, visualization, and statistical analysis.

---

## 🎯 Objectives

- Perform exploratory data analysis on restaurant data.
- Visualize trends and distributions.
- Analyze customer ratings, cuisines, pricing, and delivery services.
- Discover business insights that can support decision-making.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📂 Repository Structure

```
Cognifyz-Data-Analysis/
│
├── Dataset/
│   └── Dataset.csv
│
├── Level1/
│   ├── Level1.ipynb
│   ├── Level1_Report.txt
│   └── Images/
│
├── Level2/
│   ├── Level2.ipynb
│   ├── Level2_Report.txt
│   └── Images/
│
├── Level3/
│   ├── Level3.ipynb
│   ├── Level3_Report.txt
│   └── Images/
│
├── README.md
└── requirements.txt
```

---

# 📊 Level 1 Tasks

### ✅ Task 1 – Top Cuisines

- Identified the three most common cuisines.
- Calculated their percentage distribution.

**Key Findings**

- North Indian – **41.46%**
- Chinese – **28.64%**
- Fast Food – **20.79%**

---

### ✅ Task 2 – City Analysis

- Identified the city with the most restaurants.
- Calculated average ratings by city.

**Key Findings**

- Highest number of restaurants: **New Delhi**
- Highest average rating (minimum 5 restaurants): **London (4.54)**

---

### ✅ Task 3 – Price Range Distribution

- Visualized restaurant price ranges.
- Calculated percentage distribution.

**Key Findings**

| Price Range | Percentage |
|-------------|-----------:|
| 1 | 46.53% |
| 2 | 32.59% |
| 3 | 14.74% |
| 4 | 6.14% |

---

### ✅ Task 4 – Online Delivery

- Compared restaurants offering online delivery.
- Analyzed ratings based on delivery availability.

**Key Findings**

- Restaurants offering delivery: **25.66%**
- Average rating with delivery: **3.25**
- Average rating without delivery: **2.47**

---

# 📊 Level 2 Tasks

### ✅ Restaurant Ratings

- Analyzed aggregate rating distribution.
- Calculated average votes.

**Most common rating category:** Average

---

### ✅ Cuisine Combination Analysis

- Identified the most common cuisine combinations.
- Compared ratings across combinations.

Examples:

- North Indian + Chinese
- North Indian + Mughlai
- Bakery + Desserts

---

### ✅ Geographic Analysis

- Visualized restaurant locations using latitude and longitude.
- Identified geographic clusters.

Main clusters were found around:

- New Delhi
- Bangalore
- London
- US cities

---

### ✅ Restaurant Chains

- Identified restaurant chains.
- Compared ratings and popularity.

Top chains include:

- Cafe Coffee Day
- Domino's Pizza
- Subway
- McDonald's
- Pizza Hut

---

# 📊 Level 3 Tasks

### ✅ Restaurant Reviews Analysis

Since the dataset did not contain review text, **Rating Text** and **Votes** were used as sentiment and engagement proxies.

Findings:

- Positive restaurants: **36.44%**
- Poor-rated restaurants: **1.95%**
- Higher-rated restaurants generally receive more votes.

---

### ✅ Votes Analysis

Analyzed relationship between customer votes and ratings.

Highest voted restaurants include:

- Toit
- Truffles
- Hauz Khas Social
- Peter Cat

Correlation between votes and ratings:

**0.314**

This indicates a moderate positive relationship.

---

### ✅ Price Range vs Online Delivery & Table Booking

Analyzed how restaurant services change across price ranges.

Findings:

- Mid-range restaurants offer online delivery most frequently.
- Premium restaurants are much more likely to provide table booking.

---

# 📈 Key Insights

- North Indian cuisine dominates the dataset.
- New Delhi contains the highest number of restaurants.
- Restaurants offering online delivery generally receive better ratings.
- Higher-rated restaurants tend to receive more customer engagement.
- Premium restaurants prioritize reservations over delivery services.

---

# 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/Cognifyz-Data-Analysis.git
```

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open any notebook and run all cells.

---

# 📸 Sample Outputs

You can include screenshots of:

- Cuisine distribution charts
- Rating histograms
- Geographic scatter plots
- Price range visualizations
- Correlation plots

---

# 📚 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Visualization
- Statistical Analysis
- Business Insight Generation
- Python Programming
- Pandas & NumPy
- Matplotlib & Seaborn

---
