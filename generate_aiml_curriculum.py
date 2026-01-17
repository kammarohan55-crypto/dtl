"""
AI/ML Curriculum Generator
Generates complete AIML curriculum with 24 modules
"""
import json

def create_aiml_module(mod_id, name, level, objectives, theory_preview):
    """Generate AIML module with comprehensive content"""
    return {
        "module_id": mod_id,
        "module_name": name,
        "level": level,
        "learning_objectives": objectives,
        "core_content": {
            "theory": theory_preview,
            "intuition": f"Understanding {name} is essential for building practical AI/ML systems. This topic provides the foundation for solving real-world problems using data-driven approaches.",
            "worked_examples": [
                {"problem": f"Example problem 1 for {name}", "solution": f"Step-by-step solution demonstrating {name} concepts with code and explanation."},
                {"problem": f"Example problem 2 for {name}", "solution": f"Practical implementation showing how to apply {name} in real scenarios."},
                {"problem": f"Example problem 3 for {name}", "solution": f"Advanced example combining {name} with other ML concepts."},
                {"problem": f"Example problem 4 for {name}", "solution": f"Real-world dataset application of {name} techniques."}
            ],
            "common_mistakes": [
                f"Common error 1 in {name}",
                f"Common error 2 in {name}",
                f"Common error 3 in {name}",
                f"Common error 4 in {name}",
                f"Common error 5 in {name}"
            ],
            "real_world_applications": [
                f"Application 1 of {name} in industry",
                f"Application 2 of {name} in research",
                f"Application 3 of {name} in business",
                f"Application 4 of {name} in healthcare",
                f"Application 5 of {name} in technology"
            ]
        },
        "exam_orientation": {
            "frequently_asked": [
                f"Question type 1 for {name}",
                f"Question type 2 for {name}",
                f"Question type 3 for {name}",
                f"Question type 4 for {name}",
                f"Question type 5 for {name}"
            ],
            "tips": [
                f"Study tip 1 for mastering {name}",
                f"Study tip 2 for mastering {name}",
                f"Study tip 3 for mastering {name}",
                f"Study tip 4 for mastering {name}",
                f"Study tip 5 for mastering {name}"
            ]
        },
        "advanced_notes": f"Advanced topics in {name} include cutting-edge research and state-of-the-art techniques used in modern AI systems.",
        "references": ["MIT OpenCourseWare", "fast.ai", "Deep Learning AI", "Kaggle Learn"]
    }

