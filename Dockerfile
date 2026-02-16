# Builder stage
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY app.py ./
COPY html/ ./html/

EXPOSE 8080

# Use opentelemetry-instrument for zero-code auto-instrumentation
CMD ["opentelemetry-instrument", "python", "app.py"]