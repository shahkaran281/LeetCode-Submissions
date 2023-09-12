class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& v) {
        for(int i=0;i<9;i++){
            set<int> visited;
            for(int j=0;j<9;j++){
                if(v[i][j]!='.'){
                    int n = int(v[i][j]) - int('0');
                if(visited.find(n)!=visited.end()){
                    return false;
                }
                else{
                    if(n < 0 || n > 9){
                        return false;
                    }
                    visited.insert(n);
                }
                }
            }
        }
        for(int i=0;i<9;i++){
            set<int> visited;
            for(int j=0;j<9;j++){
                if(v[j][i]!='.'){
                    int n = int(v[j][i]) - int('0');
                if(visited.find(n)!=visited.end()){
                    return false;
                }
                else{
                    if(n < 0 || n > 9){
                        return false;
                    }
                    visited.insert(n);
                }
                }
            }
        }
        for(int i=0;i<9;i+=3){
            for(int j=0;j<9;j+=3){
                set<int> visited;
                for(int k=0;k<3;k++){
                    for(int l=0;l<3;l++){
                        if(v[i+k][j+l]!='.'){
                            int n = int(v[i+k][j+l]) - int('0');
                            if(visited.find(n)!=visited.end() || n < 0 || n > 9){
                                return false;
                            }
                            else{
                                visited.insert(n);
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
};