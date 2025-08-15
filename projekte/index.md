---
layout: page
title: Projekte
subtitle: Eine Übersicht über unsere Projekte
hero_description: Hier findest du alle unsere Projekte, sortiert nach Kategorien. Entdecke praktische Lösungen und kreative Ansätze aus unserem Makerspace.
permalink: /projekte/
hide_hero: false
hero_height: is-medium
hero_show_title: true
hero_show_subtitle: true
hero_link: /kontakt/
hero_link_text: Projekt vorschlagen
---

<!-- Smart City & IoT -->
{% assign smart_city_projekte = site.projects | where: "category", "Smart City & IoT" %}
{% if smart_city_projekte.size > 0 %}
## Smart City

<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 3rem;">
{% for projekt in smart_city_projekte %}
  <a href="{{ projekt.url }}" class="button is-light is-rounded" style="margin: 0;">{{ projekt.title }}</a>
{% endfor %}
</div>
{% endif %}

<!-- Elektronik & Sensoren -->
{% assign elektronik_projekte = site.projects | where: "category", "Elektronik & Sensoren" %}
{% if elektronik_projekte.size > 0 %}
## Elektronik & Sensoren

<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 3rem;">
{% for projekt in elektronik_projekte %}
  <a href="{{ projekt.url }}" class="button is-light is-rounded" style="margin: 0;">{{ projekt.title }}</a>
{% endfor %}
</div>
{% endif %}

<!-- Reparatur & Nachhaltigkeit -->
{% assign reparatur_projekte = site.projects | where: "category", "Reparatur & Nachhaltigkeit" %}
{% if reparatur_projekte.size > 0 %}
## Reparatur & Nachhaltigkeit

<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 3rem;">
{% for projekt in reparatur_projekte %}
  <a href="{{ projekt.url }}" class="button is-light is-rounded" style="margin: 0;">{{ projekt.title }}</a>
{% endfor %}
</div>
{% endif %}

<!-- 3D-Druck & Konstruktion -->
{% assign druck_projekte = site.projects | where: "category", "3D-Druck & Konstruktion" %}
{% if druck_projekte.size > 0 %}
## 3D-Druck & Konstruktion

<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 3rem;">
{% for projekt in druck_projekte %}
  <a href="{{ projekt.url }}" class="button is-light is-rounded" style="margin: 0;">{{ projekt.title }}</a>
{% endfor %}
</div>
{% endif %}

<!-- Weitere Projekte -->
{% assign sonstige_projekte = site.projects | where: "category", "Sonstiges" %}
{% if sonstige_projekte.size > 0 %}
## Weitere Projekte

<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 3rem;">
{% for projekt in sonstige_projekte %}
  <a href="{{ projekt.url }}" class="button is-light is-rounded" style="margin: 0;">{{ projekt.title }}</a>
{% endfor %}
</div>
{% endif %}
