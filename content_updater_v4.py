
import json
import os
import random

# ==========================================
# CONFIGURATION
# ==========================================

OUTPUT_DIR = r"c:\Users\Rohan\Desktop\dtl\frontend"
QUIZ_DIR = os.path.join(OUTPUT_DIR, "quizzes")

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Generated: {filepath}")

# ==========================================
# 1. DEEP CONTENT ENGINE (Procedural Generation)
# ==========================================

def generate_deep_theory(name, subject, category_keywords):
    """
    Generates a multi-paragraph, academic-style explanation (aiming for ~300-500 words of depth).
    """
    
    # 1. Contextual Definition (Paragraph 1)
    if subject == "programming_c":
        p1 = f"In the realm of system programming, **{name}** stands as a foundational concept. It is not merely a syntactic feature but a core mechanism that allows developers to interact directly with the machine's architecture. When we discuss {name}, we are referring to a precise instruction set or data structure that bridges high-level logic with low-level execution."
    elif subject == "mathematics":
        p1 = f"In rigorous mathematical analysis, **{name}** is a fundamental construct. It provides a framework for quantifying relationships and modeling abstract phenomena. Unlike arithmetic, which deals with concrete numbers, the study of {name} allows mathematicians to generalize patterns and solve broad classes of problems using symbolic logic."
    else: # AIML
        p1 = f"**{name}** represents a critical component in the modern Artificial Intelligence pipeline. As we move from classical algorithms to data-driven approaches, {name} serves as a key enabler for extracting patterns from high-dimensional data. It is essential for minimizing error rates and optimizing model generalization."

    # 2. Operational Logic (Paragraph 2)
    p2 = ""
    if "loop" in category_keywords:
        p2 = f"Operationally, {name} functions by evaluating a condition and executing a block of instructions repeatedly. This cyclic execution is what gives software its power to automate tasks. The CPU checks the termination criteria at each iteration, ensuring the program does not enter an infinite state unless explicitly designed to do so."
    elif "memory" in category_keywords or "pointer" in category_keywords:
        p2 = f"At the hardware level, {name} involves the direct manipulation of memory addresses. By managing the Stack and Heap, {name} allows for dynamic resource allocation, which is crucial for performance-critical applications. Failure to understand this mechanism often leads to segmentation faults or memory leaks."
    elif "equation" in category_keywords or "algebra" in category_keywords:
        p2 = f"The core mechanism of {name} relies on balancing equations. By isolating variables and applying inverse operations, we can determine unknown values. This process adheres to strict axioms, ensuring that the equality holds true across all transformations."
    elif "neural" in category_keywords:
        p2 = f"Technically, {name} operates through a series of matrix multiplications and non-linear transformations. Each 'neuron' in this architecture computes a weighted sum of its inputs, adds a bias, and passes the result through an activation function. This layered approach allows the system to approximate complex, non-convex functions."
    else:
        p2 = f"The operational logic of {name} is multifaceted. It begins with the standard initialization of parameters, followed by a systematic execution phase. In professional environments, {name} is often optimized for efficiency, ensuring it scales correctly with input size."

    # 3. Significance & Application (Paragraph 3)
    p3 = f"Why is {name} considered indispensable? In real-world engineering, it allows for the construction of robust systems. Whether it is optimizing a database query, rendering 3D graphics, or predicting stock market trends, concepts derived from {name} are at work. Mastery of this topic differentiates a novice from an expert, as it requires both theoretical understanding and practical intuition."

    return f"{p1}\n\n{p2}\n\n{p3}"

def get_smart_formula(name, subject):
    """Returns valid LaTeX ($$) or Code Block (```) based on context."""
    name_lower = name.lower()
    
    if subject == "programming_c":
        if "pointer" in name_lower:
            return "```c\nint x = 10;\nint *ptr = &x;\nprintf(\"Value: %d\", *ptr);\n```"
        if "loop" in name_lower:
            return "```c\nfor(int i=0; i<N; i++) {\n    // O(N) Complexity\n    process(i);\n}\n```"
        if "struct" in name_lower:
            return "```c\nstruct Entity {\n    int id;\n    float value;\n};\n```"
        return "```c\n// Standard Implementation\nvoid execute_logic() {\n    // Critical Section\n}\n```"
        
    elif subject == "mathematics":
        if "integ" in name_lower: return r"$$ \int_{a}^{b} f(x) dx = F(b) - F(a) $$"
        if "deriv" in name_lower: return r"$$ \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h} $$"
        if "matrix" in name_lower: return r"$$ \mathbf{A} \mathbf{x} = \mathbf{b} $$"
        return r"$$ f(x) = \sum_{i=0}^{n} a_i x^i $$"
        
    else: # AIML
        if "loss" in name_lower or "regres" in name_lower: return r"$$ MSE = \frac{1}{n} \sum (y_i - \hat{y}_i)^2 $$"
        if "bayes" in name_lower: return r"$$ P(A|B) = \frac{P(B|A)P(A)}{P(B)} $$"
        return r"$$ y = \sigma(Wx + b) $$"

