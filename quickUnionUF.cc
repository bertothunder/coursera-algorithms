#include <iostream>
#include <vector>
#include <assert.h>

typedef unsigned int uint;

class QuickUnionUF {
private:
	uint numElems;
	std::vector<uint> nodes;

	bool connected(uint i, uint j) {
		return root(i) == root(j);
	}

	uint root(uint i) {
		while (i != nodes[i]) {
			i = nodes[i];
		}
		return i;
	}
public:
	QuickUnionUF(uint n) {
		numElems = n;
		for (uint i = 0; i < n; ++i) {
			nodes.push_back(i);
		}
	}

	~QuickUnionUF() {
		nodes.clear();
	}

	void unite(uint i, uint j) {
		if (i > numElems || j > numElems) {
			std::cout << "Indices can't be greater than " << numElems << std::endl;
			return;
		}
		auto old_j = nodes[j];
		if (!connected(i,j)) {
			nodes[i] = old_j;
		}
	}

	bool find(uint i, uint j) {
		return connected(i, j);
	}

	void show() {
		for(auto ix: nodes) {
			std::cout << ix << " ";
		}
		std::cout << std::endl;
	}
};

int main() {
	QuickUnionUF quf(10);
	quf.unite(1,3);
	quf.unite(9,0);
	quf.unite(0,1);
	quf.unite(2,5);
	quf.show();
	assert(quf.find(1,0) == true);
	quf.unite(5,0);
	quf.show();
	assert(quf.find(2,0) == true);
	assert(quf.find(2,8) == false);
}