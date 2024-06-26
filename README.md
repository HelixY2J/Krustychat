# Overview

This chat application is implemented by Django, HTMX, Websockets and Redis.Initially, the browser makes a standard HTTP request to the server to fetch the chat page.Once the page is loaded, HTMX triggers a request to upgrade to a WebSocket connection, allowing asynchronous communication between the browser and server via Django Channels.Each user is assigned an unique channel and to broadcast messages in real time to multiple users,channel layers are used which group individual channels. For efficient communication management,Redis is integrated to provide better in memory storage and caching.

![Architecture](./img/krusty%20_design02.png)




## Installation

1. Clone the repo

```bash
    git clone https://github.com/HelixY2J/Krustychat.git
```
2. Create a virtual environment

```bash
    pip install -r requirements.txt
```

3. Create the intial database schema

```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
```

4. Run the server

```bash
    python3 manage.py runserver
```

### Features to be added

- Group chat
- Private chat room
- File sharing
