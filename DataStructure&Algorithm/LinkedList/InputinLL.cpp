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

Node * input(){
    int data;
    cin >> data;
    Node * head = NULL;
    // tail is created which stores the address of the last node!
    Node * tail = NULL;
    // when user want to end the link list he/she hass to add -1!
    while (data != -1)
    {
        Node *newnode = new Node(data);
        if(head == NULL){
            head = newnode;
            tail = newnode;
        } 
        else
        {
            tail -> next = newnode;
            tail = tail -> next;
        }
        cin>>data;
    }
    return head;
}

void ans(Node * head){
    // temp variable is created bcz we have to save the value of head for further processes!
    Node * temp =head;

    while (temp != NULL)
    {
        cout << temp->data << endl;
        temp = temp->next;
    }
    
}

int main(){
    Node * head =input();
    ans(head);
    return 0;
}


// CodeBy:RahulMahajan
// CC:anonymous0201
// CF:anonymous3107