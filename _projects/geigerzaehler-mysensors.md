---
layout: page
title: Geigerzähler mit SBM-20-Zählrohr
permalink: /projekte/elektronik-sensoren/geigerzaehler-mysensors/
date: 2019-11-26
excerpt: Aufbau eines Geigerzählers mit SBM-20-Zählrohr, KiCAD-Dateien und Bauteilliste.
category: Elektronik & Sensoren
---

<picture>
  <source type="image/webp" srcset="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_fertig.webp' | relative_url }}">
  <img src="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_fertig.jpg' | relative_url }}" alt="Bestückte Geigerzähler-Platine mit eingesetztem SBM-20-Zählrohr" class="title-image">
</picture>

## Geigerzähler mit SBM-20-Zählrohr

Dieser Geigerzähler verwendet ein SBM-20-Zählrohr zur Erfassung von Beta- und Gamma-Strahlung. Die Schaltung basiert auf den [Arbeiten von Jeff Keyzer (MightyOhm)](https://mightyohm.com/blog/products/geiger-counter/). Für das Projekt wurden Schaltung und Platine in KiCAD umgesetzt.

Das Zählrohr wird mit 400 V betrieben. Die Schaltung besteht aus einer Hochspannungserzeugung mit einem 555-basierten Flyback-Treiber und einem Impulsformer. Dieser gibt die Zählimpulse mit 5-V-TTL-Pegel aus. Der Ausgang lässt sich mit einem dafür geeigneten digitalen Eingang eines Arduino verbinden.

Grundlagen zu Geiger-Müller-Zählrohren beschreibt die [japanischsprachige Seite von Einstlab](http://einstlab.web.fc2.com/geiger/geiger.html).

<div class="columns is-centered">
  <div class="column is-three-quarters-desktop">
    <figure class="card">
      <div class="card-image">
        <a class="image" href="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Datenblatt_SBM20.jpg' | relative_url }}">
          <img src="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Datenblatt_SBM20.webp' | relative_url }}" alt="Russischsprachiges Datenblatt des SBM-20 mit Maßzeichnung und elektrischen Kenndaten." loading="lazy">
        </a>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Datenblatt des SBM-20-Zählrohrs</div>
      </figcaption>
    </figure>
  </div>
</div>

### Schaltung und Bauteile

- [KiCAD-Dateien für Schaltung und Platine (ZIP)]({{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_KiCAD.zip' | relative_url }})
- [Bauteilliste (ODS)]({{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/BOM.ods' | relative_url }})

<div class="columns is-centered">
  <div class="column is-three-quarters-desktop">
    <figure class="card">
      <div class="card-image">
        <a class="image" href="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_Anschluss.jpg' | relative_url }}">
          <img src="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_Anschluss.webp' | relative_url }}" alt="Bestückte Platine mit markierten Testpunkten TP1 und TP2 sowie den Anschlüssen GND, TTL-Ausgang und +5 V." loading="lazy">
        </a>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Pinbelegung und Lage der Testpunkte</div>
      </figcaption>
    </figure>
  </div>
</div>

<div class="notification is-danger">
  <strong>Achtung: Hochspannung.</strong> Die Schaltung arbeitet mit 400 V und kann auch deutlich höhere Spannungen erzeugen. Bei Inbetriebnahme und Betrieb ist deshalb Vorsicht erforderlich. Die angegebenen Bauteilwerte und insbesondere die Spannungsfestigkeit müssen eingehalten werden. Nur die Bauteile aus der Stückliste verwenden.
</div>

### Aufbau und Inbetriebnahme

#### Platine bestücken

Die Bauteile in dieser Reihenfolge bestücken: Widerstände, Dioden, Kondensatoren, Transistoren, IC, Trimmpoti, Spule und Steckverbinder. **Das SBM-20-Zählrohr bleibt zunächst ausgebaut.**

#### Hochspannung einstellen

Ohne eingesetztes Zählrohr die Betriebsspannung von 5 V anlegen: +5 V an Pin 1 von J3, Masse an Pin 3. Die Hochspannung wird anschließend mit dem Trimmpoti VR1 auf 400 V eingestellt.

Ein direkt an TP1 angeschlossenes Multimeter belastet die Hochspannungserzeugung und verfälscht die Messung. Beim im Projekt verwendeten UNI-T61D mit 10 MΩ Eingangswiderstand sank die Spannung dabei auf etwa 200 bis 260 V. Für die Messung wird deshalb ein Widerstand von 1 GΩ in Reihe zum Multimeter geschaltet.

Bei einem Multimeter mit 10 MΩ Eingangswiderstand entsprechen die 400 V an TP1 einer Anzeige von etwa 3,96 V. Dieser Wert gilt für den in der Abbildung gezeigten Spannungsteiler aus 1 GΩ und 10 MΩ.

<div class="columns is-centered">
  <div class="column is-three-quarters-desktop">
    <figure class="card">
      <div class="card-image">
        <a class="image" href="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Spannungsteiler_erklärt.png' | relative_url }}">
          <img src="{{ '/assets/images/projekte/elektronik-sensoren/geigerzaehler/Spannungsteiler_erklärt.webp' | relative_url }}" alt="Messschaltung mit 1-GΩ-Vorwiderstand und 10-MΩ-Multimeter zwischen TP1 und GND; 3,96 V Anzeige entsprechen 400 V an TP1." loading="lazy">
        </a>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Messung der Hochspannung mit Vorwiderstand und Multimeter</div>
      </figcaption>
    </figure>
  </div>
</div>

Beim Hochspannungsabgleich kann der Makerspace unterstützen.

#### Zählrohr einsetzen und Impulse prüfen

Nach dem Abgleich auf 400 V die Schaltung von der Versorgungsspannung trennen. Erst danach das SBM-20 einsetzen und dabei die Polung beachten. Die Anode ist meist mit „+“ markiert.

Nach dem Wiederanschließen der Versorgungsspannung lässt sich mit einem Oszilloskop an TP2 prüfen, ob Zählimpulse ausgegeben werden. Bei normaler Umgebungsstrahlung können zwischen den Impulsen längere Abstände liegen.

Der ursprüngliche Bericht nennt eine Uhr mit Leuchtziffern als mögliche Testquelle. Das gilt nur bei radioaktiver Leuchtfarbe; grün leuchtende Ziffern allein sind dafür kein Beleg. Jeff Keyzer erläutert diesen Unterschied bei [historischen Uhren und Instrumentenskalen](https://mightyohm.com/blog/2012/02/feed-your-geiger-readily-available-radioactive-test-sources/).
