# Automation Patterns
demo python selenium on automation exercise site.
This is purposely left very basic. Do not take this as a professional testing project. I am just trying to show the basic ideas for some patterns.  

## Patterns 

### POM
This is your basic base level pattern. The main purpose is to model the pages of the software under test. In this example I chose to use a base page that adjusts
how you return attributes, but you can use properties, methods, what ever works for your team. 
For more reading on the POM:
- https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
- https://www.selenium.dev/documentation/test_practices/design_strategies/

### Actions 
Although for login specifically I wouldn't repeat this, for simplicities sake, lets assume we will.
Instead of having the three steps repeated we can abstract those away into a login action. 
These are good if you want to start creating domain specific language for your tests inside a facade. 

### ScreenPlay
This is a very basic implementation. This is a pattern that really starts to add a lot more effort into building your test libraries. 
The basic idea is instead of testing around the pages or actions, your build your tests around user types. This is good for app's with comlex functionalites, multiple user types, or multiple formats (web, api, mobile, ect). 

### Robot
I did not demo this but the selenium site does have a small example. I personally wouldn't use this for tests. It is worth mentioning though because with some tweaks you might be able to see how you can extend some driver functionalities inside an "ActionBot" class to pass into your page objects instead of the webdirver.

## summary
Hopefully this gives you a rough starting point on how to start thiniing about structuring your code.

