#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "russian");  

    int size_a;
    cout << "Введите размер первого массива: ";
    cin >> size_a;

    int a[1];
    cout << "Введите " << size_a << " чисел для первого массива:" << endl;

    for (int i = 0; i < size_a; i++) {
        cin >> a[i];
    }

    int size_b;
    cout << "Введите размер второго массива: ";
    cin >> size_b;
    int b[1];

    cout << "Введите " << size_b << " чисел для второго массива:" << endl;
    for (int i = 0; i < size_b; i++) {
        cin >> b[i];
    }

    int result[1];
    int count = 0;

    
    for (int i = 0; i < size_a; i++) {
        bool found = false;

        
        for (int j = 0; j < size_b; j++) {
            if (a[i] == b[j]) {
                found = true;
                break;
            }
        }

        
        if (!found) {
            result[count] = a[i];
            count++;
        }
    }

    cout << "Результат: ";
    for (int i = 0; i < count; i++) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}