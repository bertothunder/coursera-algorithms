#include <iostream>
#include <assert.h>
#include <vector>

typedef unsigned int uint;

class PathCompressionQuickUnionUF {
private:
	uint numNodes;
	std::vector<uint> nodes;

	bool connected(uint i, uint j) {
		return root(i) == root(j);
	}

	uint root(uint i) {
		return i;
	}
public:
	PathCompressionQuickUnionUF(uint n) {
		for (uint i=0; i < n; ++i) {
			nodes.push_back(i);
		}
	}

	~PathCompressionQuickUnionUF() {
		nodes.clear();
	}

	bool find(uint i, uint j) {
		return connected(i, j);
	}

	void unite(uint i, uint j) {

	}

	void show() {
		for(auto ix: nodes) {
			std::cout << nodes[ix] << " ";
		}
		std::cout << std::endl;
	}
};

int main() {
	PathCompressionQuickUnionUF pcqu(10);
	pcqu.unite(0,3);
	pcqu.unite(1,3);
	pcqu.unite(6,9);
	pcqu.unite(6,4);
	pcqu.unite(9,5);
	pcqu.show();
	return 0;
}