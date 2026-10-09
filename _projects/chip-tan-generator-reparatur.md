---
layout: page
title: Chip-TAN-Generator Reparatur und Mod
permalink: /projekte/reparatur-nachhaltigkeit/chip-tan-generator-reparatur/
excerpt: Ein KOBIL-Chip-TAN-Generator mit fehlerhafter Displayanzeige wird auf USB-Stromversorgung umgebaut.
category: Reparatur & Nachhaltigkeit
gallery:
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/head_1.jpg
    alt: Auf dem Display fehlen Teile der Zeichen.
    caption: Unvollständige Displayzeichen
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/head_2.jpg
    alt: Die Aufforderung zum Einstecken der Karte ist nur teilweise lesbar.
    caption: Hinweis zum Einstecken der Karte
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/head_3.jpg
    alt: Auch in der Menüanzeige fehlen Teile der Zeichen.
    caption: Auswahlmenü mit Anzeigefehlern
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_1.jpg
    alt: Die USB-Platine liegt neben dem geöffneten Gerät.
    caption: Geöffnetes Gerät mit USB-Platine
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_2.jpg
    alt: Im offenen Batteriefach ist die Verkabelung zu sehen.
    caption: Verkabelung im Batteriefach
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_3.jpg
    alt: Die USB-Buchse sitzt seitlich im Gehäuse.
    caption: Seitliche USB-Buchse
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_4.jpg
    alt: Das USB-Kabel ist an der seitlichen Buchse angeschlossen.
    caption: Angeschlossenes USB-Kabel
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_5.jpg
    alt: Bei angeschlossenem USB-Kabel zeigt das Display „Suche Anfang“.
    caption: Startsuche im USB-Betrieb
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_6.jpg
    alt: Das Display zeigt bei angeschlossenem USB-Kabel das Auswahlmenü.
    caption: Auswahlmenü im USB-Betrieb
  - image_path: /assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/Back.jpg
    alt: Die abgenommene Rückwand liegt neben der freigelegten Platine.
    caption: Rückwand und freigelegte Platine
---

<picture>
            <source type="image/webp" srcset="/assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/head_1.webp">
            <img src="/assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/head_1.jpg" alt="Auf dem Display fehlen Teile der Zeichen." class="title-image" style="object-position: center 15%;">
          </picture>

## KOBIL Chip-TAN-Generator: Reparatur und USB-Umbau

Für Banküberweisungen unterwegs wurde ein zweiter optischer Chip-TAN-Generator von KOBIL gesucht. Im Internet waren mehrere Geräte günstig als defekt angeboten. Häufig waren Buchstaben und Zahlen auf dem Display kaum noch lesbar. Auch das für dieses Projekt beschaffte Gerät hatte diesen Fehler: Am Displaykabel bestand ein Kontaktproblem.

### Teil 1: Displayreparatur

#### Gehäuse öffnen

Zuerst werden die vier Schrauben der Rückwand gelöst, die im Bild gelb markiert sind. Nach dem Abnehmen der Rückwand folgen die beiden blau markierten Schrauben der Kartenführung. Sobald die Kartenführung und die Abdeckung der Fotosensoren entfernt sind, lässt sich die Platine herauskippen.

<div class="columns is-centered">
  <div class="column is-two-thirds-desktop">
    <figure class="card">
      <div class="card-image">
        <div class="image">
          <img src="/assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/Back.webp" alt="Rückwand mit vier gelb markierten Schraubenpositionen und geöffnetes Gerät mit zwei blau markierten Schrauben der Kartenführung." loading="lazy">
        </div>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Schrauben der Rückwand und der Kartenführung</div>
      </figcaption>
    </figure>
  </div>
</div>

#### Kontakt am Displaykabel wiederherstellen

Die Kontaktstellen des Displaykabels an der Platine und am Displayglas müssen wieder verbunden werden. Der markierte Bereich zeigt die Leiterbahnen unterhalb des Displays.

<div class="columns is-centered">
  <div class="column is-one-third-desktop is-half-tablet">
    <figure class="card">
      <div class="card-image">
        <div class="image">
          <img src="/assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/front_blank.webp" alt="Vorderseite der Platine mit markierten Leiterbahnen am unteren Rand des Displays." loading="lazy">
        </div>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Kontaktbereich des Displaykabels</div>
      </figcaption>
    </figure>
  </div>
