#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

stack<char> st;

const char ALIAS = '&';
string angel = "";

void decomp(char c)
{
    if (c == ')')
    {
        char popC = ' ';
        char buf[10000] = {
            0,
        };

        int pos = 0;
        popC = st.top();
        st.pop();

        while (popC != '(')
        {
            buf[pos] = popC;
            pos++;

            popC = st.top();

            
            st.pop();

             if (popC == '(')
            {
                break;
            }

           
        }

        string str = "";

        for (int i = 0; i < pos; i++)
        {
            if (buf[pos - i - 1] == '&')
            {
                str += angel;
            }
            else
            {
                str += buf[pos - i - 1];
            }
        }

        char numBuf[10000] = {
            0,
        };
        int numPos = 0;

        popC = st.top();
        st.pop();

        while (popC != ')')
        {
            numBuf[numPos] = popC;
            numPos++;

            if (st.empty())
            {
                break;
            }

            popC = st.top();
            if (popC == '(' || popC == '&')
            {
                break;
            }
            st.pop();
        }


        int multNum = 0;
        for (int i = 0; i < numPos; i++)
        {
            multNum *= 10;
            multNum += numBuf[numPos - i - 1] - '0';
        }

        string final = "";

        for (int i = 0; i < multNum; i++)
        {
            angel += str;
        }

        st.push(ALIAS);
    }
    else
    {
        st.push(c);
    }
}

string solution(string compressed)
{
    const char *chars = compressed.c_str();
    int compLength = compressed.length();

    for (int i = 0; i < compLength; i++)
    {
        decomp(compressed[i]);
    }

    vector<char> finalChars;
    while (!st.empty())
    {
        // cout << "top() : " << st.top() << endl;

        finalChars.insert(finalChars.begin(), st.top());
        st.pop();
    }

    string finalStr = "";

    for (int i = 0; i < finalChars.size(); i++)
    {
        char c = finalChars[finalChars.size() - i - 1];

        if (c == '&')
        {
            finalStr += angel;
        }
        else
        {
            finalStr += c;
        }
    }

    return finalStr;
}

int main()
{
    string compressed = "2(2(hi)2(co))x2(bo)";
    string ans = solution(compressed);

    cout << "ans : " << ans << endl;
}