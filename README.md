# Smart-Expense-Tracker-with-Insights
This project is a web-based expense tracker application designed to log, categorize, and analyze daily expenses in a simple and efficient way. It helps automate common personal finance tasks such as tracking spending, generating monthly summaries, and visualizing expense distributions.

Watch the demo video here : 

Features
Expense Logging Add and manage daily expenses easily.

Expense Analysis View monthly summaries and identify the highest spending category.

Visualizations

Generate charts for category-wise breakdowns
Track spending trends over time
Data Storage Keeps track of expenses efficiently using local JSON storage.

Technology Stack
Backend: Python with Flask
Frontend: HTML, CSS
Data Handling & Visualization: JSON, Matplotlib

Prerequisites
Python 3.x
pip (Python package installer)

Installation
Clone the repository to your local system or download the project files
Open a terminal in the project directory
Install the required dependencies using: pip install -r requirements.txt

Running the Application

Run the following command in the project root directory:

python app.py

After running, the application will start (check console for the localhost port, typically http://127.0.0.1:5000).

Project Structure
app.py – Main backend application file (Flask server and routing)
expense_manager.py – Core logic for managing expenses and file operations
plotter.py – Functions for generating visualizations using Matplotlib
expenses.json – JSON file used for data storage
static/ – Frontend static files (CSS, images, etc.)
templates/ – HTML templates for the web interface
requirements.txt – Project dependencies

Final Note
This project demonstrates the basic working of an expense tracking application, including data handling, web development, and data visualization. It is useful for understanding full-stack development using Python and Flask.
