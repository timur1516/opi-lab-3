import org.junit.jupiter.api.Test;
import ru.timur.web3.controller.AreaCheckBean;

import static org.junit.jupiter.api.Assertions.assertTrue;

public class AreaCheckTest {
    private final AreaCheckBean areaCheckBean = new AreaCheckBean();

    @Test
    public void testHitInArea() {
        assertTrue(areaCheckBean.isHit(0.1, 0.1, 1.0));
    }
}
