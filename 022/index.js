//Eine Funktionsdeklaration steht vor der Funktionsdefinition und gibt den Namen, den Rückgabetyp, die Speicherklasse und andere Attribute einer Funktion an
function Rounak(string) {
  const name = "ahmad ";
  const name2 = "nima";
  const ergebnis = "hallo " + name + name2;
  return ergebnis;
}
const ergebnis = Rounak();
console.log(ergebnis);

console.log(mapped);
function mapArray(arr, callback) {
  const test = []

  for (let i = 0, i < arr.length, i++){
  test.push(callback(arr[i], i))

  }
  return test
}
//map()
//const array = [1, 4, 9, 16];
//const mapped = array.map((x) => x * 2);
//console.log(mapped);
// Expected output: Array [2, 8, 18, 32]
