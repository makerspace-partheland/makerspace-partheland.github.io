---
layout: page
title: Projekte
permalink: /projekte/
# classes: wide
---

## Eine Übersicht über unsere Projekte

Hier findest du alle unsere Projekte, sortiert nach Kategorien.

### Smart City
{% assign smart_city_projekte = site.projects | where: "category", "Smart City & IoT" %}
{% for projekt in smart_city_projekte %}
- [{{ projekt.title }}]({{ projekt.url }})
{% endfor %}

### Elektronik & Sensoren
{% assign elektronik_projekte = site.projects | where: "category", "Elektronik & Sensoren" %}
{% for projekt in elektronik_projekte %}
- [{{ projekt.title }}]({{ projekt.url }})
{% endfor %}

### Reparatur & Nachhaltigkeit
{% assign reparatur_projekte = site.projects | where: "category", "Reparatur & Nachhaltigkeit" %}
{% for projekt in reparatur_projekte %}
- [{{ projekt.title }}]({{ projekt.url }})
{% endfor %}

### 3D-Druck & Konstruktion
{% assign druck_projekte = site.projects | where: "category", "3D-Druck & Konstruktion" %}
{% for projekt in druck_projekte %}
- [{{ projekt.title }}]({{ projekt.url }})
{% endfor %}

### Sonstiges
{% assign sonstige_projekte = site.projects | where: "category", "Sonstiges" %}
{% for projekt in sonstige_projekte %}
- [{{ projekt.title }}]({{ projekt.url }})
{% endfor %}
