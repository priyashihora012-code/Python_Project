<div align="center">

# -- ! Retail Sales Analyzer ! --
### *Interactive Console-Based Retail Data Analysis & Visualization Tool*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"Data doesn't speak for itself — it takes a good analyzer to make it tell the story."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🔺 Part A — Data Loading & Cleaning](#-part-a--data-loading--cleaning)
- [🔢 Part B — Metrics, Filtering & Visualization](#-part-b--metrics-filtering--visualization)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Retail Sales Analyzer** is a menu-driven, interactive Python console application built with **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn** that demonstrates core data analysis concepts such as **data loading**, **cleaning**, **aggregation**, **filtering**, and **visualization**. The program presents a persistent menu interface that runs continuously until the user chooses to exit.

This project is designed to:
- Strengthen understanding of the Pandas DataFrame workflow (load → clean → analyze)
- Practice exception handling and safe user input parsing
- Apply groupby and aggregation logic to derive business metrics
- Produce clear visualizations (bar chart, line graph, heatmap) from raw retail data

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool to load, clean, analyze, and visualize retail sales data.

You are building a data analysis utility for a retail business. The program must accept a CSV dataset of sales transactions and let the user explore it — viewing summaries, cleaning missing values, computing key sales metrics, filtering records by category or product, and generating charts to reveal trends and correlations.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Load Dataset | Data I/O | Reads a retail sales CSV file into a DataFrame |
| Display Summary | Analysis | Shows shape, columns, dtypes, nulls, head, and describe() |
| Clean Data | Preprocessing | Fills missing values using fill/mean strategies |
| Calculate Metrics | Aggregation | Computes total, average, highest, and lowest sales |
| Filter Data | Query | Filters records by Category or Product |
| Bar / Line / Heatmap | Visualization | Plots sales by category, trend over time, and correlations |

The goal is to demonstrate **practical data analysis skills** through a clean, menu-driven interactive program built on real retail data.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📂 **CSV Data Loading** | Reads any retail CSV file path provided by the user |
| 🧹 **Missing Value Handling** | Fills dates, categories, prices, and quantities intelligently |
| 📊 **Dataset Summary** | Shape, dtypes, nulls, head rows, and statistical describe() |
| 🧮 **Sales Metrics** | Total, average, highest, lowest sales, top product & category |
| 🔍 **Category/Product Filter** | Search and view matching transaction records |
| 📈 **Bar Chart** | Total sales by category |
| 📉 **Line Graph** | Sales trend over time |
| 🌡️ **Correlation Heatmap** | Relationship between price, quantity sold, and total sales |
| ⚠️ **Robust Error Handling** | Catches missing files, empty data, and invalid choices |

---

## 🏗️ Project Structure

```
📦 exam/
│
├── 📄 data.ipynb            ← Main Jupyter Notebook (entry point)
│
├── 📄 retail_sales.csv      ← Retail sales dataset (5000 records)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← Options 1-9
└────────────┬────────────────┘
             │
     ┌───────┼────────────────────────┐
     ▼       ▼                        ▼
┌─────────┐ ┌────────────────┐  ┌───────────────┐
│ 1. Load │ │ 2-5. Summary /  │  │ 6-8. Bar /     │
│ Dataset │ │ Clean / Metrics │  │ Line / Heatmap │
│         │ │ / Filter        │  │                │
└────┬────┘ └────────┬────────┘  └───────┬────────┘
     │                │                   │
     ▼                ▼                   ▼
┌─────────────────────────────────────────────────┐
│           Print / Plot Output to Console          │
└────────────────────────┬──────────────────────────┘
                          │
                          ▼
                  Loop Back to Menu
                          │
                  (Choice: 9) Exit ✅
```

---

## 🔺 Part A — Data Loading & Cleaning

### 📝 1. What is the RetailAnalyzer Class?

`RetailAnalyzer` is the core class of the project. It wraps a Pandas DataFrame and exposes methods for loading, inspecting, cleaning, analyzing, and visualizing retail sales data — all driven from a single interactive `main_menu()` loop.

---

### 🗺️ 2. Core Methods — Overview

| Method | Purpose | Logic Used |
|--------|---------|------------|
| 1️⃣ | `load_data()` | Reads CSV via `pd.read_csv`, handles missing/empty file errors |
| 2️⃣ | `display_summary()` | Prints shape, columns, dtypes, nulls, head, and describe() |
| 3️⃣ | `clean_data()` | Fills missing Date, Product, Category, Price, Quantity, Total Sales |

---

### 🔺 3. Load Dataset

> Prompts the user for a CSV path and loads it into a DataFrame, with error handling for missing or empty files.

**Logic:**
```python
def load_data(self):
    file_path = input("Enter CSV file path: ")
    self.df = pd.read_csv(file_path)
    print(f"Rows    : {self.df.shape[0]}")
    print(f"Columns : {self.df.shape[1]}")
```

**Output (retail_sales.csv):**
```
Dataset Loaded Successfully.
Rows    : 5000
Columns : 6
```

---

### 🏔️ 4. Clean Data

> Fills missing values column by column using forward-fill for dates, "Unknown" for text fields, and column means for numeric fields.

**Logic:**
```python
self.df["Date"] = self.df["Date"].ffill()
self.df["Product"] = self.df["Product"].fillna("Unknown")
self.df["Category"] = self.df["Category"].fillna("Unknown")
self.df["Price"] = self.df["Price"].fillna(self.df["Price"].mean())
self.df["Quantity Sold"] = self.df["Quantity Sold"].fillna(self.df["Quantity Sold"].mean())
self.df["Total Sales"] = self.df["Total Sales"].fillna(self.df["Price"] * self.df["Quantity Sold"])
```

**Output:**
```
Missing Values Before Cleaning: ...
Missing Values After Cleaning: 0 across all columns
Data Cleaned Successfully.
```

---

### 🔻 5. Display Summary

> Prints a full dataset overview — shape, column names, data types, missing values, first 5 rows, and statistical description.

**Logic:**
```python
print(self.df.shape)
print(self.df.columns.tolist())
print(self.df.dtypes)
print(self.df.isnull().sum())
print(self.df.head())
print(self.df.describe())
```

---

## 🔢 Part B — Metrics, Filtering & Visualization

### 🔍 6. Calculate Metrics

> Computes total, average, highest, and lowest sales using NumPy, plus the most-sold product and most popular category via groupby.

**Logic:**
```python
sales = self.df["Total Sales"].dropna().to_numpy()
print(f"Total Sales   : {np.sum(sales):.2f}")
print(f"Average Sales : {np.mean(sales):.2f}")
print(f"Highest Sale  : {np.max(sales):.2f}")
print(f"Lowest Sale   : {np.min(sales):.2f}")

most_sold_product = self.df.groupby("Product")["Quantity Sold"].sum().idxmax()
most_popular_category = self.df.groupby("Category")["Total Sales"].sum().idxmax()
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔁 `pd.read_csv()` | Loads tabular data into a DataFrame |
| ➗ `groupby()` + `idxmax()` | Finds top-performing product/category |
| ➕ NumPy Aggregations | `sum`, `mean`, `max`, `min` on sales array |
| 🖨️ f-strings | Formatted metric output |
| 🎯 Filtering | Case-insensitive match on Category/Product columns |
| 📊 Matplotlib/Seaborn | Bar chart, line graph, and heatmap generation |

**Sample Output (5000-row dataset):**
```
== Sales Metrics ==
Total Sales      : 12,845,932.10
Average Sales    : 2,569.19
Highest Sale     : 9,998.40
Lowest Sale      : 12.50
Most Sold Product      : Mouse
Most Popular Category  : Electronics
```

---

### 📊 7. Filter Data

> Lets the user filter transactions by Category or Product and displays up to 10 matching records.

```python
filtered = self.df[self.df["Category"].str.lower() == category.lower()]
print(f"Total Records Found: {len(filtered)}")
print(filtered.head(10))
```

---

### 📈 8. Visualizations

| Chart | Purpose | Library |
|-------|---------|---------|
| Bar Chart | Total Sales by Category | Matplotlib |
| Line Graph | Sales Trend Over Time | Matplotlib |
| Heatmap | Correlation between Price, Quantity Sold, Total Sales | Seaborn |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🐼 **Pandas** | Latest | Data loading, cleaning, and aggregation |
| 🔢 **NumPy** | Latest | Numerical computations on sales data |
| 📊 **Matplotlib** | Latest | Bar chart and line graph plotting |
| 🌡️ **Seaborn** | Latest | Correlation heatmap visualization |
| 📓 **Jupyter Notebook** | Latest | Interactive development & execution environment |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Clean Dataset** — All missing values in Date, Product, Category, Price, Quantity Sold, and Total Sales are handled
- 🔢 **Key Sales Metrics** — Total, average, highest, and lowest sales, plus top product and category
- 🔍 **Targeted Filtering** — Instantly view transactions for any Category or Product
- 📊 **3 Visual Insights** — Bar chart, line graph, and correlation heatmap
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited
- ⚠️ **Error Feedback** — Missing files, empty data, and invalid choices are clearly reported

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers Pandas, NumPy, and visualization basics in one project |
| 🔄 **Reusability** | `RetailAnalyzer` class can be reused for any similarly structured CSV |
| 📚 **Educational** | Reinforces real-world data cleaning and aggregation workflows |
| 🖥️ **Minimal Dependencies** | Only Pandas, NumPy, Matplotlib, and Seaborn required |
| ⚡ **Fast Analysis** | Handles a 5,000-row dataset instantly |
| 🧪 **Extensible** | Easy to add new metrics, filters, or chart types |
| 📖 **Readable Code** | Clear class/method structure makes logic easy to follow |
| 🛡️ **Input Safety** | Invalid menu choices and file errors are caught and reported |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Priya Shihora

> *"Behind every clean chart is a messy dataset that got the attention it deserved."*

**🎓 Role:** Data Analysis Enthusiast | Python Developer \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Matplotlib · Seaborn · Data Cleaning & Visualization

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — DataFrame and data cleaning reference
- 🔢 [NumPy Documentation](https://numpy.org/doc/) — Numerical computing reference
- 📊 [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Plotting and visualization guide
- 🌡️ [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization guide
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 18 July, 2026*

</div>
