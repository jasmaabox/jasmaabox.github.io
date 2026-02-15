---
title: Congruence
start_date: 2019-12-01
end_date: 2020-01-01
---

I wanted to make a server to run unit tests and judge code submissions just like
UMD's submit server. The plan was to let users to upload code to a static store
and have workers download submissions and run them against tests in ephemeral
Docker containers. The unit test results could then be parsed and saved into a
database. I had gotten as far as unit testing arbitrary Python code when I ran
into <s>some</s> a lot of security issues. So many that I decided to stop.