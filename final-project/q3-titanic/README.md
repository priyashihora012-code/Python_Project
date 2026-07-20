<div align="center">

# -- ! Titanic Survival Analysis ! --
### *Data Cleaning & Exploratory Analysis of Titanic Passenger Data*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-DataFrames-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Behind every survival statistic is a story — clean data helps us find it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Cleaning](#-part-a--data-cleaning)
- [📊 Part B — Survival Analysis](#-part-b--survival-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Titanic Survival Analysis** project is a complete data cleaning and exploratory data analysis pipeline built on the classic Titanic passenger dataset. Using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**, this project fixes messy, inconsistent, and missing data before visualizing the factors that influenced passenger survival.

This project is designed to:
- Practice real-world, hands-on data cleaning (duplicates, invalid values, inconsistent text, missing data)
- Handle missing values using median/mode imputation and column dropping
- Explore survival patterns by gender, passenger class, age, and fare
- Build a correlation heatmap of numeric passenger features

---

## 🎯 Problem Statement

> **Objective:** Clean the raw Titanic dataset and analyze which factors most influenced passenger survival.

The dataset (`titanic.csv`) contains passenger-level records including demographic and ticket information, along with a `Survived` flag. The task is to clean invalid/missing entries and use visual analysis to understand how gender, class, age, and fare relate to survival.

| 📂 Column | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| `PassengerId` | Numeric | Unique passenger identifier |
| `Survived` | Binary | 0 = Did not survive, 1 = Survived |
| `Pclass` | Numeric | Passenger ticket class (1st, 2nd, 3rd) |
| `Name`, `Sex`, `Age` | Mixed | Passenger demographics |
| `SibSp`, `Parch` | Numeric | Family relations aboard |
| `Ticket`, `Fare`, `Cabin` | Mixed | Ticket and fare details |
| `Embarked` | Categorical | Port of embarkation |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Full Data Cleaning Pipeline** | Duplicates, invalid ages, inconsistent text, and missing values all handled |
| 🔡 **Text Normalization** | Standardizes `Sex` and `Embarked` casing/spacing |
| 🧮 **Missing Value Imputation** | Median for `Age`/`Fare`, mode for `Embarked`, column drop for `Cabin` |
| 👫 **Survival by Gender** | Count plot comparing survival across male/female passengers |
| 🎟️ **Survival by Class** | Count plot comparing survival across passenger classes |
| 📊 **Distribution Plots** | Histograms of Age and Fare |
| 🔥 **Correlation Heatmap** | Relationships between numeric passenger features |
| 🥧 **Survival Pie Chart** | Overall survival percentage |

---

## 🏗️ Project Structure

```
📦 q3-titanic/
│
├── 📄 titanic-1.ipynb       ← Main Jupyter Notebook (analysis)
│
├── 📄 titanic.csv            ← Source dataset
│
└── 📄 README.md              ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Dataset (titanic.csv)
      │
      ▼
┌─────────────────────────────┐
│  Inspect Data (head/tail/    │
│  info/describe/isnull)       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Clean Data                  │  ← Drop duplicates, fix invalid
│                               │    ages, normalize text
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Handle Missing Values       │  ← Median/Mode fill, drop Cabin
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Visualize & Analyze         │  ← Count plots, histograms,
│                               │    heatmap, pie chart
└────────────┬────────────────┘
             │
             ▼
       Draw Conclusions ✅
```

---

## 🧹 Part A — Data Cleaning

### 📝 1. Initial Inspection

The dataset starts with **2000 rows and 12 columns**. Duplicate rows, negative ages, and inconsistent text casing in `Sex` and `Embarked` are identified during inspection.

### 🗑️ 2. Cleaning Steps

**Logic:**
```python
df.drop_duplicates(inplace=True)
df.loc[df["Age"] < 0, "Age"] = np.nan
df["Sex"] = df["Sex"].str.strip().str.lower()
df["Embarked"] = df["Embarked"].str.strip().str.upper()
```

### 🧮 3. Missing Value Imputation

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop("Cabin", axis=1, inplace=True)
```

After cleaning, the dataset is reduced to **1980 rows**, fully free of missing values.

---

## 📊 Part B — Survival Analysis

### 👫 4. Survival by Gender & Class

> Count plots comparing survival outcomes across gender and passenger class, revealing which groups had better survival odds.

```python
sns.countplot(data=df, x="Sex", hue="Survived")
sns.countplot(data=df, x="Pclass", hue="Survived")
```

### 📊 5. Age, Fare & Correlation

> Histograms show the distribution of Age and Fare, a boxplot highlights Fare outliers, and a correlation heatmap examines relationships among numeric features.

### 🥧 6. Overall Survival Rate

> A pie chart shows the overall percentage of passengers who survived versus those who did not.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data cleaning and manipulation |
| 🔢 **NumPy** | Handling invalid/missing numeric values |
| 📊 **Matplotlib** | Base plotting library |
| 🎨 **Seaborn** | Count plots, histograms, and heatmaps |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📈 Results & Insights

- 🧹 The dataset contained missing values, duplicate records, and inconsistent data, which were cleaned before analysis
- 👩 Female passengers had a **higher survival rate** than male passengers
- 🎟️ Passenger class influenced survival, with **higher-class passengers** generally showing better survival
- 👶 Most passengers belonged to a limited age range, as shown in the age distribution
- 💰 The Fare column contained several high-value outliers
- 🔥 The correlation heatmap showed relationships between the numeric variables in the dataset

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Classic dataset ideal for learning data cleaning + EDA |
| 🧹 **Realistic Cleaning Practice** | Covers duplicates, invalid values, and text normalization |
| 📊 **Multiple Visualization Types** | Count plots, histograms, boxplot, heatmap, pie chart |
| 📖 **Readable Code** | Clear, step-by-step notebook cells with markdown observations |
| 🧪 **Extensible** | Can be extended with predictive modeling (e.g. logistic regression) |

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
