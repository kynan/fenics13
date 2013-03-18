REMOTE = origin

TALKS = fenics13

.PHONY: $(TALKS)

gh-pages: $(TALKS)
	-git branch -D old/gh-pages
	-git branch -m gh-pages old/gh-pages
	git checkout -b gh-pages
	-git commit -m "Create gh-pages"
	git push -f $(REMOTE) gh-pages

$(TALKS):
	$(MAKE) -C $@ gh-pages
