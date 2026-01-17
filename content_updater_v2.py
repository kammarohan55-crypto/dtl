
import json
import os
import random

# ==========================================
# CONFIGURATION & UTILITIES
# ==========================================

OUTPUT_DIR = r"c:\Users\Rohan\Desktop\dtl\frontend"
QUIZ_DIR = os.path.join(OUTPUT_DIR, "quizzes")

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Generated: {filepath}")

# ==========================================
# 1. RICH CONTENT DATABASE (Manual Overrides)
# ==========================================

RICH_CONTENT_DB = {
    # --- PROGRAMMING IN C ---
    "c_intro": {
        "motivation": "Why C? It's the lingua franca of computers. From your OS kernel to your microwave, C is everywhere.",
        "theory": "C is a high-level, structured programming language. It is efficient, portable, and allows direct manipulation of hardware/memory.",
        "intuition": "Think of C as a manual transmission car. You have total control, but you also have to shift gears yourself (manage memory).",
        "math_derive": "```c\n// The Classic 'Hello World'\n#include <stdio.h>\n\nint main() {\n    printf(\"Hello, World!\");\n    return 0;\n}\n```",
        "math_title": "Syntax: Basic Structure",
        "example_problem": "Write a program that prints your name.",
        "example_solution": "```c\n#include <stdio.h>\n\nint main() {\n    printf(\"My name is Developer\");\n    return 0;\n}\n```",
        "key_points": ["Developed by Dennis Ritchie at Bell Labs.", "Case sensitive language.", "Every C program must have a main() function."]
    },
    "constants_literals": {
        "motivation": "Some things in the universe shouldn't change, like Pi or the speed of light. In code, we call these Constants.",
        "theory": "Constants are fixed values that do not change during program execution. Literals are the raw values assigned to them (e.g., 3.14, 'A').",
        "intuition": "If a variable is a whiteboard (erasable), a constant is a stone tablet (permanent).",
        "math_derive": "```c\n// Two ways to define constants\n#define PI 3.14159           // Macro\nconst int MAX_USERS = 100;   // const keyword\n```",
        "math_title": "Syntax: Defining Constants",
        "example_problem": "Create a constant for gravity (9.8) and calculate weight for mass 10.",
        "example_solution": "```c\n#include <stdio.h>\n#define G 9.8\n\nint main() {\n    int mass = 10;\n    float weight = mass * G;\n    printf(\"Weight: %.2f\", weight);\n    return 0;\n}\n```",
        "key_points": ["#define is a preprocessor directive (no memory).", "const creates a read-only variable (uses memory).", "String literals are enclosed in double quotes."]
    },
    
    # --- MATHEMATICS ---
    "linear_equations": {
        "motivation": "Used to model relationships with a constant rate of change, like speed/distance or cost/revenue.",
        "theory": "A linear equation is an algebraic equation where each term is either a constant or the product of a constant and a single variable.",
        "intuition": "Graphically, it's always a straight line. The solution is where two lines intersect.",
        "math_derive": r"$$ y = mx + c $$" + "\n\nWhere:\n- $m$: Slope (gradient)\n- $c$: Y-intercept",
        "math_title": "Standard Form",
        "example_problem": "Solve for x: $2x + 3 = 13$",
        "example_solution": "$$ 2x = 13 - 3 $$\n$$ 2x = 10 $$\n$$ x = 5 $$",
        "key_points": ["Degree of the equation is always 1.", "In 2D, represents a line.", "Typically solved by isolation."]
    },

    # --- AIML ---
    "python_basics": {
         "motivation": "Python is the #1 language for AI because of its simplicity and powerful libraries like NumPy and PyTorch.",
         "theory": "Python is an interpreted, high-level language with dynamic semantics. Its design philosophy emphasizes code readability.",
         "intuition": "Python reads almost like English. It handles the dirty work (memory, types) so you can focus on the logic.",
         "math_derive": "```python\n# Python List Comprehension\nsquares = [x**2 for x in range(10)]\nprint(squares)\n```",
         "math_title": "Syntax: Pythonic Style",
         "example_problem": "Create a function to return the sum of a list.",
         "example_solution": "```python\ndef calculate_sum(numbers):\n    return sum(numbers)\n\nprint(calculate_sum([1, 2, 3]))\n```",
         "key_points": ["Indentation matters (whitespace sensitive).", "Dynamically typed.", "Rich ecosystem (PyPI)."]
    }
}

