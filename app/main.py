import mod

data = [
  {
    "Country": "Colombia",
    "Population": 500
  },
  {
    "Country": "Bolivia",
    "Population": 300
  }
]

def run():

  keys, values = (mod.get_population())
  print(keys, values)
  
  results = mod.population_by_country(data,"Colombia")
  print(results)


if __name__=="__main__":
  run()