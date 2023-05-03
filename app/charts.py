import matplotlib.pyplot as plt

def generate_bar_chart():
  label = ["a","b","c","d"]
  values = [100,200,80,65]
  #fig = figura
  #ax = coordenas donde se va a empezar a graficar
  fig, ax = plt.subplots()
  ax.bar(label,values)
  plt.savefig('bar.png')
  plt.close()

if __name__ == "__main__":
  generate_bar_chart()