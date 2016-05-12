# Estimate v0.0.1

## URL based task listing

### / 
* Create mock up - Needs refining!!
* Implement explanatory section in template - Needs prototyping!!
* Implement dropdown with email-password signin and Github signin (need dropdown design in mckup, consider just a signin button redirecting). 
Also implement if user is not logged in show signin dropdown else show email/user with logout(see allauth template tags) in base html - Needs prototyping!!
* Implement challenge button linking to /account/signin-github/ - 20 minutes
* Implement view (fbv that is FormView like) and urlpattern - 20 minutes

### /account/signin-github/
* Implement a simple TemplateView with urlpattern - 10 minutes
* Implement a redirect to /account/bind-github/ if user only has email registration and no Github account. - 20 minutes
* Get github button/sign and implement the template - 20 minutes

### /account/bind-email/
* Find out how/if I can bind email address to Social account(easer then the inverse) in view - Needs prototyping!!
* Implement View (looks like UpdateView/FormView/CreateView like, use fbv) that redirects to /challenge/create/ when valid email used in form - 10 min
* Implement template - 20 minutes

### /challenge/create/
* Create left and right boxes on template and fill in lorem ipsum on right side - 20 minutes
* Implement SO like form - 20 minutes
* Implement project github link form with ajax validation that checks if filled in repo exists on your Github or associated accounts
(let it display a 'loading' symbol while in process of validation - Needs prototyping!!
* Implement Form that has minimum one email field and an add button for dynamically adding fields. Alternatively use one field that 
allows a comma seperated list of email addresses like when sending rl email. Validates through ajax/javascript. - Needs prototyping!!
* Create email template and let email be sent to designated jurors with a link as /account/juror-signin/challenge/1/ (in view) - 3u
* Let designated juror accounts be created in the background (not with celery initially) (in view) and add this user to Challenge.jurors  - Needs prototyping!!
* Create the view (create view, but function based) with urlpattern - 30 minutes 

### /challenge/detail/1/
* Implement decorator to block off all users that are not juror or clencher to the challenge. If that is the case, redirect them to Error page: 'You 
are not allowed to see this page. Only the clencher and jurors to this challenge can view this page.'. Also implement this error page - Needs prototyping!!
* Implement content on right hand side box - Needs prototyping!!
* Clicking on judgement button summons a comment box. Find out which type of box, how I can implement such a comment box - Needs prototyping!!
* Implement if-else on right bottom side box. If in case of Clencher, content is different then case of Juror - 20 minutes
* Implement head-tail comment system. - Needs prototyping!!
* Implement indication if vote is positive or negative of Juror. Also the majority of votes at the end of voting period creates a 
sign on the challenge that is successful or not. - 2 hours

### /challenge/list/243/
* Make sketch how it is supposed to look like - 40 minutes
* Write view (just a ListView) and urlpattern - 20 minutes
* Write template. - 2u

### /account/signin-juror/challenge/1/
* Create View that shows a login form, when form successfully filled in this logs user(juror) in and redirects to specified challenge. - 40 minutes
* Write template - 30 minutes

### /challenge/vote-list/
Alternative name URL: /juror/to-vote-list/
* Make sketch how it is supposed to look like - 40 minutes
* Write view (just a ListView) and urlpattern - 10 minutes
* Write template. - 3u

### /account/bind-github/
* Find out how/if I can connect a the registered user with Github account that is then signed in, in a view. - Needs prototyping!!
* Make urlpattern and make template - 20 minutes

### NA (Functionality not bound to url)


# Uncertain tasks work list

## Very high uncertainty
### /account/bind-email/
* Find out how/if I can bind email address to Social account(easer then the inverse) in view - Needs prototyping!!

### /account/bind-github/
* Find out how/if I can connect a the registered user with Github account that is then signed in, in a view. - Needs prototyping!!

### /challenge/detail/1/
* Implement thread-comment system - Needs prototyping!!
* Clicking on judgement button summons a comment box. Find out which type of box, how I can implement such a comment box - Needs prototyping!!


## Significantly lower uncertainty 
### /challenge/create/
* Implement project github link form with ajax validation that checks if filled in repo exists on your Github or associated accounts
(let it display a 'loading' symbol while in process of validation - Needs prototyping!!

### /challenge/create/
* Implement Form that has minimum one email field and an add button for dynamically adding fields. Alternatively use one field that 
allows a comma seperated list of email addresses like when sending rl email. Validates through ajax/javascript. - Needs prototyping!!

### / 
* Create mock up - Needs refining!!
* Implement dropdown with email-password signin and Github signin (need dropdown design in mckup, consider just a signin button redirecting). 
Also implement if user is not logged in show signin dropdown else show email/user in base html - Needs prototyping!!
* Implement explanatory section in template - Needs prototyping!!

### /challenge/create/
* Let designated juror accounts be created in the background (not with celery initially) (in view) and add this user to Challenge.jurors  - Needs prototyping!!

### /challenge/detail/1/
* Implement content on right hand side box - Needs prototyping!!
* Implement decorator to block off all users that are not juror or clencher to the challenge. If that is the case, redirect them to Error page: 'You 
are not allowed to see this page. Only the clencher and jurors to this challenge can view this page.'. Also implement this error page - Needs prototyping!!
