import static org.junit.Assert.*;

import org.junit.Test;

public class TestTricycle {

	@Test
	public void test() {
		Tricycle t = new Tricycle();
		assertEquals("Check number of wheels", 3, t.getNumWheels());
	}

}