QUIZ_DB = {
    "constants_literals": [
        {"q": "Which keyword is used to declare a constant variable in C?", "opts": ["const", "#define", "static", "final"], "ans": 0, "exp": "'const' is the keyword. #define is a preprocessor directive."},
        {"q": "What is the correct syntax for a character literal?", "opts": ["'A'", "\"A\"", "A", "{A}"], "ans": 0, "exp": "Character literals are in single quotes. Strings are in double quotes."},
        {"q": "Does a #define macro use memory storage?", "opts": ["No, it's text substitution", "Yes, in stack", "Yes, in heap", "Depends on compiler"], "ans": 0, "exp": "Preprocessor macros are text replacements before compilation, using no runtime memory."},
        {"q": "What happens if you try to assign a value to a const variable?", "opts": ["Compilation Error", "Runtime Error", "Warning", "It updates"], "ans": 0, "exp": "Compiler forbids writing to read-only locations."},
        {"q": "Which is a floating point literal?", "opts": ["3.14", "314", "0x314", "'3.14'"], "ans": 0, "exp": "Numbers with decimal points are floating point literals."}
    ],
    "linear_equations": [
        {"q": "What is the degree of a linear equation?", "opts": ["1", "2", "0", "Undefined"], "ans": 0, "exp": "Linear means the highest power of the variable is 1."},
        {"q": "In y = mx + c, what does 'm' represent?", "opts": ["Slope", "Intercept", "Variable", "Constant"], "ans": 0, "exp": "m represents the gradient or slope of the line."},
        {"q": "How many solutions does 2x = 10 have?", "opts": ["One unique solution", "Infinite", "None", "Two"], "ans": 0, "exp": "Linear equations in one variable have one unique solution."},
        {"q": "The graph of a linear equation is a...", "opts": ["Straight Line", "Parabola", "Circle", "Hyperbola"], "ans": 0, "exp": "Linear relationships map to straight lines."},
        {"q": "If 3x + 5 = 20, what is x?", "opts": ["5", "3", "15", "4.5"], "ans": 0, "exp": "3x=15 -> x=5."}
    ]
}

# ==========================================
# 2. SMART GENERATORS
# ==========================================

