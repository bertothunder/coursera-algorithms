
#include "linkedlist.h"
#include <iostream>
#include <algorithm>
#include <iterator>
#include <assert.h>

//================================================= Node

template<class Type>
struct LinkedList<Type>::Node
{
    Type data;
    Node* next;

};

//================================================= iterator

template<class Type>
class LinkedList<Type>::iterator : public std::iterator<std::input_iterator_tag,
                                        Type,
                                        Type,
                                        const Type*,
                                        Type>
{
private:
    LinkedList<Type>::Node* _cur;
public:
    explicit iterator(LinkedList<Type>::Node* node): _cur(node) {}
    iterator& operator++()
    {
        LinkedList<Type>::Node* it(_cur);
        if (_cur->next != nullptr) {
            it = _cur->next;
            _cur = it;
        }
        return _cur*;
    }
    iterator operator++(int) { iterator retval = *this; ++(*this); return retval; }
    bool operator==(iterator other) const { return other->data == _cur->data; }
    bool operator!=(iterator other) const { return other->data != _cur->data; }
    Type& operator*() const { return _cur->data; }
};

template<class Type>
LinkedList<Type>::iterator LinkedList<Type>::begin() {
     return iterator(this->_root);
}

template<class Type>
LinkedList<Type>::iterator LinkedList<Type>::end() {
     return iterator(this->_tail);
}


//================================================= LinkedList

template<class Type>
LinkedList<Type>::LinkedList()
{
    this->_size = 0;
    this->_root = nullptr;
    this->_tail = nullptr;
}

template<class Type>
LinkedList<Type>::LinkedList(const LinkedList<Type> &other)
{
    Type val = other.root();
}

template<class Type>
LinkedList<Type>::~LinkedList()
{
    Node* it = this->_root;
    while(it != this->_tail) {
        it = this->_root->next;
        delete this->_root;
        this->_root = it;
    }
    delete this->_tail;
}

template<class Type>
Type& LinkedList<Type>::operator++()
{

}

template<class Type>
void LinkedList<Type>::insert(const Type& val)
{
    Node* node(new Node());
    node->data = val;
    node->next = nullptr;
    if (this->_tail) {
        std::cout << "Tail found with " << this->_tail->data << ", point next to node" << std::endl;
        this->_tail->next = node;
        this->_tail = node;
    }
    else {
        if (!this->_root) {
            std::cout << "No root, pointing root to node" << std::endl;
            this->_root = node;
        }
        if (!this->_tail) {
            std::cout << "No tail, pointing tail to root" << std::endl;
            this->_tail = this->_root;
        }
    }
    ++this->_size;
}

template<class Type>
void LinkedList<Type>::remove(const std::uint16_t index)
{
    // TODO: throw an exception if index is out of scope
    //if ()
//    if (this->_tail) {
//        this->_tail;
//    }
    --this->_size;
}

template<class Type>
const Type& LinkedList<Type>::root()
{
    return this->_root->data;
}

/// Returns the tail of the list
template<class Type>
const Type& LinkedList<Type>::tail()
{
    return this->_tail->data;
}

/// Looks for an item stored in the list.
template<class Type>
const std::uint16_t LinkedList<Type>::find(const Type& value)
{
    return this->_tail->data;
}

/// Returns the number of nodes available in the list
template<class Type>
const std::uint16_t LinkedList<Type>::size() {
    return _size;
}

template<class Type>
void LinkedList<Type>::show() {
    Node* it = this->_root;
    while (it != this->_tail) {
        std::cout << it->data << " -> ";
        it = it->next;
    }
    std::cout << it->data << std::endl;
}



int main(void) {
    int a(10);
    int b(20);
    int c(30);

    LinkedList<int> lista;
    lista.insert(a);
    lista.insert(b);
    lista.insert(c);
    assert(lista.size() == 3);

    lista.show();
}
