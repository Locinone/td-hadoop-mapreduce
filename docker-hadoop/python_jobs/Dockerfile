FROM python:3.11-slim

# Install HDFS client dependency
RUN pip install --no-cache-dir hdfs

# Set working directory
WORKDIR /app

# Copy your scripts and data
COPY spark_jobs/ /app/

# Default command
CMD ["bash"]
