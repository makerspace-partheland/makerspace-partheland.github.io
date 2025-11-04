---
layout: page
title: Praxisbeispiele - Heimautomatisierung
permalink: /projekte/smart-city/praxisbeispiele/
excerpt: Praxisnahe Beispiele für die Nutzung von Umweltdaten in der Heimautomatisierung mit echten Standorten aus dem Partheland
category: Smart City & IoT
---

# Praxisbeispiele - Heimautomatisierung

Unsere Sensorstationen im gesamten Partheland liefern Echtzeitwerte zu Temperatur, Luftfeuchtigkeit, Luftdruck, Feinstaub, Licht, UV-Strahlung und weiteren Umweltparametern.

Über MQTT oder Home Assistant können diese Werte für Automationen im Alltag genutzt werden.

Nachfolgend einige praxisnahe Beispiele, jeweils mit einem realen Ort aus dem Partheland als Referenz.

---

## Wäsche-Trocknung, Beispiel Großpösna

Bei niedriger Luftfeuchtigkeit und ohne Regen erfolgt eine Benachrichtigung, dass sich das Trocknen der Wäsche im Freien lohnt.

Das funktioniert auch im Winter, solange die Luft trocken genug ist, da feuchte Luft langsamer Wasser aufnimmt.

**Funktionsweise:**

Wenn die relative Außenluftfeuchte unter etwa 70 % liegt und kein Regen erkannt wird, erfolgt die Meldung "Wäsche kann draußen getrocknet werden".

**Benötigt:**

- Median Großpösna: Temperatur, Luftfeuchtigkeit
- Regensensor Großpösna (sobald verfügbar)

---

## Kellerentlüftung, Beispiel Belgershain

Wenn die Außenluft trockener ist als im Keller, wird empfohlen, das Kellerfenster kurzzeitig zu öffnen.

Das senkt die Feuchtigkeit und beugt Schimmelbildung vor.

**Hinweis:**

Ein zusätzlicher Feuchtesensor im Keller ist erforderlich.

**Benötigt:**

- Median Belgershain: Luftfeuchtigkeit
- Innensensor im Keller: Luftfeuchtigkeit

---

## Fenster-Lüftungsempfehlung, Beispiel Wolfshain

Wird die Außenluft deutlich kühler und trockener als die Innenluft, erfolgt eine Empfehlung zur manuellen Lüftung.

So lässt sich das Raumklima verbessern, ohne Energie zu verschwenden.

**Hinweis:**

Ein Innen-Temperatur- und Feuchtesensor ist notwendig.

**Benötigt:**

- Median Wolfshain: Temperatur, Luftfeuchtigkeit
- Innensensor: Temperatur, Luftfeuchtigkeit

---

## Holzofen-Erkennung mit Windrichtung, Beispiel Beucha

Steigt der Feinstaubwert (PM2.5 / PM10) plötzlich an und kommt der Wind aus Richtung eines Nachbarn mit Holzofen, erfolgt eine Warnung, die Fenster geschlossen zu halten.

Bleibt die Luftqualität schlecht, kann automatisch ein Luftreiniger aktiviert werden.

**Hinweis:**

Ein Windmesser wird künftig an der Station ergänzt.

**Benötigt:**

- Beucha: PM2.5, PM10, Windrichtung (zukünftig)
- Innen-Feinstaubsensor: PM2.5, PM10 (zur Innenraumkontrolle)

---

## Tageslichtabhängige Innenbeleuchtung, Beispiel Klinga

Sinkt die Außenhelligkeit unter einen definierten Schwellenwert, dimmt die Innenbeleuchtung automatisch hoch.

So bleibt der Helligkeitseindruck im Raum konstant und angenehm.

**Benötigt:**

- Median Klinga: Beleuchtungsstärke

---

## Regenwarnung, Beispiel Threna

Wird Regen erkannt oder der Luftdruck fällt stark, erfolgt eine Benachrichtigung zum Schließen offener Fenster oder Hereinholen von Wäsche und Geräten.

Besonders praktisch bei wechselhaftem Wetter.

**Benötigt:**

- Threna: Regen (sobald verfügbar)
- Median Threna: Luftdruck, Luftfeuchtigkeit

---

## Wettertendenz-Vorbereitung, Beispiel Brandis

Ein starker Abfall des Luftdrucks kündigt häufig Wind oder Regen an.

Das System kann eine Vorwarnung ausgeben ("Wetterumschwung steht bevor") oder bei starkem Druckabfall optional einen Hinweis für wetterfühlige Personen anzeigen.

**Benötigt:**

- Median Brandis: Luftdruck

---

## Badeempfehlung, Beispiel Kirchbruch Beucha

Erreicht die Wassertemperatur eines Gewässers mindestens 22 °C und gleichzeitig die Lufttemperatur über 25 °C, erfolgt eine Benachrichtigung "Optimales Badewetter".

Im Winter kann bei Temperaturen unter 5 °C eine "Eisbade-Info" ausgegeben werden.

**Benötigt:**

- Kirchbruch Beucha: Wassertemperatur
- Median Beucha: Lufttemperatur

---

## Praxisbeispiel aus Zweenfurth: Frostschutz fürs Gartenhaus

Ein Bürger aus Zweenfurth nutzt die lokalen Sensordaten, um sein Gartenhaus im Winter automatisch frostfrei zu halten.

Ziel ist, Pflanzen und Geräte bei stabilen Temperaturen zwischen 8 und 10 °C sicher zu überwintern, ohne manuelles Eingreifen.

**Funktionsweise:**

Die Außentemperatur der SenseBox wird mit der Innentemperatur und einem Tür-/Fensterkontakt kombiniert.

Sinkt die Außentemperatur unter 5 °C und ist das Gartenhaus geschlossen, aktiviert sich automatisch eine Infrarot-Heizung.

Steigt die Innentemperatur über 10 °C, schaltet sie sich wieder ab.

**Benötigt:**

- Zweenfurth: Außentemperatur
- Innensensor: Temperatur im Gartenhaus
- Tür-/Fensterkontakt: Status geschlossen/offen
- Steckdose oder Schaltaktor: Ansteuerung der Infrarot-Heizung

Dieses Beispiel zeigt, wie sich regionale Umweltdaten aus dem Partheland mit einfachen Smart-Home-Komponenten zu einer praxisnahen und energiesparenden Lösung kombinieren lassen.

Weitere Informationen zum Zugriff auf die Sensordaten und weitere Nutzungsmöglichkeiten findest Du auf unserer Seite [Sensordaten nutzen](/projekte/smart-city/daten-nutzen/). Fragen, Ideen oder Erfahrungsaustausch? Kontaktiere uns über unsere [Kontaktseite](/austausch/).