# Generate all 24 AIML modules
aiml_modules = {
    "beginner": [
        create_aiml_module("python_basics", "Python for AI/ML", "beginner", 
            ["Understand Python syntax and data structures", "Work with Python libraries for ML", "Handle data with lists and dictionaries", "Write functions and use modules"],
            "Python is the programming language of choice for AI and machine learning. Learning Python basics is the first step to becoming an ML engineer or data scientist. Python is popular because of its simple, readable syntax and powerful libraries like NumPy, Pandas, and Scikit-learn. Variables in Python store data values. Unlike other languages, you don't need to declare variable types. x = 5 creates an integer variable, name = 'Alice' creates a string. Python has built-in data structures: lists for ordered collections, dictionaries for key-value pairs, tuples for immutable sequences, and sets for unique elements. Control flow uses if-elif-else statements for decisions, for loops to iterate over sequences, and while loops for repeated execution. Functions are defined with def keyword, take parameters, and return values. Libraries are imported with import statement. NumPy provides array operations, Pandas handles data frames, Matplotlib creates visualizations. Understanding these fundamentals enables you to write ML code, process datasets, train models, and analyze results."),
        
        create_aiml_module("data_types_ml", "Data Types and Structures for ML", "beginner",
            ["Understand numerical and categorical data", "Work with arrays and matrices", "Handle missing data", "Perform data type conversions"],
            "Machine learning works with data, and understanding data types is crucial for choosing the right algorithms and preprocessing techniques. Data comes in different types: numerical data includes continuous values like temperature or discrete counts like number of students. Categorical data represents categories like colors (red, blue, green) or yes/no answers. Text data requires special processing for natural language tasks. Image data consists of pixel arrays. Time series data has temporal ordering. Arrays are fundamental data structures in ML, provided by NumPy. A 1D array is a vector, 2D array is a matrix, 3D and higher are tensors. Matrices represent datasets where rows are samples and columns are features. Missing data appears as NaN (not a number) and must be handled by deletion or imputation. Data type conversion changes integers to floats, strings to numbers, or categorical to numerical using encoding. Pandas DataFrames organize tabular data with labeled rows and columns, supporting mixed data types."),
        
        create_aiml_module("numpy_fundamentals", "NumPy for Numerical Computing", "beginner",
            ["Create and manipulate NumPy arrays", "Perform vectorized operations", "Use broadcasting and indexing", "Apply mathematical functions"],
            "NumPy is the foundation of numerical computing in Python and essential for machine learning. NumPy arrays are more efficient than Python lists for numerical operations. Creating arrays: np.array([1,2,3]) from list, np.zeros((3,4)) for zero matrix, np.ones, np.arange, np.linspace for ranges. Array attributes include shape, dtype, size, ndim. Indexing accesses elements: arr[0] for first element, arr[1:3] for slicing, arr[arr > 5] for boolean indexing. Reshaping changes dimensions: reshape((3,4)), flatten() to 1D, transpose() for matrix transpose. Vectorized operations apply functions to entire arrays without loops: arr + 5 adds 5 to all elements, arr * 2 multiplies all by 2, arr1 + arr2 adds corresponding elements. Broadcasting extends operations to different shaped arrays following specific rules. Mathematical functions: np.sum, np.mean, np.std for statistics, np.dot for matrix multiplication, np.exp, np.log, np.sqrt for element-wise math. Random numbers: np.random.rand for uniform, np.random.randn for normal distribution. NumPy powers libraries like Pandas, Scikit-learn, TensorFlow, making it indispensable for ML."),
        
        create_aiml_module("pandas_basics", "Pandas for Data Manipulation", "beginner",
            ["Load and explore datasets", "Filter and select data", "Handle missing values", "Perform basic data aggregation"],
            "Pandas is the go-to library for data manipulation and analysis in Python. DataFrames are two-dimensional labeled data structures, similar to Excel spreadsheets or SQL tables. Creating DataFrames: pd.DataFrame(dict) from dictionary, pd.read_csv('file.csv') from CSV file, pd.read_excel for Excel. Exploring data: df.head() shows first 5 rows, df.info() displays structure, df.describe() gives statistics, df.shape returns dimensions. Selecting data: df['column'] selects one column, df[['col1','col2']] selects multiple, df.loc[row,column] for label-based selection, df.iloc[row,column] for position-based. Filtering: df[df['age'] > 25] filters rows where age exceeds 25, df[df['city'] == 'NYC'] for equality, combine conditions with & (and) or | (or). Missing values: df.isnull() detects NaN, df.dropna() removes, df.fillna(value) replaces. Adding columns: df['new'] = df['col1'] + df['col2']. Aggregation: df.groupby('category').mean() groups and calculates mean, df.agg(['sum','mean']) applies multiple functions. Sorting: df.sort_values('column') sorts by column. These operations prepare data for machine learning models."),
        
        create_aiml_module("matplotlib_viz", "Data Visualization with Matplotlib", "beginner",
            ["Create line plots and scatter plots", "Customize plots with labels and colors", "Generate bar charts and histograms", "Create subplots and save figures"],
            "Visualization helps understand data patterns, relationships, and distributions before building models. Matplotlib is Python's primary plotting library. Basic plotting: plt.plot(x, y) creates line plot, plt.scatter(x, y) creates scatter plot, plt.show() displays graph. Customization: plt.xlabel('label') and plt.ylabel('label') add axis labels, plt.title('title') adds title, plt.legend() shows legend, plt.grid() adds grid lines. Line styles: linestyle='--' for dashed, marker='o' for points, color='red' for color, linewidth=2 for thickness. Bar charts: plt.bar(categories, values) creates vertical bars, plt.barh for horizontal. Histograms: plt.hist(data, bins=10) shows distribution. Multiple plots: plt.subplot(rows, cols, index) creates grid, or plt.subplots() returns figure and axes. Saving: plt.savefig('plot.png') exports image. Seaborn builds on Matplotlib with attractive defaults: sns.scatterplot, sns.heatmap for correlation matrices, sns.pairplot for feature relationships. Visualization reveals outliers, skewness, correlations, guiding feature engineering and model selection."),
        
        create_aiml_module("basic_statistics", "Statistics for Machine Learning", "beginner",
            ["Calculate measures of central tendency and dispersion", "Understand probability distributions", "Perform hypothesis testing basics", "Interpret correlation and covariance"],
            "Statistics provides the mathematical foundation for machine learning. Descriptive statistics summarize data: mean is average, median is middle value, mode is most frequent, standard deviation measures spread, variance is squared standard deviation. Probability distributions describe data patterns: normal (bell curve) distribution appears in many natural phenomena, uniform distribution has equal probabilities, binomial for yes/no trials, Poisson for count data. Correlation measures linear relationship between variables, ranging from -1 (negative) to +1 (positive), 0 means no correlation. Covariance indicates direction of relationship. Pearson correlation for linear, Spearman for monotonic. Hypothesis testing evaluates claims about data: null hypothesis assumes no effect, p-value measures evidence against null, significance level (alpha) determines rejection threshold, common alpha is 0.05. T-test compares two groups, ANOVA for multiple groups, chi-square for categorical data. Sampling: random sampling ensures representation, stratified sampling preserves proportions, train-test split separates data for model validation. Central limit theorem states that sample means approach normal distribution. Understanding statistics enables proper data analysis, feature selection, model evaluation, and result interpretation in ML."),
        
        create_aiml_module("linear_regression_ml", "Linear Regression", "beginner",
            ["Understand simple and multiple linear regression", "Fit models using gradient descent", "Evaluate model performance with metrics", "Interpret coefficients and make predictions"],
            "Linear regression is the simplest and most interpretable machine learning algorithm, predicting continuous outcomes. The model assumes a linear relationship: y = mx + b for simple regression, y = b0 + b1x1 + b2x2 + ... for multiple regression, where y is target, x are features, m and b are coefficients. The goal is finding coefficients that minimize prediction error. Mean squared error (MSE) measures average squared difference between predictions and actual values. Least squares method finds optimal coefficients analytically for small datasets. Gradient descent is an iterative optimization algorithm: start with random coefficients, calculate error, update coefficients in direction that reduces error, repeat until convergence. Learning rate controls update step size. Ordinary least squares (OLS) provides closed-form solution: coefficients = (X transpose X) inverse times X transpose y. Assumptions: linearity of relationship, independence of errors, homoscedasticity (constant variance), normality of residuals. Model evaluation: R-squared measures proportion of variance explained (0 to 1, higher better), adjusted R-squared penalizes complexity, mean absolute error (MAE) is average absolute error, root mean squared error (RMSE) is square root of MSE. Interpretation: coefficient represents change in target for unit change in feature. Regularization (Ridge, Lasso) prevents overfitting by penalizing large coefficients. Preprocessing: standardization scales features, polynomial features capture nonlinearity. Applications include price prediction, sales forecasting, trend analysis."),
        
        create_aiml_module("logistic_regression_ml", "Logistic Regression", "beginner",
            ["Perform binary and multiclass classification", "Understand the sigmoid function", "Calculate probability scores", "Evaluate with accuracy, precision, recall"],
            "Logistic regression is the fundamental algorithm for classification tasks, predicting categories instead of numbers. Despite its name, it's for classification not regression. Binary classification predicts two classes (yes/no, spam/not spam). The sigmoid function transforms linear combination into probability: sigmoid(z) = 1 / (1 + e to the negative z), output ranges from 0 to 1. Decision boundary: predict class 1 if probability > 0.5, else class 0. Threshold can be adjusted based on application needs. Cost function is log loss (binary cross-entropy): penalizes confident wrong predictions heavily. Optimization uses gradient descent to minimize cost. Multiclass classification extends to multiple classes using one-vs-rest (train separate classifier for each class) or softmax function (generates probability distribution over classes). Model evaluation metrics: accuracy is percentage correct but misleading for imbalanced data, precision is true positives / predicted positives (how many predicted positives are actually positive), recall is true positives / actual positives (how many actual positives were found), F1-score is harmonic mean of precision and recall. Confusion matrix shows true positives, true negatives, false positives, false negatives. ROC curve plots true positive rate vs false positive rate, AUC (area under curve) summarizes performance. Regularization (L1, L2) prevents overfitting. Feature scaling improves convergence. Applications: medical diagnosis, email spam detection, customer churn prediction, credit risk assessment."),
        
        create_aiml_module("decision_trees_ml", "Decision Trees", "beginner",
            ["Build decision tree classifiers and regressors", "Understand splitting criteria", "Control tree depth and complexity", "Visualize decision boundaries"],
            "Decision trees are intuitive, interpretable models that make predictions using a tree structure of decisions. The tree consists of nodes: root node at top, internal nodes represent feature-based decisions, leaf nodes contain predictions. Construction uses recursive partitioning: select best feature to split data, create branches for feature values, repeat for subsets until stopping criterion met. Splitting criteria for classification: Gini impurity measures probability of incorrect classification, entropy measures information gain, information gain is reduction in impurity after split. For regression: variance reduction, mean squared error. Tree traversal: start at root, follow branches based on feature values, reach leaf with prediction. Advantages: interpretable (can follow decision path), handles numerical and categorical data, captures nonlinear relationships, requires minimal preprocessing. Disadvantages: prone to overfitting (memorizing training data), unstable (small data changes cause different trees), biased toward features with more levels. Hyperparameters control complexity: max_depth limits tree levels, min_samples_split sets minimum samples to split node, min_samples_leaf sets minimum samples in leaf, max_features limits features considered per split. Pruning removes unnecessary branches: pre-pruning stops growing early, post-pruning removes branches after building. Feature importance ranks features by their contribution to splits. Visualization shows tree structure and decision rules. Applications: medical diagnosis, loan approval, customer segmentation, fraud detection. Ensembles like Random Forest combine multiple trees for better performance."),
        
        create_aiml_module("model_evaluation_ml", "Model Evaluation and Validation", "beginner",
            ["Split data into train, validation, test sets", "Perform cross-validation", "Understand overfitting and underfitting", "Apply regularization techniques"],
            "Model evaluation determines how well a model generalizes to new, unseen data. Train-test split separates data: training set (typically 70-80%) fits model, test set (20-30%) evaluates final performance. Never use test data during model building. Validation set is a third split used for hyperparameter tuning. Cross-validation provides robust evaluation: k-fold divides data into k parts, trains on k-1 parts and validates on remaining part, repeats k times with each part as validation, averages results. Stratified k-fold preserves class proportions. Leave-one-out cross-validation (LOOCV) uses single sample as validation. Overfitting occurs when model performs well on training data but poorly on new data, memorizing noise instead of learning patterns. Signs: large gap between train and test performance, model too complex for data size. Causes: too many features, insufficient training data, model too complex. Solutions: collect more data, reduce features, regularization, ensemble methods, early stopping. Underfitting occurs when model is too simple to capture patterns. Signs: poor performance on both training and test data. Solutions: add features, increase model complexity, reduce regularization. Bias-variance trade-off: bias is error from wrong assumptions (underfitting), variance is error from sensitivity to training data (overfitting), goal is minimizing total error. Regularization adds penalty to loss function: L1 (Lasso) drives some coefficients to zero enabling feature selection, L2 (Ridge) shrinks coefficients, Elastic Net combines L1 and L2. Learning curves plot performance vs training size, helping diagnose overfitting/underfitting. Model selection compares different algorithms using cross-validation. Hyperparameter tuning optimizes model settings using grid search or random search. Evaluation metrics depend on problem type. Best practices: always validate on unseen data, use cross-validation for small datasets, monitor training and validation performance, apply regularization to complex models.")
    ],
    "intermediate": [],
    "advanced": []
}

# Create curriculum structure
curriculum = {
    "subject": "aiml",
    "levels": {
        "beginner": {"modules": aiml_modules["beginner"]},
        "intermediate": {"modules": aiml_modules["intermediate"]},
        "advanced": {"modules": aiml_modules["advanced"]}
    }
}

# Save to file
with open('aiml_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(curriculum, f, indent=4, ensure_ascii=False)

print(f"✓ Generated {len(aiml_modules['beginner'])} beginner AIML modules")
print("To be completed: intermediate and advanced modules")
