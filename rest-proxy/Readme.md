
## Install Rest Proxy

```bash

BROKER_URL=""
API_KEY=""
API_SECRET=""

SASL_JAAS_CONFIG=$(echo "org.apache.kafka.common.security.plain.PlainLoginModule required username\=\"${API_KEY}\" password\=\"${API_SECRET}\";" | base64 -w 0 )

# test
helm install \
--dry-run --debug \
--set saslJaasConfig="${SASL_JAAS_CONFIG}" \
--set bootstrapServers=${BROKER_URL} 
--name rest-proxy \
--namespace taco-tuesday .

# delete 
helm del --purge rest-proxy;

```


