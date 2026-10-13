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

<section class="section main-section pt-0">
  <div class="container">
    <div class="columns is-multiline is-centered">
      
      <!-- Telegram Kanäle -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card standard-card full-height">
          <div class="card-content standard-card-content large centered">
            <div class="card-content-body">
              <h2 class="title is-3 has-text-weight-bold primary-title mb-1rem">
                Telegram-Kanäle
              </h2>
              <div class="content body-text mb-2rem">
                <p>In unseren Telegram-Kanälen werden täglich Ideen diskutiert und Fragen beantwortet.</p>
              </div>
            </div>
            <div class="buttons is-centered button-group column card-cta">
              <a href="https://t.me/makerspacepartheland" target="_blank" rel="noreferrer noopener"
                 class="button is-primary is-large is-rounded has-text-weight-semibold full-width"
                 aria-label="Hauptkanal (öffnet in neuem Tab)">
                Hauptkanal
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Termine vor Ort -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card standard-card full-height">
          <div class="card-content standard-card-content large centered">
            <div class="card-content-body">
              <h2 class="title is-3 has-text-weight-bold primary-title mb-1rem">
                Termine vor Ort
              </h2>
              <div class="content body-text mb-2rem">
                <p>Veranstaltungen finden unregelmäßig statt.</p>
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
                  <p>Austausch ist auch außerhalb der Termine über Telegram möglich.</p>
                {% endif %}
              </div>
            </div>
            <div class="buttons is-centered button-group column card-cta">
              <a href="/termine/" class="button is-primary is-large is-rounded has-text-weight-semibold full-width">
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
              <p><strong>Temporärer Makerspace im Coworking Brandis</strong><br>
              Markt 8, 04821 Brandis<br></p>
              
              <p><strong>Öffnungszeiten:</strong><br>
              Nach Kontaktaufnahme per Telegram oder E-Mail</p>
              
              <p><strong>E-Mail:</strong> {% include email.html user="info" domain="makerspace-partheland.de" %}</p>
              
              <p class="font-small">
                Unser Verein arbeitet vollständig ehrenamtlich. Über Telegram können wir Anfragen zeitlich flexibel beantworten.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
