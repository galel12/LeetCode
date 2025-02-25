public class Median_of_Two_Sorted_Arrays_4 {
    class Solution {
        public double findMedianSortedArrays(int[] nums1, int[] nums2) {
            double ans = (nums1.length > nums2.length) ? Median(nums2, nums1) : Median(nums1, nums2);
            return ans;
        }

        private double Median(int[] A, int[] B) {
            int low = 0, high = A.length;
            /*
             * there has to be a median so we're looping until we found it.
             * in the first loop A_index is the median of array A.
             */
            while (low <= high) {
                int A_index = (low + high) / 2;
                int B_index = (A.length + B.length + 1) / 2 - A_index; // the rest of integers in the partition
                /*
                 * each iteration update the following values until we find the right partition
                 * for the sorted merged array.
                 * A_left and B_left represents the Left partition of the merged array, i.e. all
                 * the integers to their left (including themselves) are in the lower bound of
                 * the merged array
                 * A_right and B_right represents the Right partition of the merged array, i.e.
                 * all the integers to their right (including themselves) are in the upper bound
                 * of the merged array
                 */
                int A_left = (A_index > 0) ? A[A_index - 1] : Integer.MIN_VALUE;
                int A_right = (A_index < A.length) ? A[A_index] : Integer.MAX_VALUE;
                int B_left = (B_index > 0) ? B[B_index - 1] : Integer.MIN_VALUE;
                int B_right = (B_index < B.length) ? B[B_index] : Integer.MAX_VALUE;
                /*
                 * if this condition is satisfied then we found the right indexes for this
                 * partition
                 * the maximum between: A_left, B_left is the right median
                 * the minimum between: A_right, B_right is the left median
                 */
                if (A_left <= B_right && B_left <= A_right) {
                    if ((A.length + B.length) % 2 == 1) // if the merged array has odd number of integers then the
                                                        // median is the maximum between the left partitions
                        return Math.max(A_left, B_left);
                    else // if the merged array has even number of integers then the median is the
                         // average between the maximum of the left partitions and the minimum of the
                         // right partitions
                        return ((Math.max(A_left, B_left) + Math.min(A_right, B_right)) / 2.0);
                }
                /*
                 * if(A_left > B_right) then we need to take more integers from array B and less
                 * from array A
                 * if(B_left > A_right) then we need to take more integers from array A and less
                 * from array B
                 * this is the binary search step
                 */
                else if (A_left > B_right)
                    high = A_index - 1;

                else // B_left > A_right
                    low = A_index + 1;
            }
            return -1;
        }
    }
}