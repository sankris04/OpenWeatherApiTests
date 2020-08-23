from mpmath.tests.extratest_gamma import testcases
from sympy.utilities import pytest

[pytest]
python_files=test_*
python_files=*Test
python_functions=test_*
markers=
        smoke : run some test
        Regression : run regression testcases
