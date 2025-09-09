
#include <iostream>
using namespace std;

int main()
{ 
    int n;
    cout << "enter a number from 0 to 9: ";
    cin >> n;
    if (n < 0 || n>9) {
        cout << "error";
        return 1;
    }
    for (int i = 0; i <= 9; i++) {
        cout << n << " * " << i << " = " << n * i << endl;
    }
    
}
