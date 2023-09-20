#include <bits/stdc++.h>
using namespace std;

int answer[1000004], arr[1000004], n, temp;
stack<int> st;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    fill(&answer[0], &answer[0] + n, -1);

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    for(int i = 0; i < n; i++){
        temp = arr[i];
        while(st.size() && arr[st.top()] < temp) {
            answer[st.top()] = temp;
            st.pop();
        }
        st.push(i);
    }


    for(int i = 0; i < n; i++) cout << answer[i] << " ";

    cout << "\n";
    return 0;
}