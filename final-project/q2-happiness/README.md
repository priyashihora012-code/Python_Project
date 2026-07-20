<div align="center">

# -- ! World Happiness Report Analysis ! --
### *Exploratory Data Analysis of Global Happiness Scores (2019)*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrames-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Happiness isn't random — the data shows exactly what drives it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🔥 Part A — Correlation Analysis](#-part-a--correlation-analysis)
- [📊 Part B — Country-wise Insights](#-part-b--country-wise-insights)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **World Happiness Report Analysis** project explores the 2019 World Happiness Report dataset using **Pandas**, **Matplotlib**, and **Seaborn**. It investigates how factors like GDP per capita, social support, and healthy life expectancy relate to a country's overall happiness score, using correlation analysis and multiple visualization techniques.

This project is designed to:
- Practice correlation analysis between multiple numeric features
- Identify the strongest drivers of happiness across countries
- Compare top and bottom-ranked countries visually
- Apply various chart types (heatmap, scatter, bar, histogram, boxplot, pie) to a single dataset

---

## 🎯 Problem Statement

> **Objective:** Analyze the 2019 World Happiness Report to identify which factors most strongly influence a country's happiness score.

The dataset (`2019.csv`) contains happiness scores for countries along with six contributing factors. The task is to explore relationships between these factors and the overall `Score`, then visualize the happiest and least happy countries.

| 📂 Column | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| `Overall rank` | Numeric | Global happiness ranking |
| `Country or region` | Categorical | Country/region name |
| `Score` | Numeric | Overall happiness score |
| `GDP per capita` | Numeric | Economic contribution to happiness |
| `Social support` | Numeric | Social contribution to happiness |
| `Healthy life expectancy` | Numeric | Health contribution to happiness |
| `Freedom to make life choices` | Numeric | Freedom contribution to happiness |
| `Generosity` | Numeric | Generosity contribution to happiness |
| `Perceptions of corruption` | Numeric | Corruption perception contribution |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔥 **Correlation Heatmap** | Visualizes relationships between all numeric factors and happiness score |
| 📊 **Scatter Plots** | GDP, Social Support, and Life Expectancy vs Happiness Score |
| 🏆 **Top 10 Happiest Countries** | Horizontal bar chart of the highest-scoring countries |
| 📉 **Bottom 10 Happiest Countries** | Horizontal bar chart of the lowest-scoring countries |
| 📈 **Score Distribution** | Histogram with KDE curve of happiness scores |
| 📦 **Boxplot** | Identifies spread and outliers in happiness scores |
| 🥧 **Pie Chart** | Share of the top 5 happiest countries |

---

## 🏗️ Project Structure

```
📦 q2-happiness/
│
├── 📄 global.ipynb          ← Main Jupyter Notebook (analysis)
│
├── 📄 2019.csv               ← Source dataset
│
└── 📄 README.md              ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (2019.csv)
      │
      ▼
┌─────────────────────────────┐
│  Inspect Data (head/tail/    │
│  info/describe/isnull)       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Correlation Analysis        │  ← df.corr() + Heatmap
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Relationship Visualization  │  ← Scatter plots per factor
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Country Comparison          │  ← Top 10 / Bottom 10 bar charts
└────────────┬────────────────┘
             │
             ▼
       Draw Conclusions ✅
```

---

## 🔥 Part A — Correlation Analysis

### 📝 1. Correlation Heatmap

> Computes the correlation matrix of all numeric columns and visualizes it as a heatmap to spot the strongest drivers of happiness.

**Logic:**
```python
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
```

**Key Observations:**

| Factor | Correlation with Score |
|--------|------------------------|
| GDP per capita | Strong positive (0.797) |
| Healthy life expectancy | Strong positive (0.786) |
| Social support | Strong positive (0.783) |
| Freedom to make life choices | Moderate positive (0.576) |
| Perceptions of corruption | Moderate positive |
| Generosity | Very weak (0.090) |

### 📈 2. Scatter Plot Relationships

> Individual scatter plots of `Score` against GDP per capita, Social support, and Healthy life expectancy, confirming the strong positive relationships found in the heatmap.

---

## 📊 Part B — Country-wise Insights

### 🏆 3. Top & Bottom 10 Countries

> Horizontal bar charts rank the 10 happiest and 10 least happy countries using `nlargest()` and `nsmallest()` on the `Score` column.

### 📈 4. Distribution & Outliers

> A histogram with KDE shows the overall spread of happiness scores, while a boxplot highlights any outliers.

### 🥧 5. Top 5 Pie Chart

> A pie chart visualizes the relative share of the top 5 happiest countries' scores.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading and correlation analysis |
| 🔢 **NumPy** | Numerical operations |
| 📊 **Matplotlib** | Base plotting library |
| 🎨 **Seaborn** | Heatmaps, scatter plots, and bar charts |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- 💰 **GDP per Capita** has a strong positive relationship with Happiness Score
- 🤝 Countries with better **Social Support** generally have higher Happiness Scores
- 🏥 **Healthy Life Expectancy** also has a positive impact on Happiness Score
- 🇫🇮 **Finland** is the happiest country in the dataset, while bottom-ranked countries score much lower
- 📊 Most countries have Happiness Scores between **4.5 and 6.5**
- 🔥 The heatmap confirms GDP, Social Support, and Life Expectancy as the strongest happiness factors

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Simple, single-dataset correlation and visualization project |
| 📊 **Diverse Visualizations** | Heatmap, scatter, bar, histogram, boxplot, and pie chart in one notebook |
| 🌍 **Global Comparison** | Enables ranking and comparison across countries |
| 📖 **Readable Code** | Clear cell-by-cell structure with markdown observations |
| ⚡ **Lightweight** | Single CSV, no external dependencies beyond core libraries |

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
