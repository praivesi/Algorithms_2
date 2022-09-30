#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int UNDEFINED = -987654321;
const int CACHE_LENGTH = 9;
const int CACHE_BUFFER = 100000;

int cache[CACHE_LENGTH][CACHE_BUFFER];

int UNIT;
int GOAL;

vector<int> calculate(int n, int count){
    vector<int> nums;

    if(count == 0){
        return nums;
    }

    if (count == 1)
    {
        nums.push_back(n);
        return nums;
    }

    if (cache[count][0] != UNDEFINED)
    {
        int iter = 0;
        while (cache[count][iter] != UNDEFINED)
        {
            nums.push_back(cache[count][iter]);
            iter++;
        }

        return nums;
    }

    int front = 1;
    int near = count - 1;

    int max = 0;
    for (int i = 0; i < count; i++)
    {
        max *= 10;
        max += n;
    }

    nums.push_back(max);

    while (front <= near)
    {
        vector<int> fvec = calculate(n, front);
        vector<int> nvec = calculate(n, near);

        fvec.erase(unique(fvec.begin(), fvec.end()), fvec.end());
        nvec.erase(unique(nvec.begin(), nvec.end()), nvec.end());

        for (int fv : fvec)
        {
            for (int nv : nvec)
            {
                nums.push_back(fv + nv);
                nums.push_back(fv - nv);
                nums.push_back(fv * nv);
                nums.push_back(fv / nv);
            }
        }
    }

    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    return nums;
}

int solution(int N, int number)
{
    int answer = 0;

    UNIT = N;
    GOAL = number;

    for (int i = 0; i < CACHE_LENGTH; i++)
    {
        for (int j = 0; j < CACHE_BUFFER; j++)
        {
            cache[i][j] = UNDEFINED;
        }
    }

    return answer;
}