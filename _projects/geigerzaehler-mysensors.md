---
layout: page
title: Geigerzähler mit MySensors-Anbindung
permalink: /projekte/elektronik-sensoren/geigerzaehler-mysensors/
excerpt: Bauanleitung für einen Geigerzähler mit SBM-20 Zählrohr und MySensors-Integration
category: Elektronik & Sensoren
---

<picture>
            <source type="image/webp" srcset="/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_fertig.webp">
            <img src="/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_fertig.jpg" alt="Geigerzähler mit SBM-20 Zählrohr - Fertig aufgebaut" class="title-image">
          </picture>

## Geigerzähler mit Anbindung als MySensors-Node

Heute soll es um ein Projekt gehen, dass den Elektroniker oder die Elektronikerin in uns weckt. Seit Tschernobyl und Fukushima weiß eigentlich jeder im Großen und Ganzen, was ein Geigerzähler ist.

Bis vor einiger Zeit war die private Beschaffung oder der Bau eines Geigerzählers für die meisten uninteressant und unrentabel. Die Ereignisse in Fukushima haben das Interesse an der Realisierung eines eigenen Geigerzählers steigen lassen. Eine große Anzahl privater Geigerzähler haben in der Gegend von Fukushima geholfen, valide Messergebnisse der Strahlenbelastung neben den staatlichen Messungen und den Messungen von Tepco zu sammeln.

Die Basics über die generelle Funktionsweise eines Geigerzählers bzw. der darin eingesetzten Geiger-Müller-Zählröhren lasse ich hier weg. Wer sich darüber informieren möchte, dem empfehle ich diese tolle Webseite zum Thema: [http://einstlab.web.fc2.com/geiger/geiger.html](http://einstlab.web.fc2.com/geiger/geiger.html) (Die Webseite ist in japanisch verfasst. Eine Übersetzung per Browser reicht zum Verständnis weitgehend aus).

Das Projekt stützt sich auf die Arbeiten von Jeff Keyzer ([https://mightyohm.com/blog/products/geiger-counter/](https://mightyohm.com/blog/products/geiger-counter/)).

Ich habe die Schaltung in einer robusten und universellen Platinenanordnung für das Geiger-Müller-Zählrohr SBM-20 aus russischer Produktion realisiert. Die SBM-20 ist eine Zählrohr zur Detektion von Beta- und Gamma-Strahlung und arbeitet mit einer Betriebsspannung von 400V. Der Impulsausgang mit 5V TTL-Pegel kann direkt an einem Digital I/O eines Arduino angeschlossen werden.

![Datenblatt der SBM-20](/assets/images/projekte/elektronik-sensoren/geigerzaehler/Datenblatt_SBM20.jpg)

Schaltung und Platine wurde in KiCAD realisiert und stehen als ZIP-Archiv zu Verfügung.

**Downloads:**
- [Geigerzähler KiCAD-Dateien](/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_KiCAD.zip)
- [Bauteilliste (BOM)](/assets/images/projekte/elektronik-sensoren/geigerzaehler/BOM.ods)

Die Originalschaltung ist relativ unspektakulär und besteht aus zwei funktionellen Abschnitten. Zum einen die Hochspannungserzeugung für das Zählrohr per 555-basierender Flyback-Treiber-Schaltung und zum anderen der Impulsformer für die Ausgabe der Zählimpulse im 5V TTL-Pegel.

> **⚠️ Wichtiger Hinweis:**  
> Die Schaltung arbeitet mit einer Hochspannung von 400V! Die Hochspannungserzeugung ist in der Lage, noch wesentlich höhere Spannungen zu generieren! Auch wenn die Schaltung keine signifikanten Ströme bereitstellen kann, ist dennoch mit Vorsicht bei der Inbetriebnahme und während des Betriebes zu arbeiten! Die angegebenen Bauteilwerte, vor allem hinsichtlich der Spannungsbelastbarkeit sind unbedingt einzuhalten und nur die Bauteile aus der Stückliste sind zu verwenden!

## Aufbau und Inbetriebnahme

Die Platine wird in der Reihenfolge Widerstände, Dioden, Kondensatoren, Transistoren, IC, Trimmpoti, Spule und Steckverbinder bestückt. Wichtig: Die SBM-20 wird jetzt noch nicht montiert.

Zur Inbetriebnahme (immer noch ohne SBM-20!) wird die Betriebsspannung von 5V (+5V an Pin 1 von J3, Masse an Pin 3 von J3) angelegt. Als nächstes wird über das Trimmpoti VR1 die Hochspannung zur Versorgung der SBM-20 auf 400V eingestellt.

Dazu einige Hinweise:  
Die Hochspannungsschaltung ist dafür ausgelegt, die SBM-20 (Innenwiderstand von rund 1GOhm) zu versorgen. Ein Multimeter hat im Spannungsmessbereich gewöhnlich einen Eingangswiderstand von rund 1MOhm bis 10MOhm. Wird das Multimeter direkt mit Testpunkt TP1 verbunden, ergeben sich grobe Messfehler. Die 10MOhm Eingangswiderstand meines, für die Messung genutzten, UNI-T61D-Multimeters reichen als Last aus, die Hochspannungserzeugung auf einen Wert von ca. 200-260V zusammen-brechen zu lassen. Um die Hochspannung fehlerfrei zu messen, ist ein 1GOhm-Widerstand in Reihe zum Multimeter zu schalten.

![Messung und Einstellen der Hochspannung für die SBM-20 mit einem Multimeter](/assets/images/projekte/elektronik-sensoren/geigerzaehler/Spannungsteiler_erklärt.png)

Wenn ihr diesen Schritt des Hochspannungsabgleiches nicht selbst durchführen wollt, unterstützen Euch Leute im Makerspace gern bei dieser Arbeit.

Ist die Hochspannung auf 400V eingestellt, kann jetzt die SBM-20 eingesetzt werden. Dazu die Schaltung unbedingt von der Versorgungsspannung abklemmen und die Polung der SBM-20 beachten (die Anode ist meist mit einem "+"-Symbol markiert).

![Pinbelegung und Lage der Testpunkte](/assets/images/projekte/elektronik-sensoren/geigerzaehler/Geigerzähler_Anschluss.jpg)

Ist alles soweit komplett, kann jetzt z.B. mit einem Oszilloskop an TP2 des Steckverbinders J3 gemessen werden, ob Zählimpuls ausgegeben werden. Da mit normaler Umgebungsstrahlung die Ausgabe von Impulsen in langen Abständen erfolgt, kann für eine schnelle Impulsfolge geschummelt werden. Einfach eine Armbanduhr oder einen Wecker, der über, im Dunklen grün leuchtende, Ziffern oder Zeiger verfügt, in ca. 1cm Abstand zu SBM-20 halten und sich über deutlich mehr Impulse freuen.

So, die Schaltung ist soweit fertig. Jetzt muss die Messung des Geigerzählers als Umweltsensor auswertbar gemacht werden. Ich bin großer Fan des [MySensors](http://www.mysensors.org)-Ökosystems. Einen Arduino-Sketch zur MySensors-Integration des Geigerzählers findet ihr im ZIP-Archiv.
