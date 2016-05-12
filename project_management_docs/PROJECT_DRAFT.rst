Inonemonth: Set yourself a tangible challenge to be completed in one month (Minimal viable product demo project)
================================================================================================================

Inonemonth is a web application that lets you set a tangible challenge for yourself in one month. Failing a challenge can be bad but it shouldn't be! Inonemonth stimulates people to challenge themselves by selected exposure of challenges and obligatory feedback of judges who fail you. 

Learn to fail and improve from it! For crying out loud challenge yourself for once/F*cking challenge yourself for once!/for God's sake challenge yourself for once.

Basic challenge flow
--------------------
The person who wants to challenge himself registers to Inonemonth. He then creates a challenge and describes it as concrete as possible(he gets examples of concrete things, look at kickstarter tips for this). Once the challenge is defined he then inputs the email address(or addresses) of the person(or people) he would like to see judge if he succeeded in the challenge(called judges). Key here is that judges can only fail you if they write why they think you didn't succeed. They can also write tips how to improve(also here judges can see some best practices how to jugde well). Each judge gets sent a unique key so the challenger knows who wrote what comment. This means that judges don't need to register to be able to judge. They can however register and add the key to their account if they preferred to have a permanent account and comment from there. You can then freely have a back and forth of comments. (Perhaps a key doesn't need to be send, just a url of the challenge detail page with key in it as querystring wich lets person make identified comments. This key sets a salted session cookie(get request(?k=0fhjDKh) + Django sessions)).

He can select other people to see the challenges. All people who are voters(judges) see the challenges but you can also let other people that can't vote see the (they get sent a spectator key or they should register themselves) challenges. These sole spectators can be elected even once the challenge has started. You can't elect new voters(judges) though once you've started the challenge. 

By default, judges comments are displayed as anonymous, only Lincolns see the identity of the Judges. However, Lincolns can choose to display names publicly(effects of this? maybe judges will be less likely to answer. Better to keep anonymous).

Challenges can't be edited in title or discription once the mails to judges are send. However challenges can be cancelled by the person who started it. He can set a new challenge replacing the old one. (time starts again from one month. Pple can see from themselves when it wouldn't be fair to start again for one month. So should be a natural barrier for pple to keep replacing their own challenge.
It must be possible to set a challenge iteratively. You can do this by making a 'challenge proposition' to one or more potential judges. You mail them with your proposition and they can tell what they would like to be different/more realistic and then you can base your challenge on that.

Challenges can at any time be made public. During the challenge or even after the challenge is done. But just having challenged yourself is something to be proud of even if it's only shown to one person. 
If you make it public on the moment. Allowing challenges to be seen public attracts and stimulates people to  

If multiple people can vote if you passed the challenge or not you need to have the majority to pass the challenge. (That means min. 1/1, 2/2, 2/3, 3/4, 3/5, 4/6, 4/7, 5/8, ... )

The challenge mail can be sent automated but advised to write the content of the mail yourself for each person since its likely only to be sent to a small number of people and addressing them personally creates more interest. These unique keys are also shown at the moment of when a mail is sent so the person can just copy-paste the key in an email. That's more likely to be read then via Inonemonth's email since some popular mail services (e.g. gmail) would put that mail under a social tab(test this).

It's also possible to explain what you want to achieve with this challenge but it's not necessesary. 

Also on main page, show: Out of all challenges x% (probably like 70%) fail. Failure is normal, don't think you're the only one.
But x%(80%?) of those who failed don't regret having started the challenge because they learned something from their mistakes. 

Accounts from challengers can be set to private or public but once you make a challenge public your profile will also be public (with parts you can choose to show and hide).

Core vocabulary
---------------
- A Challenge
- To complete a challenge/succeed in a challenge/rise to a challenge(ask on so words). : "Challenge completed! No, "Challenge is met" is better(use a green color so it is absolutely clear this means success)
- To not complete/fail at a challenge.: "Challenge not completed"/"Challenge failed" No, use "Challenge is met/not met".
- A Lincoln(the Lincolns)/Lincolner: Person who courageously faces challenges despite having failed and risking failure(referring to abraham lincoln). I don't want to use the word 'challenger' because that means the person who challenges someone. I might later want to implement also people who judge challenge someone. Courageous.  Example of name used for personality: you are a Judas.
  Or a Honeybadger.
   (Fuck it, just do it Honeybadger style)
- A Judge(the judges): Person who judges if the challenge is met.
- A Challenge messages: A message on the challenge detail page.(use challenge comment instead ?)
- A lead challenge message(=a major message/a threading message): a challenge message that spawns a new thread.
- A follow challenge message(=a minor message/a comment): a challenge message following a lead message. I'm not using the word response because a response is 
  to another specific message. My message system does not support specifying to which the follow message is directed to. This is not a problem because 
  users are able to direct to others directly by using a notation as "@johnny" to address a specific person. Not having a super convenient way to address a specific
  comment instead of a person is not that much of a problem.
- A judgement message: a lead challenge message that requires the judge passing a positive or negative judgment along with a message.
- A Judge judges or passes judgement on a challenge set by a Lincoln.

Web app pages
-------------

Each page should have its own document. To be hosted on a seperate site about the pages. (Using ReadTheDocs?)

- Description: (A homepages showing the number of private and public challenges currently running together with one big button, start challenge. Its also possible to implement either the how to here or the listing of public challenges. Maybe also list the total number of private and public challenges ever started. (don't implement yet))
  Homepage shows the concepts of the game: There are Lincolns and Judges(with a pic indicating that role). And also show the workflow.
  The top page of the bar also has a sign in (Bootstrap Jumbotron template) so people can immediately sign-in without going to another page first.
  The sign-up appears on 2 instances: (1. When clicking on Sign-in but failed(no address found).: Have you made an account yet? Don't do this.)
  2. When setting a challenge. Before you set a challenge you need to register. (Or use Github login)
  Explanation: The number of private challenges immediately shows people that it the most normal/common thing to be shy/scared about failure. This also immediately shows people new to the site that challenges can be private(is even default). 
  URL: /
  Release: 0.0.1

- Description: A challenge detail viewing page. Should be in ssl so that when page is visited with a key a person on public network can't comment in the name of someone else. Implement comments via discuss? 
  Explanation:  
  URL: 
  Release: 0.0.1 

- Description: A challenge detail editing page. Must say somewhere: 'tip: the more people you allow to judge the higher the chance of getting rich and nuanced feedback. Must include a link "Where to let 
  Must have a part: verify here. A link to your project on a project platform. It(Has a rich text editor field) allows posting a picture/video of your product(advised: one product picture/ or explanation and then just the link of the project on a project platform.  (E.g. Github, Bitbucket, Youtube, Vimeo, Dribble, a blog, ...)  
   When at the end you don't succeed you also see the message: "The first step in improvement is to know your current limitations in a given challenge. Now you likely know better what to focus on, what to improve in order to succeed. It may not be called success but it is still improvement, you are likely closer to success now then if you didn't challenge yourself. If how and why you failed the challenge is still unclear try to figure it out!".
  Explanation:  
  URL:  
  Release: 0.0.1

- Description: A registration & login page. (Can also be just via ajax on hompage like Peek). Email confirmation of Lincoln profile is neccessary, otherwise a person could sign up with an email address of person he hates, then create a challenge and invite the bosses of that person to judge. 
  Explanation:
  URL: 
  Release: 0.0.1

- Description: A registration confirmation page. With a link to challenge edit page(or possible autoredirect after x seconds of confirmation).
  Explanation:
  URL: 
  Release: 0.0.1

- Description: A profile detail page. There should not be the possibility to sort per profile(if public) on fails.
  Explanation: 
  URL: 
  Release: 0.0.1

- Description: A page with famous people who failed big but are now regarded as successful such as A. Lincoln, explanation + pics. Might not be a bad idea to write that its hard to find a history of failures with successful people because people usually try to hide it as much as possible.
  Explanation: This is to show that failing repeatedly doesn't mean you can't have huge successes.
  URL: /famous-failers/ 
  Release: Post 0.0.1 (Can be iorem ipsum)

- Description: A page about how to define good challenges. See kickstarter's tips for this. 
  Explanation: To improve the quality of the challenges set.
  URL: /defining-challenges/ or /defining-tangible-challenges/
  Release: Post 0.0.1 (Can be iorem ipsum)

- Description: A page about how to give proper feedback. Include that they should also remember it took courage from the person who challenged himself.  
  Explanation: To improve the quality of the feedback.
  URL: /giving-feedback/ or /giving-useful-feedback/
  Release: Post 0.0.1 (Can be iorem ipsum)

- Description: A page with circumstances where these challenges can be used to really help your life forward. E.g. As a developer you found a company you really want to work for but they aren't applying. Set yourself the challenge that you will develop webapp/program x in one month(or at least parts a, b and c). Or To your friends set the challenge that you will park the car in a tight spot properly in one month(too long for that probably). Set yourself to play Chopin's revolutionary etude in one month, ask your favourite pianist to be a judge and hopefully receive some helpful feedback from them at the end! They'll be honored that you spent a month trying and they can be the judge! Write your first game in Python. Write out your own git workflow. Challenge myself to implement feature x by the end of the month.
  Explanation: To inspire/show when you are in a circumstance that could immensely benefit from a one month challenge. 
  URL: /challenge-use-cases/
  Release: Post 0.0.1 (Can be iorem ipsum)

(- Description: A page showing how it works. A long scrolling page like new relic's showing the steps in creating a challenge. (Could also be part of the homepage)
  Explanation:  
  ULR: /how-it-works/
)

- Description: A challenge listing page of the public challenges. A title should say: 'challenges made public' (Could also be a part of the homepage). Per listing there is the title of the challenge and how many points were scored with a profile thumbnail of the person who challenged himself. Clicking on the challenge should go to the challenge detail page. Clicking on the profile thumbnail should go to the profile detail page. The list should be sorted chronologically by time made public by default. List can be sorted by the ones currently running first. Challenges currently running have a currently running symbol on them.
  Explanation: Enabling sorting on fails stimulates people to see their fails, focus should be taken away from failure.
  URL: /hall-of-fame/ or /public-challenges/ 
  Release: Post 0.0.1


Mechanisms not or not yet bound to a particular page
-----------------------------------------

- Description: There should be badge: daredevil(or something else), a person who has  . For private challenges there shouldn't be any badges because that might create a stigma that people with lots of these badges fail while that's not necessarily true. For a challenge made public after its time is passed no badges should be made either because otherwise every visible challenge would give a badge. Let's start with people who make it public during the challenge but not before to not give them a badge either. People could see anyway by viewing "challenges running".  

- Description: If a user makes a challenge public his profile will become public too(as long as at least one challenge is public). However, only his picture and his personal info he wants to be shown is shown, never the number of his private challenges. A user without public profiles can also choose to set his account public but it's not default. Challenges once made public can be made private again (and profile becomes private again if his profile is private by default.) 

System fixes/improvements
------------------------


Todo in current release
------------------------ 
- Make about/contributing/ ... pages as https://asciinema.org/ (spirit of project). Also look at it's README etc. .

Possible future features
------------------------
- Send link to autologin (see how allauth generates that autologin link (also check it out how it looks) + how it is used to login. 
  For now just use /account/signin-juror/challenge/1/

- When a juror signs in, he should see "bind github account" link in navbar.

- There shouldn't need to be a logout page, just a logout link on top right of navbar. That is enough.

- Put link to change/reset password in juror invitation email and juror challenge signin page.

- Implement feedback form on side of each page (like with angelhub)

- Implement "alpha" sign on top/side of each page. (Better smthing like "experimental phase" or othr)

- Let comments also have a comment history such as in stackoverflow.

- In post challenge system, you get visuals/pics(gifs, dude with glasses), 
  awesome, that took ballz.

- Implement that you can also make an Inonemonth.markdown file in your project,
  implement button, read "Inonemonth.markdown file" which autoreads. This file is
  only read once, at creation of challenge. (instead of needing to fill in body).
  Cool would be that the body is saved as an "Inonemonth.markdown" file and that you 
  can download it and add to your project.
  Jurors could see diffs of Inonemonth.markdown file of original if adjustments to the 
  challenge were made. (See how bitdeli implements its stuff inside your project)

- Github, Twitter, Facebook and OpenID registration (and log in?). => No

- At the end of the voting period, no existing headcomments and tailcomments should be able to be deleted. Only new tailcomments should be possible to make.

- Should be able to get message in account inbox that someone answered your comment.

- First release allows only to use public repo's, in further releases challenges should also be able to work on private repo's.

- Implement post-evalutation field for a challenge where judges are allowed to pass their judgement on again.

- Implement displaying the git log messages list made only on the 'challenge branch' on the challenge detail page.

- A few example/challenge/detail/1 pages showing a few good successful and failed challenges (with succesful and non-succesful post-evaluation).

- Challenges can be initiated by a 'challenge proposition'. A back and forth mailing between Lincoln and judges to optimize(make more realistic/with better rewards) defining a challenge. The normal challenge initiation is called 'unilateral'.

- Judges can also upvote (not downvote) the feedback or comment of another person such as in Stackoverflow. The feedback is then autosorted with the feedback with the highest points on top.

- Allow challenge setters(Lincolns) that judges can't see eachothers comments. (Effects of this ?)

- People who set challenges public get a "balls of steel" or "big cohones"(foto van man die voor leeuw ligt/iets anders daring/of twee balls) reward, visible on their profile.

- Recognise .challenge.md files in github repos or READMEs(that requires markdown/rst interpretation in site) for on challenge pages. 

- Fix rendering/style issue after validating forms in invite-jurors and then pressing "remove".

- Make autocreate of project/branch on create/challenge if the branch/repo doesn't exist yet? (Then the custom validation 
  will become unnessesary there)

- When no challenges are made yet, on profile of challenges, let content show in steps what to do to make a challenge:
  E.g. like on Travis, if there are no repos set up yet: https://travis-ci.org/getting_started
  This step wise layout could also be used for the homepage of inonemonth!!

Reasons to open source
----------------------

- You receive help and issues are open for everyone to place making the quality of your site ultimately much higher. 
- You have a decent open source project for on Github profile which makes it possible to show future employers the quality of Django code.
- If you work a long time on a closed source project people will want to know what you've been doing. (A reason not to do non-closed source)


Project workflow
----------------
- It's ok to experiment, but always write code in feature branches so you can squash weird commits together. (Ensure fearless development is possible)
- Written test must cover >= 70% of the python code. (Use coverage and django-discover runner)
- Use adaptivelab's Python style guide sensibly.
- Just before releasing publicly to Adaptivelab for the first time, go over the whole methodology one more time.
- Have a clear structure beforehand of the models you are going to use (db structure). Can write this in code immediately with model tests. (or first write them all in core and then make apps accordingly and place them in right apps.)

Target group
------------
- Primarilly programmers/hobby coders/pple with technical skills who know what github is. Can be used for non-programming projects but strongly geared towards projects in github.


Todo
----

- Know how the adaptivelabs flow works (including squashing commits) (adapt their workflow to one person flow)
- Main model: Kitsune(= Fabric bolt). Uses Bootswatch for bootstrap theme.

Design page tips
----------------
- If you are having a hard time to come up with a sensible layout of your page first start with designing the coherent elements on your page seperately (e.g. a how to infographic, a challenge list, ...)

User stories URL flows
----------------------
- Flow I: User sets up challenge for first time (clencher)
  1. / 
  2. /account/github-signin/
  3. /account/bind-email/
  4. /challenge/create/
  5. /challenge/detail/1/
  (opt. /challenge/list/243/)

- Flow II: User sets up a second (or higher number) challenge with new browser window (clencher)
  1. /
  2. /challenge/create/
  3. /challenge/detail/1/

- Flow III: User is invited by mail to vote (Juror)
  1. /account/juror-signin/challenge/2/
  2. /challenge/detail/1/

- Flow IV: User logs in to vote (Juror)
  1. /
  2. /challenge/to-vote-list/

- Flow V: User that has only been a Juror starts a challenge
  1. /
  2. /account/bind-github/
 


Example challenge
----------------
- Premise: I want to get the position of web developer at Heroku, I meet most essential requirements but 
  there is one skill they stress on that I miss completely: Experience with designing a RESTful API. 

- Challenge title: In one month I want to attain the following... Implement a RESTful API for my existing pastebin webapp.

- Challenge body: 
  ....  .


**Example user story**  
James wants to get the position of web developer at Heroku, he meets the most essential requirements but there is one skill they stress on that he misses completely: Experience with designing a RESTful API. 

So he goes to Inonemonth to set himself the following challenge "Implement a RESTful API for my existing pastebin webapp". For that he creates a seperate branch on his project called API. He invites Heroku and two other interesting companies to show his skills and courage.





===========================
===========================

TO DO:

- Check challenge flow and edit if necessary.
- Make mock ups of the seperate pages. Look for an existing example page for each of them.

General 
------
Only the people who you invite (You have to invite them from before you launch your challenge or it won't start >> no! not necess, companies e.g. will think they would own you somthing otherwise. Just gives them judging power)

People are scared of challenges. Failing a challenge can have nasty consequences but it is something every human being should risk to be become the best he/she can. Risking failure is the . Failure is even necessary (provide case). 

How is it different from kickstarter? Minimizes risk of failure, not public exposure necessarily and focused on feedback, not on getting money.

How is it different from HabitForge? Is completely free(certainly free accounts don't have adds)

Make open source like gittip? or Make private?

See gittip code as example for registrations, stats showing etc. .


Types of challenges
-------------------

One-sided non-recompensational
The description of the terms of the challenge are set solely by the person who commits himself to the challenge. He does this without a commitment of compensation from the parties he sends the challenger key to.  (They don't need to register to make comments, the key is unique to a specific person, so by using that 

The challenge is launched by the person and he send



A challenge that comes from yourself (Non-binding)
(non-recompensational challenges)

and

Back and forth about terms. (You send, do you accept these terms of the challenge and other person can then show you which descriptions of the challenge he wants to have edited)
Retributional/compensational challenges. A challenge with a reward (Where you say, if I am able to do x and y in z amount of time, I get g from the challenger) 
(this is implemented later)


Who can Initiate a challenge
----------------------------

Both the person who commits to doing the challenge or a person who wants to challenge someone else (sends email to person). 

It's the most basic functionality for anyone to challenge themselves and to elect people to be accountable to.

Challenging an other person but yourself is something probably better suited for paid account.


Some situations where challenges can have awesome consequences
--------------------------------------------------------------

non-recompensational challenges:

- Challenge a company you want to that you'll you want to learn (links to example of such a challenge)
- Challenge yourself to implement 2 skills listed in the description of the ideal candidate 
you didn't know before sensically 


recompensational challenges:

- Challenge your employer to get a raise of $200 if you manage to create one project that implements a non-relational database where it makes sense to use one.


What are good challenges?
-------------------------
- Quantify as much as possible: e.g. I'll make at leaset one of this and one of that. If you can't quantify your challenges you should dig deeper into the subject until you can.


