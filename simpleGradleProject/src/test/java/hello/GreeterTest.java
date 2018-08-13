package hello;
import hello.Greeter;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class GreeterTest{
    @Test
    public void shouldDisplayHelloWorld(){
        Greeter greeter = new Greeter();
        assertEquals("Hello world!", greeter.sayHello());
    }
}