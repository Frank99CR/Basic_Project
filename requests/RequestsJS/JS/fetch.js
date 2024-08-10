// Ejercicio 1

// Ejercicio 2 (POST Method Implementation)

const data = {
  name: "Jennifer",
  data: {
    userEmail: "weaverJennifer@ymail.com",
    userPassword: "%WeaJen?$",
    userAdress: "New York",
  },
};

async function createUser(data) {
  try {
    const response = await fetch(`https://api.restful-api.dev/objects`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    const result = await response.json();
    console.log("Success:", result);
    const idUser = result.id;
    console.log(idUser);
    return idUser;
  } catch (error) {
    console.log("Error:", error);
  }
}

//createUser(data);

//Ejercicio 3

const userId = "ff80818190db30490190dd75d12701e0";
const userEmail = "weaverJennifer@ymail.com";

async function requestUser(userId) {
  try {
    const response = await fetch(
      `https://api.restful-api.dev/objects/${userId}`
    );
    if (!response.ok) {
      throw new Error(`Error during request: ${response.status}`);
    }
    const data = await response.json();
    console.log("Success:", data);
  } catch (error) {
    console.log("Error: ", error);
  }
}

//requestUser(userId);

//Ejericio 4

const updatedData = {
  name: "Jennifer Weaver",
  data: {
    userEmail: "weaverJennifer@ymail.com",
    userPassword: "%WeaJen?$",
    userAdress: "New York US",
  },
};

const updatedId = "ff808181905dc8b9019064bec5c00db9";

async function updateUser(userId, updatedData) {
  try {
    const response = await fetch(
      `https://api.restful-api.dev/objects/${userId}`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(updatedData),
      }
    );
    const result = await response.json();
    console.log("Success:", result);
  } catch (error) {
    console.log("Error:", error);
  }
}

//updateUser(updatedId, updatedData);
