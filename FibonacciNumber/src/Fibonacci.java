
public class Fibonacci {
	public static void main(String args[])
	{
		System.out.println("Hi lets do fibonacci");
		System.out.println(getFibonacciRecursive(40));
		System.out.println(getFibonacci(40));
		
	}
	
	public static int getFibonacciRecursive(int n)
	{
		
		if (n == 0)
			return 0;
		else if (n == 1 || n == 2)
			return 1;
		return getFibonacciRecursive(n-1) + getFibonacciRecursive(n-2);
		
	}
	public static int getFibonacci(int n)
	{
		int[] a = new int[n+1];
		if (n > 2)
		{
			
			for (int f = 3; f<=n; f++)
			{
			a[0]=0;
			a[1]=1;
			a[2]=1;
			//a[3]=2;
			//a[4]=3;
			a[f]=a[f-1] + a[f-2];
			
			//for (int i = 5; i<=n; i++)
			//	a[i]=a[i-1]+a[i-2];
			}
		}else if (n == 0)
			a[n]= 0;
		else if (n == 1 || n == 2)
			a[n]= 1;
			
		
			return a[n];
	}
}
