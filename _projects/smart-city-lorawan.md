---
layout: page
title: LoRaWAN Netzwerk
permalink: /projekte/smart-city/lorawan/
excerpt: LoRaWAN-basiertes Netzwerk für energieeffiziente Umweltsensoren im Partheland
category: Smart City & IoT
---

<picture>
  <source type="image/webp" srcset="/assets/images/projekte/smart-city/sensebox-home-solar.webp">
  <img src="/assets/images/projekte/smart-city/sensebox-home-solar.jpg" alt="senseBox:home solarbetrieben" class="title-image" style="object-position: bottom center;">
</picture>

# LoRaWAN Netzwerk

LoRaWAN übermittelt Messwerte von einer Wiese, einem Feld oder einem Kleingarten zu Dir nach Hause, ohne dass am Messstandort Internet oder Mobilfunk benötigt wird. Die Abkürzung steht für _Long Range Wide Area Network_, also ein Funknetz für große Entfernungen. Es wurde speziell entwickelt, um kleine Datenmengen extrem energiesparend über mehrere Kilometer zu übertragen.

## Batterie- und Solarbetrieb

LoRaWAN ermöglicht es, Sensoren über lange Zeiträume mit einer simplen Batterie zu versorgen. Der Energieverbrauch ist so gering, dass Sensoren mit Batterien oder kleinen Solarzellen und Akkus über Jahre hinweg autark arbeiten können. Ein Stromanschluss entfällt. Laufende Ausgaben für Mobilfunkverträge oder Internet fallen nicht an. Die Datenübertragung über das öffentliche LoRaWAN-Netzwerk ist kostenlos.

Du kannst Messstationen dort aufbauen, wo Du Daten brauchst, aber weder Strom noch Internet verfügbar sind: in Kleingärten, auf Sportplätzen, an Badeseen, auf Grünflächen, Feldern, in Wäldern oder am Ortsrand.

## Warum LoRaWAN statt WLAN, LTE oder 5G?

LoRaWAN wurde für Sensornetzwerke konzipiert. Die Reichweite beträgt im Freien mehrere Kilometer, deutlich mehr als die paar hundert Meter, die WLAN schafft.

Aber LoRaWAN hat auch klare Grenzen. Die Datenübertragung ist langsam und eignet sich nur für kleine Datenmengen: Temperatur, Luftfeuchtigkeit, Füllstände. Willst Du Kamerastreams übertragen, Sprache in Echtzeit senden oder häufige Updates? Dann brauchst Du WLAN, LTE oder 5G. Wände und Decken können das Funksignal abschwächen. Auch innerhalb von Gebäuden ist LoRaWAN nutzbar. Reicht der Empfang am vorgesehenen Standort nicht aus, kann ein Platz näher am Fenster oder eine geeignete Außenantenne helfen.

Zu diesem Zweck wurde LoRaWAN entworfen, um alle paar Minuten wenige Messwerte von einem Sensor auf dem Feld zu übertragen. Solche Übertragungen sind auch an abgelegenen Orten ohne Strom- oder Internetanschluss möglich.

## Funktionsweise

Von dem Sensor aus werden die Daten über LoRa-Gateways an Dich übermittelt. Ein solches Gateway kann man sich wie einen Briefkasten vorstellen. Liegt ein Sensor im Empfangsbereich eines Gateways, nimmt dieses die Datenpakete über eine Stabantenne auf, deren Länge zwischen 30 und 80 cm liegt. Da das Gateway eine Internetverbindung besitzt, leitet es die empfangenen Pakete weiter.

Die Datenpakete werden auf einer Frequenz zwischen 863 und 870 MHz gesendet. Diese Frequenz ist europaweit lizenzfrei nutzbar – jeder darf sie verwenden. Auch Alarmanlagen, Funktastaturen oder Garagentorfernbedienungen nutzen diesen Bereich, ohne sich gegenseitig zu stören.

**Wichtig beim Kauf:** Achte auf die Bezeichnung **868 MHz** oder **EU868** bei LoRaWAN-Geräten. Module mit **433 MHz** oder **915 MHz** (USA/Australien) funktionieren im Partheland-Netzwerk nicht.

## The Things Network (TTN)

Das Partheland-Netzwerk basiert auf dem **The Things Network (TTN)** – einer weltweiten, offenen LoRaWAN-Infrastruktur:

- **Kosteneffizienz**: TTN ist kostenlos nutzbar und nutzt das energieeffiziente LoRaWAN-Protokoll. Das ermöglicht den Betrieb von Sensoren und vernetzten Geräten mit minimalem Stromverbrauch und ohne laufende Kosten.
- **Sicherheit**: Die Daten werden mit dem Advanced Encryption Standard (AES) verschlüsselt und authentifiziert – ein sehr sicheres Verfahren.

## Betrieb und Wartung

Den Betrieb und die Wartung der LoRaWAN-Gateways in Brandis und dessen Ortsteilen übernimmt der Makerspace Partheland e.V., inklusive der Sensoren-Webseite und Infrastruktur. In allen weiteren Partheland-Kommunen kümmern sich die jeweiligen Multiplikatoren um Gateway-Betrieb und Wartung.

## Kostenfreier Zugang zum Netzwerk

<div class="notification is-success is-light">
  <div class="content">
    <p>
      Das LoRaWAN-Netzwerk im Partheland ist für Dich <strong>kostenfrei zugänglich</strong>. Du kannst eigenständig Sensoren betreiben und das Netzwerk nutzen.
    </p>
  </div>
</div>

**Netzabdeckung prüfen:**

Ist Dein Standort bereits abgedeckt? Prüfe die aktuelle Netzabdeckung im Partheland unter [ttnmapper.org/heatmap/](https://ttnmapper.org/heatmap/).

---

<div class="columns is-multiline is-centered" style="margin-top: 2rem;">
  <div class="column is-4-desktop is-6-tablet is-12-mobile">
    <div class="card modern-card standard-card full-height">
      <div class="card-content callout-card-content">
        <div class="callout-card-body">
          <h2 class="title is-3 is-spaced has-text-weight-bold has-text-centered callout-title">
            Daten nutzen
          </h2>
          <h3 class="subtitle is-5 mt-0 has-text-weight-medium has-text-centered callout-subtitle">
            Zugriff & Anwendung
          </h3>
          <div class="content has-text-centered callout-content">
            <p>Alle Informationen zum Zugriff auf die Sensordaten sowie praktische Anwendungsbeispiele.</p>
          </div>
        </div>
        <div class="has-text-centered callout-actions">
          <a href="/projekte/smart-city/daten-nutzen/" class="button is-success is-medium is-rounded has-text-weight-semibold" aria-label="Erkunden - Sensordaten nutzen">
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
          <h2 class="title is-3 is-spaced has-text-weight-bold has-text-centered callout-title">
            Praxisbeispiele
          </h2>
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
          <h2 class="title is-3 is-spaced has-text-weight-bold has-text-centered callout-title">
            Kontakt & Austausch
          </h2>
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
