// Write `makeCounter(start=0, step=1)` that returns an object with three methods: `increment()`, `decrement()`, and `reset()`. The counter's value is never directly accessible — only through the methods. Create two counters with different settings, show they don't interfere with each other.

function makeCounter(start = 0, step = 1){
    let counter = start;
    return {
        increment(){
            counter = counter + step;
            return counter
        },
        
        decrement(){
            counter = counter - step;
            return counter;
        },

        reset(){
            counter = start;
            return counter;
        }
    }
}

const counter = makeCounter(5, 10);
const counter1 = makeCounter(1,3);
console.log(counter.increment())
console.log(counter.decrement());
console.log(counter.reset())

console.log(counter1.increment())
console.log(counter1.decrement());
console.log(counter1.reset())