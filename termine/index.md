---
layout: default
title: Termine
permalink: /termine/
---

{% assign upcoming = site.events | where_exp: "e", "e.date" | where_exp: "e", "e.date >= site.time" | sort: "date" %}
{% assign past = site.events | where_exp: "e", "e.date" | where_exp: "e", "e.date < site.time" | sort: "date" | reverse %}

### Reparatur‑Treff (unregelmäßig)

Details und Hinweise findest du hier: [Reparatur‑Treff](/termine/reparatur-treff/)

### Anstehend
{% if upcoming and upcoming.size > 0 %}
<ul>
  {% for e in upcoming %}
    <li>
      <a href="{{ e.url }}">{{ e.title }}</a>
      {%- if e.date %} – {{ e.date | date: "%d.%m.%Y" }}{%- endif -%}
      {%- if e.location %} · {{ e.location }}{%- endif -%}
    </li>
  {% endfor %}
{% else %}
  <p>Aktuell sind keine Termine geplant.</p>
{% endif %}


### Vergangen
{% if past and past.size > 0 %}
<ul>
  {% for e in past %}
    <li>
      <a href="{{ e.url }}">{{ e.title }}</a>
      {%- if e.date %} – {{ e.date | date: "%d.%m.%Y" }}{%- endif -%}
      {%- if e.location %} · {{ e.location }}{%- endif -%}
    </li>
  {% endfor %}
{% else %}
  <p>Es sind noch keine vergangenen Termine eingetragen.</p>
{% endif %}


