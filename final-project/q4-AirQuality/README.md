<div align="center">

# -- ! Air Quality Analysis ! --
### *Data Cleaning & Time-Series Analysis of Air Pollution Sensor Data*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrames-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Clean air starts with clean data — every sensor reading tells part of the story."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Cleaning](#-part-a--data-cleaning)
- [📊 Part B — Pollution Analysis](#-part-b--pollution-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Air Quality Analysis** project cleans and explores hourly air pollution sensor readings using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**. The raw dataset contains sensor error codes, empty columns, and missing readings, all of which are handled before analyzing pollutant levels and their relationship with weather conditions.

This project is designed to:
- Practice cleaning sensor data containing placeholder error values (`-200`)
- Remove empty/unnamed columns and rows with missing key fields
- Analyze pollutant distributions, correlations, and time trends
- Study the relationship between temperature and pollution levels

---

## 🎯 Problem Statement

> **Objective:** Clean the raw air quality sensor dataset and analyze pollution trends and their relationship with weather variables.

The dataset (`airquality.csv`) contains hourly readings of gases like CO, NOx, NO2, and Benzene, along with temperature (`T`), relative humidity (`RH`), and absolute humidity (`AH`). Sensor errors are encoded as `-200`, which must be treated as missing data before analysis.

| 📂 Column | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| `Date`, `Time` | Date/Time | Timestamp of the reading |
| `CO(GT)` | Numeric | Carbon monoxide concentration |
| `NOx(GT)`, `NO2(GT)` | Numeric | Nitrogen oxide concentrations |
| `C6H6(GT)` | Numeric | Benzene concentration |
| `T`, `RH`, `AH` | Numeric | Temperature, relative & absolute humidity |
| `PT08.S1`–`S5` | Numeric | Sensor response values |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Sensor Error Handling** | Converts `-200` placeholder values into proper `NaN` |
| 🗑️ **Column Cleanup** | Drops empty/unnamed columns from the raw CSV |
| 🧮 **Mean Imputation** | Fills missing numeric values with column means |
| 📊 **Distribution Analysis** | Histogram with KDE for CO(GT) levels |
| 🔥 **Correlation Heatmap** | Relationships among pollutants and weather variables |
| 📦 **Boxplot** | Identifies outliers in CO(GT) readings |
| 🌡️ **Scatter Plot** | Temperature vs CO(GT) relationship |
| 📈 **Time-Series Line Plot** | CO(GT) levels tracked over time |

---

## 🏗️ Project Structure

```
📦 q4-AirQuality/
│
├── 📄 air.ipynb              ← Main Jupyter Notebook (analysis)
│
├── 📄 airquality.csv          ← Source dataset
│
└── 📄 README.md               ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (airquality.csv)
      │
      ▼
┌─────────────────────────────┐
│  Inspect Data (head/tail/    │
│  info/describe/dtypes)       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Clean Data                  │  ← Drop duplicates, replace -200,
│                               │    drop empty columns
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Handle Missing Values       │  ← Mean imputation, drop
│                               │    rows missing Date/Time
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Visualize & Analyze         │  ← Histogram, heatmap, boxplot,
│                               │    scatter, line plot
└────────────┬────────────────┘
             │
             ▼
       Draw Conclusions ✅
```

---

## 🧹 Part A — Data Cleaning

### 📝 1. Initial Inspection

The dataset starts with **9471 rows and 17 columns**, including extra unnamed columns from the raw CSV export.

### 🗑️ 2. Handling Sensor Errors

**Logic:**
```python
df.replace(-200, np.nan, inplace=True)
numeric_columns = df.select_dtypes(include=np.number).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
df.drop(columns=["Unnamed: 15", "Unnamed: 16"], inplace=True)
df.dropna(subset=["Date", "Time"], inplace=True)
```

After cleaning, the dataset is reduced to **9358 valid rows**, free of sensor error codes and empty columns.

---

## 📊 Part B — Pollution Analysis

### 📊 3. CO(GT) Distribution

> A histogram with KDE curve shows how CO(GT) values are distributed, while a boxplot reveals the presence of high-value outliers.

```python
sns.histplot(df["CO(GT)"], bins=30, kde=True)
```

### 🔥 4. Correlation Between Pollutants & Weather

> A correlation heatmap examines relationships among all numeric pollutant and weather columns, helping identify which variables move together.

### 🌡️ 5. Temperature vs Pollution & Trends Over Time

> A scatter plot compares temperature against CO(GT), and a time-series line plot tracks how CO(GT) levels fluctuate across the recorded period.

```python
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
plt.plot(df["Date"], df["CO(GT)"])
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data cleaning and manipulation |
| 🔢 **NumPy** | Handling sensor error codes and means |
| 📊 **Matplotlib** | Base plotting and time-series charts |
| 🎨 **Seaborn** | Histograms, heatmaps, scatter, boxplots |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- 🧹 The dataset contained missing values, empty columns, and invalid values (`-200`), which were cleaned before analysis
- 📊 Most CO(GT) values were concentrated in a lower range, while a few high values indicated higher pollution levels
- 📦 The boxplot revealed the presence of outliers in the CO(GT) data
- 🔥 The correlation heatmap showed relationships among different air quality and weather variables
- 🌡️ The scatter plot indicated no strong linear relationship between temperature and CO(GT)
- 📈 The line plot showed that CO(GT) levels varied over time, indicating fluctuations in air quality

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Real Sensor Data Practice** | Teaches handling of encoded error values (`-200`) |
| 🧹 **Comprehensive Cleaning** | Covers empty columns, missing rows, and mean imputation |
| 📊 **Multiple Visualization Types** | Histogram, heatmap, boxplot, scatter, and time-series plot |
| ⏱️ **Time-Series Ready** | Demonstrates working with datetime-indexed pollution data |
| 📖 **Readable Code** | Clear, step-by-step notebook cells with markdown observations |

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
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/PriyaShihora-686533312/)

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
