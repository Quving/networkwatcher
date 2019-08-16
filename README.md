# Networkwatcher


## Description

This repository contains scripts to monitor your current network (what ever through which network interface) in respect of reponse-time and package-loss.


## Instructions

### Record your network
To do that, you have to record first.

``` python record.py. ```

That command creates a txt-file with the naming pattern record_YYYY-MM-DD.txt.

### Visualize the records.

``` python plot.py record_YYYY-MM-DD.txt ```