#include <bits/stdc++.h>
using namespace std;

int flag, arr[26];
string s, res, mid;

int main() {

    cin >> s;

    for(int i = 0; i < s.size(); i++) {
        arr[(int)s[i] - 65]++;
    }

    for(int i = 0; i < 26; i++) {
        if(arr[i] & 1) {
            flag++;
            arr[i]--;
            if(flag == 2) {
                cout << "I'm Sorry Hansoo" << "\n";
                return 0;
            }
            mid = char(i + 65);
        }
        for(int j = 0; j < arr[i]; j += 2){
            res += char(i+65);
        }
    }

    cout << res << mid;
    reverse(res.begin(), res.end());
    cout << res << "\n";
    return 0;
}