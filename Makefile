SLIDES = slides
SLIDES_HTML = index.html
SLIDES_DEPS = index.html parallel_12/speedup_linear.svg parallel_48/speedup_linear.svg

REMOTE = origin

server:
	ipython notebook --pylab inline --no-browser

slides: plot
	nbconvert.py --format reveal $(SLIDES).ipynb
	mv $(SLIDES)_slides.html $(SLIDES_HTML)

plot:
	(cd parallel_48; python speedup_linear.plot.py)
	(cd parallel_12; python speedup_linear.plot.py)

publish: slides
	git add $(SLIDES_DEPS)
	-git branch -D old/gh-pages
	-git branch -m gh-pages old/gh-pages
	git checkout -b gh-pages
	-git commit -m "Create gh-pages"
	git push -f $(REMOTE) gh-pages
