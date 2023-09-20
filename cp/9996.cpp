#include <bits/stdc++.h>
using namespace std;

int n, pos;
string temp, str, pre, suf;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    cin >> temp;
    pos = temp.find("*");
    pre = temp.substr(0, pos);
    suf = temp.substr(pos + 1);

    for(int i = 0; i < n; i++) {
        cin >> str;
        if(str.size() >= pre.size() + suf.size()) {
            if(str.substr(0, pre.size()) == pre && str.substr(str.size() - suf.size()) == suf) {
                cout << "DA" << "\n";
            }
            else cout << "NE" << "\n";
        }
        else cout << "NE" << "\n";
    }


    return 0;
}