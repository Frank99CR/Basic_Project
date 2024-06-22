// Ejercicios de Async/Await

//Ejercicio #1

const getData = async () => {
  console.log("1. Requesting data");
  const response = await fetch(`https://reqres.in/api/users/2`);
  const data = await response.json();
  console.log("Data loaded! Returning...");
  console.log(data);
  //console.log(data.data.first_name);
};

//getData();

// Ejercicio #2

async function getData2() {
  console.log("1. Requesting data");
  try {
    const response = await fetch(`https://reqres.in/api/users/23`);
    const data = await response.json();
    console.log("Data loaded!, Returning...");
    console.log(data);

    if (Object.keys(data).length === 0) {
      throw new Error("No user found!");
    }
  } catch (error) {
    if (error.message === "No user found!") {
      console.log("No user found!");
    } else {
      console.log("Request Unsuccessful!");
    }
  }
}

//getData2();

// Ejercicio #3  (Revisar HTML)

//Ejercicios de Promises

// Ejercicio #1

const pokeId1 = 4;
const pokeId2 = 5;
const pokeId3 = 6;

async function getpokemonData(id1, id2, id3) {
  console.log("1. Enviando request");
  const [response1, response2, response3] = await Promise.all([
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokeId1}`),
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokeId2}`),
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokeId3}`),
  ]);

  console.log("2. Respuesta recibida");

  const data1 = await response1.json();
  const data2 = await response2.json();
  const data3 = await response3.json();

  console.log(`Data from API 1: ${data1.name}`);
  console.log(`Data from API 2: ${data2.name}`);
  console.log(`Data from API 3: ${data3.name}`);
}

//getpokemonData(pokeId1,pokeId2,pokeId3);

//Ejercicio 2

async function pokemonName(id1, id2, id3) {
  console.log("1. Enviando request");

  const promise1 = fetch(`https://pokeapi.co/api/v2/pokemon/${pokeId1}`);
  const promise2 = fetch(`https://pokeapi.co/api/v2/pokemon/${pokeId2}`);
  const promise3 = fetch(`https://pokeapi.co/api/v2/pokemon/${pokeId3}`);

  const arrayPromises = [promise1, promise2, promise3];

  try {
    const response = await Promise.any(arrayPromises);
    const data = await response.json();
    console.log(data.name);
  } catch (error) {
    console.log("No Pokemon found!");
  }
}

//pokemonName(pokeId1, pokeId2, pokeId3);

// Ejercicio 3

function fourPromises() {
  const p1 = new Promise((resolve) => setTimeout(resolve, 3000, "very"));
  const p2 = new Promise((resolve) => setTimeout(resolve, 1000, "dogs"));
  const p3 = new Promise((resolve) => setTimeout(resolve, 4000, "cute"));
  const p4 = new Promise((resolve) => setTimeout(resolve, 2000, "are"));

  Promise.all([p1, p2, p3, p4])
    .then((response) => console.log(response.join(" ")))
    .catch((error) => console.log(error));
}

//fourPromises();

//Ejercicio 4

const userId = 2;

console.log("1. Enviando request");
const userName = fetch(`https://reqres.in/api/users/${userId}`);

userName
  .then((response) => {
    console.log("2. Response recibido");
    const data = response.json();
    return data;
  })
  .then((data) => {
    console.log(data.data.first_name);
  })
  .catch((error) => {
    console.log(`3. Usuario no encontrado: ${error}`);
  })
  .finally(() => {
    console.log("4. Request finalizado");
  });

  console.log("Codigo finalizado!");
