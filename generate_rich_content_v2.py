"""
Rich Content Generator for Ethical AI Curriculum Builder
Generates comprehensive JSON curricula for Mathematics, AIML, and C Programming.
"""
import json
import os

def create_rich_module(mod_id, name, level, subject):
    """Generate a module with detailed, subject-specific content."""
    
    # Customized content based on subject and module
    theory_text = ""
    examples = []
    
    if subject == "mathematics":
        theory_text = (
            f"### Introduction to {name}\n\n"
            f"{name} is a fundamental concept in {level} mathematics. "
            "To understand this topic deeply, we must first look at its historical context and primary definitions. "
            "In rigorous mathematical terms, we define the core properties that govern this system.\n\n"
            "### Core Concepts\n"
            "1. **Definition**: The precise mathematical definition involves understanding the relationship between variables and constants within the system. "
            "For example, when dealing with these structures, one must pay close attention to the axioms of equality and inequality.\n"
            "2. **Properties**: Key properties include associativity, commutativity, and distributivity where applicable. "
            "Understanding these properties allows for the simplification of complex expressions.\n\n"
            "### Detailed Analysis\n"
            "Moving beyond the basics, we explore how {name} interacts with other mathematical entities. "
            "Consider the graphical representation: plotted on a Cartesian plane, these functions exhibit distinct behaviors "
            "such as linearity, curvature, or periodicity depending on their parameters.\n\n"
            "### practical Applications\n"
            "This concept is not just theoretical. It is widely used in physics for modeling motion, in economics for optimizing cost functions, "
            "and in computer science for algorithm analysis."
        )
        examples = [
            {
                "problem": f"Solve for x in the context of {name}: Given the equation 2x + 5 = 15.",
                "solution": "Step 1: Subtract 5 from both sides.\n2x = 10\n\nStep 2: Divide by 2.\nx = 5\n\nVerification: 2(5) + 5 = 10 + 5 = 15."
            },
            {
                "problem": "Explain the geometric interpretation of this concept.",
                "solution": "Geometrically, this represents a line with a slope of 2 intersecting the y-axis at (0, 5)."
            }
        ]
        
    elif subject == "aiml":
        theory_text = (
            f"### Mastering {name} in AI/ML\n\n"
            f"In the landscape of Artificial Intelligence, {name} plays a critical role in the {level} processing pipeline. "
            "Whether you are building a simple predictor or a complex neural architecture, this component is essential.\n\n"
            "### Theoretical Foundation\n"
            "At its heart, {name} relies on statistical probability and linear algebra. "
            "We model the problem space by defining a loss function that we seek to minimize. "
            "The algorithm iteratively updates its parameters using optimization techniques like Gradient Descent.\n\n"
            "### Implementation Details\n"
            "When implementing {name}, data preprocessing is key. You must normalize your inputs to ensure stability. "
            "Common libraries like TensorFlow and PyTorch provide high-level abstractions, but understanding the matrix operations "
            "(dot products, eigenvectors) is crucial for debugging.\n\n"
            "### Ethical Considerations\n"
            "As an Ethical AI Architect, consider bias. Does the dataset used for {name} represent diverse populations? "
            "Ensure that your model does not perpetuate existing societal inequalities."
        )
        examples = [
            {
                "problem": f"Implement a basic {name} utilizing Python and NumPy.",
                "solution": "```python\nimport numpy as np\n\ndef model(x):\n    return np.dot(x, weights) + bias\n```\nThis snippet shows the forward pass."
            },
            {
                "problem": "How do you handle overfitting in this context?",
                "solution": "Use regularization techniques such as L1 (Lasso) or L2 (Ridge), or implement Dropout layers if using Neural Networks."
            }
        ]

    elif subject == "programming_c":
        theory_text = (
            f"### Deep Dive into {name} in C\n\n"
            f"{name} is a powerful feature of the C language, allowing for efficient memory manipulation and system-level control. "
            "Unlike higher-level languages, C gives you direct access to hardware resources, which makes {name} both potent and dangerous.\n\n"
            "### Syntax and Semantics\n"
            "The syntax for {name} involves specific keywords and operator precedence. "
            "For instance, understanding the difference between `*` (dereference) and `&` (address-of) is vital when dealing with pointers related to {name}.\n\n"
            "### Memory Management\n"
            "Improper use of {name} can lead to segmentation faults or memory leaks. "
            "Always ensure that any memory allocated dynamically using `malloc` is properly freed using `free`.\n\n"
            "### Best Practices\n"
            "1. Always initialize variables.\n"
            "2. Use tools like Valgrind to check for leaks.\n"
            "3. Follow the principle of least privilege when exposing data via headers."
        )
        examples = [
            {
                "problem": f"Write a C program to demonstrate {name}.",
                "solution": "```c\n#include <stdio.h>\n\nint main() {\n    // Implementation of {name}\n    printf(\"Hello, {name}\");\n    return 0;\n}\n```"
            },
            {
                "problem": "Debug the following snippet related to this topic.",
                "solution": "The error was a buffer overflow. By increasing the array size to `char buf[256]`, we prevent writing past the end of the buffer."
            }
        ]

    return {
        "module_id": mod_id,
        "module_name": name,
        "level": level,
        "subject": subject,
        "learning_objectives": [
            f"Understand the core principles of {name}",
            f"Apply {name} to solve complex problems",
            f"Analyze the efficiency/implications of {name}",
            "Master the syntax and implementation details"
        ],
        "core_content": {
            "theory": theory_text,
            "intuition": f"Think of {name} as a building block. Just as bricks make a wall, {name} constructs the foundation for advanced topics.",
            "worked_examples": examples,
            "common_mistakes": [
                f"Confusing {name} with related concepts",
                "Syntax errors in implementation",
                "Overlooking edge cases",
                "ignoring performance constraints"
            ],
            "real_world_applications": [
                f"Used in high-frequency trading algorithms ({name})",
                "Essential for autonomous vehicle navigation",
                "Critical for secure cryptographic systems",
                "Foundational for scientific simulations"
            ]
        },
        "exam_orientation": {
            "frequently_asked": [
                f"Define {name} and give an example.",
                "Compare and contrast approach A vs approach B.",
                "Solve a problem involving...",
                "Write a code snippet to..."
            ],
            "tips": [
                "Focus on the definitions.",
                "Practice coding by hand.",
                "Draw diagrams to visualize the logic."
            ]
        },
        "advanced_notes": f"For advanced students: Look into research papers regarding {name} optimization.",
        "references": ["MIT OpenCourseWare", "Standard Documentation", "Academic Papers"]
    }

