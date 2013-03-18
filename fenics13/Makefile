include ../common.mk

SLIDES_DEPS = index.html parallel_12/speedup_linear.svg parallel_48/runtime_linear.svg

slides: plot

plot:
	(cd parallel_48; python runtime_linear.plot.py)
	(cd parallel_12; python speedup.py)
