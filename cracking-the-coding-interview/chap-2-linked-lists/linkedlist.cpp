#include <vector>
#include <iostream>
#include <algorithm>
#include "linkedlist.h"

using namespace std;

Node::Node()
{
    value = 0;
    next = NULL;
}

// ======

LinkedList::LinkedList()
{
    cout << "Initializing Linked List" << endl;
    head = NULL;
}

LinkedList::~LinkedList()
{
    Node * deleter = head;
    Node * leadTracer = deleter->next;

    while (deleter != NULL)
    {
        //cout << "Deleting Node - Value [" << deleter->value << "]" << endl;
        delete deleter;

        deleter = leadTracer;
        if (deleter == NULL)
            break;

        leadTracer = leadTracer->next;
    }

    head = NULL;
}

void LinkedList::printList()
{
    Node * tracer = head;

    while (tracer != NULL)
    {
        cout << "(" << tracer->value << ") --> ";
        tracer = tracer->next;
    }

    cout << "NULL" << endl;
}

bool LinkedList::appendNode(int value)
{
    //cout << "Append Node - Value [" << value << "]" << endl;

    Node * newNode = new Node();
    newNode->value = value;

    Node * tracer = head;
    if (tracer == NULL)
    {
        head = newNode;
        return true;
    }

    while (tracer->next != NULL)
        tracer = tracer->next;

    tracer->next = newNode;
    return true;
}

Node * LinkedList::getNthNode(int n)
{
    Node * tracer = head;

    int counter = 0;
    while (counter != n && tracer != NULL)
    {
        tracer = tracer->next;
        counter++;
    }
    
    return tracer;
}

Node * LinkedList::insertNode(Node * loc, int value)
{
    Node * newNode = new Node();
    newNode->value = value;

    if (loc == head)
    {
        newNode->next = head;
        head = newNode;
        return newNode;
    }

    Node * tracer = head;

    while (tracer != NULL)
    {
        if (tracer->next == loc)
        {
            newNode->next = tracer->next;
            tracer->next = newNode;
            return newNode;
        }
        
        tracer = tracer->next;
    }

    return NULL;
}

bool LinkedList::deleteNode(Node * tbd)
{
    if (tbd == NULL)
        return false;

    if (tbd == head)
    {
        head = tbd->next;
        delete tbd;
        return true;
    }

    // traverse until the node to be deleted
    Node * tracer = head;
    while (tracer->next != tbd && tracer != NULL)
        tracer = tracer->next;

    tracer->next = tbd->next;
    delete tbd;
    return true;
}

bool LinkedList::deleteValues(int value)
{
    cout << "Deleting Node - Value [" << value << "]" << endl;

    Node * tracer = head;
    while (tracer != NULL)
    {
        if (tracer->next->value == value)
            deleteNode(tracer->next);

        tracer = tracer->next;
    }

    return true;
}

/* Delete All Nodes

   Cracking the Coding Interview
   Question 2.1

   Description:
       Removes all duplicates from an unsorted linked list
*/
bool LinkedList::deleteAllDuplicates()
{
    vector<int> trackerList;

    Node * tracer = head;
    if (tracer != NULL)
        trackerList.push_back(tracer->value);

    while (tracer->next != NULL)
    {
        // Could not find value in list
        if (find(trackerList.begin(), trackerList.end(), tracer->next->value) == trackerList.end())
        {
            trackerList.push_back(tracer->next->value);
            tracer = tracer->next;
        }
        else
        {
            deleteNode(tracer->next);
        }
    }

    return true;
}

/* 'K'th to Last Element

    Cracking the Coding Interview
    Question 2.2

    Description:
        Find's the 'K'th to last element of a singly linked list
*/
int LinkedList::kthToLast(int k)
{
    Node * tracer = head;

    if (head == NULL)
        return -1;

    int len = 1;
    while (tracer->next != NULL)
    {
        tracer = tracer->next;
        len += 1;
    }

    if (k > len)
        return -2;

    tracer = head;
    for (int i = 0; i < len - k; i++)
        tracer = tracer->next;

    return tracer->value;
}

int LinkedList::kthToLastRecursive(int k)
{
    int kthValue;
    int indexSize = kthToLastR(head, k, kthValue);

    return kthValue;
}

int LinkedList::kthToLastR(Node * start, int k, int & kthValue)
{
    if (start == NULL)
        return 0;

    int kthElement = kthToLastR(start->next, k, kthValue) + 1;
    if (kthElement == k)
        kthValue = start->value;

    return kthElement;
}

/* Deleting the (middle) node

    Cracking the Coding Interview
    Question 2.3

    Description:
        Delete a node in the middle of a linked list
        (not the first or last). Given a reference to only
        that node
*/
bool LinkedList::deleteMiddleNode(Node * deleter)
{
    Node * tracer = head;
    if (tracer == NULL)
        return false;

    if (tracer->next == NULL)
        return false;

    if (deleter->next == NULL)
        return false;

    while (tracer->next != NULL)
    {
        if (tracer->next == deleter)
        {
            tracer->next = deleter->next;
            delete deleter;
            return true;
        }
    }

    return true;
}


bool LinkedList::partition(int part)
{
    if (head == NULL)
        return true;
    
    Node * tracer = head;
    while (tracer->value < part)
        tracer = tracer->next;

    Node * startLoc = tracer;
    while (tracer != NULL)
    {
        if (tracer->value < part)
        {
            insertNode(startLoc, tracer->value);
            deleteNode(tracer);
            tracer = startLoc;
        }

        tracer = tracer->next;
    }

    return true;
}

int LinkedList::reverseValue()
{
    Node * tracer = head;
    int multiplier = 1;
    int sum = 0;

    while (tracer != NULL)
    {
        sum += tracer->value * multiplier;
        multiplier *= 10;
        tracer = tracer->next;
    }

    return sum;
}



