##EC2 Nginx Deployment
# Commands Used

sudo dnf update -y
sudo dnf install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
sudo nano /usr/share/nginx/html/index.html


# Screenshots

# Summary
Today I deployed a public web server on EC2 using Nginx.
I customized the default webpage, enabled the service, and verified the output in the browser
This completes my basic web deployment skills for AWS.