---
title: Old
description: Mostly complete projects that I stopped working on.
---

### Weather Station

*Jun 2022 - Dec 2022*

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


### Cartoon Avatar

*Apr 2020 - May 2020*

Early on into the pandemic, I came across a project called
[avatarify](https://github.com/alievk/avatarify-python) which used the power of
ML to let people's facial movements drive static image animation. This would
output a video stream that could then be fed via a virtual OBS camera into Zoom,
allowing you to show up in meetings with a funny avatar controlled by your face.
Live2D Vtubers were also taking off around this time, so I thought to combine
these two and try to make a shitty clone of Live2D in the spirit of avatarify.

My version was much simpler and just used perspective transformations to warp
images for each facial landmark. I then stitched all the images with some
scaling and translation into one and streamed it to an OpenCV window. The window
could then be captured in OBS and output as a virtual webcam, same as avatarify.
When I tested it out in Zoom, it worked terribly since Python (and my computer)
is obscenely slow. I also remember calling my friends with it, and they got
extremely confused, watching a video of a dilapidated Miho lag out on Discord.

Disappointed with the results and having much newfound respect for the quality
of Live2D, I stopped working on this one.


### Kuiperbowl Mobile

*Sep 2019 - Dec 2019*

A native mobile client for my quizbowl platform, Kuiperbowl, and my first foray
into mobile apps. Abandoned after I upgraded Kuiperbowl to v3. I also got tired
of running into build problems with React Native.

### Shiritori Bot

*Jun 2019*

I used to be really into Reddit. I was also really into learning Japanese. These
two interests combined and birthed Shiritori Bot, a bot that would moderate
[shiritori](https://en.wikipedia.org/wiki/Shiritori) games. Players could create
a post with the starting word and the game would be played in chains in the
comments, using Jisho to validate words. I ran it for a while on /r/test but got
really bored playing with myself and stopped working on it.

Side note: I got the crazy idea to put shiritori on the blockchain after this
but then the crypto bros showed up and made me not want to even think about
Ethereum.

### NG Signal Challenge

*Sep 2019 - Oct 2019*

Our team's submission to Northrop's 2019 signal challenge. The goal was to
accurately classify a wide variety of sounds into 27 classes. We tried to do
this by scraping soundbites off Google AudioSet and training ResNet to classify
the waveforms via transfer learning. It did not work.

### It's Ac Caption Dumper

*Jul 2019 - Aug 2019*

[It's Academic](https://en.wikipedia.org/wiki/It's_Academic) (It's Ac) is a
local high school quiz show that the *REEAALLY* good quizbowlers at my high
school got the pleasure to be on. As practice, all quizbowl club members were
conscripted to transcribe an It's Ac game from [CBS
Baltimore](https://baltimore.cbslocal.com/category/its-academic/) into packet
form (which was a painful process since I didn't know about AdBlock at the
time). Later in life, I would imagine an automated process for automatically
transcribing and generating packets from those games which culminated into this
project. Then much later in life, CBS Baltimore would update their site and
break my script which is why this project is now housed here.

### Fortune Cookie ML

*Mar 2019 - Apr 2019*

I tried to make an RNN to classify text as fortune or not fortune. I never did
figure out whether it worked well or not.

### Acorn Identifier

*Oct 2018*

I had found a infographic explaining how to identify different types of acorns
on a Japanese subreddit at one point. I also remember learning about expert
systems in my last year of high school, so I though it would be the perfect
opportunity to try and implement an expert system while trying out my Japanese
translation skills. I think I tried doing it in COBOL originally but realized
that I don't know anything about the language, and ended up switching to pyknow
in Python. At some point, I translated the entire infographic and embedded it in
pyknow. Then I realized no one I knew really cared about identifying acorns, so
I abandoned the project.

### Auto Bongo Cat

*Oct 2018*

Bongo cat videos were all the rage back then. I thought it would be cool if I
could take songs and automatically generate bongo cat videos for them by
detecting the beats. It didn't really work. I don't know much about music or
signals, so I gave up.

### Emergency Vehicle Finder

*Sep 2018 - Nov 2018*

Our team's submission to Northrop's 2018 image classification challenge. I did
not know how to do deep learning at the time, so we used traditional CV with
Haar classifiers. It did not work.

### CMSC Undergrad Calendar

*Sep 2018*

I've already written a blog post about this one on my main site. The gist of it
was that the UMD undergrad CS department's calendar was a nightmare to navigate
and did not mirror to a Google Calendar. I wrote some really ass Selenium to
scrape it into Google Calendar, got murdered in September by DST, lived to tell
the tale, and then promptly gave up working on the scraper soon afterwards
because I couldn't (and probably still can't) understand Google OAuth.

### Falling Words

*Aug 2018*

I made a physics demo with words that collided into each other a la Monogatari.
The hope was to try to do polygonal collision afterwards or maybe break up each
character into polygons and try and form a mural. Neither seemed very easy or
fulfilling, so I stopped.

### Elf on the Shelf

*Apr 2018 - May 2018*

A script I made in high school that would automatically generate Elf on the
Shelf memes and tweet them to our school broadcast program's hashtag. I made it
to try and impress my then-girlfriend. Now I have many technical and
non-technical regrets pertaining to its existence.

### Chattering With Me

*Oct 2017 - Nov 2018*

This was a pseudo-anonymous chatroom and one of my first web projects. I had
learned about WebSockets from a CTF and was also really into Durarara!! at the
time. Wanting to make a chatroom like the one from the show, I ended up
scrapping together something with Django Channels, made my first domain name
purchase, and deployed the app on AWS.

I also entered it into 2017's [Congressional App
Challenge](https://www.congressionalappchallenge.us/) and lost. Then my hacker
friend found out the site was vulnerable to XSS, redirecting everyone to Trump's
then-Twitter and teaching me the valuable lesson of input sanitization.

We had a lot of fun goofing off in research class with this until the semester
ended. Then the domain name expired and Django Channels went through a major
update which broke the app. I eventually sorted out all the dependency issues,
but by then we were all busy and in college, so I put the app to rest.

Although long dead, Chattering With Me did provide me with lots of my initial
web deployment experience. It also laid down the mental groundwork for what
would later become Kuiperbowl.

### Mana Filter

*Aug 2017 - Sep 2018*

One of my earliest repos on GitHub. I was a summer intern <s>playing with</s>
researching VR at the time. Halfway through the internship, I got bored of
flying through Google Earth and learned OpenCV. I was also into Mousou Telepathy
at the time. In the manga, there's this character, Mana, who gets teased because
her hair drills look like croissants. Inspired by Mana, I thought it would be
funny if I could have croissant hair drills in real life and ended up modifying
an OpenCV facial recognition tutorial to post-process a picture of croissants on
my head. It actually worked quite well as long as there was enough light. The
project was sort of done at that point, so now it's here. Maybe I'll revive it
someday into a web app or something.

As an aside, during that time, I also got to see the [2017
eclipse](https://en.wikipedia.org/wiki/Solar_eclipse_of_August_21,_2017). That
was cool.