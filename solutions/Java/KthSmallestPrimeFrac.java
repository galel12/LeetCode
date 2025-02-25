public class KthSmallestPrimeFrac {
	class Solution {
		public int[] kthSmallestPrimeFraction(int[] arr, int k) {
			int[] ans = new int[2];
			int left = 0, right = arr.length - 1, mid;

			while (left <= right) {
				mid = left + (right - left) / 2;

				for (int i = 0; i < arr.length; i++) {
					int numerator = arr[i];

				}
			}
			return ans;

		}
	}
}
