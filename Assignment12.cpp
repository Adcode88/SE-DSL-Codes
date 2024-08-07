#include<iostream>
using namespace std;
#define max 50

struct QueueElement{
    string data;
    int priority;
};

class Queue{
    private:

    QueueElement queue[max];
    int front, rear;

    public:

    void initialise(){
        front = -1;
        rear = -1;
    }

    int full(){
        if(rear==max-1){
            return 1;
        }
        else
            return 0;
    }

    int empty(){
        if((front==-1 && rear==-1) || (front==rear+1)){
            return 1;
        }
        else{
            return 0;
        }
    }

    void enqueue(string element, int priority){
        if(full()==1){
            cout << "\nOverflow";
        }
        else if(empty()==1){
            front=0;
            rear=0;
            queue[0].data=element;
            queue[0].priority=priority;
        }
        else{
            rear++;
            for(int i=rear-1;i>=front;i--){
                if(priority<queue[i].priority){
                    queue[i+1].data=queue[i].data;
                    queue[i+1].priority=queue[i].priority;
                    queue[i].data=element;
                    queue[i].priority=priority;
                }
                else{
                    queue[i+1].data=element;
                    queue[i+1].priority=priority;
                    break;
                }
            }
        }
    }

    void dequeue(){
        if(empty()==1){
            cout << "\nUnderflow";
        }
        else{
            front++;
        }
    }

    void display(){
        if(empty()==1){
            cout << "\nUnderflow";
        }
        else{
            for(int i=front; i<=rear; i++){
                cout << "Job" << queue[i].priority << ": " << queue[i].data << "  ";
            } 
        }
        cout << endl;

    }

};

int main(){

    Queue q;
    q.initialise();
    
    while(1<2){

        cout << endl; 
        cout << endl;

        int c;

        cout << "Press 0 to exit\nPress 1 to Add Job\nPress 2 to Delete Job\nPress 3 to Display Job Queue\n";
        cout << "Enter Your Choice:";
        cin >> c;
        cout << endl;

        if(c==0){
            break;
        }
        else if(c==1){
            string job;
            int priority;
            cout << "Enter Job Code: ";
            cin >> job;
            cout << endl; 
            cout << "Enter Priority: ";
            cin >> priority;
            cout << endl; 
            q.enqueue(job,priority);
        }
        else if(c==2){
            q.dequeue();
        }
        else if(c==3){
            cout << endl;
            q.display();
        }
        else{
            cout << "INVALID INPUT";
        }

    }

    cout << endl; 
    cout << endl;

    return 0;
}