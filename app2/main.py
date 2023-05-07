import utils
import read_csv
import charts
import pandas as pd

def run():
  data = read_csv.read_csv('data.csv')
  '''
  data = read_csv.read_csv('data.csv') #1
  data = list(filter(lambda item : item['Continent'] == 'South America',data)) #2

  countries = list(map(lambda x: x['Country'], data)) #3
  percentages = list(map(lambda x: x['World Population Percentage'], data)) #4
  charts.generate_pie_chart(countries, percentages) #5
  '''

  df = pd.read_csv('data.csv') #1
  df = df[df['Continent'] == 'Africa'] #2
  countries = df['Country'].values #3
  percentages = df['World Population Percentage'].values #4
  charts.generate_pie_chart(countries, percentages) #5

  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()