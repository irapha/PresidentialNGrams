# PresidentialNGrams
Use markov chains and nGrams to generate presidential speeches, based on previous ones.

How It Works
------------
A Markov chain is a process that determines a sequence of events (in our case, characters) based solely on the probability of an event given a few events prior to it. That probability is decribed in an nGram.

This algorithm takes in presidential speeches from the past, creates nGram representations for it, then generates text from those nGram models.

### Quick Demo
Run `python tests.py` to visualize our quick demo.

How To Use
----------
```
from markov import *
model1 = build_model(tokensOrString, n) # n is the number of elements to base the nGram on.
model2 = build_model(tokensOrString2, n)

model = merge_models([model1, model2])

# seed is the initial token, where to start the generation from.
# iters will determine the length of the result text
generatedTokens = generate(model, n, seed, iters)

print "".join(generatedTokens)
```

