---
title: Weather Station
start_date: 2022-06-01
end_date: 2022-12-01
---

I wanted to try my hand at more hardware projects and thought a weather station
would be a good starting point. The idea was that the weather station would
collect data like temperature and humidity and report it to a server which would
finally display it in some charts on a website.

This was still during the COVID-era Raspberry Pi shortage, so the only thing I
could get my hands on at the time were Picos. These did not have Wi-Fi on board,
so I also managed to find a guide to link a Pico to an ESP32 Wi-Fi coprocessor.
I thought I would also take this as a chance to practice my soldering. I did not
do a good job at this, so much so I ended up destroying the Pico and had to buy
another one.

Eventually, I did get everything soldered and wired up on a breadboard. I wrote
some code for the Pico to periodically send data to a Cloudflare KV store and a
Worker to list the weather data for the website. Since I wanted the worker to
list all the data in reverse chronological order while only using a single API
call to the KV store, I ended up writing a hacky way to send the weather station
payload as metadata and `MAX_INT - currentTime` as the key. 

After that, the whole thing did manage to work for a little bit. Then I got
stuck trying to weather-proof my setup. Shortly after, the Pico stopped
communicating with the ESP32 coprocessor again which I'm pretty sure was a
result of my less-than-stellar soldering ability (or me frying some part of the
Pico by passing more than 5V into it). I tried to debug it with a multimeter,
but I did not really know what I was doing due to a severe lack of electronics
experience. This was also not helped much by the fact that the multimeter was in
Chinese.

At this point, I got very fed up with the whole thing and called it done.