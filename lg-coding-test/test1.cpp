#include <string>
#include <vector>

using namespace std;

int main(){

}


int solution(vector<int> arr) {
    int** count = new int*[arr.size()];
    int* moved = new int[arr.size()];

    for(int i = 0; i < arr.size(); i++){
        count[i] = new int[10];
    }

    for(int i = 0; i < arr.size(); i++){
        moved[i] = false;
        for(int j = 0; j < 10; j++){
            count[i][j] = 0;
        }
    }

    for (int i = 0; i < arr.size(); i++)
    {
        int number = arr[i];

        int curDigit = -1;
        while (number != 0)
        {
            curDigit = number % 10;
            number /= 10;

            count[i][curDigit]++;
        }
    }

    int groupCnt = 0;
    for(int i = 0; i < arr.size(); i++){
        moved[i] = true;
        groupCnt++;

        for(int j = 0; j < arr.size(); j++){
            if(moved[j]) {continue;}

            int matched = false;
            for(int k = 0; k < 10; k++){
                if(count[i][k] != count[j][k]){
                    matched = true;
                    break;
                }
            }

            if(matched){
                moved[j] = true;
            }
        }
    }

    return groupCnt;
}