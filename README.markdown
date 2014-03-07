Inonemonth
==========
> Fail wisely

**What is it?**   
A webapp that stimulates power users to set challenges for themselves by aiming to minimize the negative consequences of and maximize the learning experience from a failed attempt.

Core concepts: [Git(hub) branch](http://git-scm.com/book/ch3-1.html), Github compare, SMART objective, minimizing risk, maximizing learning from mistakes, reducing influence of factors other than performance in voting behavior. 

**How does it work?**  
To start a challenge a user must [define one and indicate a branch of a project 
on his Github account where his progress will be measured on](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_create.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9jaGFsbGVuZ2VzX2NyZWF0ZS5wbmciLCJleHBpcmVzIjoxMzk0NjM3MjY3fQ%3D%3D--5963dec884bb359c9da8ea99a6cfe8b043fc5288). 

He must then [invite minimum one person](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_invite_jurors.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9jaGFsbGVuZ2VzX2ludml0ZV9qdXJvcnMucG5nIiwiZXhwaXJlcyI6MTM5NDYzNzMyOX0%3D--9bb2ef5d817198c3e445938baecae4983e332c9a) who can decide after one month if he will have succeeded in his challenge or not. 
The user who creates a challenge is called the [clencher](https://inonemonth.herokuapp.com/glossary/#clencher) for that given challenge, the users 
who get invited are called [jurors](https://inonemonth.herokuapp.com/glossary/#juror).

On the [challenge detail page](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_detail_challenge_period_clencher.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9jaGFsbGVuZ2VzX2RldGFpbF9jaGFsbGVuZ2VfcGVyaW9kX2NsZW5jaGVyLnBuZyIsImV4cGlyZXMiOjEzOTQ2Mzc0MDl9--0b0e0b189b73ea403cc0a2ec2828120a18d6b802) there is a link to a [Github compare](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/github_compare.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9naXRodWJfY29tcGFyZS5wbmciLCJleHBpcmVzIjoxMzk0NjMzMDA3fQ%3D%3D--96449f1bdcfcc75962dd666345fddd24fd603d2f) which shows all the changes made on the designated challenge 
branch since the challenge started. After a period of one month jurors get one week to comment and cast their votes about the attempt. The clencher is able to see the identity of each juror but the jurors cannot see each other's identities.

Currently this webapp is especially lacking features which stimulate 
the learning experience from a failed attempt. However, [a features is 
planned to improve that](https://github.com/RobrechtDR/inonemonth/blob/master/TODO.rst#likely-coming-in-future-releases).

**Plans for releasing the code?**   
Yes, I plan to make the code public at some point.

**Development stage**  
Private alpha


Urls
----

* `/`

  ![home](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/home.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9ob21lLnBuZyIsImV4cGlyZXMiOjEzOTQ2MzA1Njh9--27c43648f4ba3e8d6fa47e30415d7be18355af8d)


* `/accounts/signin-github/`

  ![accounts_signin_github](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_signin_github.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9hY2NvdW50c19zaWduaW5fZ2l0aHViLnBuZyIsImV4cGlyZXMiOjEzOTQ2MzA2NjF9--3aac4ec75cc47e05e1805cc7d9745e25878f6b15)


* `/accounts/social/signup/`

  ![accounts_social_signup](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_social_signup.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9hY2NvdW50c19zb2NpYWxfc2lnbnVwLnBuZyIsImV4cGlyZXMiOjEzOTQ2MzE2ODZ9--a21f8ea9a30fd18b5268b703b54ba242ab6faf8d)


* `/accounts/confirm-email/`

  ![accounts_confirm_email](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_confirm_email.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9hY2NvdW50c19jb25maXJtX2VtYWlsLnBuZyIsImV4cGlyZXMiOjEzOTQ2MzEyNDl9--0cda55b3e6ffd10c6e43ac66cbaae911c40ee9ee)

  ![accounts_confirm_email2](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_confirm_email2.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9hY2NvdW50c19jb25maXJtX2VtYWlsMi5wbmciLCJleHBpcmVzIjoxMzk0NjMxNDI2fQ%3D%3D--b0990b031cebbc5cb16ed2c5df765401c7c59293)


* `/challenges/create/`

  ![challenges_create](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_create.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9jaGFsbGVuZ2VzX2NyZWF0ZS5wbmciLCJleHBpcmVzIjoxMzk0NjMwNzQzfQ%3D%3D--3074106a7011e4815880d68b96a14915f2576bdc)


* `/challenges/1/invite_jurors/`

  ![challenges_invite_jurors](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_invite_jurors.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9jaGFsbGVuZ2VzX2ludml0ZV9qdXJvcnMucG5nIiwiZXhwaXJlcyI6MTM5NDYzMDgzMX0%3D--58cfd74bd95cf115e7967af999caff639f246c45)


* `/challenges/1/detail/`

  ![challenges_detail_challenge_period_clencher](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_detail_challenge_period_clencher.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9jaGFsbGVuZ2VzX2RldGFpbF9jaGFsbGVuZ2VfcGVyaW9kX2NsZW5jaGVyLnBuZyIsImV4cGlyZXMiOjEzOTQ2MzA4OTh9--2bbc8287be12ae25f4f2b6f812996530748c34f1)

  ![challenges_detail_comments_juror](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_detail_comments_juror.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9jaGFsbGVuZ2VzX2RldGFpbF9jb21tZW50c19qdXJvci5wbmciLCJleHBpcmVzIjoxMzk0NjMwOTAwfQ%3D%3D--a833791ff20e0a059b886eb4d2d08afdd681ad31)


* `/accounts/signin-juror/challenges/1/`

  ![accounts_signin_juror](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_signin_juror.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9hY2NvdW50c19zaWduaW5fanVyb3IucG5nIiwiZXhwaXJlcyI6MTM5NDYzMTc3MX0%3D--69ad081a6fe89ebdc3819ccea2cdb68585a1f1ae)


* `/accounts/social/connections/`

  ![accounts_social_connections](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_social_connections.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9hY2NvdW50c19zb2NpYWxfY29ubmVjdGlvbnMucG5nIiwiZXhwaXJlcyI6MTM5NDYzMTUzOX0%3D--d0cff527f3aed1b15eb23159c6c353cab1bd6f63)


* `/accounts/logout/`

  ![accounts_logout](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_logout.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9hY2NvdW50c19sb2dvdXQucG5nIiwiZXhwaXJlcyI6MTM5NDYzMTQ1OH0%3D--6ac829fea4e8a50e813ac078262f05fc53c7c595)

* `/glossary/`

  ![glossary](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/glossary.png?token=2156349__eyJzY29wZSI6IlJhd0Jsb2I6Um9icmVjaHREUi9pbm9uZW1vbnRoL21hc3Rlci8ubWlzYy9nbG9zc2FyeS5wbmciLCJleHBpcmVzIjoxMzk0NjMxMTE1fQ%3D%3D--28e196bf0bb42562a6bf10539d678316b46e1041)


Installation
------------
See [Install](https://github.com/RobrechtDR/inonemonth/blob/master/INSTALL.markdown).
