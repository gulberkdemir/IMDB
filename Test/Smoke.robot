*** Variables ***


*** Settings ***
Resource  ../Sources/Pages/LoginPageObject.robot
Resource  ../Sources/Pages/Top250PageObject.robot
Resource  ../Sources/Pages/CommonPageObject.robot
Resource  ../Sources/Pages/WatchListPageObject.robot
Test Setup  Begin Web Test
Test Teardown  End Web Test

*** Test Cases ***


Case1

    Given User doesn’t logs in IMDB
    And User visits the “Top 250 rated movies” pages
    And User clicks on “your rating” area for any movie
    Then User should be navigated to “IMDB login” page



Case 4
    Given User logs in IMDB
    And User visits the “Top 250 rated movies” pages
    And User hovers over “click to add watchlist” area for any movie
    And User sees tooltip includes “click to add watchlist”
    When User clicks on “click to add watchlist” area
    Then User sees tooltip includes “click to remove from watchlist”
    And User should see the movie’s name in the watchlist page
