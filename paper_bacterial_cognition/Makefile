LATEX=pdflatex
BIBTEX=bibtex
MAIN=main

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex
	# bibtex not needed (thebibliography inline); second pass resolves refs

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).bbl $(MAIN).blg $(MAIN).fls $(MAIN).fdb_latexmk

distclean: clean
	rm -f $(MAIN).pdf

view: $(MAIN).pdf
	open $(MAIN).pdf

check:
	@echo "--- line count ---" && wc -l $(MAIN).tex
	@echo "--- sections ---" && grep -n "section{" $(MAIN).tex
	@echo "--- refs ---" && grep -c "bibitem" $(MAIN).tex
	@echo "--- figures ---" && grep -c "begin{figure" $(MAIN).tex