def get_content_card(mod_id, name, level, subject):
    # Check Database first
    if mod_id in RICH_CONTENT_DB:
        db = RICH_CONTENT_DB[mod_id]
        return {
             "motivation": {"title": "Motivation", "content": db["motivation"]},
             "concept_overview": {"title": "Key Points", "points": db["key_points"]},
             "intuition": {"title": "Intuitive Understanding", "content": db["intuition"]},
             "math_derivation": {"title": db["math_title"], "content": db["math_derive"]},
             "worked_example": {"title": "Worked Example", "problem": db["example_problem"], "solution": db["example_solution"]},
             "key_takeaways": {"title": "Key Takeaways", "points": ["Review definitions carefully.", "Practice similar problems.", "Check units/syntax."]}
        }

    # Fallback: Smart Templates
    
    # --- C PROGRAMMING ---
    if subject == "programming_c":
        code_example = "int main() {\n    // Code \n    return 0;\n}"
        if "loop" in name.lower():
            code_example = "for(int i=0; i<10; i++) {\n    printf(\"%d\", i);\n}"
        elif "array" in name.lower():
            code_example = "int arr[5] = {1, 2, 3, 4, 5};\nprintf(\"%d\", arr[0]);"
        elif "pointer" in name.lower():
            code_example = "int x = 10;\nint *ptr = &x;\nprintf(\"%p\", ptr);"
        elif "struct" in name.lower():
            code_example = "struct Point {\n    int x;\n    int y;\n};\nstruct Point p1 = {10, 20};"
            
        return {
             "motivation": {"title": "Concept Definition", "content": f"Exploring {name}, a critical component of C programming usage."},
             "concept_overview": {"title": "Key Syntax Rules", "points": ["Follow strict syntax.", "Terminate statements with semicolons.", "Declare before use."]},
             "intuition": {"title": "Mental Model", "content": f"Think of {name} as a specific instruction to the computer's CPU."},
             "math_derivation": {"title": "Syntax Pattern", "content": f"```c\n{code_example}\n```"},
             "worked_example": {"title": "Live Coding", "problem": f"Implement {name} in a complete program.", "solution": f"```c\n#include <stdio.h>\n\nint main() {{\n    // Implementation of {name}\n    {code_example}\n    return 0;\n}}\n```"},
             "key_takeaways": {"title": "Common Bugs", "points": ["Segmentation faults.", "Syantax errors.", "Logic errors."]}
        }

    # --- MATHEMATICS ---
    elif subject == "mathematics":
        formula = r"$$ x = \dots $$"
        if "Matrix" in name: formula = r"$$ A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} $$"
        elif "Integral" in name: formula = r"$$ \int f(x) dx = F(x) + C $$"
        elif "Derivative" in name: formula = r"$$ \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h} $$"
        elif "Logic" in name: formula = r"$$ P \land Q \rightarrow R $$"
        
        return {
             "motivation": {"title": "Mathematical Context", "content": f"{name} provides a framework for solving specific classes of problems."},
             "concept_overview": {"title": "Theorems & Definitions", "points": ["Based on fundamental axioms.", "Requires logical steps.", "Used in applied math."]},
             "intuition": {"title": "Visualization", "content": "Visualize this concept as a transformation or a mapping."},
             "math_derivation": {"title": "Standard Formula", "content": formula},
             "worked_example": {"title": "Problem Solving", "problem": f"Find the value for a standard case of {name}.", "solution": f"Using the formula {formula}:\n1. Substitute knowns.\n2. Evaluate.\n3. Verify."},
             "key_takeaways": {"title": "Exam Tips", "points": ["Show all steps.", "Don't skip intermediate calculations.", "Box your final answer."]}
        }

    # --- AIML ---
    else:
        return {
             "motivation": {"title": "Machine Learning Context", "content": f"{name} is essential for building robust AI models."},
             "concept_overview": {"title": "Key Algorithm", "points": ["Data dependent.", "Optimizes objective function.", "Tuned via hyperparameters."]},
             "intuition": {"title": "How it works", "content": "It learns patterns from data to make predictions on unseen inputs."},
             "math_derivation": {"title": "Mathematical formulation", "content": r"$$ y = f(x; \theta) $$"},
             "worked_example": {"title": "Implementation", "problem": f"Train a {name} model.", "solution": "1. Import library.\n2. Fit(X, y).\n3. Predict(X_new)."},
             "key_takeaways": {"title": "Best Practices", "points": ["Clean data first.", "Check for overfitting.", "Validate metrics."]}
        }

