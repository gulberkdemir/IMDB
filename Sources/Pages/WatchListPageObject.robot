*** Settings ***
Library  SeleniumLibrary
Library    ../Variables/PythonKeywords.py
Library    Collections
Library    RequestsLibrary
Library    String

Resource   ../Variables/CommonVariables.robot
Resource   ../Variables/Top250Variables.robot
Resource   ../Variables/WatchListVariables.robot

*** Variables ***

*** Keywords ***



User should see the movie’s name in the watchlist page
    click this element    ${WatchListButton}
    find my movie in watchlist    ${filenames}
