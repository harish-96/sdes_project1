
all: ../output/trajectory.png ../output/phase_portrait.png ../output/140010046.pdf ../output/vanderpol_animation.mp4

../output/trajectory.png: main.py vdp_osc.py input.csv
	python main.py

../output/phase_portrait.png: main.py vdp_osc.py input.csv
	python main.py

../output/vanderpol_animation.mp4: main.py vdp_osc.py input.csv
	python main.py

../output/140010046.pdf: ../output/phase_portrait.png 140010046.tex
	pdflatex --output-directory=../output 140010046.tex
