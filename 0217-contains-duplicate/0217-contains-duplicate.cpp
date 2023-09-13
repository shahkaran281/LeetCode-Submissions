class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> visited;
        for(int i=0;i<nums.size();i++){
            if(visited.find(nums[i])!=visited.end()){
                return true;
            }
            else{
                visited.insert(nums[i]);
            }
        }
        return false;
    }
};