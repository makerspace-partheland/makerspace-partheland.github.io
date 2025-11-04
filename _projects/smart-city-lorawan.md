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

Wie kommen Messdaten von einer Wiese, einem Feld oder einem Kleingarten zu Dir nach Hause – ohne Internet oder Mobilfunk? Die Antwort heißt LoRaWAN. Diese Abkürzung steht für _Long Range Wide Area Network_, also ein Funknetz für große Entfernungen. Es wurde speziell entwickelt, um kleine Datenmengen extrem energiesparend über mehrere Kilometer zu übertragen.

## Batterie- und Solarbetrieb

Stell Dir vor, ein Sensor läuft jahrelang mit einer einfachen Batterie. Klingt unrealistisch? Mit LoRaWAN ist genau das möglich. Der Energieverbrauch ist so gering, dass Sensoren mit Batterien oder kleinen Solarzellen und Akkus über Jahre hinweg autark arbeiten können. Kein Stromanschluss nötig, keine laufenden Kosten für Mobilfunkverträge oder Internet. Die Datenübertragung läuft über das öffentliche LoRaWAN-Netzwerk – kostenlos.

Das eröffnet völlig neue Möglichkeiten: Du kannst Messstationen an Orten aufbauen, wo es weder Strom noch Internet gibt. In Kleingärten, auf Sportplätzen, an Badeseen, auf Grünflächen, Feldern, in Wäldern oder am Ortsrand. Überall dort, wo Du Daten brauchst, aber keine Infrastruktur hast.

## Warum LoRaWAN statt WLAN, LTE oder 5G?

LoRaWAN wurde von Grund auf für Sensornetzwerke konzipiert und unterscheidet sich fundamental von den bekannten Funktechnologien. Die Reichweite? Im Freien mehrere Kilometer – deutlich mehr als die paar hundert Meter, die WLAN schafft.

Aber LoRaWAN hat auch klare Grenzen. Die Datenübertragung ist langsam und eignet sich nur für kleine Datenmengen: Temperatur, Luftfeuchtigkeit, Füllstände. Willst Du Kamerastreams übertragen, Sprache in Echtzeit senden oder häufige Updates? Dann brauchst Du WLAN, LTE oder 5G. Auch die Gebäudedurchdringung ist schwächer – Sensoren in Gebäuden benötigen oft eine Außenantenne oder müssen nah am Fenster stehen.

Für Umweltsensoren ist LoRaWAN dagegen perfekt. Alle paar Minuten ein paar Messwerte von einem Sensor auf dem Feld? Genau dafür wurde es gemacht. An abgelegenen Orten ohne Strom- oder Internetanschluss.

## Funktionsweise

Wie kommen die Daten vom Sensor zu Dir? Dafür braucht es sogenannte LoRa-Gateways. Stell Dir das wie einen Briefkasten vor: Befindet sich ein Sensor im Empfangsgebiet eines Gateways, empfängt dieses die Datenpakete über eine 30 bis 80 cm lange Stabantenne. Das Gateway ist mit dem Internet verbunden und leitet die Pakete weiter – fertig.

Die Datenpakete werden auf einer Frequenz zwischen 863 und 870 MHz gesendet. Diese Frequenz ist europaweit lizenzfrei nutzbar – jeder darf sie verwenden. Auch Alarmanlagen, Funktastaturen oder Garagentorfernbedienungen nutzen diesen Bereich, ohne sich gegenseitig zu stören.

**Wichtig beim Kauf:** Achte auf die Bezeichnung **868 MHz** oder **EU868** bei LoRaWAN-Geräten. Module mit **433 MHz** oder **915 MHz** (USA/Australien) funktionieren im Partheland-Netzwerk nicht.

## The Things Network (TTN)

Das Partheland-Netzwerk basiert auf dem **The Things Network (TTN)** – einer weltweiten, offenen LoRaWAN-Infrastruktur:

- **Kosteneffizienz**: TTN ist kostenlos nutzbar und nutzt das energieeffiziente LoRaWAN-Protokoll. Das ermöglicht den Betrieb von Sensoren und vernetzten Geräten mit minimalem Stromverbrauch und ohne laufende Kosten.
- **Sicherheit**: Die Daten werden mit dem Advanced Encryption Standard (AES) verschlüsselt und authentifiziert – ein sehr sicheres Verfahren.

## Betrieb und Wartung

Den Betrieb und die Wartung der LoRaWAN-Gateways in Brandis und dessen Ortsteilen übernimmt der Makerspace Partheland e.V., inklusive der Sensoren-Webseite und Infrastruktur. In allen weiteren Partheland-Kommunen kümmern sich die jeweiligen Multiplikatoren um Gateway-Betrieb und Wartung.

## Kostenfreier Zugang zum Netzwerk

<div class="notification is-success is-light" style="border-left: 4px solid var(--brand-green); box-shadow: 0 4px 20px rgba(0, 170, 0, 0.1); margin: 2rem 0;">
  <div class="content">
    <p style="margin-bottom: 0; font-size: 1.1rem; font-weight: 500;">
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
          <h2 class="title is-3 has-text-weight-bold has-text-centered callout-title">
            Daten nutzen
          </h2>
          <h3 class="subtitle is-5 has-text-weight-medium has-text-centered callout-subtitle">
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
