console.log("Getting started with javascript");

var myNumber = 10;
console.log(myNumber);

var myArray = [8, [10, 90, 23], "peanut"];
console.log(myArray[0]);


// python : for item in array:

for (var i = 0 ; i < myArray.length ; i++ ) {
    var item = myArray[i];
    console.log(item);

}

var myObject = {
    "myName": "sam",
    myAge: 23


}

console.log(myObject["myName"]);

var myFunc = function(x, y) {
    return x * y

};

console.log(myFunc(9, 4));

var sillyArray = [4, 5, 3, 7];

var loopFunc = function(item) {
    console.log(item);
};

sillyArray.forEach(loopFunc);

sillyArray.forEach(function(item) {
    console.log(item);
});
