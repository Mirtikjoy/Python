a = { 54,23,53,67,23,}

a.add("hi")  # add method takes only one arguments

a.update("joy")
a.update({234,567}) # udates method Can have more than one arguments

a |= {1,2} # shorthend of updates method

a.discard("joy")
print(a)