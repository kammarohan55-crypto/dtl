
import json
import os

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
# CONTENT GENERATORS
# ==========================================

def get_math_module(id, name, level):
    # Dynamic content generation based on module name for Mathematics
    # Enforcing LaTeX and Lab Manual constraints
    
    # Generic templates customized by topic
    is_beginner = level == "beginner"
    
    definition = f"Mathematical study of {name.lower()} involving rigorous definitions and proofs."
    if "Linear" in name:
        definition = "Study of lines, planes, and linear mappings using equations of the form $ax + by = c$."
    elif "Calculus" in name or "Limits" in name:
        definition = "Analysis of change and motion dealing with limits, derivatives, and integrals."
    elif "Probability" in name:
        definition = "Measure of the likelihood that an event will occur, quantified as a number between 0 and 1."
        
    formula = r"$$ f(x) = \dots $$"
    if "Linear" in name:
        formula = r"$$ y = mx + c $$"
    elif "Limits" in name:
        formula = r"$$ \lim_{x \to a} f(x) = L $$"
    elif "Matrices" in name:
        formula = r"$$ A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} $$"
        
    return {
        "module_id": id,
        "module_name": name,
        "level": level,
        "subject": "mathematics",
        "learning_objectives": [
            f"Define {name} and its fundamental properties.",
            f"Solve problems involving {name} using standard formulas.",
            "Apply concepts to engineering and real-world scenarios."
        ],
        "content_cards": {
            "motivation": {
                "title": "Definition & Significance",
                "content": definition
            },
            "concept_overview": {
                "title": "Key Concepts",
                "points": [
                    f"{name} forms the backbone of engineering mathematics.",
                    "Crucial for modeling physical systems.",
                    "Requires understanding of prerequisite algebraic structures.",
                    "focus on logical derivation and proof."
                ]
            },
            "intuition": {
                "title": "Intuitive Understanding",
                "content": f"Think of {name} not just as abstract symbols, but as a tool to describe the real world. For instance, in physics, it models forces; in CS, it optimizes algorithms. Visualization is key to mastering this."
            },
            "math_derivation": {
                "title": "Important Formulas / Rules",
                "content": f"Key mathematical relationship:\n\n{formula}\n\nWhere variables represent system states or inputs."
            },
            "worked_example": {
                "title": "Worked Example",
                "problem": f"Solve a standard problem involving {name}.",
                "solution": f"**Step 1:** Identify the given values.\n**Step 2:** Apply the formula {formula}.\n**Step 3:** Substitute and solve.\n\nResult leads to a verified solution."
            },
            "key_takeaways": {
                "title": "Key Takeaways & Common Mistakes",
                "points": [
                    "Always check units and dimensions.",
                    "Don't confuse variables with constants.",
                    "Verify your final answer with a quick check."
                ]
            }
        },
        "core_content": {
             # Legacy support if needed, but we focus on content_cards
             "theory": "Legacy placeholder",
             "worked_examples": [],
             "intuition": "",
             "common_mistakes": [],
             "real_world_applications": []
        }
    }

def get_aiml_module(id, name, level):
    # Content for AI/ML
    definition = f"A subfield of AI focusing on {name}."
    if "Neural" in name:
        definition = "Computational models inspired by the human brain's network of neurons."
    elif "Regression" in name:
        definition = "Statistical method to model the relationship between a dependent and independent variable."
        
    return {
        "module_id": id,
        "module_name": name,
        "level": level,
        "subject": "aiml",
        "learning_objectives": [
            f"Understand the core intuition behind {name}.",
            "Implement basic algorithms related to this topic.",
            "Analyze performance and common pitfalls."
        ],
        "content_cards": {
            "motivation": {
                "title": "Definition",
                "content": definition
            },
            "concept_overview": {
                "title": "Core Concepts",
                "points": [
                    "Data-driven approach to problem solving.",
                    "Requires training on labeled or unlabeled datasets.",
                    "Performance measured by accuracy, precision, and recall."
                ]
            },
            "intuition": {
                "title": "Intuition",
                "content": f"Imagine teaching a child to recognize patterns. {name} works similarly by optimizing parameters to minimize error. It learns from examples rather than explicit rules."
            },
            "math_derivation": {
                "title": "Key Algorithm / Formula",
                "content": r"$$ J(\theta) = \frac{1}{2m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2 $$" + "\n\n(Example Cost Function)"
            },
            "worked_example": {
                "title": "Practical Example",
                "problem": f"How to apply {name} to a dataset?",
                "solution": "1. **Data Prep**: Clean and normalize data.\n2. **Model Selection**: Choose the algorithm.\n3. **Training**: Fit the model to data.\n4. **Evaluation**: Test on unseen data."
            },
            "key_takeaways": {
                "title": "Key Takeaways",
                "points": [
                    "Data quality is more important than algorithm complexity.",
                    "Beware of overfitting.",
                    "Always split data into train/test sets."
                ]
            }
        },
        "core_content": {}
    }

