#ifndef __LINKEDLIST_H__
#define __LINKEDLIST_H__

#include <cstdint>
#include <algorithm>


template<class Type>
class LinkedList {
private:
    struct Node;
    Node* _root;
    Node* _tail;
    std::uint16_t _size;
public:
    class iterator;

    iterator begin();
    iterator end();

public:
    LinkedList();
    LinkedList(const LinkedList& other);
    ~LinkedList();

    /// Inserts a new node in the linked list
    void insert(const Type& val);
    /// Remove a node in the list by index
    void remove(const std::uint16_t index);

    /// Returns the head of the node
    const Type& root();
    /// Returns the tail of the list
    const Type& tail();

    Type& operator++();

    /// Looks for an item stored in the list.
    const std::uint16_t find(const Type& value);

    /// Returns the number of nodes available in the list
    const std::uint16_t size();

    void show();
};

#endif // __LINKEDLIST_H__