def generate_curriculum_file(subject, module_list):
    curriculum = {
        "subject": subject,
        "levels": {
            "beginner": {"modules": []},
            "intermediate": {"modules": []},
            "advanced": {"modules": []}
        }
    }
    
    # Split modules evenly for simplicity in this generator
    # 10 beginner, 8 intermediate, 6 advanced (TOTAL 24)
    
    for i, mod_name in enumerate(module_list):
        mod_id = mod_name.lower().replace(" ", "_").replace("&", "and").replace("/", "_")
        
        if i < 10:
            level = "beginner"
        elif i < 18:
            level = "intermediate"
        else:
            level = "advanced"
            
        module = create_rich_module(mod_id, mod_name, level, subject)
        curriculum["levels"][level]["modules"].append(module)
        
    return curriculum

# Define Module Lists (Same as Roadmap)
math_modules = [
    "Number Systems", "Linear Equations", "Algebraic Expressions", "Sets & Relations", "Functions Introduction", 
    "Coordinate Geometry", "Probability Basics", "Statistics Basics", "Polynomials", "Inequalities", # Beginner (10)
    "Matrices", "Limits & Continuity", "Differentiation", "Integration", "Differential Equations", 
    "Vector Algebra", "Permutations & Combinations", "Probability Distributions", # Intermediate (8)
    "Linear Algebra", "Multivariable Calculus", "Optimization Techniques", "Numerical Methods", 
    "Probability Theory", "Math for Machine Learning" # Advanced (6)
]

aiml_modules = [
    "Python for AI/ML", "NumPy Fundamentals", "Pandas for Data", "Data Visualization", "Statistics for ML", 
    "Linear Regression", "Logistic Regression", "Decision Trees", "K-Nearest Neighbors", "Model Evaluation", # Beginner
    "Neural Networks", "Convolutional Neural Networks", "Recurrent Neural Networks", "Natural Language Processing", 
    "Clustering Algorithms", "Dimensionality Reduction", "Ensemble Methods", "Support Vector Machines", # Intermediate
    "Transformers & Attention", "Generative Adversarial Networks", "Reinforcement Learning", "ML Operations", 
    "Advanced Deep Learning", "Advanced Optimization" # Advanced
]

c_modules = [
    "Introduction to C", "Variables & Data Types", "Operators", "Control Flow", "Loops", 
    "Functions", "Arrays", "Strings", "Pointers Basics", "Structures", # Beginner
    "Dynamic Memory", "File I/O", "Preprocessor", "Multi-file Programs", "Linked Lists", 
    "Stacks & Queues", "Recursion", "Sorting Algorithms", # Intermediate
    "Trees & Graphs", "Hash Tables", "Memory Management", "Bit Manipulation", 
    "System Programming", "Advanced Pointers" # Advanced
]

# Generate and Save
print("Generating Rich Curricula...")

math_curr = generate_curriculum_file("mathematics", math_modules)
with open('frontend/mathematics_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(math_curr, f, indent=4)
# Copy to backend/.. root as well for API access if needed, or just rely on frontend copy? 
# The implementation plan says backend loads from root, let's keep them consistent.
with open('mathematics_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(math_curr, f, indent=4)
print("✓ Mathematics Curriculum Updated")

aiml_curr = generate_curriculum_file("aiml", aiml_modules)
with open('frontend/aiml_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(aiml_curr, f, indent=4)
with open('aiml_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(aiml_curr, f, indent=4)
print("✓ AIML Curriculum Updated")

c_curr = generate_curriculum_file("programming_c", c_modules)
with open('frontend/programming_c_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(c_curr, f, indent=4)
with open('programming_c_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(c_curr, f, indent=4)
print("✓ C Programming Curriculum Updated")
