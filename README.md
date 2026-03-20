# Lab DA-2: Publish-Subscribe System with MQTT Message Broker

This repository contains a complete MQTT publish-subscribe lab setup using:

- Node-RED for publishers, subscribers, and dashboard
- Eclipse Mosquitto as the MQTT message broker
- A Smart Campus Monitoring use case

## System Overview

The system models two campus sensor publishers:

- `campus/blockA/temperature`
- `campus/blockB/humidity`

It also publishes retained device status messages on:

- `campus/blockA/status`
- `campus/blockB/status`

The wildcard subscriber listens to:

- `campus/+/status`

The dashboard visualizes live temperature, humidity, and device status.

## Repository Structure

- `flows/smart-campus-mqtt.json` - importable Node-RED flow
- `logs/sample-mqtt-log.txt` - sample message log for submission
- `report.md` - markdown report for PDF export
- `docker-compose.yml` - local Mosquitto broker setup
- `mosquitto/mosquitto.conf` - broker configuration
- `assets/flow-diagram.svg` - illustrative flow diagram
- `assets/dashboard-mockup.svg` - illustrative dashboard mockup

## Prerequisites

- Node.js
- Node-RED
- Docker Desktop

Node-RED dashboard package:

```powershell
npm install -g node-red
cd $env:USERPROFILE\.node-red
npm install node-red-dashboard
```

## Run the MQTT Broker

From this repository:

```powershell
docker compose up -d
```

This starts Mosquitto on `localhost:1883`.

## Run Node-RED

Start Node-RED:

```powershell
node-red
```

Then open:

- Editor: [http://127.0.0.1:1880](http://127.0.0.1:1880)
- Dashboard: [http://127.0.0.1:1880/ui](http://127.0.0.1:1880/ui)

## Import the Flow

1. Open the Node-RED editor.
2. Click the menu in the top-right.
3. Choose `Import`.
4. Open `flows/smart-campus-mqtt.json`.
5. Click `Import`, then `Deploy`.

## What the Flow Demonstrates

### Publishers

- Publisher 1 sends temperature data every 5 seconds with QoS 1.
- Publisher 2 sends humidity data every 7 seconds with QoS 2.
- Two status publishers send retained `online` messages for each block.

### Subscribers

- Dedicated subscribers listen to temperature and humidity topics.
- A wildcard subscriber listens to `campus/+/status`.

### Dashboard

- Temperature gauge and chart
- Humidity gauge and chart
- Text widgets for Block A and Block B status

## QoS and Retained Messages

- QoS 1 is used for temperature data to show at-least-once delivery.
- QoS 2 is used for humidity data to show exactly-once delivery.
- Retained messages are used on status topics so new subscribers immediately receive the latest online state.

## Submission Notes

Before final submission, capture:

1. A real screenshot of the imported Node-RED flow
2. A real screenshot of the dashboard while messages are updating
3. A short terminal/debug log showing:
   - `campus/blockA/temperature`
   - `campus/blockB/humidity`
   - `campus/blockA/status` or `campus/blockB/status`

You can use `report.md` as the source for your PDF submission in VTOP.
