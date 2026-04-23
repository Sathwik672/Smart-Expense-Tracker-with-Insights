import os
import matplotlib
matplotlib.use('Agg')  # Headless mode
import matplotlib.pyplot as plt

def generate_pie_chart(category_breakdown, static_dir='static'):
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    filepath = os.path.join(static_dir, 'pie_chart.png')
    
    if not category_breakdown:
        # Create an empty plot if no data
        plt.figure(figsize=(6, 6))
        plt.pie([1], labels=["No Data"], colors=['#ffffff'], textprops={'color': '#000000'})
        plt.title('Expense Breakdown', color='#000000', fontsize=16)
        plt.savefig(filepath, facecolor='white')
        plt.close()
        return 'pie_chart.png'

    labels = list(category_breakdown.keys())
    sizes = list(category_breakdown.values())

    # Grayscale color palette
    colors = ['#cccccc', '#999999', '#666666', '#eeeeee', '#bbbbbb', '#888888', '#dddddd', '#777777']
    colors = (colors * ((len(labels) // len(colors)) + 1))[:len(labels)]

    plt.figure(figsize=(6, 6))
    
    # Simple plain pie chart
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, 
            textprops={'color': '#000000', 'fontsize': 12},
            wedgeprops={'edgecolor': '#000000', 'linewidth': 1})
            
    plt.title('Expense Breakdown', color='#000000', fontsize=16, pad=20)
    
    # Save the plot with white background
    plt.savefig(filepath, facecolor='white', bbox_inches='tight')
    plt.close()

    return 'pie_chart.png'
