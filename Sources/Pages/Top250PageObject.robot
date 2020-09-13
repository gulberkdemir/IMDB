*** Settings ***
Library  SeleniumLibrary
Library    ../Variables/PythonKeywords.py
Library    Collections
Library    RequestsLibrary
Library    String

Resource   ../Variables/CommonVariables.robot
Resource   ../Variables/Top250Variables.robot
*** Variables ***

*** Keywords ***
User doesn’t logs in IMDB

    wait element is visible    ${SignIn}
    ${text} =    get text of element    ${SignIn}
    elements should be equal   ${text}    Sign In


User visits the “Top 250 rated movies” pages
    wait element is visible    ${YourRatingsElement}
    ${text} =    get text of element    ${Top250Line}
    elements should be equal   ${text}    Top 250 as rated by IMDb Users


User clicks on “your rating” area for any movie
    Click on any your rating

User hovers over “click to add watchlist” area for any movie
    hover over any add to wathclist    ${AddToWathclistElements}

User sees tooltip includes “click to add watchlist”
    check tooltip before adding

User clicks on “click to add watchlist” area
    click to add to watchlist    ${AddToWathclistElements}

User sees tooltip includes “click to remove from watchlist”
    check tooltip after adding


