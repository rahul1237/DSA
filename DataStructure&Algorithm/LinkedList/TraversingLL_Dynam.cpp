#include <iostream>
using namespace std;


class Node{
    public:
    int data;
    Node * next;
    Node(int data){
        this -> data = data;
        next = NULL;
    }
};

void ans(Node * head){
    // temp variable is created bcz we have to save the value of head for futher processes!
    Node * temp =head;

    while (temp != NULL)
    {
        cout << temp->data << endl;
        temp = temp->next;
    }
    
}

int main(){
    Node * n1 =new Node(1);
    // head variable store the block n1 which contains address of node n1
    Node * head = n1;
    Node * n2 =new Node(2);
    Node * n3 =new Node(3);
    Node * n4 =new Node(4);
    Node * n5 =new Node(5);
    n1->next=n2;
    n2->next=n3;
    n3->next=n4;
    n4->next=n5;

    ans(head);

    return 0;
}


// CodeBy: RAHUL MAHAJAN
// CC: anonymous0201
// CF: anonymous3107