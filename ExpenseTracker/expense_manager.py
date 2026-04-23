import json
import os
from collections import defaultdict

DATA_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=4)

def add_expense(date_str, category, amount, description):
    expenses = load_expenses()
    expense = {
        'id': len(expenses) + 1,
        'date': date_str,
        'category': category,
        'amount': float(amount),
        'description': description
    }
    expenses.append(expense)
    save_expenses(expenses)
    return expense

def get_insights():
    expenses = load_expenses()
    if not expenses:
        return {
            'total_spent': 0,
            'category_breakdown': {},
            'highest_category': 'None',
            'highest_category_amount': 0
        }
    
    total_spent = 0
    category_breakdown = defaultdict(float)
    
    for expense in expenses:
        amount = expense.get('amount', 0)
        category = expense.get('category', 'Other')
        total_spent += amount
        category_breakdown[category] += amount
        
    highest_category = max(category_breakdown, key=category_breakdown.get)
    highest_amount = category_breakdown[highest_category]
    
    return {
        'total_spent': total_spent,
        'category_breakdown': dict(category_breakdown),
        'highest_category': highest_category,
        'highest_category_amount': highest_amount
    }
