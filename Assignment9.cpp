#include <iostream>
using namespace std;

class Stack{
    private:

    char stack[20];
    int top=-1;

    public:
    
    int i;

    Stack(char inp[20]){
        for(i=0; inp[i]!='\0'; i++){
            if(inp[i]=='(' || inp[i]=='{' || inp[i]=='['){
                top=top+1;
                stack[top]=inp[i];
            }
            else if(inp[i]==')' || inp[i]=='}' || inp[i]==']'){
                top--;
            }
        }
        if(top == -1){
            cout << "Expression is Correctly Paranthesized";
        }
        else{
            cout << "Expression is NOT Correctly Paranthesized";
        }
    }
};

int main(){

    char inp[20];

    cout << "Enter Expresion:";
    cin >> inp;

    Stack obj1(inp);

    return 0;
}


/*class StackNode{
public:
	char charachter;
	StackNode *next = NULL;
};

class Stack{
public:
	StackNode *head = NULL;
	bool push(char a);
	bool pop();
	bool isEmpty();
	void display();
	char getTop();

};

void Stack::display(){
	StackNode *nextnode;
	if (!head){
		cout<<"Empty\n";
	}
	else{
		nextnode = head;
		while (nextnode)
		{
            cout<<nextnode->charachter<<endl;
			nextnode = nextnode->next;
		}
		
	}
}

bool Stack::push(char a){
	StackNode *newnode;
	newnode = new StackNode;
	newnode->charachter = a;

	if (!head){
		head = newnode;
	}
	else{
		StackNode *next;
		next = head;
		while(next->next){
			next = next->next;
		};
		next->next = newnode;
	}
	return 1;
}

bool Stack::pop(){
	if (!head){
		return 0;
	}
	else{
		StackNode *next, *prev;
		next = head;
		if (!next->next){
			delete next;
			head = NULL;
		}
		else{
			prev = next;
			next = next->next;
		while(next->next){
			prev = next;
			next = next->next;
		};
		delete next;
		prev->next = NULL;
		}
	}
	return 1;
}

bool Stack::isEmpty(){
	if (!head){
		return 1;
	}
	else{
		return 0;
	}
}

char Stack::getTop(){
	if (!head){
		return '0';
	}
	else{
		StackNode *nextnode;
		nextnode = head;
		while (nextnode->next)
		{
			nextnode = nextnode->next;
		}
		return nextnode->charachter;		
	}
}

int main(){

    cout << "\n";
    cout << "\n";
    cout << "\n";

    int check = 1;

    while(1<2){
        cout << "TO EXIT PRESS 0 \nTO ENTER EQUATION PRESS 1 \nENTER:";
        cin >> check;
        cout << "\n";
        if(check == 0 ){
            cout << "\n";
            cout << "EXITED";
            cout << "\n";
                        
            break;
        }
        char s;
        Stack st;
        int i =0;
        cout << "Enter The Equation: ";
        string equ;
        cin >> equ;
        cout << "\n";
        while(equ[i] != '\0'){
            s = equ[i];
            switch (s)
            {
            case '(':
                st.push('(');
                break;
            case '[':
                st.push('[');
                break;
            case '{':
                st.push('{');
                break;
            case ')':
                if (st.getTop() == '('){
                    st.pop();
                }
                else{
                    cout<<"Problem in equation\n";
                    return 0;
                }
                break;
            case ']':
                if (st.getTop() == '['){
                    st.pop();
                }
                else{
                    cout<<"Problem in equation\n";
                    return 0;
                }
                break;
            case '}':
                if (st.getTop() == '{'){
                    st.pop();
                }
                else{
                    cout<<"Problem in equation\n";
                    return 0;
                }
                break;
            default:
                break;
            }
            i++;
        }
        if (st.isEmpty()){
            cout<<"Equation is correct\n";
        }
        else{
            cout<<"Problem in equation\n";
        }
        cout << "\n" ;
    }
}
*/