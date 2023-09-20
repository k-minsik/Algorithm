#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int a, b, c;

    while(true) {
        cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0){
            break;
        }
        if (c*c == b*b + a*a) {
            cout << "right" << "\n";
        }
        else if (b*b == c*c + a*a) {
            cout << "right" << "\n";
        }
        else if (a*a == b*b + c*c) {
            cout << "right" << "\n";
        }
        else {
            cout << "wrong" << "\n";
        }
    }



    return 0;
}