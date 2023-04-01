---
title: Old
description: Mostly complete projects that I stopped working on.
---

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