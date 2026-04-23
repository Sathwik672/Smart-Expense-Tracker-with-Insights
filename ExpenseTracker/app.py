from flask import Flask, render_template, request, redirect, url_for
from expense_manager import add_expense, get_insights, load_expenses
from plotter import generate_pie_chart

app = Flask(__name__)

@app.route('/')
def index():
    insights = get_insights()
    expenses = load_expenses()
    
    chart_filename = generate_pie_chart(insights['category_breakdown'], 'static')
    
    return render_template('index.html', insights=insights, chart_filename=chart_filename, expenses=expenses[-5:])

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date_str = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        description = request.form['description']
        
        add_expense(date_str, category, amount, description)
        return redirect(url_for('index'))
        
    return render_template('add_expense.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
