#include <iostream>
using namespace std;

class Node{
    public:
    int data;
    Node *next;
    Node(int data){
        this -> data = data;
        next=NULL;
    }
};

void ansend(Node * head){
    while (head!= NULL)
    {
        cout<< head -> data << endl;
        head=head -> next;
    }
}

void anstend(Node * head){
    while (head->next!=NULL)
    {
        cout<< head->data << endl;
        head=head->next;
    }
    
}


int main(){
    Node n1(1);
    Node *head = &n1;
    Node n2(2);
    n1.next = &n2;
    Node n3(3);
    n2.next = &n3;
    Node n4(4);
    n3.next = &n4;
    Node n5(5);
    n4.next = &n5;
    // for printing the linklist till it end!
    cout<< "Whole Elements Of LinkedList"<<endl;
    ansend(head);
    // for stop printing where null is present in node
    cout<< "First n-1 elements of LinkedList if orignal Length is 'n' "<<endl;
    anstend(head);
    return 0;
}