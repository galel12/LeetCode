public class First_Missing_Positive_41 {
    
    class Solution {
        public int firstMissingPositive(int[] nums) {
            
            int n = nums.length, curr, next;
            
            for(int i = 0; i < n; i++)
            {
                curr = nums[i];
                while((curr >= 1 && curr <= n) && curr != (next = nums[curr - 1]))
                {
                    nums[curr - 1] = curr;
                    curr = next;
                }
            }
            
            for(int i = 0; i < n; i++)
            {
                if(nums[i] != i + 1)
                    return i + 1;
            }
            return n + 1;
        }
    }
}
