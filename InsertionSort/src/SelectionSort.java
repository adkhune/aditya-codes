
public class SelectionSort {
	
	public static void main(String [] args)
	{
		System.out.println("Lets go for Selection sort now");
		int tmp;
		int minIndex = 0;// find the min number and pass its index to swap the numbers
		int [] numbers = {2,4,5,1,3,8,9,2,2,10,34};
		printArray(numbers);
		//tmp = numbers[minIndex];
		for (int i = 0; i<=numbers.length-2 ;i++)
		{
			minIndex = i;
			for(int j = i; j<=numbers.length-1;j++)
			{
				
				if(numbers[minIndex] > numbers[j])
				{
					minIndex = j;
					//System.out.println("minIndex=" + minIndex);
				}
			}
				
			tmp = numbers[minIndex];
			numbers[minIndex] = numbers[i];
			numbers[i] = tmp;
		}
		System.out.println(" ");
		printArray(numbers);
		
	}
	
	
	
	public static void printArray(int[] a)
	{
		for(int s=0; s<a.length;s++)
			System.out.print(a[s] + " ");
	}

}
