def test_function():
    a = 5
    print(a)
    
    def inner_function():
        print('Я в области видимости - test_function')
    inner_function()
        
        
test_function()
inner_function()