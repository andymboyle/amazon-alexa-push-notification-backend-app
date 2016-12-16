# amazon-alexa-push-notification-backend-app

Recently, I helped build, with Ryan Nagle, the first-ever Amazon Alexa Skill to use their push notifications API, which isn't yet released to the public. 

It was built in conjunction with Breaking News, and was meant to be a skill where you could get recent news alerts from our API, as well as receive higher-level push notifications to your Alexa-backed device. The app is currently in beta testing on the Amazon side, but it most likely won't ever see the light of day, as Breaking News is shutting down Dec. 31st.

# Cool story dude, but what is this for?

But it was awesome to build, and I know others can learn a bit from how we managed to hack something together, so I'm attempting to create a whole new app that shows one how to use these systems.

This is meant to show you what your backend can look like if you wanted to build that portion of the Amazon Alexa push notification stack. It'll contain a basic API to store Amazon user IDs, as well as a place to store "content," also accessible via an API.

It'll also contain some basic management commands that show you how to push to the Amazon Alexa API stack. I'll be leaving placeholder URLs for the Amazon Alexa push notification APIs, as that information is not yet public. When it becomes public, I'll update it here accordingly.

# Wow that's nice of you, but is there more?

Eventually, I'll also build a companion Amazon Alexa Skill that meshes with this app and shows you the proper way to receive push notifications on your Skill, as well as a basic app. It's all kind of tricky and you need a bunch of moving parts, hence me feeling the need for an open source version of how it all fits together.

Anywho, this is all for teaching purposes and to help others. Yell at me (google my name to find my email) if you have any questions. Thanks!