#Make file for Homework 5
CC	= g++ -Wall -MMD -c
OBJS	= exprtest.o  parser.tab.o scanner.o  driver.o 

all: exprtest

exprtest: ${OBJS}
	g++ -Wall -g -MDD -o exprtest ${OBJS}

exprtest.o: exprtest.cpp driver.hpp expression.hpp 
	${CC} exprtest.cpp

driver.o: driver.cpp driver.hpp scanner.hpp
	${CC} driver.cpp

parser.tab.o: expression.hpp scanner.hpp driver.hpp 
	bison parser.ypp
	${CC} parser.tab.cpp

scanner.o: scanner.ll scanner.hpp
	flex -t scanner.ll > scanner.cpp
	${CC} scanner.cpp
clean: 
	rm -f *.o *.d *~ *.hh core exprtest parser.tab.cpp scanner.cpp parser.tab.hpp 
