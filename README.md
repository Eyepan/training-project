# Training Project

This was an exercise to practice how to deploy a full stack application in EC2. This exercise uses Flask and Jinja2 Templates to render out a simple student application.

# Setup:

Get your EC2 instance up and running

```
sudo apt update;
sudo apt upgrade -y;
sudo apt install nginx python3 python3-pip python3-venv;
```

Edit the NGINX configuration by creating a new file in `/etc/nginx/sites-enabled`. I named mine as `server_config` but feel free to name it anything you want.

```conf
server {
    listen 80;
    server_name 31.1.0.2; # {your ec2 public ip}
    location / {
        proxy_pass http:127.0.0.1:5000; # {your flask/fastapi/express application api endpoint}
    }
}
```

And then, restart nginx to apply the configuration by doing

```
sudo systemctl restart nginx
```

Check that `nginx` is working perfectly by doing

```
sudo systemctl status nginx
```

And then, clone this repository in your EC2 instance, install the required dependencies and run `main.py`

```
git clone https://github.com/Eyepan/training-project.git
cd training-project
pip install -r requirements.txt
python main.py
```

And you're done. To check, go to `http://{your public ip}` and see.
