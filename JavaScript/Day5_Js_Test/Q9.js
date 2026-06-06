// Create a `user` object with at least 6 properties, including an `address` object nested inside (city, country). In one destructuring line, pull out the name and the city from the nested address. Create a new object with everything from the original but a different city — without changing the original. Verify they're independent.

const user = {
    name : "Akash",
    age : 21,
    classSem : "Btech 6th",
    dept : "CSE",
    uni_name : "Akal University",
    address : {
        city : "Sirsa",
        country : "India"
    }
};

const {
    name, address : {city}
} = user;

console.log(name, city);

const newObj = {...user};
// newObj.address.city = "Delhi"; // This will actually change the original user's city value as well

const copy = structuredClone(user);

copy.address.city = "Delhi";

console.log("Original: ", user);
console.log("New Copy: ", copy);
