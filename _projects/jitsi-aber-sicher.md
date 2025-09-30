---
layout: page
title: Jitsi aber sicher
permalink: /projekte/sonstiges/jitsi-aber-sicher/
excerpt: Sichere Konfiguration von Jitsi Meet für vertrauliche Videokonferenzen
category: Sonstiges
gallery:
  - image_path: /assets/images/projekte/sonstiges/jitsi/jitsi.png
    alt: Jitsi Meet Logo
    caption: Jitsi Meet Logo
  - image_path: /assets/images/projekte/sonstiges/jitsi/hetzner_jitsi.png
    alt: Hetzner Jitsi Konfiguration
    caption: Hetzner Jitsi Konfiguration
---

<picture>
            <source type="image/webp" srcset="/assets/images/projekte/sonstiges/jitsi/jitsi.webp">
            <img src="/assets/images/projekte/sonstiges/jitsi/jitsi.png" alt="Jitsi Meet Logo" class="title-image">
          </picture>

## Jitsi – aber sicher!

Jitsi Meet ist eine Open-Source-Alternative zu kommerziellen Videokonferenz-Lösungen wie Zoom. In diesem Artikel beschreibe ich, wie man einen eigenen Jitsi-Server sicher konfiguriert.

## Warum Jitsi?

Jitsi Meet bietet mehrere Vorteile:

- **Open Source**: Vollständig transparente Software
- **Datenschutz**: Keine Datenübertragung an Dritte
- **Kostenlos**: Keine Lizenzgebühren
- **Anpassbar**: Vollständige Kontrolle über die Konfiguration

## Sichere Installation

### Server-Anforderungen
- **Betriebssystem**: Ubuntu 20.04 LTS oder neuer
- **RAM**: Mindestens 4GB
- **CPU**: Mindestens 2 Kerne
- **Festplatte**: Mindestens 20GB freier Speicher

### Grundinstallation
```bash
# System aktualisieren
sudo apt update && sudo apt upgrade -y

# Jitsi-Repository hinzufügen
curl -sL https://download.jitsi.org/jitsi-key.gpg.key | sudo apt-key add -
curl -sL https://download.jitsi.org/stable/deb/jitsi-stable.list | sudo tee /etc/apt/sources.list.d/jitsi-stable.list

# Jitsi installieren
sudo apt update
sudo apt install jitsi-meet -y
```

## Sicherheitskonfiguration

### SSL-Zertifikat
```bash
# Let's Encrypt Zertifikat einrichten
sudo /usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh
```

### Firewall-Einstellungen
```bash
# UFW aktivieren
sudo ufw enable

# Notwendige Ports öffnen
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 10000/udp
```

### Prosody-Konfiguration
```bash
# Prosody-Konfiguration bearbeiten
sudo nano /etc/prosody/conf.avail/apeunit.test.cfg.lua
```

### Jicofo-Konfiguration
```bash
# Jicofo-Konfiguration bearbeiten
sudo nano /etc/jitsi/jicofo/sip-communicator.properties
```

## Fazit

Mit der richtigen Konfiguration bietet Jitsi Meet eine sichere und datenschutzkonforme Alternative zu kommerziellen Lösungen. Die eigene Kontrolle über den Server gibt die Gewissheit, dass vertrauliche Gespräche auch vertraulich bleiben.