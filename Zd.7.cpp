
#include <iostream>
using namespace std;

int main()
{
    double r;
    cout << "vvedite radius: ";
    cin >> r;
    double d = 2 * r;
    cout << "diametr: " << d << endl << endl;

    int s = 0;
    for (int i = 100; i <= 500; i++) {
        s += i;
    }
    cout << "summa ot 100 do 500 = " << s << endl << endl;

    int a;
    cout << "Vvedite chislo a: ";
    cin >> a;

    if (a >= 500) {
        cout << "Error!" << endl;
        return 1;
    }

    int W = 0;
    for (int i = a; i <= 500; i++) {
        W += i;
    }
    cout << "Summa chisel ot " << a << " do 500: " << W << endl;

    return 0;
}