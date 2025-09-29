---
layout: page
title: Termine
subtitle: Veranstaltungen und Treffen im Makerspace
hide_hero: false
hero_height: is-medium
hero_show_title: true
hero_show_subtitle: true
permalink: /termine/
---

{% assign upcoming = site.events | where_exp: "e", "e.date" | where_exp: "e", "e.date >= site.time" | sort: "date" %}
{% assign past = site.events | where_exp: "e", "e.date" | where_exp: "e", "e.date < site.time" | sort: "date" | reverse %}

{% comment %} Filter Reparatur-Treff events {% endcomment %}
{% assign reparatur_events = upcoming | where_exp: "e", "e.title contains 'Reparatur-Treff'" %}
{% assign next_reparatur = reparatur_events.first %}
{% assign other_upcoming = "" | split: "" %}
{% for e in upcoming %}
  {% unless e.title contains 'Reparatur-Treff' %}
    {% assign other_upcoming = other_upcoming | push: e %}
  {% endunless %}
{% endfor %}


<!-- Anstehende Termine (falls vorhanden) -->
{% if upcoming and upcoming.size > 0 %}
<section class="section termine-upcoming-section">
  <div class="container">
    
    
    <h2 class="title is-4 has-text-centered termine-section-title">
      Anstehende Termine
    </h2>
    <div class="columns is-multiline is-centered">
      
      <!-- Reparatur-Treff zuerst -->
      {% if next_reparatur %}
        <div class="column is-4-desktop is-6-tablet is-12-mobile">
          {% assign accent_class = '' %}
          {% if next_reparatur.accent == 'green' %}
            {% assign accent_class = 'accent-green' %}
          {% elsif next_reparatur.accent == 'orange' %}
            {% assign accent_class = 'accent-orange' %}
          {% endif %}
          {% if accent_class != '' %}
            <div class="card modern-card termine-card {{ accent_class }}">
          {% else %}
            <div class="card modern-card termine-card standard">
          {% endif %}
            <div class="card-content termine-card-content">
              <div class="termine-card-body">
                <h3 class="title is-5 has-text-weight-bold has-text-centered termine-event-title">
                  <a href="{{ next_reparatur.url }}">{{ next_reparatur.title }}</a>
                </h3>
                <p class="subtitle is-6 has-text-weight-medium has-text-centered termine-event-date">
                  {{ next_reparatur.date | date: "%d.%m.%Y" }}{% if next_reparatur.start_time %}, {{ next_reparatur.start_time }}{% if next_reparatur.end_time %} - {{ next_reparatur.end_time }}{% endif %}{% endif %}
                </p>
                {% if next_reparatur.excerpt %}
                  <div class="content is-size-6 has-text-centered termine-event-content">
                    {{ next_reparatur.excerpt }}
                  </div>
                {% endif %}
              </div>
              <div class="has-text-centered termine-card-actions">
                <a href="{{ next_reparatur.url }}" class="button is-small is-primary is-rounded">
                  Details
                </a>
              </div>
            </div>
          </div>
        </div>
      {% endif %}
      
      <!-- Andere Events -->
      {% for e in other_upcoming %}
        <div class="column is-4-desktop is-6-tablet is-12-mobile">
          {% assign accent_class = '' %}
          {% if e.accent == 'green' %}
            {% assign accent_class = 'accent-green' %}
          {% elsif e.accent == 'orange' %}
            {% assign accent_class = 'accent-orange' %}
          {% endif %}
          {% if accent_class != '' %}
            <div class="card modern-card termine-card {{ accent_class }}">
          {% else %}
            <div class="card modern-card termine-card standard">
          {% endif %}
            <div class="card-content termine-card-content">
              <div class="termine-card-body">
                <h3 class="title is-5 has-text-weight-bold has-text-centered termine-event-title">
                  <a href="{{ e.url }}">{{ e.title }}</a>
                </h3>
                {% if e.date %}
                  <p class="subtitle is-6 has-text-weight-medium has-text-centered termine-event-date">
                    {{ e.date | date: "%d.%m.%Y" }}{% if e.start_time %}, {{ e.start_time }}{% if e.end_time %} - {{ e.end_time }}{% endif %}{% endif %}
                  </p>
                {% endif %}
                {% if e.excerpt %}
                  <div class="content is-size-6 has-text-centered termine-event-content">
                    {{ e.excerpt }}
                  </div>
                {% endif %}
              </div>
              <div class="has-text-centered termine-card-actions">
                <a href="{{ e.url }}" class="button is-small is-primary is-rounded">
                  Details
                </a>
              </div>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</section>
{% endif %}

<!-- Vergangene Termine -->
{% if past and past.size > 0 %}
<section class="section termine-past-section">
  <div class="container">
    <h2 class="title is-4 has-text-centered termine-section-title">
      Vergangene Termine
    </h2>
    <div class="columns is-multiline is-centered">
      {% for e in past limit: 6 %}
        <div class="column is-4-desktop is-6-tablet is-12-mobile">
          <div class="card modern-card termine-card past">
            <div class="card-content termine-card-content past">
              <div class="termine-card-body">
                <h3 class="title is-6 has-text-weight-semibold has-text-centered termine-event-title past">
                  <a href="{{ e.url }}">{{ e.title }}</a>
                </h3>
                {% if e.date %}
                  <p class="subtitle is-7 has-text-weight-medium has-text-centered termine-event-date past">
                    {{ e.date | date: "%d.%m.%Y" }}{% if e.start_time %}, {{ e.start_time }}{% if e.end_time %} - {{ e.end_time }}{% endif %}{% endif %}
                  </p>
                {% endif %}
                {% if e.excerpt %}
                  <div class="content is-size-6 has-text-centered termine-event-content past">
                    {{ e.excerpt | truncate: 120 }}
                  </div>
                {% endif %}
              </div>
              <div class="has-text-centered termine-card-actions">
                <a href="{{ e.url }}" class="button is-small is-light is-rounded">
                  Ansehen
                </a>
              </div>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</section>
{% endif %}
{% include events-list-structured-data.html events=upcoming list_name='Anstehende Termine Makerspace Partheland' %}



