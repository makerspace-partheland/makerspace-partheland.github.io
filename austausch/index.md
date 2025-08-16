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

<section class="section" style="padding: 4rem 1.5rem;">
  <div class="container">
    <div class="columns is-multiline is-centered">
      
      <!-- Telegram Kanäle -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-radius: 12px;">
          <div class="card-content" style="padding: 2.5rem 2rem; text-align: center;">
            <h2 class="title is-3 has-text-weight-bold" style="color: #2c3e50; margin-bottom: 1rem;">
              Täglich aktive Telegram-Kanäle
            </h2>
            <h3 class="subtitle is-5 has-text-weight-medium" style="color: #34495e; margin-bottom: 1.5rem;">
              Hier ist immer etwas los
            </h3>
            <div class="content" style="color: #5a6c7d; line-height: 1.6; margin-bottom: 2rem;">
              <p>Täglich neue Ideen, Fragen und spannende Diskussionen in unseren Telegram-Kanälen.</p>
            </div>
            <div class="buttons is-centered" style="flex-direction: column; gap: 1rem;">
              <a href="https://t.me/makerspacepartheland" target="_blank" rel="noreferrer noopener" 
                 class="button is-primary is-large is-rounded has-text-weight-semibold" 
                 class="button is-primary is-large is-rounded has-text-weight-semibold" style="width: 100%;">
                Makerspace Partheland Public
              </a>
              <a href="https://t.me/+J04U0UCk43MxNTMy" target="_blank" rel="noreferrer noopener" 
                 class="button is-success is-large is-rounded has-text-weight-semibold" 
                 style="width: 100%;">
                Unsere Themenwelt
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Termine vor Ort -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-radius: 12px;">
          <div class="card-content" style="padding: 2.5rem 2rem; text-align: center;">
            <h2 class="title is-3 has-text-weight-bold" style="color: #2c3e50; margin-bottom: 1rem;">
              Termine vor Ort
            </h2>
            <h3 class="subtitle is-5 has-text-weight-medium" style="color: #34495e; margin-bottom: 1.5rem;">
              Ehrenamtlich & unregelmäßig
            </h3>
            <div class="content" style="color: #5a6c7d; line-height: 1.6;">
              {% assign upcoming = site.events | where_exp: "e", "e.date" | where_exp: "e", "e.date >= site.time" | sort: "date" %}
              {% if upcoming and upcoming.size > 0 %}
                <p><strong>Anstehende Termine:</strong></p>
                <ul style="text-align: left;">
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
            <div class="has-text-centered" style="margin-top: 2rem;">
              <a href="/termine/" class="button is-primary is-medium is-rounded has-text-weight-semibold">
                Vergangene Termine ansehen
              </a>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<section class="section" style="padding: 2rem 1.5rem; background-color: #f8f9fa;">
  <div class="container">
    <div class="has-text-centered">
      <h2 class="title is-4" style="color: #2c3e50; margin-bottom: 1rem;">
        Vor Ort besuchen
      </h2>
      <div class="content" style="color: #5a6c7d;">
        <p><strong>Temporärer Makerspace:</strong><br>
        August-Bebel-Straße 12, 04824 Brandis, OT Beucha<br>
        (Hintereingang, 1. Etage)</p>
        
        <p><strong>Öffnungszeiten:</strong><br>
        Nach Kontaktaufnahme per Telegram oder E-Mail</p>
        
        <p><strong>E-Mail:</strong> {% include email.html user="info" domain="makerspace-partheland.de" %}</p>
        
        <p style="font-size: 0.9rem; font-style: italic;">
          Ehrenamtliche können über Telegram flexibler antworten und sich ihre Zeit frei einteilen.
        </p>
      </div>
    </div>
  </div>
</section>
