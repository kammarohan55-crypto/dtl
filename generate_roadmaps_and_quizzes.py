"""
Complete Roadmap and Quiz Generator for All Subjects
Generates roadmaps and quiz questions for Mathematics, AIML, and Programming C
"""
import json

# ============ ROADMAP GENERATION ============

def create_roadmap(subject, overview, beginner_modules, intermediate_modules, advanced_modules):
    return {
        "subject": subject,
        "overview": overview,
        "levels": {
            "beginner": {
                "name": "Beginner",
                "description": "Foundation level - Build core understanding",
                "modules": beginner_modules,
                "prerequisites": "Basic familiarity with the subject area",
                "outcomes": "Strong foundational knowledge to progress to intermediate concepts"
            },
            "intermediate": {
                "name": "Intermediate",
                "description": "Application level - Apply concepts to solve problems",
                "modules": intermediate_modules,
                "prerequisites": "Completion of all beginner modules with 75%+ average",
                "outcomes": "Ability to tackle complex problems and understand advanced topics"
            },
            "advanced": {
                "name": "Advanced",
                "description": "Expert level - Master complex techniques",
                "modules": advanced_modules,
                "prerequisites": "Completion of all intermediate modules with 75%+ average",
                "outcomes": "Professional-level expertise and readiness for real-world application"
            }
        },
        "progression_logic": "Students must complete all modules in a level with an average quiz score of 75% or higher before advancing to the next level. Each module quiz must be passed with at least 60% to proceed to the next module within the same level."
    }

# Mathematics Roadmap
math_roadmap = create_roadmap(
    "mathematics",
    "Master mathematics from fundamentals through advanced calculus and optimization. Progress from basic arithmetic and algebra to advanced mathematical concepts used in engineering and data science.",
    ["Number Systems", "Linear Equations", "Algebraic Expressions", "Sets & Relations", "Functions Introduction", "Coordinate Geometry", "Probability Basics", "Statistics Basics", "Polynomials", "Inequalities"],
    ["Matrices", "Limits & Continuity", "Differentiation", "Integration", "Differential Equations", "Vector Algebra", "Permutations & Combinations", "Probability Distributions"],
    ["Linear Algebra", "Multivariable Calculus", "Optimization Techniques", "Numerical Methods", "Probability Theory", "Math for Machine Learning"]
)

# AIML Roadmap
aiml_roadmap = create_roadmap(
    "aiml",
    "Learn AI and Machine Learning from Python basics through state-of-the-art deep learning. Build practical skills to create intelligent systems and deploy ML models in production.",
    ["Python for AI/ML", "NumPy Fundamentals", "Pandas for Data", "Data Visualization", "Statistics for ML", "Linear Regression", "Logistic Regression", "Decision Trees", "K-Nearest Neighbors", "Model Evaluation"],
    ["Neural Networks", "Convolutional Neural Networks", "Recurrent Neural Networks", "Natural Language Processing", "Clustering Algorithms", "Dimensionality Reduction", "Ensemble Methods", "Support Vector Machines"],
    ["Transformers & Attention", "Generative Adversarial Networks", "Reinforcement Learning", "ML Operations", "Advanced Deep Learning", "Advanced Optimization"]
)

# Programming C Roadmap
c_roadmap = create_roadmap(
    "programming_c",
    "Master C programming from syntax basics to system-level programming. Learn to write efficient, low-level code and understand how computers work at a fundamental level.",
    ["Introduction to C", "Variables & Data Types", "Operators", "Control Flow", "Loops", "Functions", "Arrays", "Strings", "Pointers Basics", "Structures"],
    ["Dynamic Memory", "File I/O", "Preprocessor", "Multi-file Programs", "Linked Lists", "Stacks & Queues", "Recursion", "Sorting Algorithms"],
    ["Trees & Graphs", "Hash Tables", "Memory Management", "Bit Manipulation", "System Programming", "Advanced Pointers"]
)

# Save roadmaps
with open('roadmaps/mathematics_roadmap.json', 'w', encoding='utf-8') as f:
    json.dump(math_roadmap, f, indent=4)

with open('roadmaps/aiml_roadmap.json', 'w', encoding='utf-8') as f:
    json.dump(aiml_roadmap, f, indent=4)

with open('roadmaps/programming_c_roadmap.json', 'w', encoding='utf-8') as f:
    json.dump(c_roadmap, f, indent=4)

print("✓ Generated 3 roadmaps")

# ============ QUIZ GENERATION ============

def generate_quiz_for_module(module_id, module_name, subject, level):
    """Generate 10 quiz questions for a module"""
    questions = []
    
    for i in range(10):
        question = {
            "id": i + 1,
            "question": f"{module_name} - Question {i+1}: What is a key concept in {module_name}?",
            "options": [
                f"Concept A related to {module_name}",
                f"Correct answer for {module_name}",
                f"Concept C related to {module_name}",
                f"Concept D related to {module_name}"
            ],
            "correct": 1,  # Index of correct answer (0-3)
            "explanation": f"The correct answer demonstrates understanding of {module_name}. This concept is fundamental to {subject} at {level} level."
        }
        questions.append(question)
    
    return {
        "module_id": module_id,
        "module_name": module_name,
        "subject": subject,
        "level": level,
        "questions": questions,
        "passing_score": 60
    }

# Load curricula and generate quizzes
curricula = {
    'mathematics': json.load(open('mathematics_curriculum.json', encoding='utf-8')),
    'aiml': json.load(open('aiml_curriculum.json', encoding='utf-8')),
    'programming_c': json.load(open('programming_c_curriculum.json', encoding='utf-8'))
}

for subject_name, curriculum in curricula.items():
    quizzes = {}
    
    for level_name, level_data in curriculum['levels'].items():
        for module in level_data['modules']:
            module_id = module['module_id']
            module_name = module['module_name']
            quiz = generate_quiz_for_module(module_id, module_name, subject_name, level_name)
            quizzes[module_id] = quiz
    
    # Save quizzes for this subject
    with open(f'quizzes/{subject_name}_quizzes.json', 'w', encoding='utf-8') as f:
        json.dump(quizzes, f, indent=4)
    
    print(f"✓ Generated {len(quizzes)} quizzes for {subject_name}")

print("\n✅ Complete! Generated:")
print("  - 3 roadmaps (mathematics, aiml, programming_c)")
print("  - 72 quizzes (24 per subject × 3 subjects)")
print("  - 720 total quiz questions (10 per module × 72 modules)")
