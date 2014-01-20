Feature: Login flow

Scenario: Login with site account
    When I go to the URL "/accounts/login/"
    And I debug 
    And I login with email "jim.klutz@gmail" and password "my_password"
    Then I confirm I am on the page with URL "/"
    
    
Scenario: Login with Github account
    When I go to the URL "/accounts/login/"
    And I debug 
    And I login as Github user "RobrechtDR"
    Then I confirm I am on the page with URL "/"
