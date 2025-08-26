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
<section class="section" style="padding: 4rem 1.5rem;">
  <div class="container">
    <h2 class="title is-4 has-text-centered" style="color: #2c3e50; margin-bottom: 2rem;">
      Anstehende Termine
    </h2>
    <div class="columns is-multiline is-centered">
      
      <!-- Reparatur-Treff zuerst -->
      {% if next_reparatur %}
        <div class="column is-4-desktop is-6-tablet is-12-mobile">
          {% if next_reparatur.featured %}
            <div class="card modern-card" style="height: 100%; box-shadow: 0 6px 25px rgba(0, 170, 0, 0.15); border-radius: 12px; border-left: 4px solid var(--brand-green); transition: all 0.3s ease;">
          {% else %}
            <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-radius: 12px; transition: all 0.3s ease;">
          {% endif %}
            <div class="card-content" style="padding: 2rem 1.5rem; height: 100%; display: flex; flex-direction: column;">
              <div style="flex-grow: 1;">
                <h3 class="title is-5 has-text-weight-bold has-text-centered" style="color: #2c3e50; margin-bottom: 0.5rem;">
                  <a href="{{ next_reparatur.url }}" style="color: #2c3e50; text-decoration: none;">{{ next_reparatur.title }}</a>
                </h3>
                <p class="subtitle is-6 has-text-weight-medium has-text-centered" style="color: var(--brand-blue); margin-bottom: 1rem;">
                  {{ next_reparatur.date | date: "%d.%m.%Y" }}
                </p>
                {% if next_reparatur.excerpt %}
                  <div class="content is-size-6 has-text-centered" style="color: #5a6c7d; line-height: 1.5;">
                    {{ next_reparatur.excerpt }}
                  </div>
                {% endif %}
              </div>
              <div class="has-text-centered" style="margin-top: 1rem;">
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
            <div class="card modern-card" style="height: 100%; box-shadow: 0 6px 25px rgba(0, 170, 0, 0.15); border-radius: 12px; border-left: 4px solid var(--brand-green); transition: all 0.3s ease;">
          {% else %}
            <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-radius: 12px; transition: all 0.3s ease;">
          {% endif %}
            <div class="card-content" style="padding: 2rem 1.5rem; height: 100%; display: flex; flex-direction: column;">
              <div style="flex-grow: 1;">
                <h3 class="title is-5 has-text-weight-bold has-text-centered" style="color: #2c3e50; margin-bottom: 0.5rem;">
                  <a href="{{ e.url }}" style="color: #2c3e50; text-decoration: none;">{{ e.title }}</a>
                </h3>
                {% if e.date %}
                  <p class="subtitle is-6 has-text-weight-medium has-text-centered" style="color: var(--brand-blue); margin-bottom: 1rem;">
                    {{ e.date | date: "%d.%m.%Y" }}
                  </p>
                {% endif %}
                {% if e.excerpt %}
                  <div class="content is-size-6 has-text-centered" style="color: #5a6c7d; line-height: 1.5;">
                    {{ e.excerpt }}
                  </div>
                {% endif %}
              </div>
              <div class="has-text-centered" style="margin-top: 1rem;">
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
<section class="section" style="padding: 2rem 1.5rem;">
  <div class="container">
    <h2 class="title is-4 has-text-centered" style="color: #2c3e50; margin-bottom: 2rem;">
      Vergangene Termine
    </h2>
    <div class="columns is-multiline is-centered">
      {% for e in past limit: 6 %}
        <div class="column is-4-desktop is-6-tablet is-12-mobile">
          <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-radius: 12px; transition: all 0.3s ease; opacity: 0.9;">
            <div class="card-content" style="padding: 1.5rem 1.25rem; height: 100%; display: flex; flex-direction: column;">
              <div style="flex-grow: 1;">
                <h3 class="title is-6 has-text-weight-semibold has-text-centered" style="color: #34495e; margin-bottom: 0.5rem;">
                  <a href="{{ e.url }}" style="color: #34495e; text-decoration: none;">{{ e.title }}</a>
                </h3>
                {% if e.date %}
                  <p class="subtitle is-7 has-text-weight-medium has-text-centered" style="color: #5a6c7d; margin-bottom: 0.75rem;">
                    {{ e.date | date: "%d.%m.%Y" }}
                  </p>
                {% endif %}
                {% if e.excerpt %}
                  <div class="content is-size-6 has-text-centered" style="color: #5a6c7d; line-height: 1.4;">
                    {{ e.excerpt | truncate: 120 }}
                  </div>
                {% endif %}
              </div>
              <div class="has-text-centered" style="margin-top: 1rem;">
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