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

# 📂 Repository Structure
