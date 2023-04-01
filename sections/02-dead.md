---
title: Dead
description: Incomplete projects that I stopped working on.
---

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


### Processing Diary

*Apr 2020 - Apr 2020*

I became enamored by Processing GIFs on Twitter at some point. Believing I could
make my own amazing GIFs, I thought to start a diary and write a small, fun demo
a day. Then I realized that learning Processing was gonna take actual effort.
Also my creative output is kinda low, so I made one spinny thing and gave up.

### Congruence

*Dec 2019 - Jan 2020*

I wanted to make a server to run unit tests and judge code submissions just like
UMD's submit server. The plan was to let users to upload code to a static store
and have workers download submissions and run them against tests in ephemeral
Docker containers. The unit test results could then be parsed and saved into a
database. I had gotten as far as unit testing arbitrary Python code when I ran
into <s>some</s> a lot of security issues. So many that I decided to stop.

### Sasa

*Jul 2019 - Sep 2019*

I was sad when my mobile Mastodon client disappeared, so I thought I would try
to write my own. Similarly to Kuiperbowl Mobile, I got fed up with React Native
and stopped.

### Wiki Ladders

*Apr 2019*

I wanted to turn the game [Wiki
Ladders](https://en.wikipedia.org/wiki/Wikipedia:Wiki_Ladders) into an actual
web app. Eventually, I grew dissatisfied with the way it looked and stopped.
Perhaps I may re-visit the project in the future with some new ideas.

### Foodlebug

*Feb 2019 - Apr 2019*

After seeing the disorganized manner by which college students pawn off leftover
food from catering and other sources, I wanted to make a web app to connect
people with leftovers to hungry students. Development was slow since I decided I
would do it in Go without a framework, and the app eventually succumbed to death
due to a fatal hurdle: it was impossible to determine how long a given food item
would be available for.

### Yam Engine

*Jan 2019 - Feb 2019*

After finding out about Mogura Engine, I wanted to make my own 2D game engine in
JS. Then I realized how herculean of a task that was and kind of stopped.

### Portal Helper & Portal App

*Nov 2017 - Jan 2018*

A Java API and Android app made with a friend that attempted to interface with
Portal, our county's grades system. I ended up reverse-engineering the Portal
login system at the time which paved the way for the API, but then we all
graduated and lost our school accounts which permanently halted development on
the project.

### BILL API

*Dec 2016*

A Java API for accessing BILL, my high school's one-stop shop forum/directory.
Development stopped after losing both interest and my login credentials.