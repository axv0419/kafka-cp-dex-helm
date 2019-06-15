
## Install Rest Proxy

```bash
BROKER_URL="pkc-lqrjp.us-west2.gcp.confluent.cloud:9092"
API_KEY="EO3T7XCFFK5DSA6C"
API_SECRET="NUz1XqBj1+orYHDQLLzU/qBrZs4eolhH7cGuWv1krwEV4squqKcWt+X4ovYzS9Z/"

SASL_JAAS_CONFIG=$(echo "org.apache.kafka.common.security.plain.PlainLoginModule required username\=\"${API_KEY}\" password\=\"${API_SECRET}\";" | base64 -w 0 )

#Test 
helm install --dry-run --debug --set saslJaasConfig="${SASL_JAAS_CONFIG}"  --set bootstrapServers=${BROKER_URL}  --name rest-proxy --namespace taco-tuesday .
```