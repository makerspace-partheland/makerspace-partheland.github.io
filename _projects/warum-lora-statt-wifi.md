---
layout: page
title: Warum nutzen wir LoRa und kein WiFi für die Umweltsensoren?
permalink: /projekte/smart-city/warum-lora-statt-wifi/
excerpt: Technische und praktische Gründe für die Wahl von LoRaWAN statt WiFi bei IoT-Umweltsensoren
category: Smart City & IoT
---

<img src="/assets/images/projekte/smart-city/lorawan-station.jpg" alt="LoRaWAN Station - Umweltsensoren" class="title-image">

## Warum nutzen wir LoRa und kein WiFi für die Umweltsensoren?

Bei der Auswahl der Technologie für unsere Umweltsensoren haben wir uns bewusst für LoRaWAN (Long Range Wide Area Network) entschieden, anstatt auf WiFi zu setzen. Diese Entscheidung basiert auf mehreren technischen und praktischen Überlegungen.

## Technische Vorteile von LoRaWAN

### Reichweite und Abdeckung
- **Lange Reichweite**: LoRaWAN kann Signale über mehrere Kilometer übertragen
- **Bessere Durchdringung**: Funktioniert auch durch Wände und Vegetation
- **Weniger Basisstationen**: Geringere Infrastrukturkosten

### Energieeffizienz
- **Niedriger Stromverbrauch**: Sensoren können jahrelang mit Batterien betrieben werden
- **Schlafmodi**: Sensoren können den größten Teil der Zeit im Energiesparmodus verbringen
- **Optimierte Übertragung**: Nur bei Bedarf werden Daten gesendet

## Praktische Vorteile

### Kosten
- **Geringere Betriebskosten**: Keine WiFi-Infrastruktur erforderlich
- **Skalierbarkeit**: Einfache Erweiterung um weitere Sensoren
- **Wartung**: Weniger wartungsintensive Technologie

### Zuverlässigkeit
- **Stabile Verbindung**: Weniger anfällig für Interferenzen
- **Offenes Netzwerk**: Nutzung des öffentlichen The Things Network (TTN)
- **Redundanz**: Mehrere Gateway-Standorte für bessere Abdeckung

## Warum nicht WiFi?

### Nachteile von WiFi
- **Begrenzte Reichweite**: Nur wenige hundert Meter
- **Hoher Stromverbrauch**: WiFi-Module benötigen mehr Energie
- **Komplexität**: WLAN-Konfiguration und -Wartung
- **Interferenzen**: Störungen durch andere WiFi-Netzwerke

## Unser Setup

Wir nutzen das **The Things Network (TTN)** als LoRaWAN-Infrastruktur:

- **Kosteneffizienz**: TTN nutzt LoRaWAN, ein niedrigenergiespezifisches Protokoll, das es ermöglicht, IoT-Geräte mit geringem Stromverbrauch und geringen Kosten zu betreiben.
- **Sicherheit**: TTN nutzt Advanced Encryption Standard (AES) für die Datenverschlüsselung und Authentifizierung, was es sehr sicher macht.

## Fazit

LoRaWAN bietet für unsere Umweltsensoren die optimale Kombination aus Reichweite, Energieeffizienz und Kosten. Die Technologie ermöglicht es uns, ein flächendeckendes Netzwerk von Sensoren aufzubauen, ohne die Komplexität und Kosten einer WiFi-Infrastruktur zu haben.
