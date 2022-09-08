not_done = True
pizza = []
while not_done:
    x = input()
    if x != "Quit":
        pizza.append(x)
        print("Your pizza now contains",pizza)
    else:
        print("Your pizza is now being processed")
        not_done = False