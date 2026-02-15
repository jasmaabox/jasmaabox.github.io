---
title: Cartoon Avatar
start_date: 2020-04-01
end_date: 2020-05-01
---

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