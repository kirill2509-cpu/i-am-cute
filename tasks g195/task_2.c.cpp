
#include <iostream>
using namespace std;

int main()
{
    double m;
    cout << "enter the meters: ";
    cin >> m;
    double km;
    cout << "enter kilometers: ";
    cin >> km;
    double c;
    c = km * 1000;
    if (c < m) {
        cout << c << " meters";
    }
    else  {
        cout << m << " meters";
    }

}

