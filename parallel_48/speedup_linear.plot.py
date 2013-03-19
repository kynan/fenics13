import numpy as np
import matplotlib
matplotlib.use('Agg')
import pylab

fluidity = np.load('../parallel_12/fluidity.npy')
fluidity_mpi = np.load('fluidity_mpi.npy')
dolfin_mpi = np.load('dolfin_mpi.npy')
fluidity_pyop2_mpi = np.load('fluidity_pyop2_mpi.npy')

fluidity_mpi_speedup = fluidity / fluidity_mpi
dolfin_mpi_speedup = fluidity / dolfin_mpi
fluidity_pyop2_mpi_speedup = fluidity / fluidity_pyop2_mpi

fig = pylab.figure('speedup_linear', figsize=(8, 6), dpi=300)
pylab.plot(np.load('elements.npy'), fluidity_mpi_speedup, 'g--s', lw=2, label='Fluidity MPI (48 cores)')
pylab.plot(np.load('elements.npy'), dolfin_mpi_speedup, 'b-.+', lw=2, label='DOLFIN MPI (48 cores)')
pylab.plot(np.load('elements.npy'), fluidity_pyop2_mpi_speedup, 'r-<', lw=2, label='Fluidity-PyOP2 MPI (48 cores)')

pylab.legend(loc='best')
pylab.xlabel('Number of elements in the mesh')
pylab.ylabel('Relative speedup over Fluidity baseline')
pylab.title('Benchmark of an advection-diffusion problem for 100 time steps')
pylab.grid()
pylab.savefig('speedup_linear.svg', orientation='landscape', format='svg', transparent=True)
