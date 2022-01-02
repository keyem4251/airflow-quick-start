export AIRFLOW_HOME=~/IdeaProjects/airflow-quick-start/locally/airflow

setup-airflow-venv-pip:
	./setup-airflow-venv-pip.sh

airflow-db-init:
	airflow db init

USERNAME=admin

airflow-user-create:
	airflow users create \
    --username ${USERNAME} \
    --role Admin \
    --email example@example.com

airflow-webserver-start:
	airflow webserver --port 8080

airflow-scheduler-start:
	airflow scheduler