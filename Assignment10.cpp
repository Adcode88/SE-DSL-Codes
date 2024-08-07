#include <iostream>
using namespace std;

class InfixtoPostfix{
    
    private:

    int top = -1;
    char st[20];

    public:
    
    char ch;
    int i, j;

    InfixtoPostfix(char inf[20], char post[20]){
      
      j = 0;
      
      for(i=0; inf[i]!='\0'; i++){
        
        ch = inf[i];
        if(ch == '('){
            top++;
            st[top] = ch;
        }
        else{
            if(operato(ch) == 1){
                while(top!=-1 && priority(ch)>=priority(st[top])){
                    post[j] = st[top];
                    top--;
                    j++;
                }
                top++; 
                st[top] = ch;
            }
            else{
                if(ch == ')'){
                    while(top!=-1 && st[top]!='('){
                        post[j] = st[top];
                        top--;
                        j++;
                        }
                    top--;
                    }
                else{
                    post[j] = ch; 
                    j++;
                }
            }
        }
    }
    while(top!=-1){
        post[j] = st[top];
        top--;
        j++;
    }
    post[j] = '\0';
}

  int operato(char ch){
    if (ch == '+'|| ch == '-' || ch == '*' || ch == '/'){
      return (1);
      }
    else{
      return 0;
      }
  }

  int priority(char ch){
      switch (ch){
          case '/':
          case '*': return(1);
          case '+':
          case '-': return(2);
          default : return(3);
      }
  }

};


int main()
{
    cout << endl << endl;

    char inf[20], post[20], post2[20], inf2[20];

    while(1<2){

        int n;
        cout << "Enter 1 to enter Expression \nEnter 0 to exit \nEnter your choice:";
        cin>>n;

        if(n==0){
            break;
        }
        
        cout << endl;

        cout<<"Enter infix expression : ";
        cin>>inf;

        cout << "Press 1 for Prefix \nPress 2 for Postfix";

        int choice;

        cin >> choice;

        if(choice==1){

          int k=0;
          
          InfixtoPostfix obj1(inf,post);

          for(int i=obj1.j;i>=0;i--){

            inf2[k]=inf[i];
            k++;
            
          }

          inf2[k]='\0';

          InfixtoPostfix obj2(inf2,post2);

          cout<<"Prefix expression is : "<<post2<<endl;

        }
        else if(choice==2){

          InfixtoPostfix obj1(inf,post);
          cout<<"Postfix expression is : "<<post<<endl;

        }
        else{
          cout << "INVALID INPUT";
        }

        cout << endl;
    }

    cout << endl << endl;

    return 0;
}


/*#include<iostream>
using namespace std;

char stack[10];
int top = -1;

void expConvert(){
  char infix[20];
  char postfix[20];
  int i = 0;
  int j = 0;
  cout<<"\n\n Enter the Infix Expression: ";
  cin>>infix;
  for(i=0; infix[i] != '\0'; i++){
    if(infix[i] == '(' || infix[i] == '[' || infix[i] == '{'){
      top++;
      stack[top] = infix[i];
      }
    else if(infix[i] == 'a' || infix[i] == 'b' || infix[i] == 'c' || infix[i] == 'd')
    {
      postfix[j] = infix[i];
      j++;
      }
    else if(infix[i] == '+' || infix[i] == '-' || infix[i] == '*' || infix[i] == '/'){
      top++;
      stack[top] = infix[i];
      }
    else{
      switch(infix[i]){
        case ')': while(stack[top] != '('){
          postfix[j] = stack[top];
          j++;
          top--;
          }
        top--;
        break;
        case ']': while(stack[top] != '['){
          postfix[j] = stack[top];
          j++;
          top--;
          }
        top--;
        break;
        case '}': while(stack[top] != '{'){
          postfix[j] = stack[top];
          j++;
          top--;
          }
        top--;
        break;
        }
      }
    }
  postfix[j] = '\0';
  cout<<"\n\t The Postfix String: "<<postfix;
}

int main()
{
  cout<<"\n-----------------------------------------------\n";
  cout<<"**** Expression Conversion : Infix to Postfix **** ";
  cout<<"\n-----------------------------------------------\n";
  expConvert();
  cout<<"\n\n";
  return 0;
}*/