// Ejericio #1

let lista = ["BMW", "Tesla", "Mazda", "Toyota", "Ferrari"];

// lista.forEach((list) => {
//   // forEach
//   console.log(list);
// });

function printList(list) {
  // Function
  console.log(list);
}

//PrintList(lista);

// Ejercicio #2

// Opcion 1
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

function evenNumbers(list) {
  var EvenList = [];

  list.forEach((element) => {
    if (element % 2 === 0) {
      EvenList.push(element);
    }
  });
  return console.log(EvenList);
}

// Option 2

let evenNumber = numbers.filter((number) => number % 2 === 0); // Filter
//console.log(even_number);

//EvenNumbers(numbers);

// Ejercicio 3

let temperaturasCelsius = [20, 25, 15, 30, 10, 22, 18, 27, 12, 23];

let temperaturasFahrenheit = temperaturasCelsius.map((element) => { // Funcion anonima =>
  // Funtion Map
  return (element * 9) / 5 + 32;
});

//console.log (temperaturasFahrenheit)

// Ejercicio 4

// for (var number = 0; number <= 10; number++){
//   console.log("This is number: " + number)
// };

function numberChars(str) {
  let lista = [];
  let index = 0;

  for (var i = 0; i < str.length; i++) {
    if (str[i] === " ") {
      lista.push(str.slice(index, i));
      index = i + 1;
    }
  }
  lista.push(str.slice(index));

  return console.log(lista);
}

let palabra = "This is a string";

//numberOfChars(palabra);

// Ejercicio 5

// Entrada

const student = {
  name: "John Doe",
  grades: [
    { name: "math", grade: 80 },
    { name: "science", grade: 100 },
    { name: "history", grade: 60 },
    { name: "PE", grade: 90 },
    { name: "music", grade: 98 },
  ],
};

//let keys = Object.values(student);

//console.log(keys);

function studentData(student) {
  let note = 0;
  let averageNote = 0;
  let highestGrade = 0;
  let lowestGrade = 0;

  for (var i = 0; i < student.grades.length; i++) {
    note = note + student.grades[i].grade;
  }
  averageNote = note / student.grades.length;

  let studentGrades = student.grades.map((grade) => grade.grade);
  highestGrade = Math.max(...studentGrades);
  lowestGrade = Math.min(...studentGrades);

  console.log(highestGrade);
  console.log(lowestGrade);
}

//studentData(student);

