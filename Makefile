CXX = g++
CXXFLAGS = --std=c++11 -Wall -g
srcfiles = $(wildcard *.cc)
objs := $(srcfiles:.cc=)

$(objs): $(srcfiles)
	$(CXX) $(CXXFLAGS) -o $@ $^

clean:
	rm -rfv $(objs)
