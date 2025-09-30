---
layout: page
title: Smart City - Umweltsensoren und mehr
permalink: /projekte/smart-city/
excerpt: LoRaWAN-basierte Umweltsensoren für die intelligente Stadt der Zukunft
category: Smart City & IoT
---

<picture>
            <source type="image/webp" srcset="/assets/images/projekte/smart-city/smart-city-header.webp">
            <img src="/assets/images/projekte/smart-city/smart-city-header.jpg" alt="Smart City Partheland - Umweltsensoren" class="title-image">
          </picture>

# Smart City Partheland

Im Rahmen des <a rel="noreferrer noopener" href="https://open-government-kommunen.de/" target="_blank">Regionalen Open Government Labor</a> der Stadt Brandis beteiligen wir uns seit 2022 am Aufbau und dem stetigen Betrieb von Bürger-Umweltmessstationen und eines LoRaWAN Netzwerkes in der Gemeinde Brandis. Hier kümmern wir uns ehrenamtlich um alle anfallenden Dinge.

Seit Dezember 2022 unterstützen wir alle weiteren <a rel="noreferrer noopener" href="https://partheland.de" target="_blank">Partheland</a> Kommunen (Borsdorf, Naunhof mit Belgershain und Parthenstein, Großpösna und Machern) im Rahmen des Smart City Projektes durch Schulung von sogenannten Multiplikatoren, welche vor Ort die jeweiligen Ansprechpartner sind. Zudem stellen wir hierfür ehrenamtlich die Software für die jeweiligen Umweltmessstationen zur Verfügung, bereiten im Hintergrund alles für den Datentransfer vor, überwachen stetig die Stationen und Infrastruktur und viele weitere Dinge die man nicht sieht.

Alle stationären Umweltsensoren werden mittels <a rel="noreferrer noopener" href="home" target="_blank">senseBox:home</a> und mit der stromsparenden <a href="https://www.thethingsnetwork.org" target="_blank" rel="noreferrer noopener">LoRaWAN </a>Anbindung realisiert und im gesamten Partheland aufgebaut.

![LoRaWAN Station mit Sensorik](/assets/images/projekte/smart-city/lorawan-station.jpg)

Wissenstransfer und Austausch mit Bürgern, Multiplikatoren und uns, erfolgt im eigenen Telegram Kanal: <a rel="noreferrer noopener" href="https://t.me/MakerspacePartheland_SmartCity" target="_blank">https://t.me/MakerspacePartheland_SmartCity</a>

## Bürgermessstationen

Die Bürgermessstationen werden mittels **Patenschaft** betrieben. Dies bedeutet, es müssen ein paar **Regeln eingehalten** **werden**. Die Station wird durch die jeweilige Kommune **für die Bürger** bereitgestellt. Der Makerspace Partheland e.V. für Brandis, sowie die Multiplikatoren vor Ort im Partheland, befähigen den entsprechenden Paten zum Aufbau und geben Tipps. Der **Betrieb** und die (mindestens) jährliche **Wartung** wird **durch den Paten selbständig durchgeführt**.

Eine senseBox:home besteht im Partheland aus folgenden Sensoren:

- Temperatur
- relative Luftfeuchte
- Luftdruck
- Beleuchtungsstärke
- UV-Intensität
- Feinstaubsensor (PM10 und 2.5)
- Lautstärke (Mittelwert des Lautstärkepegels über eine Minute – ohne Gesprächsaufzeichnung)

Visuell dargestellt werden die Daten auf der zu den senseBoxen zugehörigen Seite <a rel="noreferrer noopener" href="https://opensensemap.org" target="_blank">https://opensensemap.org</a> und auf unserer eigenen Sensoren Seite, für detailliertere und längerfristige Datenauswertungen: <a rel="noreferrer noopener" href="https://sensoren.makerspace-partheland.de/" target="_blank"><strong>https://sensoren.makerspace-partheland.de/</strong></a>

