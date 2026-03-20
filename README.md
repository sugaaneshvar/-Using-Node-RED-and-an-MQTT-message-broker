# Lab DA-2 Report

## Title

Publish-Subscribe System with MQTT Broker using Node-RED

## Student Details

| Field | Value |
| --- | --- |
| Student Name | Suganeshvar |
| Register Number | 21MID0128 |
| Done By | 21MID0128 Suganeshvar |

## Use Case

This project implements a Smart Campus Monitoring system using the MQTT publish-subscribe model. Two publishers simulate IoT sensors deployed in different campus blocks:

- Block A temperature sensor
- Block B humidity sensor

The MQTT broker forwards messages to subscribers based on topic names. A wildcard subscriber is used for device status topics, and a live dashboard shows the current sensor values.

## Topics Used

- `campus/blockA/temperature`
- `campus/blockB/humidity`
- `campus/blockA/status`
- `campus/blockB/status`

Wildcard subscription:

- `campus/+/status`

## Publisher and Subscriber Roles

- The temperature publisher sends temperature readings to `campus/blockA/temperature`.
- The humidity publisher sends humidity readings to `campus/blockB/humidity`.
- Two status publishers send `online` messages to their status topics.
- Subscribers receive messages from the broker without directly communicating with publishers.
- The wildcard subscriber receives status messages from both blocks using one subscription pattern.

## QoS Demonstration

- Temperature messages use QoS 1, which provides at-least-once delivery.
- Humidity messages use QoS 2, which provides exactly-once delivery.
- This shows that the broker can route messages with different delivery guarantees.

## Retained Messages

Retained messages are used only for the status topics. This ensures that when a new subscriber connects, it immediately receives the latest `online` status message, even if that message was published before the subscriber connected.

QoS controls delivery guarantee, while retained messages control whether the latest broker-stored message is sent to future subscribers.

## Wildcard Explanation

The wildcard subscriber uses:

`campus/+/status`

The `+` wildcard matches exactly one topic level, so it matches:

- `campus/blockA/status`
- `campus/blockB/status`

This allows one subscriber to monitor status updates from multiple campus blocks.

## Short Log

See [logs/sample-mqtt-log.txt](/C:/Users/19138/Downloads/Distributed%20system/logs/sample-mqtt-log.txt).

Example topics shown in the log:

- `campus/blockA/temperature`
- `campus/blockB/humidity`
- `campus/blockA/status`

## Screenshots

Save your screenshots in the `assets` folder with the following names so they appear correctly in the report:

- `flow-screenshot.png`
- `dashboard-temperature.png`
- `dashboard-humidity-status.png`

### Final Node-RED Flow

![Node-RED Flow](assets/flow-screenshot.png)

### Dashboard Temperature View

![Dashboard Temperature](assets/dashboard-temperature.png)

### Dashboard Humidity and Status View

![Dashboard Humidity and Status](assets/dashboard-humidity-status.png)

## Video Demonstration Talking Points

### 1. Pub/Sub roles in the flow

- Publishers send data to the broker on specific topics.
- Subscribers receive data from the broker by subscribing to topics.
- The broker decouples senders from receivers.

### 2. How wildcards worked

- The wildcard subscriber used `campus/+/status`.
- One subscriber listened to both Block A and Block B status topics.

### 3. QoS vs retained messages

- QoS defines delivery guarantee between publisher, broker, and subscriber.
- Retained messages store the latest topic value in the broker.
- In this system, QoS 1 and QoS 2 were used for sensor data, while retained messages were used for status.

## Conclusion

The experiment successfully demonstrates an MQTT-based publish-subscribe system with multiple publishers, a wildcard subscriber, and a live dashboard using Node-RED.
