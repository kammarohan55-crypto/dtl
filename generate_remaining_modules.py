import json

# Load existing curriculum
with open('mathematics_curriculum.json', 'r', encoding='utf-8') as f:
    curriculum = json.load(f)

# Remaining beginner modules to add
beginner_modules = [
    {
        "module_id": "sets_relations",
        "module_name": "Sets and Relations",
        "level": "beginner",
        "learning_objectives": [
            "Understand the concept of sets and their representation",
            "Perform set operations including union, intersection, and complement",
            "Identify different types of relations and their properties",
            "Apply Venn diagrams to visualize set relationships"
        ],
        "core_content": {
            "theory": "A set is a well-defined collection of distinct objects. The objects in a set are called elements or members of the set. The concept of sets is fundamental to modern mathematics and provides a foundation for many mathematical structures. Sets can contain any type of objects: numbers, letters, geometric figures, or even other sets. A set is well-defined if we can clearly determine whether a given object belongs to the set or not. For example, the set of even numbers is well-defined because we can determine if any number is even. However, the set of beautiful paintings is not well-defined because beauty is subjective. Sets are typically denoted by capital letters like A, B, C, and their elements are enclosed in curly braces. For example, A equals the set containing 1, 2, 3, 4, 5. We use the symbol that looks like a curved E to denote membership. If x is an element of set A, we write x is in A. If x is not an element of A, we write x is not in A. There are several ways to represent sets. Roster or tabular form lists all elements explicitly within braces, such as A equals the set containing 2, 4, 6, 8. Set-builder form describes the property that elements must satisfy, such as B equals the set of all x such that x is an even natural number less than 10. Venn diagrams provide a visual representation of sets using circles or closed curves. The empty set or null set is a set containing no elements, denoted by the symbol that looks like a zero with a slash through it or by empty braces. For example, the set of real numbers x such that x squared equals negative 1 is empty. A finite set has a countable number of elements. An infinite set has uncountably many elements or continues indefinitely. For example, the set containing 1, 2, 3 is finite, while the set of all natural numbers is infinite. Two sets A and B are equal if they contain exactly the same elements. Order and repetition do not matter. For example, the set containing 1, 2, 3 equals the set containing 3, 2, 1, and equals the set containing 1, 2, 3, 2, 1. The cardinality of a set is the number of elements it contains. For a set A, we denote cardinality as the absolute value of A or n of A. If A equals the set containing a, b, c, then the cardinality of A is 3. A set A is a subset of set B if every element of A is also an element of B, written A is a subset of B. For example, if A equals the set containing 1, 2 and B equals the set containing 1, 2, 3, 4, then A is a subset of B. Every set is a subset of itself. The empty set is a subset of every set. A is a proper subset of B if A is a subset of B but A does not equal B, written A is a proper subset of B. The power set of a set A is the set of all subsets of A, denoted P of A or 2 to the power A. If A equals the set containing 1, 2, then P of A equals the set containing the empty set, the set containing 1, the set containing 2, the set containing 1 and 2. If a set has n elements, its power set has 2 to the power n elements. Now let us explore set operations. The union of two sets A and B, denoted A union B, is the set of elements that belong to A or B or both. Formally, A union B equals the set of all x such that x is in A or x is in B. For example, if A equals the set containing 1, 2, 3 and B equals the set containing 3, 4, 5, then A union B equals the set containing 1, 2, 3, 4, 5. The intersection of two sets A and B, denoted A intersection B, is the set of elements that belong to both A and B. Formally, A intersection B equals the set of all x such that x is in A and x is in B. Using the previous example, A intersection B equals the set containing 3. Two sets are disjoint if their intersection is the empty set, meaning they have no common elements. The difference of two sets A and B, denoted A minus B or A backslash B, is the set of elements that belong to A but not to B. Formally, A minus B equals the set of all x such that x is in A and x is not in B. If A equals the set containing 1, 2, 3, 4 and B equals the set containing 3, 4, 5, then A minus B equals the set containing 1, 2. The complement of a set A, denoted A prime or A with a bar over it, is the set of all elements in the universal set that are not in A. The universal set U is the set containing all objects under consideration. A complement equals U minus A. If U equals the set containing 1, 2, 3, 4, 5 and A equals the set containing 1, 2, then A complement equals the set containing 3, 4, 5. The symmetric difference of A and B, denoted A triangle B, is the set of elements in either A or B but not in both. It equals the quantity A union B minus the quantity A intersection B, or equivalently, the quantity A minus B union the quantity B minus A. Set operations follow several important laws. The commutative law states A union B equals B union A and A intersection B equals B intersection A. The associative law states the quantity A union B union C equals A union the quantity B union C, and similarly for intersection. The distributive law states A intersection the quantity B union C equals the quantity A intersection B union the quantity A intersection C. Also, A union the quantity B intersection C equals the quantity A union B intersection the quantity A union C. De Morgan's laws are crucial: the complement of A union B equals A complement intersection B complement, and the complement of A intersection B equals A complement union B complement. These laws allow us to simplify complex set expressions. An ordered pair consists of two elements in a specific order, written as parentheses a comma b. Two ordered pairs parentheses a comma b and parentheses c comma d are equal if and only if a equals c and b equals d. Unlike sets, order matters in ordered pairs. The Cartesian product of two sets A and B, denoted A cross B, is the set of all ordered pairs where the first element is from A and the second is from B. Formally, A cross B equals the set of all ordered pairs parentheses a comma b such that a is in A and b is in B. For example, if A equals the set containing 1, 2 and B equals the set containing x, y, then A cross B equals the set containing the ordered pairs 1 comma x, 1 comma y, 2 comma x, 2 comma y. If A has m elements and B has n elements, then A cross B has m times n elements. A relation from set A to set B is a subset of A cross B. In other words, a relation is a set of ordered pairs where the first element comes from A and the second from B. If A equals B, we say R is a relation on A. For example, if A equals the set containing 1, 2, 3, we can define a relation R where R equals the set of ordered pairs parentheses x comma y such that x is less than y. Then R contains ordered pairs 1 comma 2, 1 comma 3, 2 comma 3. The domain of a relation R is the set of all first elements in the ordered pairs. The range is the set of all second elements. Relations can have various properties. A relation R on set A is reflexive if every element is related to itself: for all a in A, the ordered pair a comma a is in R. For example, the relation equals on real numbers is reflexive because x equals x for all x. R is symmetric if whenever a is related to b, then b is related to a: if the ordered pair a comma b is in R, then the ordered pair b comma a is in R. The relation equals is symmetric because if x equals y, then y equals x. R is transitive if whenever a is related to b and b is related to c, then a is related to c: if ordered pairs a comma b and b comma c are in R, then the ordered pair a comma c is in R. The relation less than is transitive because if x is less than y and y is less than z, then x is less than z. R is antisymmetric if whenever both ordered pairs a comma b and b comma a are in R, then a equals b. The relation less than or equal to is antisymmetric. An equivalence relation is a relation that is reflexive, symmetric, and transitive. Equality is the most common example. Equivalence relations partition a set into equivalence classes where elements within each class are equivalent to each other.",
            "intuition": "Think of sets as containers that hold objects. Just as you might group similar items in boxes, sets group mathematical objects. Set operations are like operations on these containers: union combines containers, intersection finds common items, and difference removes items. Relations describe how elements from different sets or the same set connect to each other, like a mapping or correspondence between objects.",
            "worked_examples": [
                {
                    "problem": "If A equals the set containing 1, 2, 3, 4, 5 and B equals the set containing 4, 5, 6, 7, find A union B, A intersection B, A minus B, and B minus A.",
                    "solution": "A union B contains all elements in either A or B: A union B equals the set containing 1, 2, 3, 4, 5, 6, 7. A intersection B contains elements common to both: A intersection B equals the set containing 4, 5. A minus B contains elements in A but not in B: A minus B equals the set containing 1, 2, 3. B minus A contains elements in B but not in A: B minus A equals the set containing 6, 7."
                },
                {
                    "problem": "If the universal set U equals the set containing 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 and A equals the set containing 2, 4, 6, 8, find A complement.",
                    "solution": "A complement contains all elements in U that are not in A. The elements in U not in A are 1, 3, 5, 7, 9, 10. Therefore, A complement equals the set containing 1, 3, 5, 7, 9, 10."
                },
                {
                    "problem": "If A equals the set containing 1, 2 and B equals the set containing x, y, z, find A cross B and determine its cardinality.",
                    "solution": "A cross B is the set of all ordered pairs where the first element is from A and the second is from B. A cross B equals the set containing ordered pairs 1 comma x, 1 comma y, 1 comma z, 2 comma x, 2 comma y, 2 comma z. The cardinality of A is 2 and the cardinality of B is 3, so the cardinality of A cross B is 2 times 3 equals 6."
                },
                {
                    "problem": "Verify De Morgan's law: the complement of A union B equals A complement intersection B complement for U equals the set containing 1, 2, 3, 4, 5, A equals the set containing 1, 2, B equals the set containing 2, 3.",
                    "solution": "First find A union B equals the set containing 1, 2, 3. Then the complement of A union B equals the set containing 4, 5. Now find A complement equals the set containing 3, 4, 5 and B complement equals the set containing 1, 4, 5. Then A complement intersection B complement equals the set containing 4, 5. Both sides equal the set containing 4, 5, verifying the law."
                }
            ],
            "common_mistakes": [
                "Confusing union and intersection, using union when intersection is needed and vice versa",
                "Forgetting that the order matters in ordered pairs but not in sets",
                "Incorrectly calculating the power set by missing the empty set or the set itself as subsets",
                "Mixing up A minus B and B minus A, which are generally different",
                "Assuming all relations are symmetric when many relations are not"
            ],
            "real_world_applications": [
                "Database systems use set operations for querying and combining data tables",
                "Computer science applies set theory in data structures and algorithm design",
                "Logic and Boolean algebra use set operations for circuit design and programming",
                "Probability theory is built on set theory where events are sets of outcomes",
                "Social network analysis uses relations to represent connections between people"
            ]
        },
        "exam_orientation": {
            "frequently_asked": [
                "Perform set operations including union, intersection, difference, and complement",
                "Determine whether given sets are subsets, proper subsets, or equal",
                "Find the power set of a given set",
                "Apply De Morgan's laws to simplify set expressions",
                "Determine properties of relations such as reflexive, symmetric, and transitive"
            ],
            "tips": [
                "Always identify the universal set when working with complements",
                "Draw Venn diagrams to visualize set operations and verify your answers",
                "Remember that the cardinality of a power set with n elements is 2 to the power n",
                "When checking relation properties, test with specific examples from the set",
                "Use De Morgan's laws to simplify complex set expressions involving complements"
            ]
        },
        "advanced_notes": "Set theory extends to infinite sets where concepts like countability and cardinality become more subtle. Cantor's theorem shows there are different sizes of infinity. Relations generalize to functions where each element in the domain relates to exactly one element in the codomain. Order relations and partial orders are important in computer science for sorting and data structures.",
        "references": [
            "MIT OpenCourseWare",
            "NPTEL",
            "Khan Academy"
        ]
    }
]

# Add these modules to the beginner level
curriculum["levels"]["beginner"]["modules"].extend(beginner_modules)

# Save updated curriculum
with open('mathematics_curriculum.json', 'w', encoding='utf-8') as f:
    json.dump(curriculum, f, indent=4, ensure_ascii=False)

print("Added 1 beginner module. Remaining: 6 beginner + 8 intermediate + 6 advanced")
