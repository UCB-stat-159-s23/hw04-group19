from ligotools import readligo as rl

# test if the loaddata function works properly on H1
def test_loaddata_forH1():
    strain, time, channel_dict = rl.loaddata('../../data/H-H1_LOSC_4_V2-1126259446-32.hdf5', 'H1')
    assert (len(strain) == 131072)

# test if the loaddata function works properly on L1
def test_loaddata_forL1():
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata("../../data/L-L1_LOSC_4_V2-1126259446-32.hdf5", 'L1')
    assert (strain_L1.any())
    assert (time_L1.any())
    assert (chan_dict_L1 is not None)

# test if the data read is correct
def test_read_hdf5_H1():
    data = rl.loaddata("../../data/H-H1_LOSC_4_V2-1126259446-32.hdf5")
    assert data[0][0] == 2.177040281449375e-19

# test if the data read is correct
def test_read_hdf5_L1():
    data = rl.loaddata("../../data/L-L1_LOSC_4_V2-1126259446-32.hdf5")
    assert data[0][1] == -1.0358627404014794e-18