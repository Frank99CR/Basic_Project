// Ejercicio 1

function isEven() {
  console.log("This number is Even");
}

function isOdd() {
  console.log("This number is Odd");
}

function callbackTest(number, isEven, isOdd) {
  console.log("Callback executed");
  if (number % 2 === 0) {
    isEven();
  } else {
    isOdd();
  }
}

//callbackTest(4, isEven, isOdd);
//callbackTest(5, isEven, isOdd);


// Ejercicio 3 (check HTML folder)
