#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int solution(string name){

    string alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    unordered_map<char,int> dic;

    for(int i; i<= alpa.size(); i++){
        dic[alpa[i]] = min(i, 26-i);
    };

    int move = name.length() -1 ;
    int total = 0;

    for(int i; i<name.length(); i++){
        total = total + dic[name[i]];

    }




}