# ==========================================
# 2. SMART QUIZ GENERATOR V2 (Anti-Repetition)
# ==========================================

def get_random_quiz(name, subject):
    """Generates 5 distinct questions to avoid repetition."""
    questions = []
    
    # Template Pools
    q_templates = [
        # Conceptual
        {
            "q": f"Which statement best describes the primary purpose of **{name}**?",
            "opts": [
                f"It is a core mechanism for structuring logic in {subject}.",
                "It is a graphical user interface tool.",
                "It is used solely for hardware cooling.",
                "It is a deprecated feature."
            ],
            "correct": 0,
            "exp": f"{name} is fundamental to the theoretical underpinnings of {subject}."
        },
        # Operational
        {
            "q": f"When implementing **{name}**, what is a critical consideration?",
            "opts": [
                "Ensuring correct syntax and logical flow.",
                "Making sure the computer is plugged in.",
                "Using the loudest keyboard switches.",
                "Deleting all other files."
            ],
            "correct": 0,
            "exp": "Precision and logic are paramount to avoid errors."
        },
        # Outcome
        {
            "q": f"What is a common result of misusing **{name}**?",
            "opts": [
                "Logical errors or unexpected system behavior.",
                "The monitor turns blue instantly.",
                "The internet speed increases.",
                "Nothing happens."
            ],
            "correct": 0,
            "exp": "Incorrect usage typically leads to bugs, crashes, or false results."
        },
        # Contextual (Subject Specific)
        {
            "q": f"In the context of **{subject}**, how is **{name}** categorized?",
            "opts": [
                "As a fundamental building block.",
                "As a user-facing cosmetic feature.",
                "As a hardware peripheral.",
                "As a type of coffee."
            ],
            "correct": 0,
            "exp": "It plays a structural role in the discipline."
        }
    ]
    
    # Add subject-specific flavor
    if subject == "programming_c":
        q_templates.append({
            "q": f"Which of the following creates a compilation error related to **{name}**?",
            "opts": ["Missing semicolons or type mismatches.", "Too many comments.", "Variable names that are too short.", "Using tabs instead of spaces."],
            "correct": 0,
            "exp": "C is a strongly typed, syntax-sensitive language."
        })
    elif subject == "mathematics":
        q_templates.append({
            "q": f"To solve a problem involving **{name}**, what is the first step?",
            "opts": ["Define the variables and constraints.", "Guess the number 7.", "Draw a perfect circle.", "Ignore the problem."],
            "correct": 0,
            "exp": "Formulation is the first step in mathematical problem solving."
        })
    else:
        q_templates.append({
            "q": f"How does **{name}** improve model performance?",
            "opts": ["By optimizing the mapping from input to output.", "By downloading more RAM.", "By using a cooler logo.", "By ignoring the data."],
            "correct": 0,
            "exp": "AI techniques aim to minimize error functions."
        })

    # Shuffle and Build
    random.shuffle(q_templates)
    
    final_qs = []
    for i, t in enumerate(q_templates[:5]):
        # Randomize Options
        options = t["opts"]
        correct_opt = options[0] # Original correct answer
        random.shuffle(options)
        new_correct_idx = options.index(correct_opt)
        
        final_qs.append({
            "id": i+1,
            "question": t["q"],
            "options": options,
            "correct": new_correct_idx,
            "difficulty": "Medium",
            "explanation": t["exp"]
        })
        
    return {"module_id": "quiz_id", "questions": final_qs}

# ==========================================
# 3. GENERATION LOGIC
# ==========================================

# (Importing Lists - Shortened for script fit, but represents FULL LISTS)
# I will use the full lists logic 

