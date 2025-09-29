---
layout: page
title: Austausch & Begegnung
subtitle: Für Neugierige und Interessierte
hide_hero: false
hero_height: is-medium
hero_show_title: true
hero_show_subtitle: true
permalink: /austausch/
---

<section class="section main-section">
  <div class="container">
    <div class="columns is-multiline is-centered">
      
      <!-- Telegram Kanäle -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card standard-card full-height">
          <div class="card-content standard-card-content large centered">
            <h2 class="title is-3 has-text-weight-bold primary-title mb-1rem">
              Täglich aktive Telegram-Kanäle
            </h2>
            <h3 class="subtitle is-5 has-text-weight-medium secondary-title mb-1-5rem">
              Hier ist immer etwas los
            </h3>
            <div class="content body-text mb-2rem">
              <p>Täglich neue Ideen, Fragen und spannende Diskussionen in unseren Telegram-Kanälen.</p>
            </div>
            <div class="buttons is-centered button-group column">
              <a href="https://t.me/makerspacepartheland" target="_blank" rel="noreferrer noopener" 
                 class="button is-primary is-large is-rounded has-text-weight-semibold full-width">
                Hauptkanal
              </a>
              <a href="https://t.me/+J04U0UCk43MxNTMy" target="_blank" rel="noreferrer noopener" 
                 class="button is-success is-large is-rounded has-text-weight-semibold full-width">
                Unsere Themenwelt
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Termine vor Ort -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card standard-card full-height">
          <div class="card-content standard-card-content large centered">
            <h2 class="title is-3 has-text-weight-bold primary-title mb-1rem">
              Termine vor Ort
            </h2>
            <h3 class="subtitle is-5 has-text-weight-medium secondary-title mb-1-5rem">
              Ehrenamtlich & unregelmäßig
            </h3>
            <div class="content body-text">
              {% assign upcoming = site.events | where_exp: "e", "e.date" | where_exp: "e", "e.date >= site.time" | sort: "date" %}
              {% if upcoming and upcoming.size > 0 %}
                <p><strong>Anstehende Termine:</strong></p>
                <ul class="text-left">
                  {% for e in upcoming limit: 3 %}
                    <li>
                      <a href="{{ e.url }}">{{ e.title }}</a>
                      {%- if e.date %} – {{ e.date | date: "%d.%m.%Y" }}{%- endif -%}
                    </li>
                  {% endfor %}
                </ul>
              {% else %}
                <p>Aktuell sind keine Termine geplant.</p>
                <p><em>Aber in unseren Telegram-Kanälen ist immer etwas los!</em></p>
              {% endif %}
            </div>
            <div class="has-text-centered mb-2rem">
              <a href="/termine/" class="button is-primary is-medium is-rounded has-text-weight-semibold">
                Vergangene ansehen
              </a>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="section secondary-section compact-top">
  <div class="container">
    <div class="columns is-centered">
      <div class="column is-8-desktop is-10-tablet is-12-mobile">
        <div class="card modern-card standard-card full-height">
          <div class="card-content standard-card-content large centered">
            <h2 class="title is-3 has-text-weight-bold primary-title mb-1rem">
              Vor Ort besuchen
            </h2>
            <div class="content body-text">
              <p><strong>Temporärer Makerspace:</strong><br>
              August-Bebel-Straße 12, 04824 Brandis, OT Beucha<br>
              (Hintereingang, 1. Etage)</p>
              
              <p><strong>Öffnungszeiten:</strong><br>
              Nach Kontaktaufnahme per Telegram oder E-Mail</p>
              
              <p><strong>E-Mail:</strong> {% include email.html user="info" domain="makerspace-partheland.de" %}</p>
              
              <p class="font-small">
                Ehrenamtliche können über Telegram flexibler antworten und sich ihre Zeit frei einteilen.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
