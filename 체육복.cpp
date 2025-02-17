#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void removeValue(vector<int>& vec, int value){
    vec.erase(remove(vec.begin(), vec.end(), value), vec.end());
}

int solution(int n, vector<int> lost, vector<int> reserve){

    sort(lost.begin(), lost.end());
    vector<int> lost1 = lost;

    for(int i: lost1){
        if(find(reserve.begin(), reserve.end(), i) != reserve.end()){
            removeValue(lost, i);
            removeValue(reserve, i);

        }

    }

    vector<int> lost2 = lost;

    for(int i: lost2){

        if(find(reserve.begin(), reserve.end(), i-1) != reserve.end()){
            removeValue(lost, i);
            removeValue(reserve, i-1);
        }

        else if (find(reserve.begin(), reserve.end(), i+1) != reserve.end()){
            removeValue(lost, i);
            removeValue(reserve, i+1);
        }

    }

    return n - lost.size();
    


}
