import static org.junit.Assert.*;

import org.junit.Test;

public class AddSeqTest {

	@Test
	public void test1() {
		AddSeq a = new AddSeq();
		assertEquals("addition of seq of numbers", 55, a.getAdditionTill(10));
	}

}
