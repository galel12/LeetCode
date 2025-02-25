public class First_Missing_Positive_41 {
    class Solution {
        public int firstMissingPositive(int[] nums) {
            int n = nums.length, curr, next;
            /* Place Numbers in Their Correct Positions: 
               Loop through the array and swap numbers to their correct position if they are in the range [1, n].
             */
            for(int i = 0; i < n; i++)
            {
                curr = nums[i];
                while((curr >= 1 && curr <= n) && curr != (next = nums[curr - 1]))
                {
                    nums[curr - 1] = curr;      // Place curr in its correct index (curr - 1)
                    curr = next;                // Move to the swapped number
                }
            }
            // After reordering, iterate the array again to check which number is out of place.
            for(int i = 0; i < n; i++)
            {
                if(nums[i] != i + 1)
                    return i + 1; // First missing positive found
            }
            return n + 1; // If all numbers are in correct positions, return n + 1
        }
    }
}
