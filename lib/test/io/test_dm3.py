import numpy as np
from generate_dm_testing_files import data_types
from eelslab import load
from nose.tools import assert_true


# TODO: use fixtures to load the data

old = False
def test_dtypes():
    for key in data_types.iterkeys():
        s = load("dm3_1D_data/test-%s.dm3" % key, old = old)
        yield check_dtype, s.data_cube.dtype, np.dtype(data_types[key]), key

# TODO: the RGB data generated is not correct        
def test_1D_content():
    for key in data_types.iterkeys():
        dat = np.arange(1,3, dtype = data_types[key])
        s = load("dm3_1D_data/test-%s.dm3" % key, old = old)
        yield check_content, s.data_cube, dat, key

def check_dtype(d1, d2, i):
    assert_true(d1 == d2, msg = 'test_dtype-%i' % i)

def check_content(dat1, dat2, i):   
    assert_true(np.all(dat1 == dat2) == True, msg = 'test_dtype-%i' % i)