def get_population():
  key=["col","bol"]
  values=[300,400]
  return key, values

def population_by_country(data, country):
  result= list(filter(lambda item : item["Country"]==country, data))
  return result