countries = ['Russia', 'USA', 'UK']
capitals = ['Moscow', 'Wasi', 'London']
population = [145_934_462, 331_002_651, 80_345_321]




for countr, cap, popul in zip(countries, capitals, population):
    print(f'{cap} is the capital of {countr}, population: {popul}')

        