"""
Managing the test data.
"""

import os
test_dir = os.path.dirname(os.path.abspath(__file__))

demo_sbml = os.path.join(test_dir, 'demo_9_annotated.xml')
galactose_sbml = os.path.join(test_dir, 'galactose_28_annotated.xml')
vdp_sbml = os.path.join(test_dir, 'van_der_pol.xml')

