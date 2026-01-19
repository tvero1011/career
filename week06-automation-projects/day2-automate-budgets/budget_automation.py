import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# Replace these with your info
ACCOUNT_ID = "123456789012"  # Your AWS Account ID
BUDGET_NAME = "CareerC-MonthlyBudget"
BUDGET_LIMIT = 10  # $10 limit for practice

def create_budget():
    try:
        client = boto3.client("budgets")

        # Define the budget
        budget = {
            "BudgetName": BUDGET_NAME,
            "BudgetLimit": {"Amount": str(BUDGET_LIMIT), "Unit": "USD"},
            "TimeUnit": "MONTHLY",
            "BudgetType": "COST"
        }

        # Define notification (alert at 80%)
        notification = {
            "NotificationType": "ACTUAL",
            "ComparisonOperator": "GREATER_THAN",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE",
            "NotificationState": "ALARM"
        }

        # Define subscribers (your email if you want notifications)
        subscribers = [
            {
                "SubscriptionType": "EMAIL",
                "Address": "your-email@example.com"  # replace with real email
            }
        ]

        # Create the budget
        response = client.create_budget(
            AccountId=ACCOUNT_ID,
            Budget=budget,
            NotificationsWithSubscribers=[{
                "Notification": notification,
                "Subscribers": subscribers
            }]
        )

        print(f"Budget '{BUDGET_NAME}' created successfully!")

    except NoCredentialsError:
        print("AWS credentials not available.")
    except ClientError as e:
        print(f"An AWS error occurred: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    create_budget()
