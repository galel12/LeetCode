
public class SumofAllSubsetXORTotals {
	
	public int subsetXORSum(int[] nums) {
		
        return subsetXORSum(nums, 0, 0);
    }
	
	public int subsetXORSum(int[] nums, int index, int XOR_Sum) {
        
		if(index == nums.length)
			return XOR_Sum;
		
		int include = subsetXORSum(nums, index + 1, XOR_Sum^nums[index]);
		int exclude = subsetXORSum(nums, index + 1, XOR_Sum);
		
		return include + exclude;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {5,1,6};
		int[] nums2 = {3,4,5,6,7,8};
		
		//create object of the class above
		SumofAllSubsetXORTotals answer = new SumofAllSubsetXORTotals();
		
		System.out.println("The sum of all XOR totals for every subset is: " + answer.subsetXORSum(nums2));
	}

}
