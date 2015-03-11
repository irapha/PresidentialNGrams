### DEMO ###
from markov import *
from source import *

n = 6
iters = 2000

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
print "".join(generate(model, n, None, iters))
