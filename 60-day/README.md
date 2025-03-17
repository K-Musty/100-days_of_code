 # DAY 60 of 100 - Make POST Requests with Flask and HTML Forms
---

- POST requests with Flask, HTML Forms, send emails with smtplib

### Challenges

- HTML Forms -Revision - Creating a Form from Scratch
- Handle POST Requests with Flask Servers
- Get the Contact Form from Day 59 to work
- Sending Emails with SMTPLIB

#### Tasks
- Add a route in main.py to receive data from the form from Day 59
- Update the code in contact.html and main.py so that the information the user has entered into the form and return a ```<h1>``` that says "Successfully sent your message".
- Combine the "/contact" route with "/form-entry" so that they are both under the route "/contact" but depending on which method (GET/POST) that triggered the route, handle it appropriately.
- Instead of returning a ```<h1>``` that says "Successfully sent message", update the contact.html file so that the ```<h1>``` on the contact.html file becomes "Successfully sent message".
- Send form contents as an email using smtplib.
