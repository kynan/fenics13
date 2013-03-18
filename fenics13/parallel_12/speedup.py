import numpy as np
import matplotlib
matplotlib.use('Agg')
import pylab

versions = [
    'PyOP2 Sequential',
    'DOLFIN Sequential',
    'DOLFIN MPI',
    'Fluidity MPI',
    'PyOP2 CUDA',
    'PyOP2 MPI',
    'PyOP2 OpenMP'
]
data = dict((v, np.loadtxt('speedup.txt', usecols=(i+1,))) for i, v in enumerate(versions))
elements = np.loadtxt('speedup.txt', np.int, usecols=(0,))

fig = pylab.figure('speedup_linear', figsize=(8, 6), dpi=300)
for k, v in data.items():
    pylab.plot(elements, v, lw=2, label=k)
pylab.legend(loc='upper right', ncol=2, labelspacing=0.1, prop={'size':14})
pylab.xlabel('Number of elements in the mesh')
pylab.ylabel('Relative speedup over Fluidity baseline')
pylab.title('Benchmark of an advection-diffusion problem for 100 time steps')
pylab.grid()
pylab.savefig('speedup_linear.svg', orientation='landscape', format='svg', transparent=True)
