#include<iostream>
using namespace std;
#define max 50

class Queue{

    private:
    string queue[max];
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

    void enqueue(string element){
        if(full()==1){
            cout << "\nOverflow";
        }
        else if(empty()==1){
            front=0;
            rear=0;
            queue[0]=element;
        }
        else{
            rear++;
            queue[rear]=element;
        }
    }

    void dequeue();

    void display(){
        if(empty()==1){
            cout << "\nUnderflow";
        }
        else{
            for(int i=front; i<=rear; i++){
                cout << "Job" << i+1-front << ": " << queue[i] << "  ";
            } 
        }
        cout << endl;

    }

};

void Queue :: dequeue(){
        if(empty()==1){
            cout << "\nUnderflow";
        }
        else{
            front++;
        }
    }

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
            cout << "Enter Job Code: ";
            cin >> job;
            cout << endl; 
            q.enqueue(job);
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