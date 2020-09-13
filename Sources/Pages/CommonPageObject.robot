*** Settings ***
Library     SeleniumLibrary
Library    ../Variables/PythonKeywords.py
Library    Collections
Library    RequestsLibrary
Library    String

Resource   ../Variables/CommonVariables.robot

*** Variables ***

*** Keywords ***
Begin Web Test
    OPEN BROWSER    ${BASE_URL}    ${BROWSER}
    maximize the browser
    #please open default browser



End Web Test
    please close browser
