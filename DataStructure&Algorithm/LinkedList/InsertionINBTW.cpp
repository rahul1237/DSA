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


void insert(Node *head,int i,int data){
    Node *newnode= new Node(data);
    int a = 0;
    Node * temp = head;
    while (a<i-1)
    {
        temp=temp->next;
        a++;
    }

    Node *b=temp->next;
    temp->next = newnode;
    newnode->next=b;
    
}


void ans(Node * head){
    // temp variable is created bcz we have to save the value of head for further processes!
    Node * temp =head;

    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    
}

int main(){
    cout<<"Enter the elements of linked list and -1 to exit!"<<endl;
    Node * head =input();
    int i;
    int data;
    cout<<"Enter the index of new node and its value!"<<endl;
    cin >> i >>data;
    // ans(head);
    insert(head,i,data);
    cout<<" "<<endl;
    ans(head);
    return 0;
}


// CodeBy:RahulMahajan
// CC:anonymous0201
// CF:anonymous3107