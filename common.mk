SLIDES ?= slides
SLIDES_HTML ?= index.html

server:
	ipython notebook --pylab inline --no-browser

slides:
	nbconvert.py --format reveal $(SLIDES).ipynb
	mv $(SLIDES)_slides.html $(SLIDES_HTML)
