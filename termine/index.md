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
    <!-- Farblegende -->
    <div class="event-legend">
      <div class="event-legend-item">
        <div class="event-legend-color featured"></div>
        <span class="event-legend-text">Besonderes</span>
      </div>
      <div class="event-legend-item">
        <div class="event-legend-color members-only"></div>
        <span class="event-legend-text">
          <span class="members-only-icon">
            <svg viewBox="0 0 24 24">
              <path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM12 17c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zM15.1 8H8.9V6c0-1.71 1.39-3.1 3.1-3.1s3.1 1.39 3.1 3.1v2z"/>
            </svg>
          </span>
          Vereinsintern
        </span>
      </div>
    </div>
    
    <h2 class="title is-4 has-text-centered termine-section-title">
      Anstehende Termine
    </h2>
    <div class="columns is-multiline is-centered">
      
      <!-- Reparatur-Treff zuerst -->
      {% if next_reparatur %}
        <div class="column is-4-desktop is-6-tablet is-12-mobile">
          {% if next_reparatur.featured %}
            <div class="card modern-card termine-card featured">
          {% elsif next_reparatur.members_only %}
            <div class="card modern-card members-only-event termine-card">
          {% else %}
            <div class="card modern-card termine-card standard">
          {% endif %}
            <div class="card-content termine-card-content">
              <div class="termine-card-body">
                <h3 class="title is-5 has-text-weight-bold has-text-centered termine-event-title">
                  {% if next_reparatur.members_only %}
                    <span class="members-only-icon">
                      <svg viewBox="0 0 24 24">
                        <path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM12 17c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zM15.1 8H8.9V6c0-1.71 1.39-3.1 3.1-3.1s3.1 1.39 3.1 3.1v2z"/>
                      </svg>
                    </span>
                  {% endif %}
                  <a href="{{ next_reparatur.url }}">{{ next_reparatur.title }}</a>
                </h3>
                <p class="subtitle is-6 has-text-weight-medium has-text-centered termine-event-date">
                  {{ next_reparatur.date | date: "%d.%m.%Y" }}
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
          {% if e.featured %}
            <div class="card modern-card termine-card featured">
          {% elsif e.members_only %}
            <div class="card modern-card members-only-event termine-card">
          {% else %}
            <div class="card modern-card termine-card standard">
          {% endif %}
            <div class="card-content termine-card-content">
              <div class="termine-card-body">
                <h3 class="title is-5 has-text-weight-bold has-text-centered termine-event-title">
                  {% if e.members_only %}
                    <span class="members-only-icon">
                      <svg viewBox="0 0 24 24">
                        <path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zM12 17c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zM15.1 8H8.9V6c0-1.71 1.39-3.1 3.1-3.1s3.1 1.39 3.1 3.1v2z"/>
                      </svg>
                    </span>
                  {% endif %}
                  <a href="{{ e.url }}">{{ e.title }}</a>
                </h3>
                {% if e.date %}
                  <p class="subtitle is-6 has-text-weight-medium has-text-centered termine-event-date">
                    {{ e.date | date: "%d.%m.%Y" }}
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
                    {{ e.date | date: "%d.%m.%Y" }}
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