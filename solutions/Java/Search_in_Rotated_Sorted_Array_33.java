public class Search_in_Rotated_Sorted_Array_33 {

    class Solution {
        public int search(int[] nums, int target) {
            int n = nums.length;
            
            // pivot - index of the largest element
            int pivot = findMax(nums, 0, n - 1);
            
            int low = 0;
            int high = nums.length - 1;
    
            if (target <= nums[pivot] && target >= nums[low])
                high = pivot;
            else
                low = pivot + 1;
            
            while(low <= high)
            {
                int mid = (low + high) / 2;
                if(nums[mid] == target)
                    return mid;
                else if (nums[mid] < target)
                    low = mid + 1;
                else 
                    high = mid - 1;
            }
            return -1;
        }
        
        //finds maximum index in sort and rotated array in O(lg(n)) using binary search
        public static int findMax(int[] arr, int low, int high) {
            
            if(arr[low] < arr[high])
                return high;
            
            int ans = 0;
            
            while(low <= high)
            {
                int mid = low + (high - low) / 2;
                
                if(arr[mid] >= arr[0])
                {
                    ans = mid;
                    low = mid + 1;
                }
                else 
                {
                    high = mid - 1;
                }
            }
            return ans;
        }
    }
}
