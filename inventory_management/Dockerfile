# Your Solution
FROM python:3.12
WORKDIR /inventory_management
COPY ./* .
ENV DATABASE_URL=postgresql://lyons_sit722_part3_user:zDHiWCqUrH5QFe5Geqg29YICMRzCpaci@dpg-cr6ptd5ds78s73c28o90-a.oregon-postgres.render.com/lyons_sit722_part3
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0 --port $PORT