def get_smart_quiz(mod_id, name, subject):
    # Check DB
    if mod_id in QUIZ_DB:
        q_list = QUIZ_DB[mod_id]
        final_qs = []
        for i, q in enumerate(q_list, 1):
             final_qs.append({
                 "id": i,
                 "question": q["q"],
                 "options": q["opts"],
                 "correct": q["ans"],
                 "difficulty": "Easy" if i<3 else "Medium",
                 "explanation": q["exp"]
             })
        return {"module_id": mod_id, "questions": final_qs}
        
    # Fallback Generator
    questions = []
    for i in range(1, 6):
        q_text = f"What is the primary purpose of {name}?"
        if i == 2: q_text = f"Which of the following describes {name} correctly?"
        if i == 3: q_text = f"In a standard application, how is {name} used?"
        
        options = ["Correct Option", "Wrong A", "Wrong B", "Wrong C"]
        if subject == "programming_c":
             if i==1: q_text = f"Identify the valid syntax for {name}:"
             options = ["Valid Syntax", "Syntax Error", "Logic Error", "Warning"]
             
        questions.append({
            "id": i,
            "question": q_text,
            "options": options,
            "correct": 0,
            "difficulty": "Easy",
            "explanation": f"The correct answer derives from the core definition of {name}."
        })
    return {"module_id": mod_id, "questions": questions}

# ==========================================
# 3. MODULE LISTS (Copied from V1)
# ==========================================

MATH_MODULES = {
    "beginner": [
        ("number_systems", "Number Systems"),
        ("linear_equations", "Linear Equations"),
        ("algebraic_expressions", "Algebraic Expressions"),
        ("sets_relations", "Sets and Relations"),
        ("functions_intro", "Introduction to Functions"),
        ("coordinate_geometry", "Coordinate Geometry"),
        ("trigonometry_basics", "Trigonometry Basics"),
        ("complex_numbers_intro", "Complex Numbers Introduction"),
        ("logarithms", "Logarithms"),
        ("sequences_series", "Sequences and Series"),
        ("limit_intro", "Introduction to Limits"),
        ("differentiation_basics", "Differentiation Basics"),
        ("integration_basics", "Integration Basics"),
        ("probability_basics", "Probability Basics"),
        ("statistics_basics", "Statistics Basics"),
        ("vectors_intro", "Introduction to Vectors"),
        ("matrices_det_intro", "Matrices & Determinants Intro"),
        ("conic_sections", "Conic Sections"),
        ("permutation_combination", "Permutation & Combination"),
        ("binomial_theorem", "Binomial Theorem"),
        ("math_logic", "Mathematical Logic"),
        ("inequalities", "Inequalities"),
        ("polynomials", "Polynomials"),
        ("mensuration", "Mensuration (Area & Volume)")
    ],
    "intermediate": [
        ("matrices", "Matrices"),
        ("determinants", "Determinants"),
        ("eigenvalues", "Eigenvalues & Eigenvectors"),
        ("vector_calculus", "Vector Calculus"),
        ("diff_equations_1", "Differential Equations I"),
        ("diff_equations_2", "Differential Equations II"),
        ("laplace_transforms", "Laplace Transforms"),
        ("fourier_series", "Fourier Series"),
        ("complex_analysis", "Complex Analysis"),
        ("probability_dist", "Probability Distributions"),
        ("numerical_methods_1", "Numerical Methods I"),
        ("numerical_methods_2", "Numerical Methods II"),
        ("partial_diff_eq", "Partial Differential Equations"),
        ("z_transforms", "Z-Transforms"),
        ("optimization_tech", "Optimization Techniques"),
        ("discrete_math", "Discrete Mathematics"),
        ("graph_theory", "Graph Theory"),
        ("group_theory", "Group Theory"),
        ("linear_algebra", "Linear Algebra Advanced"),
        ("calculus_multi", "Multivariable Calculus"),
        ("stochastic_proc", "Stochastic Processes"),
        ("tensor_analysis", "Tensor Analysis"),
        ("topology_intro", "Topology Introduction"),
        ("number_theory", "Number Theory")
    ],
    "advanced": [
        ("advanced_linear_alg", "Advanced Linear Algebra"),
        ("functional_analysis", "Functional Analysis"),
        ("topology_adv", "Advanced Topology"),
        ("diff_geometry", "Differential Geometry"),
        ("measure_theory", "Measure Theory"),
        ("abstract_algebra", "Abstract Algebra"),
        ("adv_prob_theory", "Advanced Probability Theory"),
        ("harmonic_analysis", "Harmonic Analysis"),
        ("combinatorics", "Advanced Combinatorics"),
        ("cryptography_math", "Mathematical Cryptography"),
        ("control_theory", "Control Theory"),
        ("chaos_theory", "Chaos Theory"),
        ("game_theory", "Game Theory"),
        ("operations_research", "Operations Research"),
        ("fluid_dynamics_math", "Fluid Dynamics Math"),
        ("quantum_mech_math", "Quantum Mechanics Math"),
        ("algebraic_geometry", "Algebraic Geometry"),
        ("representation_theory", "Representation Theory"),
        ("category_theory", "Category Theory"),
        ("complex_manifolds", "Complex Manifolds"),
        ("homological_algebra", "Homological Algebra"),
        ("operator_theory", "Operator Theory"),
         ("calculus_variations", "Calculus of Variations"),
        ("adv_numerical_analysis", "Advanced Numerical Analysis")
    ]
}

