SELECT    kunden.vorname, kunden.nachname,
          bestellungen.bestellung_id,bestellungen.bestelldatum
FROM      kunden  LEFT JOIN bestellungen  
ON        bestellungen.kunde_id = kunden.kunde_id;

SELECT *  
FROM      produkte 
LEFT JOIN bestellpositionen 
ON        produkte.produkt_id = bestellpositionen.produkt_id 
WHERE     bestellpositionen.produkt_id IS NULL;

SELECT    k.kunde_id, k.vorname , k.nachname ,
          p.produkt_id, p.name, 
          bestellpositionen.bestellung_id, bestellpositionen.menge 
FROM      kunden k 
CROSS JOIN produkte p 
LEFT JOIN bestellpositionen 
ON        bestellpositionen.kunde_id = k.kunde_id AND bestellpositionen.produkt_id = p.produkt_id;

