#include <bits/stdc++.h>
using namespace std;

string s, s2;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> s;
    s2 = s;
    reverse(s2.begin(), s2.end());

    if(s == s2) cout << 1 << "\n";
    else cout << 0 << "\n";



    return 0;
}