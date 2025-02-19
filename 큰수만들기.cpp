#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

string solution(string number, int k){
    stack<char> st;
    string result;

    for(int i : number){
        while (!st.empty() && st.top() < i && k>0 )
        {
            st.pop();
            k--;
        }

        st.push(i); 
        
    }

    while (!st.empty()) {
        result = st.top() + result; // 문자열의 앞에 추가 (뒤집힘 방지)
        st.pop();
    }


    
}

