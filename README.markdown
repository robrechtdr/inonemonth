Inonemonth
==========
> Fail wisely

[![Build Status](https://travis-ci.org/RobrechtDR/inonemonth.png?branch=master)](https://travis-ci.org/RobrechtDR/inonemonth)
[![Coverage Status](https://coveralls.io/repos/RobrechtDR/inonemonth/badge.png?branch=master)](https://coveralls.io/r/RobrechtDR/inonemonth?branch=master)

**What is it?**   
A webapp that stimulates power users to set challenges for themselves by aiming to minimize the negative consequences of and maximize the learning experience from a failed attempt.

Core concepts: [Git(hub) branch](http://git-scm.com/book/ch3-1.html), [Github compare](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/github_compare.png), [SMART objective](http://en.wikipedia.org/wiki/SMART_criteria#Developing_SMART_goals), minimizing risk, maximizing learning from mistakes, reducing influence of factors other than performance in voting behavior. 

**How does it work?**  
To start a challenge a user must [define one and indicate a branch of a project 
on his Github account where his progress will be measured on](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_create.png). 

He must then [invite minimum one person](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_invite_jurors.png) who can decide after one month if he will have succeeded in his challenge or not. 
The user who creates a challenge is called the [clencher](https://inonemonth.herokuapp.com/glossary/#clencher) for that given challenge, the users 
who get invited are called [jurors](https://inonemonth.herokuapp.com/glossary/#juror).

On the [challenge detail page](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_detail_challenge_period_clencher.png) there is a link to a [Github compare](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/github_compare.png) which shows all the changes made on the designated challenge 
branch since the challenge started. After a period of one month jurors get one week to comment and cast their votes about the attempt. The clencher is able to see the identity of each juror but the jurors cannot see each other's identities.

Currently this webapp is especially lacking features which stimulate 
the learning experience from a failed attempt. However, [a feature is 
planned to improve that](https://github.com/RobrechtDR/inonemonth/blob/master/TODO.rst#likely-coming-in-future-releases).

**Development stage**  
Alpha


Urls
----

* `/`

  ![home](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/home.png)


* `/accounts/signin-github/`

  ![accounts_signin_github](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_signin_github.png)


* `/accounts/social/signup/`

  ![accounts_social_signup](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_social_signup.png)


* `/accounts/confirm-email/`

  ![accounts_confirm_email](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_confirm_email.png)

  ![accounts_confirm_email2](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_confirm_email2.png)


* `/challenges/create/`

  ![challenges_create](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_create.png)


* `/challenges/1/invite_jurors/`

  ![challenges_invite_jurors](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_invite_jurors.png)


* `/challenges/1/detail/`

  ![challenges_detail_challenge_period_clencher](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_detail_challenge_period_clencher.png)

  ![challenges_detail_comments_juror](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/challenges_detail_comments_juror.png)


* `/accounts/signin-juror/challenges/1/`

  ![accounts_signin_juror](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_signin_juror.png)


* `/accounts/social/connections/`

  ![accounts_social_connections](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_social_connections.png)


* `/accounts/logout/`

  ![accounts_logout](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/accounts_logout.png)

* `/glossary/`

  ![glossary](https://raw.github.com/RobrechtDR/inonemonth/master/.misc/glossary.png)


Installation
------------
See [Install](https://github.com/RobrechtDR/inonemonth/blob/master/INSTALL.markdown).
