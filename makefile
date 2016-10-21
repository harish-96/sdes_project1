#
# Makefile for SDES assignment
#

build:
	cd ./source && make all
test:
	cd source && python tests.py
clean:
	rm -rf output
	rm -rf source/__pycache__

help:
	@echo 'Run "make test" to run the tests on python code'
	@echo 'Run "make clean" to clean up all the output files and the pycache directory'
	@echo 'Run "make" or "make build" to generate output files'
