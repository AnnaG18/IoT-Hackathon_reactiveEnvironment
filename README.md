# IoT-Hackathon

## ToDo

* Projekt Name
* Hackathon Vorbesprehung
* Einarbeitung in die verschiedenen Technologien

## Table of contents

1. [Project goal](#Project-goal)
2. [Service Design](#Service-Design)
3. [Organization](#Organization)
4. [MVP](#MVP)
5. [Architecture](#Architecture)
6. [Implementation](#Implementation)
7. [IoT-Methods](#IoT-Methods)
8. [Outlook](#Outlook)
9. [Presentation](#Presentation)

## Project goal

A service utilizing beacon technology providing additional value for students and lecturers at Herman Hollerith Centre shall be designed and a MVP implemented.

## Service Design

## Organization

Das Team besteht aus folgenden Personen:

* Anna Gorr
* Johannes Wanner
* Natascha Sigle
* Peter Kühfuß

## MVP

Nach der teilweisen Implementierung des Service Design wurden im Herman Hollerith Zentrum ein Controller, ein Gateway sowie ein Sensorknoten, der Temperatur und Feuchtigkeit im Raum 125 misst, installiert.
Die MVP besteht nun darin, dass eine ganzheitliche Verbindung zwischen den einzelnen Komponenten hergestellt wird. Die Umgebungsqualität soll anhand einer Lampe farblich dargestellt werden können.

Außerdem dreht es sich um die Regelerstellung zur Umsetzung verschiedener Use Cases. Beispielweise könnte ein Use Case die farbliche Änderung einer Glühbirne von rot auf blau sein, wenn die Raumtemperatur von warm auf kalt umschwnenkt. Dazu muss bei der Regelerstellung dann eine Temperaturgrenze definiert werden. Daher ist es wichtig, dass man weiß, welcher Sensor oder welche Komponente welchen Werte rückmeldet.

## Architecture

### Used hardware

* Controller: Raspberry Pi 3 running Home-Assistant (0.35.3) on Raspbian Jessie Lite (Kernel 4.4)
* Gateway and Sensors: Arduino Nano (xcsource clone)
* Radio module: NRF24L01+
* Air/Humidity sensor: DHT-22

## Implementation

## IoT Methods

### IoT Design Principles

Designing an IoT architecture we followed the design principles stated in the IoT lecture:

* Invisibility: The sensor network is not visible and no user interaction is needed.
* Manual override: A manual override is neither applicable nor necessary in this case.
* Feedback: Sensor data can be monitored using the web UI or visuell Feedback.

## Outlook

## Presentation