AIML_MODULES = {
    "beginner": [
         ("python_basics", "Python for AI/ML"),
        ("data_types_ml", "Data Types for Machine Learning"),
        ("numpy_fundamentals", "NumPy Fundamentals"),
        ("pandas_basics", "Pandas for Data Manipulation"),
        ("matplotlib_viz", "Data Visualization (Matplotlib)"),
        ("seaborn_viz", "Statistical Viz (Seaborn)"),
        ("basic_stats", "Basic Statistics for ML"),
        ("probability_ml", "Probability for ML"),
        ("linear_algebra_ml", "Linear Algebra for ML"),
        ("calculus_ml", "Calculus for ML"),
        ("data_preprocessing", "Data Preprocessing"),
        ("eda", "Exploratory Data Analysis"),
        ("regression_intro", "Introduction to Regression"),
        ("classification_intro", "Introduction to Classification"),
        ("clustering_intro", "Introduction to Clustering"),
        ("model_evaluation", "Model Evaluation Metrics"),
        ("train_test_split", "Train-Test Split & Validation"),
        ("linear_regression_ml", "Linear Regression (ML)"),
        ("logistic_regression_ml", "Logistic Regression (ML)"),
        ("knn_ml", "K-Nearest Neighbors"),
        ("decision_trees_ml", "Decision Trees"),
        ("naive_bayes", "Naive Bayes"),
        ("feature_engineering", "Feature Engineering"),
        ("scikit_learn_intro", "Scikit-Learn Introduction")
    ],
    "intermediate": [
         ("svm", "Support Vector Machines"),
        ("ensemble_methods", "Ensemble Methods"),
        ("random_forest", "Random Forest"),
        ("gradient_boosting", "Gradient Boosting (XGBoost)"),
        ("dim_reduction", "Dimensionality Reduction (PCA)"),
        ("kmeans_clustering", "K-Means Clustering"),
        ("hierarchical_clustering", "Hierarchical Clustering"),
        ("optimization_ml", "Optimization Algorithms"),
        ("neural_networks_intro", "Introduction to Neural Networks"),
        ("activation_functions", "Activation Functions"),
        ("backpropagation", "Backpropagation"),
        ("deep_learning_basics", "Deep Learning Basics"),
        ("tensorflow_intro", "TensorFlow & Keras"),
        ("pytorch_intro", "PyTorch Basics"),
        ("cnn_basics", "Convolutional Neural Networks (CNN)"),
        ("rnn_basics", "Recurrent Neural Networks (RNN)"),
        ("nlp_basics", "NLP Basics"),
        ("word_embeddings", "Word Embeddings"),
        ("recommender_systems", "Recommender Systems"),
        ("time_series", "Time Series Analysis"),
        ("anomaly_detection", "Anomaly Detection"),
        ("hyperparameter_tuning", "Hyperparameter Tuning"),
        ("regularization", "Regularization (L1/L2)"),
        ("ml_pipeline", "ML Pipelines")
    ],
    "advanced": [
         ("advanced_cnn", "Advanced CNN Architectures"),
        ("object_detection", "Object Detection (YOLO/SSD)"),
        ("semantic_segmentation", "Semantic Segmentation"),
        ("lstm_gru", "LSTMs and GRUs"),
        ("transformers_attention", "Transformers & Attention"),
        ("bert_gpt", "BERT and GPT Models"),
        ("generative_ai", "Generative AI"),
        ("gans", "Generative Adversarial Networks (GANs)"),
        ("vae", "Variational Autoencoders"),
        ("reinforcement_learning", "Reinforcement Learning"),
        ("q_learning", "Q-Learning & DQN"),
        ("policy_gradients", "Policy Gradients"),
        ("explainable_ai", "Explainable AI (XAI)"),
        ("mlops_intro", "Introduction to MLOps"),
        ("model_deployment", "Model Deployment"),
        ("federated_learning", "Federated Learning"),
        ("edge_ai", "Edge AI"),
        ("graph_neural_networks", "Graph Neural Networks"),
        ("transfer_learning", "Transfer Learning"),
        ("meta_learning", "Meta-Learning"),
        ("self_supervised", "Self-Supervised Learning"),
        ("robotics_ai", "AI in Robotics"),
        ("ethics_in_ai", "Ethics in AI"),
        ("future_of_ai", "Future Trends in AI")
    ]
}

