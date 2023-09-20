#include <bits/stdc++.h>
using namespace std;

int n;

int main() {
    cin >> n;

    int num = 666;
    int i = 0;

    while(true) {
        if(to_string(num).find("666") != string::npos) i++;
        if(i == n) break;

        num++;
    }


    cout << num << "\n";
    return 0;
}