import json
import os
import urllib3

http = urllib3.PoolManager()

API_URL = os.environ.get("API_URL")

def extract_schema_info(detail):
    request_params = detail.get("requestParameters", {})
    response_elements = detail.get("responseElements", {})

    schema_arn = response_elements.get("schemaArn")
    schema_version_arn = response_elements.get("schemaVersionArn")

    registry_name = request_params.get("registryId", {}).get("registryName")
    schema_name = request_params.get("schemaName")

    return {
        "registry_name": registry_name,
        "schema_name": schema_name,
        "schema_arn": schema_arn,
        "schema_version_arn": schema_version_arn
    }

def lambda_handler(event, context):
    try:
        detail = event.get("detail", {})
        event_name = detail.get("eventName")


        if event_name not in [
            "CreateSchema",
            "RegisterSchemaVersion",
            "UpdateSchema"
        ]:
            print(f"Ignored event: {event_name}")
            return {"status": "ignored"}

        schema_info = extract_schema_info(detail)

        payload = {
            "eventType": event_name,
            "schemaUpdated": True,
            "schemaDetails": schema_info,
            "timestamp": detail.get("eventTime"),
            "awsAccount": detail.get("recipientAccountId"),
            "region": detail.get("awsRegion")
        }

        encoded_body = json.dumps(payload).encode("utf-8")

        response = http.request(
            "POST",
            API_URL,
            body=encoded_body,
            headers={
                "Content-Type": "application/json"
            },
            timeout=urllib3.Timeout(connect=5.0, read=10.0)
        )

        print("API response status:", response.status)
        print("API response body:", response.data.decode())

        return {
            "status": "success",
            "httpStatus": response.status
        }

    except Exception as e:
        print("Lambda execution failed:", str(e))
        raise
