# AWS Glue Schema EventBridge Lambda

> Real-time notifications for AWS Glue Schema Registry changes using EventBridge and Lambda.

This repository provides a fully event-driven solution to detect and respond to schema changes in AWS Glue Schema Registry in real time. It uses AWS CloudTrail, Amazon EventBridge, and AWS Lambda to automatically capture schema-related API events and trigger downstream notifications or integrations.

📖 **Full article explaining the architecture and implementation:**  
https://dev.to/pratik_26/how-to-get-real-time-notifications-when-aws-glue-schema-registry-changes-4nbd

---

# 🚀 Architecture Overview

This solution follows a serverless, event-driven architecture:

1. **AWS Glue Schema Registry**
   - Stores and manages schemas for streaming and data applications.
   - Events occur when schemas are created, updated, or new versions are registered.

2. **AWS CloudTrail**
   - Records all Glue Schema Registry API calls such as:
     - CreateSchema
     - RegisterSchemaVersion
     - UpdateSchema
   - These events are automatically available to EventBridge.

3. **Amazon EventBridge**
   - Captures relevant Glue events from CloudTrail.
   - Filters only schema-related changes.
   - Triggers the Lambda function.

4. **AWS Lambda**
   - Receives event from EventBridge.
   - Extracts schema metadata.
   - Sends structured notifications to external systems such as:
     - REST APIs
     - Slack
     - Microsoft Teams
     - Email
     - SNS/SQS
     - Monitoring systems

---


# ⚙️ How It Works

<img width="2704" height="1968" alt="image" src="https://github.com/user-attachments/assets/955dde90-0a5d-4848-9c12-3db5aeff859a" />


**Step-by-step flow:**

1. A schema is created or updated in AWS Glue Schema Registry.

2. CloudTrail records the API call.

3. EventBridge detects the event using a rule pattern.

4. EventBridge invokes the Lambda function.

5. Lambda extracts schema details and sends notification payload.

---

# 🛠️ Deployment Steps

**Step 1: Create Lambda Function**

Runtime: Python 3.10+

Upload lambda_function.py

Set environment variable:

API_URL=https://your-api-endpoint.com

**Step 2: Create EventBridge Rule**

Go to EventBridge Console

Create new rule

Select Event Pattern

Use the provided JSON pattern

Set target as Lambda function

**Step 3: Verify CloudTrail**

Ensure CloudTrail is enabled and logging management events.

CloudTrail → Trails → Management Events → Enabled

# 🔐 Required IAM Permissions

Lambda execution role should have minimum permissions:

logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
glue:GetSchema
glue:GetSchemaVersion

If calling external API, ensure network access is configured.

# 🧪 Testing

To test:

Create a new schema in Glue Schema Registry

OR

Register a new schema version

Then verify:

Lambda is triggered

Logs appear in CloudWatch

Notification is received

# 🧰 Technologies Used

AWS Glue Schema Registry

AWS CloudTrail

Amazon EventBridge

AWS Lambda

Python

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

Feel free to open an issue or pull request.

# 📄 License

MIT License

# 👨‍💻 Author

Pratik Ponde

GitHub: https://github.com/pratiksponde
DEV: https://dev.to/pratik_26
