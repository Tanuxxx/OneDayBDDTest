Feature: Login to CMS

    Scenario: login as oneday admin
        Given login page "http://cms.oneday.com/Admin/Account/Login"
        When user enters login: "jdineshk@gmail.com" and password: "brookdale2016"
        And submits
        Then user sees "http://cms.oneday.com/Admin/Company" page