Eine Karte aller Stationen und Gateways: <a rel="noreferrer noopener" href="https://map.makerspace-partheland.de" target="_blank">https://map.makerspace-partheland.de</a>

Seit Juli 2023 stehen, für zum Beispiel Freunde der Heimautomatisierung, die Sensordaten aller Stationen via freiem MQTT Websocket zur Verfügung:  
_wss://mqtt.makerspace-partheland.de:443/mqtt_

{% raw %}
Topic der Umweltmessstationen: senseBox:home/{%Stationsname%}  
(weitere Sensoren und Topics folgen)
{% endraw %}

Es werden die decodierten Sensordaten, sowie Name der Station, Manager (ist es eine Makerspace oder eine Smart City Station), die LoRa Rohdaten, Netzwerkdaten wie Empfangsstärke, Aufstellungsort, Empfangszeitpunkt, genutztes Gateway und Zeitstempel als JSON ausgegeben, sobald ein Datenpaket von der jeweiligen Station empfangen wurde.

Alles befindet sich aktuell im Aufbau, es kommen stetig mehr Stationen, Sensoren und Webseitenfunktionalitäten dazu. Haben wir Dein Interesse geweckt, hast Du Ideen, werden weitere Messwerte benötigt oder gibt es Fragen? Dann melde dich bei uns, den Multiplikatoren und allen Interessierten via <a rel="noreferrer noopener" href="https://t.me/MakerspacePartheland_SmartCity" target="_blank">https://t.me/MakerspacePartheland_SmartCity</a>

## LoRaWAN Netzwerk

Damit die Messstationen unabhängig von Internet-Infrastruktur die Daten senden können, also auch vom Feld oder einer Wiese, nutzen wir die LoRaWAN Technik. Diese Abkürzung steht für _Long Range Wide Area Network_ und wurde für energieeffizientes Senden von Daten über größere Entfernungen entwickelt. Dies ermöglicht somit auch Batterie oder Photovoltaik-Akku-betriebene Sensoren, wie die beiden vom Makerspace aufgebauten Umweltmessstationen <a rel="noreferrer noopener" href="https://sensoren.makerspace-partheland.de/d/l2eL6qr4x/station-brandis-nummer-3" target="_blank">Station Brandis Nummer 3</a> oder <a rel="noreferrer noopener" href="https://sensoren.makerspace-partheland.de/d/erweVEQnG/station-naunhof" target="_blank">Station Naunhof</a>

![senseBox:home solarbetrieben](/assets/images/projekte/smart-city/sensebox-home-solar.jpg)

Damit die Daten der Sensoren bei uns ankommen, werden so genannte LoRa Gateways benötigt. Einfach erklärt: befindet sich ein Sensor im Empfangsgebiet eines beliebigen LoRa Gateways, empfängt dieser die Sensoren-Pakete, mittels einer ca. 80cm langen Stabantenne. Da das Gateway mit dem Internet verbunden ist, leitet es dann das Sensoren-Paket an uns weiter.

Gesendet werden die Datenpakete auf einer Frequenz von 863 bis 870 MHz, welche europaweit lizenzfrei durch jeden nutzbar ist. Viel wird dieser Frequenzbereich auch für Alarmanlagen, Funktastaturen, Garagentorfernbedienungen und vieles mehr genutzt; ohne dass sich die Geräte in ihrem Betrieb gegenseitig stören.

Der Betrieb und die Wartung der LoRaWAN Gateways in Brandis, samt Sensoren-Webseite wird durch uns, den Makerspace Partheland e.V. durchgeführt.  
Der Betrieb und die Wartung der LoRaWAN Gateways in allen weiteren Partheland Kommunen erfolgt durch die jeweiligen Multiplikatoren.

Mehr Hintergründe zu unserer Technologieentscheidung: <a href="/projekte/smart-city/warum-lora-statt-wifi/">Warum nutzen wir LoRa und kein WiFi für die Umweltsensoren?</a>
