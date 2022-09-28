#include <iostream>
#include <vector>
#include <utility>

using namespace std;

class ThreeFractions {
public:
    ThreeFractions();
    vector<int> find(int, int, int, int);
};

// int main(){
//     ThreeFractions* tf = new ThreeFractions();
//     vector<int> result = tf->find(1, 3, 2, 3);
    
//     for(int r : result){
//         cout << r << ", ";
//     }
//     cout << endl;

//     return 0;
// }

int getGcd(int a, int b) // 최대공약수
{
	int c;
	while (b != 0)
	{
		c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int getLcm(int a, int b) // 최소공배수
{
    return a * b / getGcd(a, b);
}


template <typename T>
bool contains(vector<T> vec, const T & elem)
{
    bool result = false;

    for(T vi : vec){
        if(vi == elem){
            result = true;
            break;
        }
    }

    return result;
}

ThreeFractions::ThreeFractions(){}

vector<int> ThreeFractions::find(int n1, int d1, int n2, int d2){
    vector<int> result;

    int lcm = getLcm(d1, d2);
    int maxLcm = 0;
    int i = 1;

    while(maxLcm < 1000000000){
        i++;
        maxLcm = lcm;
        maxLcm *= i;
    }

    maxLcm = lcm * (i - 1);

    n1 *= (maxLcm / d1);
    n2 *= (maxLcm / d2);

    int curN = n1 + 1;

    while(curN != n2){
        int curGcd = getGcd(curN, maxLcm);

        int candN = curN / curGcd;
        int candD = maxLcm / curGcd;
        if(!contains(result, candN) && !contains(result, candD)){
            result.push_back(candN);
            result.push_back(candD);

            if(result.size() == 6){
                break;
            }
        } 
        
        curN++;
    }

    return result;
}

