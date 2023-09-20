#include <bits/stdc++.h>
using namespace std;

string s;

bool is_mo(string a) {
    if (a == "a" || a == "e" || a == "i" || a == "o" || a == "u"){
        return true;
    }
    else return false;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while(true) {
        cin >> s;
        if(s == "end") break;

        int cnt_mo = 0, cnt_ja = 0, flag = 1, flag2 = 0, prev = -1;

        for(int i = 0; i < s.size(); i++) {
            if(prev >= 0 && (s[prev] == s[i]) && s[i] != 'e' && s[i] != 'o') {
                flag = 0;
                break;
            }

            if(is_mo(string(1, s[i]))) {
                flag2 = 1;
                cnt_mo++;
                cnt_ja = 0;
            }
            else {
                cnt_ja++;
                cnt_mo = 0;
            }

            if(cnt_mo == 3 || cnt_ja == 3) {
                flag = 0;
                break;
            }
            prev = i;
        }
        if(flag && flag2) cout << "<" << s << "> is acceptable.\n";
        else cout << "<" << s << "> is not acceptable.\n";
    }
    return 0;
}