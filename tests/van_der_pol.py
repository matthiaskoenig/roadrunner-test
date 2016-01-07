from __future__ import print_function

import roadrunner

print(roadrunner.__version__)
from models.testdata import vdp_sbml

rr = roadrunner.RoadRunner(vdp_sbml)
print(rr.selections)

# THIS IS NOT INTEGRATING UNTIL 50 !!!!

result = rr.simulate(start=0, end=50, variableStep=True)
print('variable_step_size: {}'.format(rr.getIntegrator().getValue('variable_step_size')))

rr.getIntegrator().setValue('variable_step_size', True)
result = rr.simulate(start=0, end=50, plot=False)
print(result)
print('variable_step_size: {}'.format(rr.getIntegrator().getValue('variable_step_size')))
rr.plot()
