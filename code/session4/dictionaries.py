

films = {"Horror House": [1956, 1983, 2018]}
films["Space Race"] = [1988]

print(films)

films["Space Race"].append(2003)

print(films)

locations = {(34, -122): "Philadelphia"}

for k in films.keys():
    print("{}, {}".format(k, films[k]))

for k, v in films.items():
    print("{}, {}".format(k, v))