def generate_module(mod_id, name, level, subject):
    # Determine Keywords for Smart Generation
    keywords = name.lower()
    
    # 1. Generate Deep Theory
    theory_text = generate_deep_theory(name, subject, keywords)
    
    # 2. Get Visualization/Formula
    formula = get_smart_formula(name, subject)
    
    return {
        "module_id": mod_id,
        "module_name": name,
        "level": level,
        "subject": subject,
        "learning_objectives": [
            f"Define the core principles of {name}.",
            f"Analyze the role of {name} in {subject}.",
            "Synthesize specific techniques to solve problems."
        ],
        "content_cards": {
            "motivation": {
                 "title": "Real World Application", 
                 "content": f"{name} is not just theoretical. It is used in industry to build scalable systems. Imagine trying to build a skyscraper without deep foundations; {name} provides that structural integrity for your knowledge base."
            },
            "concept_overview": {
                "title": "Conceptual Framework", 
                "points": ["Fundamental methodology.", "Critical for advanced topics.", "Requires precise logic."]
            },
            "intuition": {
                "title": "Deep Dive & Analysis", 
                "content": theory_text
            },
            "math_derivation": {
                "title": "Technical Formulation", 
                "content": formula
            },
            "worked_example": {
                "title": "Applied Scenario",
                "problem": f"Consider a standard scenario where {name} is required. Given initial conditions X, derive Y.",
                "solution": f"**Step 1:** Identification. We identify this as a {name} problem.\n\n**Step 2:** Application. We apply the standard formula/logic.\n\n**Step 3:** Verification. The result is consistent with theoretical bounds."
            },
            "key_takeaways": {
                "title": "Exam Notes",
                "points": ["Always check your initial assumptions.", "Units matter.", "Show all working steps."]
            }
        },
        "core_content": { # Legacy Support
            "theory": theory_text,
            "intuition": "See Rich Content Card."
        }
    }

# ==========================================
# 4. EXECUTION
# ==========================================

MATH_FULL = {
    "beginner": [("number_systems", "Number Systems"), ("linear_equations", "Linear Equations"), ("algebraic_expressions", "Algebraic Expressions"), ("sets_relations", "Sets and Relations"), ("functions_intro", "Introduction to Functions"), ("coordinate_geometry", "Coordinate Geometry"), ("trigonometry_basics", "Trigonometry Basics"), ("complex_numbers_intro", "Complex Numbers Introduction"), ("logarithms", "Logarithms"), ("sequences_series", "Sequences and Series"), ("limit_intro", "Introduction to Limits"), ("differentiation_basics", "Differentiation Basics"), ("integration_basics", "Integration Basics"), ("probability_basics", "Probability Basics"), ("statistics_basics", "Statistics Basics"), ("vectors_intro", "Introduction to Vectors"), ("matrices_det_intro", "Matrices & Determinants Intro"), ("conic_sections", "Conic Sections"), ("permutation_combination", "Permutation & Combination"), ("binomial_theorem", "Binomial Theorem"), ("math_logic", "Mathematical Logic"), ("inequalities", "Inequalities"), ("polynomials", "Polynomials"), ("mensuration", "Mensuration (Area & Volume)")],
    "intermediate": [("matrices", "Matrices"), ("determinants", "Determinants"), ("eigenvalues", "Eigenvalues & Eigenvectors"), ("vector_calculus", "Vector Calculus"), ("diff_equations_1", "Differential Equations I"), ("diff_equations_2", "Differential Equations II"), ("laplace_transforms", "Laplace Transforms"), ("fourier_series", "Fourier Series"), ("complex_analysis", "Complex Analysis"), ("probability_dist", "Probability Distributions"), ("numerical_methods_1", "Numerical Methods I"), ("numerical_methods_2", "Numerical Methods II"), ("partial_diff_eq", "Partial Differential Equations"), ("z_transforms", "Z-Transforms"), ("discrete_math", "Discrete Mathematics"), ("graph_theory", "Graph Theory"), ("group_theory", "Group Theory"), ("linear_algebra", "Linear Algebra Advanced")],
    "advanced": [("advanced_linear_alg", "Advanced Linear Algebra"), ("functional_analysis", "Functional Analysis"), ("topology_adv", "Advanced Topology"), ("diff_geometry", "Differential Geometry"), ("measure_theory", "Measure Theory"), ("abstract_algebra", "Abstract Algebra"), ("cryptography_math", "Mathematical Cryptography"), ("control_theory", "Control Theory"), ("chaos_theory", "Chaos Theory"), ("game_theory", "Game Theory"), ("operations_research", "Operations Research"), ("fluid_dynamics_math", "Fluid Dynamics Math"), ("quantum_mech_math", "Quantum Mechanics Math")]
}

