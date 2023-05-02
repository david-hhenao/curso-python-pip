import csv, os

os.system("clear")

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    #print(header) 
    data_dict=[]
    
    for row in reader:
      iterable = zip(header, row)
      #print(list(iterable))
      country_dict={key:value for key, value in iterable}
      data_dict.append(country_dict)

    return data_dict
    
if __name__ == "__main__":
  data_dict=read_csv("./app/data.csv")
  print(data_dict[0])