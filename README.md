# AI & ML Coursework Repository (`AI_ML_HW`)

Welcome to my AI/ML study and homework repository. This project contains organized daily assignments, coding exercises, interactive Jupyter notebooks, markdown documentation, and projects covering Python fundamentals, NumPy, Pandas data analysis, Exploratory Data Analysis (EDA) with Matplotlib and Seaborn, and foundational Supervised Machine Learning with Scikit-Learn.

---

## 📁 Topics Covered & Folder Structure

### Week 1: Python Fundamentals & Git Basics

* **Day 1: Basics & Control Flow**
  * Variable assignment, f-strings, and data types
  * Simple and menu-based calculators using `match-case`
  * Number classification and even/odd logic

* **Day 2: List Operations & Algorithms**
  * Built-in list methods (`append`, `insert`, `remove`, `sort`, `reverse`)
  * Finding manual maximum and minimum values using loops
  * Calculating list sum and average with functions
  * Generating multiplication tables

* **Day 3: String Manipulations & Dictionaries**
  * Fundamental string operations (casing, length, reversing, vowel counting)
  * Manual string reversal for palindrome verification
  * Sentence word counter and character frequency mapping using dictionaries

* **Day 4: Advanced Logic & Pattern Printing**
  * Utility math functions (square, cube, factorial, simple interest)
  * Optimized prime number checking logic
  * Generating Fibonacci series
  * Nested loop patterns (right-angled, inverted, and pyramid star patterns)

* **Day 5: File I/O & Synthesis**
  * Safe file handling operations (`write`, `append`, `read`) using context managers (`with`)
  * Data structures combining dictionaries and lists for grade calculation
  * Comprehensive practice solving multi-concept programming challenges

---

### Week 2: NumPy & Pandas Data Analysis

* **Day 1: NumPy Fundamentals & Slicing**
  * Array creation (1D and 2D), inspecting `shape`, `size`, `ndim`, and `dtype`
  * Indexing and multi-dimensional array slicing
  * Element-wise arithmetic operations and universal math functions

* **Day 2: Array Manipulation & Statistics**
  * Reshaping arrays (`reshape`, `flatten`, `ravel`)
  * Generating random float and integer arrays (`np.random`)
  * Descriptive statistics (`mean`, `median`, `std`) and basic matrix operations (`@`)

* **Day 3: Pandas Series & DataFrames**
  * Pandas `Series` indexing, slicing, and conditional filtering
  * Creating `DataFrame` objects from Python dictionaries
  * Reading and inspecting CSV files using `head()`, `tail()`, `info()`, and `describe()`
  * Column selection and logical boolean filtering

* **Day 4: Data Manipulation & Cleaning**
  * Identifying (`isnull()`), filling (`fillna()`), and dropping (`dropna()`) missing values
  * Renaming columns and sorting rows (`sort_values`)
  * Creating derived calculated columns
  * Grouping and aggregating metrics using `groupby()` and `agg()`

* **Day 5: Mini Dataset Project & Integration**
  * Data cleaning, transformation, and regional performance reporting on sales data
  * Interactive Jupyter Notebook synthesis (`.ipynb`) covering NumPy and Pandas pipelines

---

### Week 3: Data Visualization & Exploratory Data Analysis (EDA)

* **Day 1: Matplotlib Fundamentals**
  * Creating basic line plots, bar charts, and scatter plots
  * Customizing titles, axis labels, legends, line styles, colors, and grid overlays
  * Exporting high-resolution figures (`plt.savefig()`)

* **Day 2: Advanced Matplotlib & Layouts**
  * Building multi-panel visualizations using subplots (`plt.subplots`)
  * Plotting histograms and box plots to inspect data distributions
  * Fine-tuning axis ticks, limits, and figure margins

* **Day 3: Seaborn & Statistical Graphics**
  * Categorical and count plots (`sns.countplot`, `sns.barplot`)
  * Visualizing multi-variable distributions with pair plots (`sns.pairplot`) and box plots
  * Computing correlation matrices and rendering heatmap visualizations (`sns.heatmap`)
  * Analyzing right-skewed and normal continuous features (mean vs. median behavior)

* **Day 4: Data Cleaning, Parsing & Outlier Detection**
  * String normalization, trimming whitespace, and dropping duplicate entries
  * Identifying numerical outliers using Interquartile Range (IQR) bounds and box plots
  * Parsing strings to datetimes, stripping symbols for float casting, and ordering categorical variables
  * Synthesizing key dataset observations backed by visual charts

* **Day 5: Mini EDA Project & Documentation**
  * End-to-end exploratory analysis on an e-commerce sales dataset
  * Charting net revenue per product category, discount sensitivity, and metric correlations
  * Comprehensive project documentation (`README.md`) detailing analytical findings and data cleaning pipelines

---

### Week 4: Scikit-Learn & Supervised Machine Learning Basics

* **Day 1: Scikit-Learn Setup & Data Workflow**
  * Feature vs. target identification ($X$ and $y$)
  * Setting up standard Scikit-Learn estimator workflows (`fit`, `predict`, `evaluate`)
  * Data splitting using `train_test_split` with stratification

* **Day 2: Linear Regression & Continuous Evaluation**
  * Fitting simple `LinearRegression` models and extracting coefficients
  * Visualizing regression fit lines against actual data points
  * Evaluating continuous models using MAE, MSE, RMSE, and $R^2$ metrics
  * Interpreting model parameters and residuals (`Day2_ModelInterpretation.md`)

* **Day 3: Logistic Regression & Classification Metrics**
  * Binary classification modeling using `LogisticRegression`
  * Evaluating model output with Accuracy Score
  * Constructing Confusion Matrices (TP, TN, FP, FN) and rendering heatmaps
  * Performance breakdown using Precision, Recall, and F1-Score in Classification Reports

* **Day 4: K-Nearest Neighbors (KNN) & Preprocessing**
  * Implementing `KNeighborsClassifier` and tuning $K$ parameters
  * Comparing `StandardScaler` (Z-score normalization) vs. `MinMaxScaler`
  * Benchmarking Logistic Regression against KNN performance
  * End-to-end classification practice on the Iris dataset

* **Day 5: Mini ML Project & Repository Integration**
  * Multi-class classification project on the Wine dataset using KNN
  * Complete ML pipeline documentation (`Day5_NotebookExplanation.md`)
  * Final repository sync and commit workflow summary (`Day5_GitSummary.md`)

---

## 🚀 How to Run

Execute any Python script or launch Jupyter Notebooks from the repository root:

```bash
# Week 1 Script Example
python Week1/Day5/Day5_StudentMarks.py

# Week 2 Notebook Launch Example
jupyter notebook Week2/Day5/Day5_MiniDatasetProject.ipynb

# Week 3 Notebook Launch Example
jupyter notebook Week3/Day5/Day5_MiniEDAProject.ipynb

# Week 4 Notebook Launch Example
jupyter notebook Week4/Day5/Day5_MiniMLProject.ipynb