from datetime import datetime


dag = DAG('my_dag', start_date=datetime(2020, 12, 1))

# define tasks of the DAG
start_cluster = start_clusterOperator(task_id="start_cluster", dag=dag)
input_athelete_data = SparkJobOperator(task_id="input_athlete_data", dag=dag)
input_venue_data = SparkJobOperator(task_id="input_venue_data", dag=dag)

# set up dependency flow
start_cluster.set_downstream(input_athelete_data)
input_athelete_data.set_downstream(enrich_athelete_data)
input_venue_data.set_downstream(enrich_athlete_data)
