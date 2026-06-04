# Write `outer()` with a variable `count = 0`. Inside it, write `inner()` that increments and prints count. Call `inner()` 3 times from `outer()`. It won't work right away — figure out what keyword lets `inner` actually modify `count`.

def outer():
    count = 0
    
    def inner():
        nonlocal count
        count += 1
        print(count)
    
    inner()
    inner()
    inner()

outer()