<div align="center">

# -- ! COVID-19 Global Trends Analysis ! --
### *Exploratory Data Analysis of COVID-19 Cases, Deaths & Government Stringency*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrames-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Numbers tell the story of the pandemic — visualization helps us actually read it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Cleaning](#-part-a--data-cleaning)
- [📊 Part B — Exploratory Data Analysis](#-part-b--exploratory-data-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **COVID-19 Global Trends Analysis** project is a Python-based data analysis notebook that explores COVID-19 case, death, and government stringency data across multiple countries. Using **Pandas** for data wrangling and **Matplotlib/Seaborn** for visualization, this project walks through the complete EDA pipeline — from raw data inspection to cleaning to insight generation.

This project is designed to:
- Practice reading, inspecting, and cleaning real-world time-series data
- Handle missing values and duplicate records in a structured dataset
- Convert and work with date-time data using Pandas
- Visualize trends, distributions, and correlations using multiple chart types

---

## 🎯 Problem Statement

> **Objective:** Analyze COVID-19 case, death, and stringency data for multiple countries to uncover trends and relationships in the pandemic's progression.

The dataset (`covid-data.csv`) records daily COVID-19 statistics — total cases, new deaths, and government stringency index — for six countries. The task is to clean the dataset, understand its structure, and use visualizations to compare how the pandemic and government response evolved differently across countries.

| 📂 Column | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| `date` | Date | Date of the recorded observation |
| `location` | Categorical | Country name |
| `total_cases` | Numeric | Cumulative confirmed COVID-19 cases |
| `new_deaths` | Numeric | New deaths reported on that date |
| `stringency_index` | Numeric | Government response strictness score |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Data Cleaning** | Removes duplicate rows and handles missing values |
| 📅 **Date Parsing** | Converts `date` column to proper datetime format |
| 🌍 **Multi-Country Comparison** | Analyzes trends across six different countries |
| 📈 **Trend Line Charts** | Tracks total cases, new deaths, and stringency over time |
| 🔥 **Correlation Heatmap** | Shows relationships between cases, deaths, and stringency |
| 📊 **Distribution Analysis** | Histogram and boxplot of total cases |
| 🏳️ **Country-wise Bar Charts** | Compares total cases and average stringency by country |

---

## 🏗️ Project Structure

```
📦 q1-covide/
│
├── 📄 covid-19.ipynb        ← Main Jupyter Notebook (analysis)
│
├── 📄 covid-data.csv        ← Source dataset
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (covid-data.csv)
      │
      ▼
┌─────────────────────────────┐
│  Inspect Data (head/tail/    │
│  info/describe/columns)      │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Clean Data                  │  ← Drop duplicates, drop nulls,
│                               │    parse dates
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Sort & Reset Index          │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Visualize & Analyze         │  ← Line plots, bar plots,
│                               │    heatmap, histogram, boxplot
└────────────┬────────────────┘
             │
             ▼
       Draw Conclusions ✅
```

---

## 🧹 Part A — Data Cleaning

### 📝 1. Initial Inspection

The dataset starts with **1000 rows and 5 columns**. Basic checks (`head()`, `tail()`, `info()`, `describe()`) are used to understand structure, data types, and missing values.

### 🗑️ 2. Duplicate & Missing Value Handling

**Logic:**
```python
df = df.drop_duplicates()
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
df = df.dropna()
```

After cleaning, the dataset is reduced to **769 rows** across **6 unique countries**, sorted chronologically and reindexed for consistency.

---

## 📊 Part B — Exploratory Data Analysis

### 📈 3. Case & Death Trends Over Time

> Line plots comparing `total_cases` and `new_deaths` across countries over time, using `location` as the hue.

```python
sns.lineplot(data=df, x="date", y="total_cases", hue="location", linewidth=2)
```

### 🏛️ 4. Government Stringency Analysis

> Tracks how strict government responses were across the timeline and compares the average stringency index per country using bar charts.

### 🔥 5. Correlation & Distribution

> A correlation heatmap between `total_cases`, `new_deaths`, and `stringency_index`, along with a histogram and boxplot to study the distribution and outliers in `total_cases`.

```python
sns.heatmap(df[["total_cases","new_deaths","stringency_index"]].corr(), annot=True, cmap="Blues")
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, and manipulation |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Base plotting library |
| 🎨 **Seaborn** | Statistical visualizations (line, bar, heatmap) |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- ✅ The dataset contains COVID-19 records for **six countries**
- 📈 COVID-19 cases increased over time in all countries
- 🏛️ Government stringency levels changed across different phases of the pandemic
- 🌍 Some countries reported significantly higher total cases than others
- 🎨 Visualization made it easier to compare trends, deaths, and government response across countries

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers the full EDA pipeline in one notebook |
| 🧹 **Real-World Cleaning** | Demonstrates handling duplicates, nulls, and date parsing |
| 📊 **Multiple Visualization Types** | Line, bar, heatmap, histogram, and boxplot in one project |
| 🌍 **Comparative Analysis** | Enables cross-country comparison of pandemic response |
| 📖 **Readable Code** | Clear, well-commented notebook cells |

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

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/Priya Shihora-686533312/)

**🎓 Role:** Data Analysis Enthusiast | Python Developer \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · Matplotlib · Seaborn · EDA

</div>

---

## 🙏 Acknowledgements

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — Data manipulation reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization guide
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Data analysis courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 20 July, 2026*

</div>
