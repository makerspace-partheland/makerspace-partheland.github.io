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

<section class="section" style="padding: 4rem 1.5rem;">
  <div class="container">
    <div class="columns is-multiline is-centered">
      
      <!-- Reparatur-Treff -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-radius: 12px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.05) 0%, rgba(118, 75, 162, 0.05) 100%);">
          <div class="card-content" style="padding: 2.5rem 2rem; text-align: center;">
            <h2 class="title is-3 has-text-weight-bold" style="color: #2c3e50; margin-bottom: 1rem;">
              Reparatur‑Treff
            </h2>
            <h3 class="subtitle is-5 has-text-weight-medium" style="color: #34495e; margin-bottom: 1.5rem;">
              Unregelmäßig, ehrenamtlich & nachhaltig
            </h3>
            <div class="content" style="color: #5a6c7d; line-height: 1.6; margin-bottom: 2rem;">
              <p>Gemeinsam reparieren statt wegwerfen. Ehrenamtliche unterstützen beim Analysieren und Reparieren defekter Alltagsgeräte.</p>
            </div>
            <a href="/termine/reparatur-treff/" 
               class="button is-primary is-medium is-rounded has-text-weight-semibold"
               style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border: none;">
              Details erfahren
            </a>
          </div>
        </div>
      </div>

      <!-- Anstehende Termine -->
      <div class="column is-6-desktop is-12-tablet">
        <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-radius: 12px;">
          <div class="card-content" style="padding: 2.5rem 2rem; text-align: center;">
            <h2 class="title is-3 has-text-weight-bold" style="color: #2c3e50; margin-bottom: 1rem;">
              Anstehende Termine
            </h2>
            <h3 class="subtitle is-5 has-text-weight-medium" style="color: #34495e; margin-bottom: 1.5rem;">
              Veranstaltungen und Treffen
            </h3>
            <div class="content" style="color: #5a6c7d; line-height: 1.6;">
              {% if upcoming and upcoming.size > 0 %}
                <p><strong>Kommende Veranstaltungen:</strong></p>
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
                <p><em>In unseren Telegram-Kanälen ist aber immer etwas los!</em></p>
              {% endif %}
            </div>
            <div class="has-text-centered" style="margin-top: 2rem;">
              <a href="/austausch/" class="button is-primary is-medium is-rounded has-text-weight-semibold">
                Zu den Kanälen
              </a>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- Detaillierte Termine (falls vorhanden) -->
{% if upcoming and upcoming.size > 0 %}
<section class="section" style="padding: 2rem 1.5rem 4rem;">
  <div class="container">
    <h2 class="title is-4 has-text-centered" style="color: #2c3e50; margin-bottom: 2rem;">
      Alle anstehenden Termine
    </h2>
    <div class="columns is-multiline is-centered">
      {% for e in upcoming %}
        <div class="column is-4-desktop is-6-tablet is-12-mobile">
          <div class="card modern-card" style="height: 100%; box-shadow: 0 4px 20px rgba(0,0,0,0.1); border-radius: 12px; transition: all 0.3s ease;">
            <div class="card-content" style="padding: 2rem 1.5rem; height: 100%; display: flex; flex-direction: column;">
              <div style="flex-grow: 1;">
                <h3 class="title is-5 has-text-weight-bold" style="color: #2c3e50; margin-bottom: 0.5rem;">
                  <a href="{{ e.url }}" style="color: #2c3e50; text-decoration: none;">{{ e.title }}</a>
                </h3>
                {% if e.date %}
                  <p class="subtitle is-6 has-text-weight-medium" style="color: #667eea; margin-bottom: 1rem;">
                    {{ e.date | date: "%d.%m.%Y" }}
                  </p>
                {% endif %}
                {% if e.location %}
                  <p class="is-size-7" style="color: #5a6c7d; margin-bottom: 1rem;">
                    📍 {{ e.location }}
                  </p>
                {% endif %}
                {% if e.excerpt %}
                  <div class="content is-size-7" style="color: #5a6c7d; line-height: 1.5;">
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
                <h3 class="title is-6 has-text-weight-semibold" style="color: #34495e; margin-bottom: 0.5rem;">
                  <a href="{{ e.url }}" style="color: #34495e; text-decoration: none;">{{ e.title }}</a>
                </h3>
                {% if e.date %}
                  <p class="subtitle is-7 has-text-weight-medium" style="color: #5a6c7d; margin-bottom: 0.75rem;">
                    {{ e.date | date: "%d.%m.%Y" }}
                  </p>
                {% endif %}
                {% if e.excerpt %}
                  <div class="content is-size-7" style="color: #5a6c7d; line-height: 1.4;">
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