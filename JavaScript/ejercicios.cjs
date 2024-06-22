// Ejercicio 2

const fs = require("fs");

const logData = (err,data)=>{
  console.log(data)
}

const file1 = fs.readFileSync('Archivos/secretMessage1.txt', 'utf-8', logData);
const file2 = fs.readFileSync('Archivos/secretMessage2.txt', 'utf-8', logData);

const wordsFile1 = file1.split('\n');
const wordsFile2 = file2.split('\n');


const commonWords = wordsFile1.filter(word => wordsFile2.includes(word));

  // Mostrar las palabras comunes
  console.log('Palabras comunes:', commonWords);


console.log("Reading...");