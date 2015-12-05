from __future__ import print_function
import roadrunner

rr = roadrunner.RoadRunner('../models/van_der_pol.xml')
print(rr.selections)

# THIS IS NOT INTEGRATING UNTIL 50 !!!!
result = rr.simulate(start=0, end=50, variableStep=True, plot=True)
# result = rr.simulate(start=0, end=1, variableStep=True)
print(result)

result = rr.simulate(start=0, end=50, steps=100, variableStep=False, plot=True)
print(result)
