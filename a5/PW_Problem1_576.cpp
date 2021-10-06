#include <iostream>
#include <vector>
#include <cstring>
#include <string>
 
using namespace std;

string phno;
vector <string> replace(10);
int dp[110]={0},path[110] = {0};

void init(){
    replace[0]="oqz";  replace[1]="ij";   replace[2]="abc"; replace[3]="def";
    replace[4]="gh";   replace[5]="kl";  replace[6]="mn";   replace[7]="prs";
    replace[8]="tuv";  replace[9]="wxy";
}

bool correct(string number, string word){
    for(int i = 0 ; i < number.length(); i ++){
        int len = replace[number[i]-'0'].length(),j;
        for( j = 0; j < len; j ++ ){
            if(replace[number[i]-'0'][j] == word[i]) break;
        }
        if(j >= len) return false;
    }
    return true;
}

int main(int argc, char *argv[]){
    
    replace[0]="oqz";  replace[1]="ij";   replace[2]="abc"; replace[3]="def";
    replace[4]="gh";   replace[5]="kl";  replace[6]="mn";   replace[7]="prs";
    replace[8]="tuv";  replace[9]="wxy";
    
    while(cin >> phno && phno != "-1"){
        int n;
        cin>>n;
        vector<string> word(n);
        for(int i = 0; i < n; i ++ ) cin >>word[i];
        for(int i = 0; i < 110; i ++ ) dp[i] = 9999999;
        memset(path,-1,sizeof(path));
        dp[0] = 0;
        for(int i = 1; i <= phno.length(); i ++ ){
            for(int j = 0; j < n; j ++ ){
                if( (word[j].length() + i-1) <= phno.length() && correct( phno.substr(i-1,word[j].length()) , word[j] ) ){
                    if(dp[i + word[j].length()-1] > dp[i-1] + 1){
                        dp[i + word[j].length()-1] = dp[i-1] + 1;
                        path[i + word[j].length()-1] = j;
                    }
                }
            }

        }
        if(path[phno.length()] == -1) cout<<"No solution."<<endl;
        else{
            vector <string> ans;
            int l = phno.length();
            while(path[l] != -1){
                ans.push_back(word[path[l]]);
                l = l - word[path[l]].length();
            }
            cout<<ans[ans.size()-1];
            for(int i = ans.size()-2; i >= 0 ; i-- )
                cout<<" "<<ans[i];
            cout<<endl;
        }
    }

    return 0;
}