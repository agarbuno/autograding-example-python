import hello;

def test_hello():
    assert hello.hello_world("World") == "Hello World!"

def test_print():   
    assert hello.hello_world("Alfredo") == "Hello Alfredo!"