def get_c_module(id, name, level):
    # Content for C Programming
    definition = f"Programming concept dealing with {name}."
    code_snippet = "int main() { \n    // code here \n    return 0; \n}"
    
    if "Pointer" in name:
        definition = "Variables that store memory addresses of other variables."
        code_snippet = "int x = 10; \nint *ptr = &x; \nprintf('%d', *ptr);"
    elif "Array" in name:
        code_snippet = "int arr[5] = {1, 2, 3, 4, 5};"
        
    return {
        "module_id": id,
        "module_name": name,
        "level": level,
        "subject": "programming_c",
        "learning_objectives": [
            f"Understand the syntax and usage of {name}.",
            "Write C programs implementing this concept.",
            "Debug common errors related to {name}."
        ],
        "content_cards": {
            "motivation": {
                "title": "Definition & Syntax",
                "content": definition
            },
            "concept_overview": {
                "title": "Key Points",
                "points": [
                    "Essential for low-level memory manipulation.",
                    "Standard feature in C99 and C11 standards.",
                    "Requires careful syntax adherence."
                ]
            },
            "intuition": {
                "title": "Mental Model",
                "content": f"Visualize {name} as a specific tool in your toolbox. It allows you to control how computer memory is accessed and modified directly."
            },
            "math_derivation": {
                "title": "Syntax & Example",
                "content": f"```c\n{code_snippet}\n```\n\n**Output:**\n```\n> Result depends on logic\n```"
            },
            "worked_example": {
                "title": "Lab Exercise",
                "problem": f"Write a program to demonstrate {name}.",
                "solution": f"**source.c**\n```c\n#include <stdio.h>\n\n{code_snippet}\n```\n\n**Explanation:**\nWe include stdio.h for I/O functions. The main function is the entry point."
            },
            "key_takeaways": {
                "title": "Viva Questions & Mistakes",
                "points": [
                    "Q: What is the size of this data type?",
                    "Missing semicolons is a common syntax error.",
                    "Always initialize variables before use."
                ]
            }
        },
         "core_content": {}
    }

def generate_quiz(module_id, name, subject):
    questions = []
    # Generate 5 standardized questions per module
    for i in range(1, 6):
        q_type = "Concept"
        if i == 2: q_type = "Syntax/Formula"
        if i == 3: q_type = "Application"
        if i == 4: q_type = "Error Analysis"
        if i == 5: q_type = "Edge Case"
        
        q_text = f"Standard question regarding {name} ({q_type})."
        options = [
            f"Correct answer for {name} context.",
            f"Incorrect option A (misconception).",
            f"Incorrect option B (unrelated).",
            f"Incorrect option C (opposite)."
        ]
        
        # Topic specific flavor
        if subject == "programming_c":
            if i == 2: q_text = "Identify the correct syntax:"
        elif subject == "mathematics":
            if i == 2: q_text = "Select the correct formula:"
        
        questions.append({
            "id": i,
            "question": q_text,
            "options": options,
            "correct": 0,
            "difficulty": "Medium" if i > 2 else "Easy",
            "explanation": f"The correct answer is derived from the fundamental definition of {name}. Option A implies... which is wrong because..."
        })
        
    return {
        "module_id": module_id,
        "questions": questions
    }

# ==========================================
# MAIN EXECUTION
# ==========================================

# Define detailed module lists for 3 subjects
# Based on common engineering curriculum standards

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
        ("mathematics", MATH_MODULES, get_math_module),
        ("aiml", AIML_MODULES, get_aiml_module),
        ("programming_c", C_MODULES, get_c_module)
    ]
    
    for subj_key, module_map, content_fn in subjects:
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
                mod_content = content_fn(mod_id, mod_name, level)
                curriculum_data["levels"][level]["modules"].append(mod_content)
                
                # 2. Generate Quiz
                quiz_content = generate_quiz(mod_id, mod_name, subj_key)
                quiz_data_all[mod_id] = quiz_content
                
        # Save Files
        save_json(os.path.join(OUTPUT_DIR, f"{subj_key}_curriculum.json"), curriculum_data)
        save_json(os.path.join(QUIZ_DIR, f"{subj_key}_quizzes.json"), quiz_data_all)

if __name__ == "__main__":
    if not os.path.exists(QUIZ_DIR):
        os.makedirs(QUIZ_DIR)
        
    generate_full_curriculum_and_quizzes()
    print("\n✅ All content and quizzes generated successfully!")
