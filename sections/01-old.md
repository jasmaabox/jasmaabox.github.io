---
title: Old
description: Mostly complete projects that I stopped working on.
---

### Kuiperbowl Mobile

*Sep 2019 - Dec 2019*

A native mobile client for my quizbowl platform, Kuiperbowl, and my first foray into mobile apps.
Abandoned after I upgraded Kuiperbowl to v3. I also got tired of running into build problems with React Native.

### NG Signal Challenge

*Sep 2019 - Oct 2019*

Our team's submission to Northrop's 2019 signal challenge. The goal was to accurately classify
a wide variety of sounds into 27 classes. We tried to do this by scraping soundbites off Google
AudioSet and training ResNet to classify the waveforms via transfer learning. It did not work.

### It's Ac Caption Dumper

*Jul 2019 - Aug 2019*

[It's Academic](https://en.wikipedia.org/wiki/It's_Academic) (It's Ac) is a local high school quiz show
that the *REEAALLY* good quizbowlers at my high school got the pleasure to be on. As practice, all quizbowl club
members were conscripted to transcribe an It's Ac game from [CBS Baltimore](https://baltimore.cbslocal.com/category/its-academic/)
into packet form (which was a painful process since I didn't know about AdBlock at the time). Later in life, I would imagine an
automated process for automatically transcribing and generating packets from those games which culminated into this project. Then
much later in life, CBS Baltimore would update their site and break my script which is why this project is now housed here.

### Fortune Cookie ML

*Mar 2019 - Apr 2019*

I tried to make an RNN to classify text as fortune or not fortune. I never did figure out whether
it worked well or not.

### Emergency Vehicle Finder

*Sep 2018 - Nov 2018*

Our team's submission to Northrop's 2018 image classification challenge. I did not know how to do
deep learning at the time, so we used traditional CV with Haar classifiers. It did not work.

### Falling Words

*Aug 2018*

I made a physics demo with words that collided into each other a la Monogatari. The hope was to try
to do polygonal collision afterwards or maybe break up each character into polygons and try and form a mural.
Neither seemed very easy or fulfilling, so I stopped.

### Elf on the Shelf

*Apr 2018 - May 2018*

A script I made in high school that would automatically generate Elf on the Shelf memes and tweet them to
our school broadcast program's hashtag. I made it to try and impress my then-girlfriend. Now I have many technical
and non-technical regrets pertaining to its existence.

### Chattering With Me

*Oct 2017 - Nov 2018*

This was a pseudo-anonymous chatroom and one of my first web projects.
I had learned about WebSockets from a CTF and was also really into Durarara!! at the time. Wanting to make a
chatroom like the one from the show, I ended up scrapping together something with Django Channels,
made my first domain name purchase, and deployed the app on AWS.

I also entered it into 2017's [Congressional App Challenge](https://www.congressionalappchallenge.us/) and lost.
Then my hacker friend found out the site was vulnerable to XSS, redirecting everyone to Trump's then-Twitter and teaching
me the valuable lesson of input sanitization.

We had a lot of fun goofing off in research class with this until the semester ended. Then the domain name expired
and Django Channels went through a major update which broke the app. I eventually sorted out all the dependency issues, but by then
we were all busy and in college, so I put the app to rest.

Although long dead, Chattering With Me did provide me with lots of my initial web deployment experience. It also laid down
the mental groundwork for what would later become Kuiperbowl.