C_MODULES = {
    "beginner": [
        ("c_intro", "Introduction to C"),
        ("c_environment", "Setting up Environment"),
        ("c_structure", "Structure of C Program"),
        ("variables_datatypes", "Variables & Data Types"),
        ("constants_literals", "Constants & Literals"),
        ("io_operations", "Input/Output Operations"),
        ("operators_arithmetic", "Arithmetic Operators"),
        ("operators_relational", "Relational/Logical Operators"),
        ("bitwise_operators", "Bitwise Operators"),
        ("if_else", "If-Else Statements"),
        ("switch_case", "Switch Case"),
        ("loops_while", "While & Do-While Loops"),
        ("loops_for", "For Loops"),
        ("break_continue", "Break and Continue"),
        ("arrays_1d", "1D Arrays"),
        ("arrays_2d", "2D/Multi-dimensional Arrays"),
        ("strings_basics", "String Handling Basics"),
        ("string_functions", "String Library Functions"),
        ("functions_basics", "User Defined Functions"),
        ("function_params", "Function Parameters"),
        ("recursion_basics", "Recursion Basics"),
        ("pointers_intro", "Introduction to Pointers"),
        ("pointer_arithmetic", "Pointer Arithmetic"),
        ("structures_intro", "Introduction to Structures")
    ],
    "intermediate": [
       ("pointers_arrays", "Pointers and Arrays"),
        ("pointers_functions", "Pointers and Functions"),
        ("dynamic_memory", "Dynamic Memory (malloc/free)"),
        ("structures_pointers", "Pointers to Structures"),
        ("unions", "Unions"),
        ("typedef_enums", "Typedef & Enums"),
        ("file_io_basics", "File I/O Basics"),
        ("file_modes", "File Modes & Operations"),
        ("binary_files", "Binary File Handling"),
        ("preprocessor_directives", "Preprocessor Directives"),
        ("macros", "Macros in C"),
        ("header_files", "User Defined Header Files"),
        ("storage_classes", "Storage Classes"),
        ("type_casting", "Type Casting"),
        ("error_handling", "Error Handling (errno)"),
        ("sorting_algos", "Basic Sorting Algorithms"),
        ("searching_algos", "Basic Searching Algorithms"),
        ("linked_list_singly", "Singly Linked Lists"),
        ("linked_list_doubly", "Doubly Linked Lists"),
        ("stacks_c", "Stacks Implementation"),
        ("queues_c", "Queues Implementation"),
        ("command_line_args", "Command Line Arguments"),
        ("bit_fields", "Bit Fields"),
        ("volatile_const", "Volatile & Const Keywords")
    ],
    "advanced": [
         ("adv_pointers", "Advanced Pointers (Function Pointers)"),
          ("memory_leaks", "Debugging Memory Leaks"),
          ("optimization_c", "Code Optimization Techniques"),
          ("multithreading_c", "Multithreading Basics"),
          ("socket_prog", "Socket Programming Basics"),
          ("graphics_c", "Graphics Programming in C"),
          ("system_calls", "System Calls"),
          ("process_management", "Process Management"),
          ("ipc_basics", "Inter-Process Communication"),
          ("shared_memory", "Shared Memory"),
          ("semaphores", "Semaphores"),
          ("signals_handling", "Signal Handling"),
          ("makefiles", "Makefiles & Build Systems"),
          ("static_dynamic_libs", "Static vs Dynamic Libraries"),
          ("embedded_c_intro", "Introduction to Embedded C"),
          ("kernel_modules", "Basics of Kernel Modules"),
          ("data_structures_adv", "Advanced Data Structures"),
          ("hash_tables_c", "Hash Tables Implementation"),
          ("trees_bst", "Binary Search Trees"),
          ("graphs_c", "Graph Representation"),
          ("bfs_dfs", "BFS and DFS Implementation"),
          ("complex_macros", "Complex Macros"),
          ("variadic_functions", "Variadic Functions"),
          ("secure_coding", "Secure Coding Practices")
    ]
}

