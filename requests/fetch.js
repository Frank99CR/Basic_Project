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
  } catch (error) {
    console.log("error:", error);
  }
}

createUser(data);
