const Beschreibung = document.getElementById("Beschreibung");
Beschreibung.textContent = "das ist meine Änderung";
//
const überschrift = document.querySelector("h1");
überschrift.innerHTML = "Meine Überschrift <strong>wurde geändert</strong>";
//
const kacheln = document.querySelectorAll(".kachel");
kacheln.forEach((kachel) => {
  kachel.style.backgroundColor = "#e015a3ff";
  kachel.classList.add("aktiviert");
});
//
const image = document.querySelector("img");
image.scr = "oving-back-silhouette-gray-cloud-on-the_2709689.mp4";
image.alt = "Bewegungshintergrund";
//
const status = document.getElementById("status-anzeige");
status.dataset.initialStatus = "bereit";
console.log(status.dataset.initialStatus);
