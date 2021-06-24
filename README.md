# web2
Additional code:
  nginx.conf:
    server {
    listen       80;
    server_name  localhost;

    location /hello {
        proxy_pass http://0.0.0.0:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    }
    
Launch gunicorn:
  gunicorn -b 0.0.0.0:8080 hello:application
  #launch from directory with WSGI application hello.py
  
