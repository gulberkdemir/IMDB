*** Settings ***
Library  SeleniumLibrary
Library    ../Variables/PythonKeywords.py
Library    Collections
Library    RequestsLibrary
Library    String

Resource   ../Variables/CommonVariables.robot
Resource   ../Variables/Top250Variables.robot
Resource   ../Variables/LoginVariables.robot
*** Variables ***

*** Keywords ***

User should be navigated to “IMDB login” page
    wait element is visible    ${SignInTextInLogin}
    ${text} =    get text of element    ${SignInTextInLogin}
    elements should be equal    ${text}    Sign in

    wait element is visible    ${SignInImdb}
    ${text} =    get text of element    ${SignInImdb}
    elements should be equal   ${text}   Sign in with IMDb

     ${text} =    get text of element    ${SignInWithAmazon}
    elements should be equal   ${text}   Sign in with Amazon

    ${text} =    get text of element    ${SignInWithFacebook}
    elements should be equal   ${text}   Sign in with Facebook

    ${text} =    get text of element    ${SignInWithApple}
    elements should be equal   ${text}   Sign in with Apple

     ${text} =    get text of element    ${CreateNewAccount}
    elements should be equal   ${text}   Create a New Account


User logs in IMDB
    wait element is visible   ${SignIn}
    wait element is visible    ${YourRatingsElement}
    click this element    ${SignIn}
     wait element is visible   ${SignInImdb}
     click this element    ${SignInImdb}
     wait element is visible    ${Email}
     type something    ${Email}    d.gulberk@hotmail.com
     type something    ${Password}    Test1234**
     click this element    ${RealSignInButton}
     wait element is visible    ${myname}
     ${text} =    get text of element    ${myname}
     elements should not be equal  ${text}  Sign In

