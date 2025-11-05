---
layout: page
title: Sensordaten nutzen
permalink: /projekte/smart-city/daten-nutzen/
excerpt: Zugriff auf Umweltdaten via MQTT und REST-API für Privatpersonen, Vereine, Schulen, Kommunen und Gewerbe
category: Smart City & IoT
---

# Sensordaten nutzen

Die Umweltdaten der Messstationen im gesamten Partheland stehen Dir kostenlos zur Verfügung. Ob Privatperson, Verein, Schule, Kommune oder Gewerbe, die Daten kannst Du frei nutzen.

## Inhaltsverzeichnis

- [Was messen wir?](#was-messen-wir)
- [Wie kommst Du an die Daten?](#wie-kommst-du-an-die-daten)
- [Nutze die Daten in Deinem Smart Home](#nutze-die-daten-in-deinem-smart-home)
- [Sensordaten im Unterricht](#sensordaten-im-unterricht)
- [Fragen? Kontaktiere uns!](#fragen-kontaktiere-uns)

---

## Was messen wir?

Überall im Partheland stehen Messstationen. Die meisten davon sind sogenannte "senseBox:home" Stationen, das sind kompakte Umweltsensoren, die verschiedene Werte erfassen:

- **Temperatur und Luftfeuchte**: wie warm und feucht ist es gerade?
- **Luftdruck**: ein Indikator für Wetteränderungen
- **Helligkeit**: wie hell ist es draußen?
- **UV-Intensität**: wie stark ist die Sonneneinstrahlung?
- **Feinstaub** (PM10 und PM2.5): winzige Partikel in der Luft, die Deine Gesundheit beeinflussen können
- **Lautstärke**: wie laut ist es in der Umgebung?

**Was bedeutet "Median"?** Die Stationen senden nicht jeden einzelnen Messwert. Stattdessen berechnen sie einen Mittelwert über ein bestimmtes Zeitintervall, den sogenannten Median. Das filtert Ausreißer heraus und liefert verlässlichere Daten. Manche Stationen senden zusätzlich die höchsten gemessenen Werte (Maximalwerte). So erkennst Du zum Beispiel kurze Lärm- oder Feinstaubspitzen.

Neben den senseBox:home Stationen gibt es auch spezialisierte Sensoren: **Pegelsensoren** messen Wasserstände in Bächen und Flüssen. **Wassertemperatursensoren** erfassen die Temperatur in Gewässern und manchmal auch die Lufttemperatur drumherum.

---

## Wie kommst Du an die Daten?

Du möchtest wissen, wo die Stationen stehen und welche Werte sie aktuell messen? Oder brauchst Du die Daten für Dein Smart Home oder eine Datenanalyse? Je nachdem, was Du vorhast, gibt es verschiedene Wege, von einfachen Karten bis hin zu technischen Schnittstellen.

### Auf einen Blick: Karten und Visualisierungen

Am einfachsten verschaffst Du Dir einen Überblick über unsere interaktive Karte. Die Anzahl und Standorte der Stationen ändern sich laufend, deshalb listen wir sie hier nicht einzeln auf, die Karten zeigen Dir immer die aktuellen Daten.

**Unsere eigene Karte** unter [map.makerspace-partheland.de](https://map.makerspace-partheland.de) ist für alle Geräte mit Browser gedacht, ob Smartphone, Tablet oder Computer. Hier siehst Du nicht nur alle Stationen und ihre aktuellen Sensorwerte, sondern auch die LoRaWAN-Gateways. Diese Gateways sind die "Empfangsstationen", die die Daten von den Sensoren empfangen und weiterleiten, ähnlich wie ein Router bei Deinem WLAN zu Hause.

Für detailliertere Auswertungen und längerfristige Datenverläufe gibt es unsere [Sensoren-Seite](https://sensoren.makerspace-partheland.de/). Hier kannst Du zum Beispiel sehen, wie sich die Temperatur oder der Feinstaubwert über Wochen oder Monate entwickelt hat.

**Mobil unterwegs?** Die Partheland App (für [Android und iOS](https://partheland.de/2022/11/jetzt-gehts-app-im-partheland/)) zeigt die Sensordaten unter dem Menüpunkt "Umweltdaten" als Karte an. Die App wurde von den Partheland-Kommunen entwickelt und bildet eine zentrale Plattform für Verwaltungsangebote sowie Dienstleistungen der Region. So hast Du neben den Umweltdaten auch Zugriff auf aktuelle Informationen und Services der sieben Partheland-Kommunen, alles in einer App.

Alle Stationen, die Teil des größeren openSenseMap-Netzwerks sind, findest Du zusätzlich auf [openSenseMap](https://opensensemap.org).

### Technische Zugriffsmöglichkeiten

Brauchst Du die Daten für Dein Smart Home oder möchtest Du eigene Programme damit entwickeln? Dann gibt es verschiedene technische Schnittstellen.

### Echtzeitdaten über MQTT WebSocket

**Was ist MQTT?** Das ist ein Übertragungsprotokoll, eine Art digitale Sprache, mit der Geräte Daten austauschen. Es ist besonders energieeffizient und wird häufig im Internet der Dinge (IoT) eingesetzt. Du kannst Dir das wie einen Radio-Sender vorstellen: Die Messstation "sendet" ihre Daten, und Dein Gerät "hört mit", indem es sich auf den richtigen Kanal (Topic) einstellt.

Die Verbindung läuft über `wss://mqtt.makerspace-partheland.de:443/mqtt`.

**Topics – die Kanäle für Deine Daten:**
- `senseBox:home/[Stationsname]`: Daten einer bestimmten senseBox:home Station
- `sensoren/[Sensorname]`: Daten spezialisierter Sensoren (z.B. Wasserstand)
- `senseBox:home/median`: Medianwerte für einzelne Orte oder das gesamte Partheland

**Wie genau funktioniert das?** Alle technischen Details, JSON-Formate und die komplette Topic-Struktur findest Du unter [api-docs.makerspace-partheland.de](http://api-docs.makerspace-partheland.de).

### Historische Daten über die REST-API

**Was ist eine REST-API?** Stell Dir das wie eine Bibliothek vor: Du stellst eine Anfrage (z.B. "Gib mir die Temperaturdaten vom letzten Monat"), und die API liefert Dir die Daten zurück. Das funktioniert über normale Webadressen, perfekt für Webseiten, Apps oder Datenanalysen.

Die Basis-URL lautet: `https://data.makerspace-partheland.de/`

Hier bekommst Du:
- Aktuelle Messdaten aller Stationen
- Historische Daten für längere Zeiträume
- Detaillierte Informationen zu einzelnen Stationen

**Hinweis:** Die REST-API befindet sich noch im Ausbau. Die vollständige Dokumentation mit allen Endpunkten und Beispielen findest Du unter [api-docs.makerspace-partheland.de](http://api-docs.makerspace-partheland.de).

---

## Nutze die Daten in Deinem Smart Home

Du hast ein Smart Home? Dann kannst Du die Sensordaten aus Deiner Region direkt einbinden. Warum solltest Du das tun? Weil die Daten aus Deiner unmittelbaren Umgebung stammen, nicht von einer Wetterstation 20 Kilometer entfernt.

### Home Assistant

Wir haben eine fertige Integration für Home Assistant entwickelt. Du findest sie in unserem [GitHub Repository](https://github.com/makerspace-partheland/smartcity-sensorbridge-partheland).

**Was bringt Dir das?** Nach der Installation siehst Du lokale Umweltdaten direkt in Deinem Smart Home Dashboard. Die Integration legt für jede Messstation ein eigenes Gerät an, unter dem alle verfügbaren Sensoren aufgelistet werden. Die Daten aktualisieren sich in Echtzeit.

### ioBroker

ioBroker unterstützt MQTT WebSocket von Haus aus, Du brauchst keine zusätzliche Bridge oder Erweiterung.

**So richtest Du es ein:**
1. Öffne den MQTT-Adapter in ioBroker
2. Trage als URL ein: `wss://mqtt.makerspace-partheland.de:443/mqtt`
3. Aktiviere "WebSocket" und "SSL"
4. Port: `443`
5. Path: `/mqtt`

**Welche Daten willst Du empfangen?**
- `senseBox:home/+`: alle senseBox:home Stationen
- `senseBox:home/median`: Medianwerte
- `sensoren/+`: spezialisierte Sensoren (Wasserstand etc.)

ioBroker wandelt die Daten automatisch in Objekte um. Mit JavaScript-Scripts kannst Du die Daten noch weiter verarbeiten, zum Beispiel Durchschnittswerte berechnen oder Benachrichtigungen verschicken.

### Praxisbeispiele aus dem Partheland

Du willst konkrete Anwendungsfälle sehen? Auf unserer Seite [Praxisbeispiele](/projekte/smart-city/praxisbeispiele/) zeigen wir Dir, wie die Sensordaten in echten Szenarien genutzt werden. Dort findest Du auch Standorte und detaillierte Beschreibungen.

---

## Sensordaten im Unterricht

Die Sensordaten eignen sich hervorragend für den Unterricht, und zwar in verschiedenen Fächern. Es gibt zwei grundsätzliche Ansätze:

### Vorhandene Daten analysieren

Mehrere Jahre historische Daten stehen Dir zur Verfügung. Hier geht es nicht ums Messen selbst, sondern um den Umgang mit echten Daten. Was lässt sich aus den Daten ablesen? Wie vergleicht man verschiedene Standorte? Wie hängen Temperatur und Feinstaub zusammen?

**Konkrete Idee:** Schüler vergleichen ihre eigenen Beobachtungen (z.B. "Es war heute sehr heiß") mit den tatsächlichen Messwerten aus dem eigenen Ort. So entsteht ein direkter Bezug zwischen subjektiver Wahrnehmung und objektiven Daten.

### Selbst messen

Alternativ können Schüler auch einen eigenen Sensor aufbauen und ihre Messdaten mit denen des Netzwerks vergleichen. Das fördert das Verständnis für Sensortechnik und zeigt, wie unterschiedlich Messwerte je nach Standort und Bedingungen ausfallen können.

### Fachübergreifende Projektideen

- **Physik:** Wie funktioniert ein Feinstaubsensor? Was ist ein Median? Wie genau sind die Messungen?
- **Informatik:** Datenvisualisierung erstellen, API-Aufrufe programmieren, eigene Dashboards bauen
- **Biologie:** Wie beeinflussen Umweltfaktoren Pflanzen und Tiere? Was sagen die Gewässertemperaturen über die Ökologie aus?
- **Mathematik:** Statistik anwenden, Langzeitanalysen durchführen, Korrelationen finden

---

<div class="columns is-multiline is-centered" style="margin-top: 2rem;">
  <div class="column is-4-desktop is-6-tablet is-12-mobile">
    <div class="card modern-card standard-card full-height">
      <div class="card-content callout-card-content">
        <div class="callout-card-body">
          <h2 class="title is-3 has-text-weight-bold has-text-centered callout-title">
            LoRaWAN Netzwerk
          </h2>
          <h3 class="subtitle is-5 has-text-weight-medium has-text-centered callout-subtitle">
            Energieeffiziente Vernetzung
          </h3>
          <div class="content has-text-centered callout-content">
            <p>Erfahre mehr über das Netzwerk, Batterie- und Solarbetrieb sowie die Vorteile gegenüber WiFi, LTE und 5G.</p>
          </div>
        </div>
        <div class="has-text-centered callout-actions">
          <a href="/projekte/smart-city/lorawan/" class="button is-primary is-medium is-rounded has-text-weight-semibold" aria-label="Erkunden - LoRaWAN Netzwerk">
            Erkunden
          </a>
        </div>
      </div>
    </div>
  </div>
  
  <div class="column is-4-desktop is-6-tablet is-12-mobile">
    <div class="card modern-card standard-card full-height">
      <div class="card-content callout-card-content">
        <div class="callout-card-body">
          <h2 class="title is-3 has-text-weight-bold has-text-centered callout-title">
            Praxisbeispiele
          </h2>
          <h3 class="subtitle is-5 has-text-weight-medium has-text-centered callout-subtitle">
            Anwendungsbeispiele
          </h3>
          <div class="content has-text-centered callout-content">
            <p>Detaillierte Anwendungsbeispiele mit echten Standorten aus dem Partheland.</p>
          </div>
        </div>
        <div class="has-text-centered callout-actions">
          <a href="/projekte/smart-city/praxisbeispiele/" class="button is-success is-medium is-rounded has-text-weight-semibold" aria-label="Erkunden - Praxisbeispiele">
            Erkunden
          </a>
        </div>
      </div>
    </div>
  </div>
  
  <div class="column is-4-desktop is-6-tablet is-12-mobile">
    <div class="card modern-card standard-card full-height">
      <div class="card-content callout-card-content">
        <div class="callout-card-body">
          <h2 class="title is-3 has-text-weight-bold has-text-centered callout-title">
            Interesse geweckt?
          </h2>
          <h3 class="subtitle is-5 has-text-weight-medium has-text-centered callout-subtitle">
            Kontakt & Austausch
          </h3>
          <div class="content has-text-centered callout-content">
            <p>Kontaktiere uns über unsere Telegram-Kanäle oder per E-Mail für Fragen, Ideen und Erfahrungsaustausch.</p>
          </div>
        </div>
        <div class="has-text-centered callout-actions">
          <a href="/austausch/" class="button is-primary is-medium is-rounded has-text-weight-semibold" aria-label="Entdecken - Kontakt & Austausch">
            Entdecken
          </a>
        </div>
      </div>
    </div>
  </div>
</div>
