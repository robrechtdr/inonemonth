import time

from django.core.management import call_command
from fabric.api import local
from lettuce import step, world, before, after
from lettuce.django import django_url, mail
from splinter import Browser


####################
# Setup and teardown
####################
@before.all
def setup():
    """
    Setup each time harvest command is ran
    """
    #local("django-admin.py syncdb --all --settings=inonemonth.settings.test --noinput")

    # Running harvest with -T option does setup and teardown as with unittests
    # See: https://github.com/gabrielfalcao/lettuce/issues/73
    print "Before all: New test db setup!"
    world.browser = Browser()


@before.each_scenario
def scenario_setup(scenario):
    """
    Setup before each scenario
    """

    #local("django-admin.py syncdb --all --settings=inonemonth.settings.test --noinput")

    print "Before scenario: Flush db ..."
    # It's safe to assume changes to the db schema will not be
    # made in between running scenarios. So merely deleting the
    # data with the flush command is sufficient.
    call_command('flush', interactive=False, verbosity=1)
    # Runs in test env only!!
    print "Before scenario: ... db flushed!"
    call_command('setup_allauth_social', 'github', domain="http://localhost", setting="test")
    # Profile factories with dummies should be ran here.

'''
@before.each_step
def setup(step):
    print "before step"
    call_command('setup_allauth_social', 'github', domain="http://localhost", setting="test")
    from django.contrib.sites.models import Site
    Site.objects.create(domain="http://kaka.com", name="kaka")
'''

@after.all
def teardown(total):
    """
    Clean up after harvest call
    """
    world.browser.quit()


######################################################
# Type T steps - These should only be used temporarily
######################################################
@step(u'I debug')
@step(u'I wait')
def i_debug(step):
    import pdb; pdb.set_trace()


#####################################################################
# Type A steps - These should be the only functions that directly use
#   splinter's `Browser` in their body
#####################################################################
@step(u'I go to the URL "(.*)"')
def i_go_to_the_url(step, url):
    # Wtf, fixtures are loaded, yet still when world.browser... line
    # is called below, the Site table only has one entry again.
    call_command('loaddata', 'core/initial_data.json')
    ###########################################################
    world.browser.visit(django_url(url))


# If the clickable item is a link, preference should be given to this step
@step(u'I click on the link with text "(.*)"')
def i_click_on_the_link_with_text(step, text):
    link = world.browser.find_link_by_text(text)
    link.click()


@step(u'I click on the element with id "(.*)"')
def i_click_on(step, element_id):
    clickable_element = world.browser.find_by_id(element_id).first
    clickable_element.click()


@step(u'I fill in "(.*)" in the element with id "(.*)"')
def i_fill_in(step, value, element_id):
    input_element = world.browser.find_by_id(element_id).first
    input_element.type(value)


@step(u'I confirm the presence of the element with id "(.*)"')
def i_confirm_presence(step, element_id):
    element_li = world.browser.find_by_id(element_id)
    element_li.first


##############################################
# Type B steps - Steps other than type A and T
##############################################

@step(u'I log in with email "(.*)" and password "(.*)"')
def i_login(step, email, password):
    step.given('I go to the "/" URL')
    step.given('I fill in "%s" in the element with id "id_identification"' % email)
    step.given('I fill in "%s" in the element with id "id_password"' % password)
    step.given('I click on the element with id "login"')


@step(u'I log out')
def i_logout(step):
    step.given('I click on the element with id "sign-out-dropdown"')
    step.given('I click on the link with text "Sign out"')

