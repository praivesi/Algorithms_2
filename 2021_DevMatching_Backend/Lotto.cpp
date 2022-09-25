#include <string>
#include <vector>
#include <iostream>

using namespace std;

int getRank(int count){
    if(count == 6) return 1;
    else if(count == 5) return 2;
        else if(count == 4) return 3;
        else if(count == 3) return 4;
        else if(count == 2) return 5;
        else return 6;
}

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    
    int zeros = 0;
    bool matchFlag = false;
    vector<int> unmatched, matched;
    for(int i = 0; i < 6; i++){
        if(lottos[i] == 0){
            zeros++;
        }
        
        for(int j = 0; j < 6; j++){
            if(win_nums[i] == lottos[j])
            {
                matched.push_back(win_nums[i]);
                matchFlag = true;
                break;
            }
        }
        
        if(!matchFlag){
        unmatched.push_back(win_nums[i]);
        } 
        
        matchFlag = false;
    }
    
    int maxNums = matched.size() + zeros;
    maxNums = maxNums > 6 ? 6 : maxNums;
    
    answer.push_back(getRank(maxNums));
    answer.push_back(getRank(matched.size()));
    
    return answer;
}