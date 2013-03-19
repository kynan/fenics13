import numpy as np
import matplotlib
matplotlib.use('Agg')
import pylab

fig = pylab.figure('runtime_linear', figsize=(8, 6), dpi=300)
pylab.plot(np.load('elements.npy'), np.load('fluidity_mpi.npy'), 'g--s', lw=2, label='Fluidity (cores: 48)')
pylab.plot(np.load('elements.npy'), np.load('dolfin.npy'), 'c-.*', lw=2, label='DOLFIN (cores: 48)')
pylab.plot(np.load('elements.npy'), np.load('fluidity_pyop2_mpi.npy'), 'm-<', lw=2, label='Fluidity-PyOP2 (backend: mpi)')

pylab.legend(loc='upper left')
pylab.xlabel('Number of elements in the mesh')
pylab.ylabel('Overall runtime in seconds')
pylab.title('Benchmark of an advection-diffusion problem for 100 time steps')
pylab.grid()
pylab.savefig('runtime_linear.svg', orientation='landscape', format='svg', transparent=True)
