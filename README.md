# Pat's Online Minimart

***Pat's Online Minimart*** is a minimum viable product (MVP) of an online store that allows its online shoppers to browse various items sold by Uncle Pat and for Uncle Pat himself to manage his store items in an inventory style. 

## Usage

1. Clone this repository into any directory on your computer.
2. Launch a terminal and access the "pat-online-minimart" directory. 
3. Check that you have Python 3.10.12 and above installed by typing `python --version` or `python3 --version`. Otherwise, you may install it via https://www.python.org/downloads/. 
4. Install the required Python modules by typing `python -m pip install -r requirements.txt`. 
5. Finally, launch the server by typing `python run.py` or `python3 run.py`. You should now see the application being served on http://127.0.0.1:5000. 

## Assumptions and Interpretations

1. Uncle Pat's admin account(s) is/are pre-created in `run.py` for this MVP without a dedicated registration portal, just for testing purposes of the user and admin views of the online store. 
2. Uncle Pat only requires item name, item description, item price and quantity (i.e. stock) be listed in his online store for shoppers' browsing. He does not require a shopping cart to be implemented at this stage.

## Deployment on Cloud Environment

I am currently taking the AWS CLF-C01 Certified Cloud Practitioner certification and hence, I am more familiar with the Amazon Web Services (AWS). Given that my web application was developed in Python flask, I can leverage on AWS Lambda's serverless offering. 

With serverless deployment, we will not require a container for our application. AWS Lambda will scale and manage the computing resources while API gateway acts as a trigger for the Lambda function, allowing it to handle HTTP requests from the Internet. By integrating the AWS Lambda with API gateway, there will be a frontend to handle the HTTP requests and route them to the appropriate Lambda function. As AWS Lambda does not natively support the WSGI standard used by Python flask, we will need the AWSGI adapter that allows the Flask application to understand the event format from the API gateway and respond accordingly. Thereafter, our flask application code can be included in an AWS Lambda function.

In the AWS Management Console, we can configure API Gateway to define the REST API endpoints and their corresponding HTTP methods (e.g., GET, POST, etc.). Each endpoint will be linked to the appropriate AWS Lambda function that we created and we can make them publicly accessible for us to serve our Flask application in the cloud.

Below are two helpful articles which provide detailed instructions on how to deploy a flask application on cloud environment with different serverless components: 

- [Deploying a Python Flask application to AWS Lambda with Serverless Framework and CircleCI](https://medium.com/swlh/deploying-a-python-flask-application-to-aws-lambda-with-serverless-framework-and-circleci-3f57437f0758)
- [Deploying a Python Flask Application to AWS Lambda with AWS Serverless Application Model (SAM)](https://awstip.com/deploying-flask-applications-on-aws-lambda-with-sam-a-comprehensive-guide-to-serverless-python-be0d4884f960)

## Security Hardening Techniques on a Cloud Environment 



## Acknowledgements 

- **Darren Chua** | [@chydarren](https://github.com/chydarren)
- **Tutorial Republic** (For the open-source Bootstrap CRUD Data Table for Database with Modal Form frontend template) 

## Credits 

Please refrain from [plagiarising](https://www.comp.nus.edu.sg/cug/plagiarism/) or passing it off as your own work. 

Chua Han Yong Darren © 2023. Code released under the MIT License. 
