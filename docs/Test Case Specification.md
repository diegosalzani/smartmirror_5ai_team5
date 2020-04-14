# Test Case Specification

# For

# Team 5

## April 1st, 2020

## Prepared by:

### Diego Salzani


## Revision History

### Version Date Name Description

```
1 1/4/20 Salzani Diego Initial Document
```

## 1 Introduction

This document provides the test cases to be carried out for the Smart Mirror Application. Each item to be
tested is represented by an individual test case. Each case details the situations and expected outputs.

## 2 Test Cases: Smart Mirror

```
Test ID 2.
Title Powering on
Feature Smart Mirror connects to the server.
Objective Showing the right infos on the mirror
Setup The code is already installed in the Smart Mirror
Test Data Location
Time-zone
Weather
Test Actions 1. Power on Smart Mirror
```
2. Select current location
Expected Results The mirror shows the data requested: Time, Weather, School
schedule and News.

```
Test ID 2.
Title Couldn’t connect to the server
Feature Smart Mirror can’t get infos from the server
Objective Check if an internet connection is avabile
Setup Every cable is properly pugged in
Test Data Server address
Test Actions 1. Try to connect to the server
```
2. No reply from the server
Expected Results Shows an error of connection message


```
Test ID 2.
Title Incorrect location
Feature Smart mirror shows infos of an incorrect location
Objective Confirm if the user is using a VPN service
Setup Every cable is properly pugged in and connected to the internet
Test Data User location
Test Actions 1. Try to restart the smart mirror
```
2. Showing incorrect values

Expected Results An option to manually set location is shown


