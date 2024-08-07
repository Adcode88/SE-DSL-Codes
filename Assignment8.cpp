#include <iostream>
#include <list>
using namespace std;

// Node class  
class node {
    public:
    int start;
    float end;
    int min;
    int max;
    bool booking; 
    node *next;  
};

class list1{
    public:
    node *head;
    list1(){head=NULL;}
    void append(int start, int min, int max);
    void add_appointment();
    void display();
    void book(int start);
    void cancel(int start);
    void sort();
    void sortptr();
    void swap(node *prev, node *current, node *nextnode);
};


void list1::append(int start, int min, int max){
    node *newnode, *nextnode;
    newnode = new node;
    newnode->start = start;
    newnode->end = start + (float)(max+min)/2;
    newnode->max = max;
    newnode->min = min;
    newnode->booking = false;

    if (!head){
        this->head = newnode;
    }
    else{
        nextnode = this->head;
        while(nextnode->next){
            if (nextnode->start == start){
                break;
            }
            else{
            nextnode = nextnode->next;
            }
        }
        if (nextnode->start == start){
            cout<<"Slot already added!\n";
            delete newnode;
        }
        else{
            nextnode->next = newnode;
        }
    }
}

void list1::add_appointment(){
    int start, min, max;
    float end;
    cout<<"Enter start time: ";
    cin>>start;
    cout<<"Enter minimum time: ";
    cin>>min;
    cout<<"Enter maximum time: ";
    cin>>max;
    cout<<endl<<endl;
    this->append(start, min, max);
}


void list1::display(){
    node *nextnode;
    if (!head){
        cout<<"No slot is added!\n";
    }
    else{
        nextnode = head;
        while(nextnode){
            if (!nextnode->booking){
            cout<<"Start:"<<nextnode->start<<endl;
            cout<<"End:"<<nextnode->end<<endl;
            cout<<"Minimum time:"<<nextnode->min<<endl;
            cout<<"Maximum time:"<<nextnode->max<<endl;
            cout<<endl;
        }
            nextnode = nextnode->next;
        }
    }
}



void list1::book(int start){
    node *nextnode;
    bool temp = 0;
    if (!head){
        cout<<"no slots are available\n";
    }
    else{
        nextnode = head;
        while(nextnode){
            if (nextnode->start == start){
                if (nextnode->booking){
                    cout<<"Slot is already booked\n";
                    temp = 2;
                    break;
                }
                else{
                nextnode->booking = true;
                cout<<"Slot is booked!\n";
                temp = 1;
                break;
                }
            }
            nextnode = nextnode->next;
        }
        if (!temp){
            cout<<"Slot is not available\n";
        }
    }
}

void list1::cancel(int start){
    node *nextnode;
        if (!head){
            cout<<"no slots are available\n";
        }
        else{
            nextnode = head;
            while(nextnode){
                if (nextnode->start == start){
                    nextnode->booking = false;
                    cout<<"Slot is canceled!\n";
                    break;
                }
                nextnode = nextnode->next;
            }
            if (!nextnode){
                cout<<"Slot is not available\n";
            }
        }
}
void list1::swap(node *prev, node *current, node *nextnode){
    prev->next = nextnode;
    current->next = nextnode->next;
    nextnode->next = current;
}


void list1::sortptr(){
    node *current;
    node*previous;
    node *nextnode;
    int length = 0;
    if (!head){
        cout<<"List is empty\n";
    }
    else{
        current = head;
        nextnode = head;
        while(nextnode){
            nextnode = nextnode->next;
            length++;
        }
        while(length>2){
            current = head;
            nextnode = current->next;
            //to swap first two elements
            if (current->start > nextnode->start){
                current->next = nextnode->next;
                nextnode->next = current;
                head = nextnode;
                previous = nextnode;
                nextnode = current->next;
            }
            else{
                previous = current;
                current = nextnode;
                nextnode = current->next;
            }
            for(int i = 0; i<length-2; i++){
                if (current->start > nextnode->start){
                    this->swap(previous, current, nextnode);
                    previous = nextnode;
                    nextnode = current->next;
                }
                else{
                    previous = current;
                    current = nextnode;
                    nextnode = current->next;
                }
            }
            length--;
        }
    }
}



int main(){
    list1 a;
    cout<<"Enter 0 to exit : \n";
    cout<<"Enter 1 to add appointment \n";
    cout<<"Enter 2 to get all available slots \n";
    cout<<"Enter 3 to book appointment\n";
    cout<<"Enter 4 to cancel appointment\n";
    cout<<"Enter 5 to get sorted list of appointments\n";
    int c;
    while(true){
        cout<<"Enter your choice: ";
        cin>>c;
        if (c == 0){
            break;
        }
        else if (c == 1){
            a.add_appointment();
        }
        else if (c == 2){
            a.display();
        }
        else if (c == 3){
            int s;
            cout<<"Enter slot time: ";
            cin>>s;
            a.book(s);
        }
        else if (c == 4){
            int s;
            cout<<"Enter slot time: ";
            cin>>s;
            a.cancel(s);
        }
        else if (c == 5){
            a.sortptr();
            a.display();
        }
    }
}