rivers = {'nile':'egypt','rhine river':'germany','amazon river':'brazil'}
for river, cun in rivers.items():
    print(f"The{river.title()} runs through {cun.title()}.")

for river in rivers.keys():
    print(f"{river.title()}")

for cun in rivers.values():
    print(f"{cun.title()}")