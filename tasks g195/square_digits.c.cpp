

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    int c;
    cout << "vvedite chislo: ";
    cin >> c;
    string ns = to_string(c);
    string result = "";
    for (char w : ns) {
        int x = w - '0';
        int z = x * x;
        result += to_string(z);
    }
    int otv = 0;
    for (char c : result) {
        otv = otv * 10 + (c - '0');
        
    }
    cout << "otvet: " << otv;
    return otv;
  
    
}