</div>

Die Kontaktflächen lassen sich auf drei Arten erwärmen:

- **Heißluft:** Das Displayglas vor Hitze schützen, etwa mit einem Metallblättchen. Die Kontaktflächen mit einem Heißluftföhn erwärmen und mit einem Rakel bis zum Abkühlen andrücken. Eine dabei auftretende Verfärbung des Displays sollte nach einer Weile wieder verschwinden.
- **Lötkolben:** Die Kontaktflächen mit einem einstellbaren Lötkolben und einer großflächigen Spitze erwärmen.
- **Heißklebepistole:** Die Kontaktflächen mit der heißen Spitze erwärmen, ohne dabei Klebstoff in das Gerät einzubringen.

Anschließend wird geprüft, ob das Display wieder alle Zeichen anzeigt. Falls weiterhin Zeichen fehlen, wird der Vorgang wiederholt. Zum Einschalten genügt eine passende Plastikkarte oder ein entsprechend zugeschnittenes Stück Pappe. Eine Bankkarte ist für diesen Displaytest nicht nötig.

### Teil 2: USB-Stromversorgung

Das Gerät verwendet normalerweise CR2025-Knopfzellen. Beim beschriebenen Umbau wurde es stattdessen mit 5 V über USB betrieben. Dazu wurde VCC mit V+ und Ground mit V− auf der Platine verbunden.

<div class="columns is-centered">
  <div class="column is-one-third-desktop is-half-tablet">
    <figure class="card">
      <div class="card-image">
        <div class="image">
          <img src="/assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/back_blank.webp" alt="Rückseite der Platine mit gelb markierten Anschlusspunkten V+ und V− neben den Batteriehaltern." loading="lazy">
        </div>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Anschlusspunkte für die Stromversorgung</div>
      </figcaption>
    </figure>
  </div>
</div>

#### Micro-USB-Buchse einbauen

Anstelle eines fest angeschlossenen USB-Kabels kam eine Micro-USB-Buchse auf einer kleinen Platine zum Einsatz. Das Löten einer einzelnen Buchse wurde bei diesem Umbau als zu anstrengend empfunden. Für den Einbau wurden eine seitliche Buchsenöffnung und eine Aussparung für die kleine Platine im Bereich eines Batteriefachs in das Gehäuse geschnitten.

<div class="columns is-centered">
  <div class="column is-two-thirds-desktop">
    <figure class="card">
      <div class="card-image">
        <div class="image">
          <img src="/assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_1.webp" alt="Geöffnetes Gehäuse neben der kleinen Platine mit Micro-USB-Buchse." loading="lazy">
        </div>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Micro-USB-Buchse auf einer separaten Platine</div>
      </figcaption>
    </figure>
  </div>
</div>

Die Leitung zu V+ konnte direkt verlegt werden. Die Leitung zu V− wurde durch die vorhandene Aussparung der Batteriehalterung geführt. Eine zusätzliche kleine Öffnung im rechten Batteriefach schuf den Weg zum Kontakt. Alternativ lassen sich die Leitungen außen um die Batterieaussparungen führen.

<div class="columns is-centered">
  <div class="column is-half-tablet">
    <figure class="card">
      <div class="card-image">
        <div class="image">
          <img src="/assets/images/projekte/reparatur-nachhaltigkeit/chip-tan-generator/usb_2.webp" alt="Leitungen der USB-Stromversorgung im offenen Batteriefach." loading="lazy">
        </div>
      </div>
      <figcaption class="card-content">
        <div class="content is-size-7 has-text-centered">Kabelführung im Batteriefach</div>
      </figcaption>
    </figure>
  </div>
</div>

Für die Tests war die kleine USB-Platine mit Isolierband umwickelt. Nach dem Verlöten wurden Platine und Kabel mit Heißkleber fixiert und die Abdeckung geschlossen. Durch zu langsames Arbeiten blieb eine kleine Unebenheit. Die zusätzliche Fixierung des Kabels verhinderte, dass es beim Schließen der Batterieabdeckung verrutschte.

### Ergebnis

Nach der Displayreparatur und dem USB-Umbau funktionierte das Gerät wieder. Mit ihm wurden anschließend erste Überweisungen durchgeführt.
