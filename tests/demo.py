from __future__ import print_function
import roadrunner
print(roadrunner.__version__)

rr = roadrunner.RoadRunner('../models/demo_9_annotated.xml')
print(rr.selections)

res1 = rr.simulate(start=0, end=10, steps=100)
print(res1)
rr.plot()

