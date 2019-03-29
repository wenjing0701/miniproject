1.Set the region and zone for the new cluster:
gcloud config set compute/zone europe-west2-b
export PROJECT_ID="$(gcloud config get-value project -q)"

2.Make coding connected to database:
cluster = Cluster()
session = cluster.connect()
app = Flask(__name__)

3.A Kubernetes service defines multiple sets of pods, allowing full systems to be deployed with one script.
wget -O cassandra-peer-service.yml http://tinyurl.com/yyxnephy
wget -O cassandra-service.yml http://tinyurl.com/y65czz8e
wget -O cassandra-replication-controller.yml http://tinyurl.com/y2crfsl8

4.Steps taken to deploy application
kubectl run zzplus-user --image=gcr.io/${PROJECT_ID}/zzplus:v1
--port 8080

5.To see the pods created:
kubectl get pods

6.Using the same container, copy our data from the previous section:
kubectl cp pokemon.csv cassandra-24bgm:/pokemon.csv
run cqlsh inside the container:
kubectl exec -it cassandra-24bgm cqlsh
and build our keyspace:
CREATE KEYSPACE pokemon WITH REPLICATION =
{'class' : 'SimpleStrategy', 'replication_factor' : 2};



