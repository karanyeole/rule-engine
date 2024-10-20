from app import create_rule, combine_rules, evaluate_rule  # Adjust the import based on your structure
import json

# Sample Test Data
data = {
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 6
}

# Test Case 1: Create Rule
print("Starting Test Case 1: Creating AST from rule string")
rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
ast = create_rule(rule_string)
print("Test Case 1 - AST Representation of Rule 1:")
print(ast.to_dict())

# Test Case 2: Combine Rules
print("\nStarting Test Case 2: Combining two rules")
rules = [
    "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)",
    "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"
]
combined_ast = combine_rules(rules)
print("Test Case 2 - Combined AST:")
print(combined_ast.to_dict())

# Test Case 3: Evaluate Rule
print("\nStarting Test Case 3: Evaluating rule with sample data")
result = evaluate_rule(ast, data)
print("Test Case 3 - Evaluation Result:")
print(result)

# Test Case 4: Modify Existing Rule
print("\nStarting Test Case 4: Modifying a rule")
new_rule_string = "age > 40 AND salary < 70000"
# Here you would send a request to your modify_rule endpoint with the new rule string
