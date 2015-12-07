from __future__ import print_function

import unittest

import roadrunner
from multiscale.sbmlutils import validation

from models.testdata import demo_sbml


class DemoTestCase(unittest.TestCase):

    def test_validate_sbml(self):
        vres = validation.validate_sbml(demo_sbml, ucheck=True)
        self.assertEqual(vres["numCCErr"], 0)
        self.assertEqual(vres["numCCWarn"], 0)

    def test_roadrunner_selections(self):
        rr = roadrunner.RoadRunner(demo_sbml)
        print(rr.selections)
        self.assertTrue('time' in rr.selections)
        self.assertTrue('[e__A]' in rr.selections)
        self.assertTrue('[e__B]' in rr.selections)
        self.assertTrue('[e__C]' in rr.selections)
        self.assertTrue('[c__A]' in rr.selections)
        self.assertTrue('[c__B]' in rr.selections)
        self.assertTrue('[c__C]' in rr.selections)
        self.assertEqual(len(rr.selections), 7)

    def test_fixed_step_simulation(self):
        rr = roadrunner.RoadRunner(demo_sbml)

        tend = 10.0
        steps = 100
        s = rr.simulate(start=0, end=tend, steps=steps)

        # test end point reached
        self.assertEqual(s[-1, 0], 10)
        # test correct number of steps
        self.assertEqual(len(s['time']), steps+1)


if __name__ == '__main__':
    unittest.main()
