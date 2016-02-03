import static org.junit.Assert.*;

import org.junit.Test;

public class TestFibonacci {

	@Test
	public void test() {
		Fibonacci f = new Fibonacci();
		
		assertEquals("get n th fibonacci",1, f.getFibonacci(1));
		assertEquals("get n th fibonacci",1, f.getFibonacciRecursive(1));
	}

}
