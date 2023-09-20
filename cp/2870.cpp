#include <bits/stdc++.h>
using namespace std;

int n;
string s;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    vector<string> answer;

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> s;

        string temp = "";
        for(int j = 0; j < s.size(); j++) {
            if(s[j] >= 'a' && s[j] <= 'z') {
                if(temp.size()) {
                    answer.push_back(temp);
                    temp = "";
                }
            }
            else {
                if(temp.size() == 0 && s[j] == '0') continue;
                else {
                    temp += s[j];
                }
            }
        if(temp.size()) answer.push_back(temp);
        }
    }

    sort(answer.begin(), answer.end());
    for(string i : answer) cout << i << "\n";
    return 0;
}