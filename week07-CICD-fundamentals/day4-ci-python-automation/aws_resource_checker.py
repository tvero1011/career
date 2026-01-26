import sys
import boto3

def main():
    print("Starting AWS resource checker...")

    try:
        session = boto3.Session()
        print("Boto3 session initialized successfully.")
        print("Python automation executed inside CI pipeline.")
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
