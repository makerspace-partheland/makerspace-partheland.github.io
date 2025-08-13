---
title: Sächsischer Familientag 2024 in Brandis
date: 2024-08-17
location: Stadtpark Brandis, 04821 Brandis
excerpt: Rückblick auf unseren Stand mit Löt‑Workshops, 3D‑Druck und Umweltmessstation.
permalink: /termine/saechsischer-familientag-2024-08-17/
---
## Sächsischer Familientag 2024 in Brandis

> Dieser Blogeintrag wurde mit Unterstützung einer KI-basierten Assistenztechnologie erstellt. Sie half dabei, die gesammelten Daten zu analysieren und die Inhalte dieses Beitrags zu formulieren.
Am 17. August 2024 war der Makerspace Partheland e.V. stolz darauf, am Sächsischen Familientag in Brandis teilzunehmen. Dieser besondere Tag brachte Familien aus ganz Sachsen zusammen, um gemeinsam zu feiern und sich über verschiedene Initiativen und Projekte zu informieren.

Mit unserem Stand hatten wir wieder die Gelegenheit, für unsere Sache zu werben, Wissen zu teilen und das Mitmachen anzuregen. Neben vielen Teilnehmern an spontanen kleinen Lötworkshops und zahlreichen Interessenten am Thema 3D-Druck und Künstliche Intelligenz (zum Beispiel <https://github.com/nomic-ai/gpt4all>), präsentierten wir auch das Thema Umweltmessstationen im Partheland. Besonders hervorzuheben war unsere Umweltmessstation, die wir vor Ort aufgebaut hatten. Diese Station ist Teil unseres Smart-City-Projekts und nutzt LoRaWAN-Technologie, um verschiedene Umweltparameter zu erfassen und zu übertragen. Weitere Informationen zu diesem Projekt auf unserer Webseite [hier](/projekte/smart-city/) und [hier](/projekte/smart-city/warum-lora-statt-wifi/).

Während des Familientags haben unsere Sensoren kontinuierlich Daten gesammelt, [die nun in unserer Datenbank gespeichert sind](https://sensoren.makerspace-partheland.de/d/erweVEQnG/demostation-des-makerspace?orgId=3&from=1723881600000&to=1723906800000). Die Temperaturdaten zeigen, dass es ein heißer Tag war, mit Temperaturen, die von 25,9°C am Morgen bis zu 34,3°C am Nachmittag reichten. Die relative Luftfeuchtigkeit begann bei etwa 59,5% am Morgen und sank im Laufe des Tages auf einen Tiefstwert von 41,4% am Nachmittag. Die Beleuchtungsstärke war ebenfalls hoch, mit Spitzenwerten von bis zu 9.931 Lux um die Mittagszeit. Die UV-Intensität erreichte Spitzenwerte von bis zu 618 μW/cm² um die Mittagszeit, was auf eine starke Sonneneinstrahlung hinweist. Der Luftdruck blieb den ganzen Tag über relativ stabil und schwankte nur minimal zwischen 996 und 998 hPa. Die Lautstärke zeigte deutliche Schwankungen, mit Spitzenwerten von bis zu 93,1 dB am Nachmittag, was auf die lebhafte und fröhliche Atmosphäre des Events hinweist. Die Feinstaubbelastung (PM2.5 [2,5 µm]) zeigte ebenfalls Schwankungen, mit Spitzenwerten von bis zu 61,9 µg/m³ um die Mittagszeit, was auf eine ungesunde Luftqualität für empfindliche Gruppen hinweist. Die Feinstaubbelastung (PM10 [10 Mikrometer]) zeigte ebenfalls Schwankungen, mit Spitzenwerten von bis zu 134 µg/m³ um die Mittagszeit, was auf intensive Aktivitäten wie Grillen oder eine hohe Besucherzahl hinweisen könnte.

Diese Bedingungen waren typisch für einen heißen Sommertag und beeinflussten sicherlich das Wohlbefinden der Besucher.

### Zusammengefasste Übersicht der analysierten Daten

#### Einführung in die Datenanalyse

Bevor wir in die detaillierte Analyse der Sensordaten eintauchen, ist es wichtig, einige grundlegende Begriffe zu klären:

- Median: Der Median ist der mittlere Wert einer geordneten Datenreihe. Er teilt die Daten in zwei Hälften, wobei 50% der Werte unterhalb und 50% oberhalb des Medians liegen. Der Median ist besonders nützlich, um Ausreißer zu minimieren und ein repräsentatives Bild der Daten zu erhalten.
- Maximalwert: Der Maximalwert ist der höchste gemessene Wert in einem bestimmten Zeitraum. Er gibt Aufschluss über die extremsten Bedingungen, die während des Zeitraums aufgetreten sind.

#### Sensoreinheiten

- Temperatur: Grad Celsius (°C)
- Relative Luftfeuchtigkeit: Prozent (%)
- Beleuchtungsstärke: Lux (lx)
- UV-Intensität: Mikrowatt pro Quadratzentimeter (μW/cm²)
- Luftdruck: Hektopascal (hPa)
- Lautstärke: Dezibel (dB)
- Feinstaub PM2.5 und PM10: Mikrogramm pro Kubikmeter Luft (µg/m³)

#### Morgenstunden (10:00 – 12:00 Uhr)

- **Temperatur**
  - Median: 28,6°C
  - Maximal: 31,3°C um 11:59 Uhr
  - **Beurteilung**: Die Temperaturen waren am Morgen angenehm und stiegen allmählich an, was auf einen sonnigen Start in den Tag hinweist. Besucher konnten die frische Morgenluft genießen, bevor die Hitze des Tages einsetzte.
- **Relative Luftfeuchtigkeit**
  - Median: 54,3%
  - Maximal: 59,5% um 10:00 Uhr
  - **Beurteilung**: Die Luftfeuchtigkeit war am Morgen relativ hoch, was typisch für die frühen Stunden eines Sommertages ist. Dies könnte das Wohlbefinden der Besucher leicht beeinträchtigt haben, insbesondere bei körperlicher Aktivität.
- **Beleuchtungsstärke**
  - Median: 6.298 Lux
  - Maximal: 7.275 Lux um 11:30 Uhr
  - **Beurteilung**: Die Lichtverhältnisse waren hell und klar, was auf einen sonnigen Morgen hinweist. Dies schuf eine angenehme Atmosphäre für die Besucher, die die verschiedenen Stände und Aktivitäten erkunden konnten.
- **UV-Intensität**
  - Median: 376 μW/cm²
  - Maximal: 416 μW/cm² um 11:45 Uhr
  - **Beurteilung**: Die UV-Intensität war moderat, was auf eine zunehmende Sonneneinstrahlung hinweist. Besucher sollten sich bewusst sein, Sonnenschutz zu verwenden, um Hautschäden zu vermeiden.
- **Luftdruck**
  - Median: 998 hPa
  - Maximal: 998 hPa
  - **Beurteilung**: Der Luftdruck blieb stabil, was auf ruhige Wetterbedingungen ohne signifikante Änderungen hinweist.
- **Lautstärke**
  - Median: 67 dB
  - Maximal: 89,1 dB um 10:31 Uhr
  - **Beurteilung**: Die Geräuschkulisse war lebhaft, vergleichbar mit starkem Straßenverkehr oder einem lauten Restaurant. Dies deutet auf eine hohe Besucherzahl und viele Aktivitäten hin.
- **Feinstaub PM2.5**
  - Median: 8,4 µg/m³
  - Maximal: 45,5 µg/m³ um 10:47 Uhr
  - **Beurteilung**: Die Luftqualität war größtenteils gut, mit einigen Spitzenwerten, die auf Aktivitäten wie das Anzünden von Grillständen oder das Rauchen in der Nähe des Sensors hinweisen könnten. Diese Spitzenwerte könnten auch durch die erhöhte Besucherzahl und deren Aktivitäten verursacht worden sein.
- **Feinstaub PM10**
  - Median: 9,1 µg/m³
  - Maximal: 93,5 µg/m³ um 10:47 Uhr
  - **Beurteilung**: Die Luftqualität war größtenteils gut, mit einigen hohen Werten, die auf intensive Aktivitäten hinweisen könnten. Diese Spitzenwerte könnten durch das Anzünden von Grillständen, das Rauchen oder durch die erhöhte Besucherzahl verursacht worden sein.

#### Mittagszeit (12:00 – 14:00 Uhr)

- **Temperatur**
  - Median: 32,1°C
  - Maximal: 32,9°C um 12:29 Uhr
  - **Beurteilung**: Die Temperaturen erreichten zur Mittagszeit ihren Höhepunkt, was typisch für einen heißen Sommertag ist. Besucher sollten sich in den Schatten begeben und ausreichend Flüssigkeit zu sich nehmen, um Überhitzung zu vermeiden.
- **Relative Luftfeuchtigkeit**
  - Median: 52,2%
  - Maximal: 55,6% um 13:00 Uhr
  - **Beurteilung**: Die Luftfeuchtigkeit blieb moderat, was das Gefühl der Hitze verstärken könnte. Besucher sollten darauf achten, sich regelmäßig abzukühlen.
- **Beleuchtungsstärke**
  - Median: 8.603 Lux
  - Maximal: 9.931 Lux um 12:15 Uhr
  - **Beurteilung**: Die Lichtverhältnisse waren sehr hell, was auf eine starke Sonneneinstrahlung hinweist. Dies schuf eine lebendige und energiegeladene Atmosphäre, aber Besucher sollten Sonnenschutz verwenden.
- **UV-Intensität**
  - Median: 517 μW/cm²
  - Maximal: 618 μW/cm² um 12:22 Uhr
  - **Beurteilung**: Die UV-Intensität war hoch, was auf eine starke Sonneneinstrahlung hinweist. Besucher sollten sich bewusst sein, Sonnenschutz zu verwenden, um Hautschäden zu vermeiden.
- **Luftdruck**
  - Median: 997 hPa
  - Maximal: 997 hPa
  - **Beurteilung**: Der Luftdruck blieb stabil, was auf ruhige Wetterbedingungen ohne signifikante Änderungen hinweist.
- **Lautstärke**
  - Median: 68 dB
  - Maximal: 90,7 dB um 13:28 Uhr
  - **Beurteilung**: Die Geräuschkulisse war hoch, vergleichbar mit einem Rasenmäher oder einem lauten Restaurant. Dies deutet auf eine hohe Besucherzahl und viele Aktivitäten hin.
- **Feinstaub PM2.5**
  - Median: 18,4 µg/m³
  - Maximal: 61,9 µg/m³ um 13:48 Uhr
  - **Beurteilung**: Die Luftqualität war moderat bis ungesund für empfindliche Gruppen, mit Spitzenwerten, die auf intensive Aktivitäten hinweisen könnten. Diese Spitzenwerte könnten durch Grillen, eine hohe Besucherzahl oder durch das Kochen und Braten an den Ständen verursacht worden sein.
- **Feinstaub PM10**
  - Median: 42,3 µg/m³
  - Maximal: 134 µg/m³ um 13:48 Uhr
  - **Beurteilung**: Die Luftqualität war moderat bis ungesund für empfindliche Gruppen, mit Spitzenwerten, die auf intensive Aktivitäten hinweisen könnten. Diese Spitzenwerte könnten durch Grillen, eine hohe Besucherzahl oder durch das Kochen und Braten an den Ständen verursacht worden sein.

#### Nachmittags (14:00 – 17:00 Uhr)

- **Temperatur**
  - Median: 33,2°C
  - Maximal: 34,3°C um 15:17 Uhr
  - **Beurteilung**: Die Temperaturen blieben am Nachmittag sehr hoch, was typisch für einen heißen Sommertag ist. Besucher sollten sich in den Schatten begeben und ausreichend Flüssigkeit zu sich nehmen, um Überhitzung zu vermeiden.
- **Relative Luftfeuchtigkeit**
  - Median: 45,2%
  - Maximal: 49,1% um 14:00 Uhr
  - **Beurteilung**: Die Luftfeuchtigkeit war niedriger als am Morgen, was das Gefühl der Hitze etwas mildern könnte. Besucher sollten darauf achten, sich regelmäßig abzukühlen.
- **Beleuchtungsstärke**
  - Median: 7.830 Lux
  - Maximal: 8.605 Lux um 13:26 Uhr
  - **Beurteilung**: Die Lichtverhältnisse blieben hell, was auf eine starke Sonneneinstrahlung hinweist. Dies schuf eine lebendige und energiegeladene Atmosphäre, aber Besucher sollten Sonnenschutz verwenden.
- **UV-Intensität**
  - Median: 452 μW/cm²
  - Maximal: 483 μW/cm² um 14:19 Uhr
  - **Beurteilung**: Die UV-Intensität war hoch, was auf eine starke Sonneneinstrahlung hinweist. Besucher sollten sich bewusst sein, Sonnenschutz zu verwenden, um Hautschäden zu vermeiden.
- **Luftdruck**
  - Median: 996 hPa
  - Maximal: 996 hPa
  - **Beurteilung**: Der Luftdruck blieb stabil, was auf ruhige Wetterbedingungen ohne signifikante Änderungen hinweist.
- **Lautstärke**
  - Median: 70 dB
  - Maximal: 93,1 dB um 16:13 Uhr
  - **Beurteilung**: Die Geräuschkulisse war sehr hoch, vergleichbar mit einem Motorrad oder einem Konzert. Dies deutet auf eine lebhafte und fröhliche Atmosphäre hin.
- **Feinstaub PM2.5**
  - Median: 14,3 µg/m³
  - Maximal: 25,9 µg/m³ um 16:22 Uhr
  - **Beurteilung**: Die Luftqualität war größtenteils gut, mit einigen Spitzenwerten, die auf Aktivitäten wie Anzünden von Grillständen, Rauchen oder durch Kochen und Braten an den Ständen hinweisen könnten.
