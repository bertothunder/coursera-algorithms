#include <iostream>
#include <vector>
#include <type_traits>

typedef unsigned int uint;

class QuickFindUF {
private:
	uint numObjs;
	std::vector<uint> nodes;
public:
	QuickFindUF(uint n) {
		numObjs = n;
		for (uint i=0; i < n; ++i) {
			nodes.push_back(i);
		}
	}

	~QuickFindUF() {
		nodes.clear();
	}

	bool connected(uint i, uint j) {
		return (nodes[i] == nodes[j]);
	}

	void unionqf(uint i, uint j) {
		if (i > numObjs || j > numObjs) {
			std::cout << "" << std::endl;
			return;
		}
		if (!connected(i, j)) {
			uint old_i = nodes[i];
			uint old_j = nodes[j];
			for(uint ix = 0; ix < numObjs; ++ix) {
				if (nodes[ix] == old_i) {
					nodes[ix] = old_j;
				}
			}
		}
	}

	bool findqf(uint i, uint j) {
		return connected(i, j);
	}

	void show() {
		for(auto val: nodes) {
			std::cout << val << " ";
		}
		std::cout << std::endl;
	}
};

int main(void) {
	QuickFindUF qf(10);
	qf.unionqf(1,9);
	qf.unionqf(2,8);
	qf.unionqf(3,9);
	//static_assert(qf.findqf(1,3));
	qf.show();
	qf.unionqf(5,1);
	//static_assert(qf.findqf(1,5));
	qf.show();
}