# Thank you for reading my application!

## There's a lot going on here. Let's talk about it!

### Framework choice
I'm going to be honest, I've never started a Django or Node.js app from scratch. I've worked in both of them--recently spent a few months working extensively in a Django codebase--but I haven't started a greenfield app in either framework. Hopefully, you can forgive what I'm sure are some structures and choices that are a bit green.

Given my newness to this specific framework, I chose Django, for a couple of different reasons.
Primarily, I selected it due to its similarity to Rails. I have started dozens and dozens of Rails apps, and Django is fairly similar to Rails in a lot of ways. I felt more confident about my ability to quickly ramp up something that looked like what you all are expecting. JavaScript frameworks tend to have very opinionated differences in style, and I can tell you from my experiences in AngularJS and React that it is very easy to misuse them, or write your code in such a way that makes it very apparent you aren't familiar with those frameworks.
---


### Database     
I didn't change the default database here, since this is just a simple, lightweight app with very little going on. In a real-life scenario, I'd be more likely to use postgres.
---


### Data     
Right now, I'm not pulling data from the past 6 months. I'm only pulling the default from the API. I know that I can pass parameters to change the amount of articles grabbed and the dates of the articles received; I chose to focus elsewhere for the purposes of this exercise, though. I'm hitting the API every time you load one of the relevant views. This is, of course, terrible!

In a real-world scenario, I wouldn't hit the API from the view methods at all. Instead, I would write a job to seed the database on off-hours (run it just once on launch, and write it well enough that I can modify it to run regularly--do a small update every morning at 3, say--or if we add another topic, like "medicine", we could easily alter it and run it again). This gives me asynchronicity! We don't want users to have to hang out while our servers hit someone else's servers hit our servers hit the client. It also allows me to run the jobs on slow days/hours, so if I accidentally take down a user-facing server, there are minimal service interruptions.
---


### Service     
I built a service to pull the API, and frankly, it's full of code smells! Most importantly: I have a structure that looks roughly like Services.method(Services) and there is just no way that the correct way to invoke this is to call a method on the class and then...pass the class in. There is something fundamentally wrong with the Python here. in a real-world scenario, I'd probably ping a coworker and go "hey can I get a hand or a rubber duck on this? I'm clearly misunderstanding something." 

Additionally, I'm not fully confident that this is the right way to implement a service in Django! My goal was to build a service that was independent enough from the model and internal workings that it could easily either be replaced by a different API in the future if we found one we liked more, or fully built out into a full-feature microservice if we wanted to expand upon it. Research tells me it should live in the References app since it corresponds directly to our models, which is why I put services.py in the references directory. I'm not totally confident that I am implementing it in the right way. In a real-world scenario, I'd find another place we have a service that wraps around a 3rd-party API, and see how we implement it there. I think it's entirely possible there are better ways to structure the service and I am more than willing to improve.
---


### Serializer    
I'm not using one! In a real-world scenario, I'd likely build a serializer to alter the data I'm getting from the xml and turn it into a form that's easily consumed by the model. It didn't seem worth the cost/benefit for this project.
---


### What happens next?    
You are so astounded you immediately extend an offer without any more interviewing tasks! Okay, okay, wishful thinking. So, where would I go with this application in the future?

It depends heavily on the use case! First, there are a couple of ease-of-use changes (aside from changes listed above) that I would make regardless. The UI could be more visually appealing. I would build a header. The direction I take next would depend on our user needs. There are a couple of obvious-to-me areas we might want to move in, though, depending on where we think the application would grow.

If we think that we'd be adding a lot more data over time, then in addition to refactoring, I'd start thinking about ways to make parsing through our data easier for our human users. I'd think about things like pagination, search capabilities, adding show pages (author page could just be an index that links out to show pages with article information), things like that. There isn't an article show page, either. I'm actually not saving most of the data that we're getting from the API.

The next area that we might move in would be what I'm thinking of as "horizontal data"--looking at related content. That might mean building out a feature that suggests related articles or topics. It might also mean breaking out the service so that instead of the hard-coded values we're passing in for search terms, the user could submit other values.

Tagging would be smart to implement, starting by tagging each article/author with the specific topic among the 4 options the data was pulled for.

This could also conceivably be a standalone externally-facing product, given that it's really about parsing a public API. A project like that could be useful and also increase our reputation, so I might also clean up the code and the interface to make it more presentable to an external audience.

Most importantly, however, I would ask someone who is very familiar with Django to come and rip it apart in code review! I feel confident that I got this done in not-the-worst-way; I'm not confident that it's optimized or that it feels Django-y. Maybe the directories are in wacky places. Maybe I used a service when *everyone* who started on Django would use a banjo (okay I couldn't think of another term in the moment). I want to make the right choices for the tools I'm using, not just the right choices for the tools I have used in the past. The best way to do that in a situation like this is through feedback and iteration.
---


## Lastly     
Thank you so much for your consideration! Hopefully, this gives you a better idea of me as an engineer. What it doesn't capture is my willingness to adapt, learn, and change; I have done my best to indicate those along the way! Hope you all have a great rest of your week, and I look forward to working with you in the future.     
-ellen