def generate_full_curriculum_and_quizzes():
    subjects = [
        ("mathematics", MATH_MODULES),
        ("aiml", AIML_MODULES),
        ("programming_c", C_MODULES)
    ]
    
    for subj_key, module_map in subjects:
        curriculum_data = {
            "subject": subj_key,
            "levels": {}
        }
        quiz_data_all = {}
        
        print(f"\nProcessing {subj_key.upper()}...")
        
        for level in ["beginner", "intermediate", "advanced"]:
            curriculum_data["levels"][level] = {"modules": []}
            
            modules_list = module_map.get(level, [])
            for mod_id, mod_name in modules_list:
                # 1. Generate Content
                cards = get_content_card(mod_id, mod_name, level, subj_key)
                
                mod_content = {
                    "module_id": mod_id,
                    "module_name": mod_name,
                    "level": level,
                    "subject": subj_key,
                    "learning_objectives": [
                        f"Master the core concepts of {mod_name}.",
                        f"Solve practical problems using {mod_name}.",
                        "Understand real-world applications."
                    ],
                    "content_cards": cards,
                    "core_content": { # Minimal redundant core content for legacy/search support
                        "theory": cards["motivation"]["content"] + " " + cards["theory"]["content"] if "theory" in cards else cards["motivation"]["content"] + f" Detailed study of {mod_name}.",
                         "intuition": cards["intuition"]["content"]
                    }
                }
                
                curriculum_data["levels"][level]["modules"].append(mod_content)
                
                # 2. Generate Quiz
                quiz_content = get_smart_quiz(mod_id, mod_name, subj_key)
                quiz_data_all[mod_id] = quiz_content
                
        # Save Files
        save_json(os.path.join(OUTPUT_DIR, f"{subj_key}_curriculum.json"), curriculum_data)
        save_json(os.path.join(QUIZ_DIR, f"{subj_key}_quizzes.json"), quiz_data_all)

if __name__ == "__main__":
    if not os.path.exists(QUIZ_DIR):
        os.makedirs(QUIZ_DIR)
        
    generate_full_curriculum_and_quizzes()
    print("\n✅ content_updated_v2.py completed successfully!")
