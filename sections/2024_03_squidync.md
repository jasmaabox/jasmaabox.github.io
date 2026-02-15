---
title: Squidync
start_date: 2024-02-01
end_date: 2024-03-01
---

I was already a big user of [Hyperbeam](https://hyperbeam.com/) for watch parties and had tried out [Roll Together](https://chromewebstore.google.com/detail/roll-together/ilpfeljgdikoabaclkjgkbeegeoijfca?hl=en-US) before. Armed with my experience from making niconico-yt, I wanted to see if I could make something nicer that could also support chat messaging.

I started rifling through the Crunchyroll web app HTML and found out that Crunchyroll apparently hosts its video player on a separate site and embeds it as an iframe on each episode's site for some reason. This then led me down a deep deep rabbithole that involved designing two content scripts, video and site. The two scripts would pass video playback data between each other through the background script as a proxy. The site script would then sync playback with other clients by talking via websocket to a web server which had a connection pool with all the other clients. That server would have info on which client was the leader and broadcast the leader's playback state as the canonical video state to everyone else.

In the end, the whole thing ended up kind of working but still had many gaps. I had not figured out a good way to synchronize all clients on the same video URL and there were still a bunch of lag and syncing issues with manipulating Crunchyroll's playback. I also ended up custom-rolling all the connection pool logic for the server by writing it in Go which may have been a bad idea since this made dev very tedious. Then at some point, Crunchyroll ended its freemium service. Since I was the only one of my friends with a Crunchyroll subscription, it became (1) very annoying to test the syncer and (2) kind of pointless since no one would use it. So I quit.