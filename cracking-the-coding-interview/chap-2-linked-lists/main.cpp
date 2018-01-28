#include <iostream>
#include "linkedlist.h"

using namespace std;

LinkedList * sumLL(LinkedList * L1, LinkedList * L2)
{
    int sum1 = L1->reverseValue();
    int sum2 = L2->reverseValue();

    int finalSum = sum1 + sum2;

    LinkedList * LLF = new LinkedList();

    while (finalSum != 0)
    {
        int digit = finalSum % 10;
        finalSum = finalSum / 10;
        LLF->appendNode(digit);
    }

    return LLF;
}

int main()
{
    cout << "Begin Linked List Playground..." << endl;

    // CTCI: Question 2.1
    LinkedList * firstList = new LinkedList();
    firstList->appendNode(7);
    firstList->appendNode(1);
    firstList->appendNode(8);
    firstList->printList();
    
    LinkedList * secondList = new LinkedList();
    secondList->appendNode(5);
    secondList->appendNode(9);
    secondList->appendNode(2);
    secondList->printList();
    
    LinkedList * thirdList = sumLL(firstList, secondList);
    thirdList->printList(); 

    return 0;
}