C_FULL = {
    "beginner": [("c_intro", "Introduction to C"), ("c_environment", "Setting up Environment"), ("c_structure", "Structure of C Program"), ("variables_datatypes", "Variables & Data Types"), ("constants_literals", "Constants & Literals"), ("io_operations", "Input/Output Operations"), ("operators_arithmetic", "Arithmetic Operators"), ("operators_relational", "Relational/Logical Operators"), ("bitwise_operators", "Bitwise Operators"), ("if_else", "If-Else Statements"), ("switch_case", "Switch Case"), ("loops_while", "While & Do-While Loops"), ("loops_for", "For Loops"), ("break_continue", "Break and Continue"), ("arrays_1d", "1D Arrays"), ("arrays_2d", "2D/Multi-dimensional Arrays"), ("strings_basics", "String Handling Basics"), ("functions_basics", "User Defined Functions"), ("recursion_basics", "Recursion Basics"), ("pointers_intro", "Introduction to Pointers"), ("structures_intro", "Introduction to Structures")],
    "intermediate": [("pointers_arrays", "Pointers and Arrays"), ("pointers_functions", "Pointers and Functions"), ("dynamic_memory", "Dynamic Memory (malloc/free)"), ("structures_pointers", "Pointers to Structures"), ("unions", "Unions"), ("file_io_basics", "File I/O Basics"), ("preprocessor_directives", "Preprocessor Directives"), ("macros", "Macros in C"), ("header_files", "User Defined Header Files"), ("storage_classes", "Storage Classes"), ("error_handling", "Error Handling (errno)"), ("sorting_algos", "Basic Sorting Algorithms"), ("searching_algos", "Basic Searching Algorithms"), ("linked_list_singly", "Singly Linked Lists"), ("linked_list_doubly", "Doubly Linked Lists"), ("stacks_c", "Stacks Implementation"), ("queues_c", "Queues Implementation"), ("command_line_args", "Command Line Arguments")],
    "advanced": [("adv_pointers", "Advanced Pointers"), ("memory_leaks", "Debugging Memory Leaks"), ("optimization_c", "Code Optimization Techniques"), ("multithreading_c", "Multithreading Basics"), ("socket_prog", "Socket Programming Basics"), ("system_calls", "System Calls"), ("process_management", "Process Management"), ("ipc_basics", "Inter-Process Communication"), ("shared_memory", "Shared Memory"), ("semaphores", "Semaphores"), ("makefiles", "Makefiles & Build Systems"), ("embedded_c_intro", "Introduction to Embedded C"), ("kernel_modules", "Basics of Kernel Modules"), ("trees_bst", "Binary Search Trees"), ("graphs_c", "Graph Representation")]
}

AIML_FULL = {
    "beginner": [("python_basics", "Python for AI/ML"), ("numpy_fundamentals", "NumPy Fundamentals"), ("pandas_basics", "Pandas for Data Manipulation"), ("matplotlib_viz", "Data Visualization"), ("basic_stats", "Basic Statistics for ML"), ("linear_regression_ml", "Linear Regression (ML)"), ("logistic_regression_ml", "Logistic Regression (ML)"), ("knn_ml", "K-Nearest Neighbors"), ("decision_trees_ml", "Decision Trees"), ("naive_bayes", "Naive Bayes"), ("scikit_learn_intro", "Scikit-Learn Introduction")],
    "intermediate": [("svm", "Support Vector Machines"), ("random_forest", "Random Forest"), ("gradient_boosting", "Gradient Boosting"), ("kmeans_clustering", "K-Means Clustering"), ("neural_networks_intro", "Introduction to Neural Networks"), ("deep_learning_basics", "Deep Learning Basics"), ("tensorflow_intro", "TensorFlow & Keras"), ("pytorch_intro", "PyTorch Basics"), ("cnn_basics", "Convolutional Neural Networks"), ("rnn_basics", "Recurrent Neural Networks"), ("nlp_basics", "NLP Basics")],
    "advanced": [("transformers_attention", "Transformers & Attention"), ("bert_gpt", "BERT and GPT Models"), ("generative_ai", "Generative AI"), ("gans", "Generative Adversarial Networks"), ("reinforcement_learning", "Reinforcement Learning"), ("mlops_intro", "Introduction to MLOps"), ("ethics_in_ai", "Ethics in AI")]
}

def main():
    subjects = [("mathematics", MATH_FULL), ("aiml", AIML_FULL), ("programming_c", C_FULL)]
    
    for subj_key, level_map in subjects:
        print(f"Deep Updating: {subj_key}...")
        curriculum = {"subject": subj_key, "levels": {}}
        quizzes = {}
        
        for level, modules in level_map.items():
            level_data = {"modules": []}
            for mod_id, mod_name in modules:
                # Content
                mod_data = generate_module(mod_id, mod_name, level, subj_key)
                level_data["modules"].append(mod_data)
                
                # Quiz
                quizzes[mod_id] = get_random_quiz(mod_name, subj_key)
            
            curriculum["levels"][level] = level_data
            
        save_json(os.path.join(OUTPUT_DIR, f"{subj_key}_curriculum.json"), curriculum)
        save_json(os.path.join(QUIZ_DIR, f"{subj_key}_quizzes.json"), quizzes)

if __name__ == "__main__":
    main()
