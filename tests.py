### DEMO ###
from markov import *
from source import *

n = 3 # use 3 for word tokens, 6 for char tokens.
iters = 2000

# OPTIONAL - tokenize into words. If not run, ngrams will se chars as tokens.
# note: we might need more source materials to properly create a word-tokenized text.
source1 = source1.split(" ")
source2 = source2.split(" ")
source3 = source3.split(" ")
source4 = source4.split(" ")
source5 = source5.split(" ")
source6 = source6.split(" ")
source7 = source7.split(" ")
source8 = source8.split(" ")
source9 = source9.split(" ")
source10 = source10.split(" ")
source11 = source11.split(" ")
source12 = source12.split(" ")
source13 = source13.split(" ")
source14 = source14.split(" ")
source15 = source15.split(" ")
source16 = source16.split(" ")
source17 = source17.split(" ")
# END OF OPTIONAL WORD TOKENIZER BLOCK

# BUILD MODELS
model1 = build_model(source1, n)
model2 = build_model(source2, n)
model3 = build_model(source3, n)
model4 = build_model(source4, n)
model5 = build_model(source5, n)
model6 = build_model(source6, n)
model7 = build_model(source7, n)
model8 = build_model(source8, n)
model9 = build_model(source9, n)
model10 = build_model(source10, n)
model11 = build_model(source11, n)
model12 = build_model(source12, n)
model13 = build_model(source13, n)
model14 = build_model(source14, n)
model15 = build_model(source15, n)
model16 = build_model(source16, n)
model17 = build_model(source17, n)

model = merge_models([model1, model2, model3, model4, model5, model6, model7, model8, model9, model10, model11, model12, model13, model14, model15, model16, model17])

print " ".join(generate(model, n, None, iters))
