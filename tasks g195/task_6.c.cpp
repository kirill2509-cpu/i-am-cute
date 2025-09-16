
#include <iostream>
using namespace std;

int main()
{
    int m;
    int n;
    cout << "vvedite chislo: ";
    cin >> m;
    cout << "vvedite chislo: ";
    cin >> n;
    if (m > n) {
        cout << "number: " << m << " > " << n;
    }
    else if (m < n) {
        cout << "number: " << m << " < " << n;
    }
    else {
        cout << "The numbers are equal";
    }
}
