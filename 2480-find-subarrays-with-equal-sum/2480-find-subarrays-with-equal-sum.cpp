class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        set <int> visited;
        for(int i=0;i< nums.size()-1;i++){
                int sum = nums[i] + nums[i+1];
                if(visited.find(sum)==visited.end()){
                    visited.insert(sum);
                }
                else{
                    cout << "Repeated, returning true";
                    return true;
            }
        }
        return false;
    }
};