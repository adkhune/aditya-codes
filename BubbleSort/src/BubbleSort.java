
public class BubbleSort {
	
	public static void main(String[] args)
	{
		int n,tmp;
		System.out.println("Bubble Sort!!");
		
		int[] numbers = {5,9,1,2,3,4};// use this to sort in main
		int[] numbers1 = {5,9,1,2,3,4};// give it to method bubbleSort
		
		bubbleSort(numbers1);// return sorted array
		System.out.println(numbers1[2]);
		/* use for loop and sort an array in the main*/
		for(int i =0;i<numbers.length - 2;i++)
		{
			for(int j=0;j<numbers.length - 1;j++)
			{
				if(numbers[j]>numbers[j+1])
				{
					tmp = numbers[j];
					numbers[j] = numbers[j+1];
					numbers[j+1] = tmp;
				}
			}
		
		
		}
		
		System.out.println(numbers[2]);
		
	}
	/* use a bubbleSort method and sort an array*/
	public static int[] bubbleSort(int [] a){
		int len = a.length;
		int tmp1;
		//int[] arr = new int[len];
		
		for(int i =0;i<len - 2;i++)
		{
			for(int j=0;j<len - 1;j++)
			{
				if(a[j]>a[j+1])
				{
					tmp1 = a[j];
					a[j] = a[j+1];
					a[j+1] = tmp1;
				}
			}
		
		
		}
		return a;
	}

}
