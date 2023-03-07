FROM python:2.7

# Add sample application
ADD server.py /tmp/application.py

EXPOSE 8000

# Run it
ENTRYPOINT ["python", "/tmp/application.py"]
