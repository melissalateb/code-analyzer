// Exemple de fonction pour afficher un message
function showMessage() {
    const message = "Hello, World!";
    console.log(message);
}

// Exemple utilisant camelCase et indentation
function calculateSum(a, b) {
    return a + b;
}

// Utilisation de valeurs constantes
const MAX_SIZE = 100;

// Exemple de fonction avec un _nomPrivé et getter/setter
let _privateValue = 10;

function getPrivateValue() {
    return _privateValue;
}

function setPrivateValue(value) {
    _privateValue = value;
}

// Appel de fonctions pour démonstration
showMessage();
console.log("La somme est:", calculateSum(5, 7));
console.log("Valeur privée initiale:", getPrivateValue());
setPrivateValue(20);
console.log("Nouvelle valeur privée:", getPrivateValue());