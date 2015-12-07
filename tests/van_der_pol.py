from __future__ import print_function

import roadrunner

print(roadrunner.__version__)
from models.testdata import vdp_sbml

rr = roadrunner.RoadRunner(vdp_sbml)
print(rr.selections)

# THIS IS NOT INTEGRATING UNTIL 50 !!!!
res1 = rr.simulate(start=0, end=10, steps=5)
rr.reset()
result = rr.simulate(start=0, end=50, variableStep=True, plot=True)
# result = rr.simulate(start=0, end=1, variableStep=True)
print(result)

result = rr.simulate(0, 50, variableStep=True, plot=True)
# result = rr.simulate(start=0, end=1, variableStep=True)
print(result)

result = rr.simulate(start=0, end=50, steps=100, variableStep=False, plot=True)
print(result)
