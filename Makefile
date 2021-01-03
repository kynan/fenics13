SLIDES = slides
SLIDES_HTML = index.html
PLOT_DEPS = parallel_12/speedup_linear.svg parallel_48/speedup_linear.svg
SLIDES_DEPS = $(SLIDES_HTML) $(PLOT_DEPS)
REMOTE = origin

server:
	jupyter notebook --pylab inline --no-browser

slides: plot
	jupyter nbconvert --to slides $(SLIDES).ipynb
	mv $(SLIDES).slides.html $(SLIDES_HTML)

plot: $(PLOT_DEPS)

$(PLOT_DEPS): $@
	(cd parallel_48; python speedup_linear.plot.py)
	(cd parallel_12; python speedup_linear.plot.py)

publish: slides
	git add $(SLIDES_DEPS)
	-git branch -D old/gh-pages
	-git branch -m gh-pages old/gh-pages
	git checkout -b gh-pages
	-git commit -m "Create gh-pages"
	git push -f $(REMOTE) gh-pages
