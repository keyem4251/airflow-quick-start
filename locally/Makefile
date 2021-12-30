setup-airflow-venv-pip:
	./setup-airflow-venv-pip.sh

airflow-db-init:
	airflow db init

airflow-user-create:
	airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

airflow-webserver-start:
	airflow webserver --port 8080

airflow-scheduler-start:
	airflow scheduler