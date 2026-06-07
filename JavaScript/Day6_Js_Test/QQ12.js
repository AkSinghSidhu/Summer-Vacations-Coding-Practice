// Write `memoize(fn)` that wraps any function and caches results by argument. If the same argument is passed again, return cached — don't run the function again. Simulate a slow function with a loop. Show the cache working by calling it 3 times with the same input and 3 times with different inputs.

function slowFunction(n) {
    let result = 0;
    for(let i = 0; i < 100000000; i++) {
        result += i;
    }
    return result + n;
}

function memoize(fn){
    let cache = {};
    return function(n){
        if (n in cache){
            console.log("from cache");
            return cache[n];
        } else {
            let result = fn(n);
            cache[n] = result;
            return result;
    }
    }
}


const memoizedSlow = memoize(slowFunction);
console.log(memoizedSlow(0))
console.log(memoizedSlow(4))
console.log(memoizedSlow(0))
console.log(memoizedSlow(7))
console.log(memoizedSlow(0))
console.log(memoizedSlow(9))