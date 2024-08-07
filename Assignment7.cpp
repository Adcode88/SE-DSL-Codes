#include <iostream>
using namespace std;

struct ListNode{
	struct ListNode *next = NULL;
	struct ListNode *previous = NULL;
	bool book = 0;
};


class Cinemax{
public:
	ListNode *ptr[10];
	static int counter;
	Cinemax(){
		ListNode *newnode;
		ListNode *previous;
		for(int i = 0; i<10; i++){
			newnode = new ListNode;
			ptr[i] = newnode;
			previous = newnode;
			for(int j = 0; j<6; j++){
			newnode = new ListNode;
			newnode->previous = previous;
			previous->next = newnode;
			previous = newnode;
			}
			newnode->next = ptr[i];
			ptr[i]->previous = newnode;
		}

	}

	void Display(){
		ListNode *nptr;
		for (int i = 0; i<10; i++){
			nptr = ptr[i];
			for(int j = 1; j<= 7; j++){
				if (!nptr->book){
					cout<<i<<j<<"\t";
				}
				else{
					cout<<"NA\t";
				}
				nptr = nptr->next;
			}
			cout<<endl;
		}
	}

	void Book(int row, int seat){
		if (seat>8 || row>10){
			cout<<"Out of range \n";
		}
		else{
			ListNode *newnode;
			newnode = ptr[row];
		for(int i = 1; i<seat; i++){
			newnode = newnode->next;
		}
		if (newnode->book){
			cout<<"Seat is already booked\n";
		}
		else{
			newnode->book = true;
			cout<<"Seat is booked\n";
		}
		}
	}

	void cancel(int row, int seat){
		if (seat>8 || row>10){
				cout<<"Out of range";
			}
			else{
				ListNode *newnode;
				newnode = ptr[row];
			for(int i = 1; i<seat; i++){
				newnode = newnode->next;
			}
			if (!newnode->book){
				cout<<"Seat is not booked\n";
			}
			else{
				newnode->book = false;
				cout<<"Booking is canceled\n";
			}
		}
	}
};
int Cinemax::counter = 0;

int main(){
	Cinemax c;
		int choice;
		while(true){
            cout<<"Enter 0 to exit \n";
            cout<<"Enter 1 to book seat \n";
            cout<<"Enter 2 to cancel seat \n";
            cout<<"Enter 3 to see available seats\n";
			cout<<"Enter your choice: ";
			cin>>choice;
			if (choice == 0){
				break;
			}
			else if (choice == 1){
				int r, s;
				cout<<"Enter seat(row seat): ";
				cin>>r>>s;
				c.Book(r, s);
			}
			else if (choice == 3){
				c.Display();
			}
			else if (choice == 2){
				int r, s;
				cout<<"Enter seat(row seat): ";
				cin>>r>>s;
				c.cancel(r, s);
			}
		};
}

