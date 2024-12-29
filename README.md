# Dev Servers
**Flask App Deployment**

<img src="https://github.com/user-attachments/assets/eda41519-c1c2-4c74-9e8c-a287256bcb6f" class="circular-image" width="100px" height="100px" border-radius="50%">


## What is WSGI?
_This PR addresses WSGI, development servers, and how they work with Flask applications. It is targeted for both beginners and advanced users._

<img src="https://github.com/user-attachments/assets/3dfdb73d-8c2c-4714-ad9b-55aafe0226bd" width="100px" height="100px">

  **Web Server Gateway Interface**: Middleman for web servers and Python Frameworks. (Like Flask).

  **Defining Standardization**: Flexible communications infrastructure ensuring portability between web servers and deployment.


### Beginner Friendly

Concierge - WSGI (Restaurant), Server (Web Server). Customer (client). The greeter (PHP). Appropriates the waiter. (Python App). The waiter prepares the food. (MySQL request). And the concierge delivers it back to the customer. (PHP response).

![WSGI](https://github.com/user-attachments/assets/844b4c80-8515-45e5-942b-556b525d3b56)

#### Workflows

1.) __CLIENT REQUEST__ - `usr/bin/__browser__ > # send HTTP request to -> (NGINX, Apache, etc.)`<br>
2.) __WSGI__ - `usr/bin/__browser__ > ~handover forwarded request to Gunicorn, uWSGI, etc.)~`<br>
3.) __flask.py__ - `usr/bin/__browser__/Gunicorn ~> http://www.domain.host.icann.wsgi/sw.js=flask__app__%200dev/..\`<br>
4.) __generator.php__ - `app.py, flask.py => process.php, request.php, -> webgenerator.sql`<br>
5.) __response.xml__ - `WSGI_SECURITY.xml, WEBSITE_LOADER.js, APPLICATION_SERVER.php`<br>

_交付后，响应会延迟加载到客户端的起泡器中，然后将其放入存储应用程序密钥的浏览器中。_

## Advanced Workflow

Development Server 🕓🌑 vs. Production Server 🇨🇳🇮🇳

* Lightweight Server :electron: :neckbeard: : Ideal for localized developmentation, experimentation, and testing.
* Performance Server 🤖🎮 : Large-scale studios, office suites, gaming, etc.)

![flowchart-computation](https://github.com/user-attachments/assets/bee18878-f1c3-4141-bc3e-7311f163d72d)

### Robust, Transparent, Seamless

* Optimize traffic and SecOps 🚦🚙🚥🚗🚓
* Application Production Environments 🛠️⚒️

#### Built-in, Plugged-in, 拡大 🤓

![mysql](https://github.com/user-attachments/assets/8b33d244-5d1c-4901-ada0-f50225769052)

![image](https://github.com/user-attachments/assets/a3908416-88a7-4d65-b9e7-dea12e88caba)

> Gunicorn or uWSGI??? 🤔
> Scaling Flask...🗄️🖥️
> Maintaining Servers...💻📁
