import boto3
import sys

def main():
    print("CI/CD automation started...")

    try:
        session = boto3.Session()
        print("Boto3 session created")
        print("Automation script executed successfully via CI/CD")
    except Exception as error:
        print("Execution failed:", error)
        sys.exit(1)

if __name__ == "__main__":
    main()
