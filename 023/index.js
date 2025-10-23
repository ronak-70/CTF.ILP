const { lazy } = require("react");

function sagbegrüsen(name) {
  console.log("willkommen " + name);
}
//const name =
sagbegrüsen("rounak");
//console.log(name);

//Dynamisches Bestandsmanagement für ein Lagerhaus

let Lagerhaus = [
  { id: 101, name: "Huse", preis: 20, menge: 100, quantity: 8 },
  { id: 102, name: "Tishert", preis: 10, menge: 300, quantity: 6 },
  { id: 103, name: "Mütze", preis: 65, menge: 545, quantity: 10 },
];
//item.quantity < 10
const result = Lagerhaus.filter((item) => item.quantity < 10);

console.log("Gefilterte Produkte:", result);

//forEach
const copyLagerhaus = [];

Lagerhaus.forEach((item) => {
  copyLagerhaus.push(item);
});
console.log(copyLagerhaus);

//map()
const mappedLagerhaus = Lagerhaus.map((item) => {
  return { name: item.name, totalvalue: item.preis * item.menge };
});
console.log(mappedLagerhaus);

//finden anhand der id
//const findenitem = Lagerhaus["id" == 102];
const findenitem = Lagerhaus.find((item) => item.id === 102);
console.log(findenitem);

//neuer Item hinzufügen
Lagerhaus.unshift({
  id: 100,
  name: "pulle",
  preis: 34,
  menge: 102,
  quantity: 5,
});
console.log("Aktualisierter Lagerhaus: ", Lagerhaus);
