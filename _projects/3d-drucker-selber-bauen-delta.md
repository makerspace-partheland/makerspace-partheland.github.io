---
layout: page
title: 3D-Drucker selber bauen - Delta-Konstruktion
permalink: /projekte/3d-druck-konstruktion/3d-drucker-selber-bauen-delta/
excerpt: Bauanleitung für einen selbstgebauten Delta-3D-Drucker mit Open-Source-Komponenten
category: 3D-Druck & Konstruktion
gallery:
  - image_path: /assets/images/projekte/3d-druck-konstruktion/delta-drucker/delta-drucker-fertig.jpg
    alt: Delta-3D-Drucker - Fertig aufgebaut
    caption: Delta-3D-Drucker - Fertig aufgebaut
  - image_path: /assets/images/projekte/3d-druck-konstruktion/delta-drucker/delta-drucker-konstruktion.jpg
    alt: Delta-3D-Drucker - Konstruktionsdetails
    caption: Delta-3D-Drucker - Konstruktionsdetails
  - image_path: /assets/images/projekte/3d-druck-konstruktion/delta-drucker/delta-drucker-detail.jpg
    alt: Delta-3D-Drucker - Mechanische Komponenten
    caption: Delta-3D-Drucker - Mechanische Komponenten
---

<picture>
            <source type="image/webp" srcset="/assets/images/projekte/3d-druck-konstruktion/delta-drucker/delta-drucker-fertig.webp">
            <img src="/assets/images/projekte/3d-druck-konstruktion/delta-drucker/delta-drucker-fertig.jpg" alt="Delta-3D-Drucker - Fertig aufgebaut" class="title-image">
          </picture>

## 3D-Drucker selber bauen (Delta)

Der Bau eines eigenen 3D-Druckers ist ein spannendes Projekt, das sowohl technisches Verständnis als auch handwerkliches Geschick erfordert. In diesem Artikel beschreibe ich den Bau eines Delta-3D-Druckers mit verbesserten Sicherheits- und Funktionsmerkmalen.

## Sicherheitsverbesserungen

Einer der wichtigsten Aspekte beim Bau eines 3D-Druckers ist die Sicherheit. Ich habe mehrere Verbesserungen implementiert:

### Temperaturüberwachung
- **Thermistor-Überwachung**: Kontinuierliche Überwachung der Düsen- und Bett-Temperatur
- **Überhitzungsschutz**: Automatische Abschaltung bei kritischen Temperaturen
- **Fehlerbehandlung**: Sofortige Reaktion auf Sensorfehler

### Elektrische Sicherheit
- **Spannungsüberwachung**: Überwachung der 12V-Versorgung
- **Kurzschlussschutz**: Integrierte Sicherungen für alle Stromkreise
- **Erdung**: Korrekte Erdung aller metallischen Komponenten

## Funktionsverbesserungen

### Präzision
- **Delta-Kinematik**: Optimierte Berechnung der Bewegungsabläufe
- **Schrittmotor-Treiber**: Hochauflösende Treiber für bessere Genauigkeit
- **Kalibrierung**: Automatische Kalibrierung der Achsen

### Benutzerfreundlichkeit
- **Touchscreen**: Intuitive Bedienung über Touchscreen
- **WiFi-Anbindung**: Fernsteuerung über Netzwerk
- **Filament-Überwachung**: Automatische Erkennung von Filament-Ende

## Konstruktionsdetails

Der Drucker basiert auf der bewährten Delta-Konstruktion mit einigen eigenen Verbesserungen:

- **Rahmen**: Aluminium-Profile für maximale Stabilität
- **Bewegung**: Präzise Linearführungen
- **Antrieb**: Schrittmotoren mit Mikroschritt-Treibern
- **Düse**: Wechselbare Düsen für verschiedene Materialien

## Software

Die Steuerung erfolgt über Marlin-Firmware mit angepassten Einstellungen für die Delta-Kinematik. Alle Sicherheitsfunktionen sind in der Firmware implementiert.

## Fazit

Der selbstgebaute Delta-3D-Drucker bietet nicht nur eine kostengünstige Alternative zu kommerziellen Modellen, sondern ermöglicht auch eine vollständige Kontrolle über alle Aspekte des Druckers. Die implementierten Sicherheitsverbesserungen machen ihn zu einem sicheren und zuverlässigen Werkzeug für den Makerspace.
