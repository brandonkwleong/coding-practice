/* Node Class */

class Node
{
    public:
        Node();

        int value;
        Node * next;
};

class LinkedList
{
    Node * head;

    public:
        LinkedList();
        ~LinkedList();

        void printList();
        bool appendNode(int value);
        Node * getNthNode(int n);
        Node * insertNode(Node * loc, int value);

        bool deleteNode(Node * tbd);
        bool deleteValues(int value);
        bool deleteAllDuplicates();

        int kthToLast(int k);
        int kthToLastRecursive(int k);
        int kthToLastR(Node * start, int k, int & kthValue);

        bool deleteMiddleNode(Node * deleter);

        bool partition(int part);

        int reverseValue();
};


