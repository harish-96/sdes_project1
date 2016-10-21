
all: ../output/trajectory.png ../output/phase_portrait.png ../output/Report.pdf

../output/trajectory.png: main.py vdp_osc.py input.csv
	python main.py

../output/phase_portrait.png: main.py vdp_osc.py input.csv
	python main.py

../output/Report.pdf: ../output/phase_portrait.png Report.tex
	pdflatex --output-directory=../output Report.tex
