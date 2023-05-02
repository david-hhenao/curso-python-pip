import matplotlib.pyplot as plt

def generate_pie_chart():
    labelss = ['A','B','C']
    values = ['200','34','120']

    fig, axes = plt.subplots()
    axes.pie(values, labels=labelss)
    plt.savefig('pipe.png')
    plt.close()