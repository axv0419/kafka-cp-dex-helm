
## Install Rest Proxy


The service for this microservice will be exposed on the domain `DOMAIN_NAME`
Certificates for the `DOMAIN_NAME` will be auto generated.  A domain certificate can include alternate domain names (SAN subject alternate names) which makes that certificate  valid for 
identifying multiple domain names. Its good to have multiple SANs in a single certificate to allow it to be usable for multiple microservices. This helps in managing the cost as well as housekeeping associated with certs.

The script generates `DOMAIN_NAME` as `{DOMAIN_NAME_PREFIX}.{DOMAIN_NAME_SUFFIX}` and SANS as `{SAN_PREFIX_LIST[0]}.{DOMAIN_NAME_SUFFIX}` `{SAN_PREFIX_LIST[1]}.{DOMAIN_NAME_SUFFIX}` ...

```bash

BROKER_URL=""
API_KEY=""
API_SECRET=""
# staging  OR production
CERT_AUTH_TYPE="staging"

## Read explanation above
DOMAIN_NAME_SUFFIX="eu-dev.dexcom-apps.com"
DOMAIN_NAME_PREFIX="event-bus-api-a"
SAN_PREFIX_LIST="event-bus-api-b,event-bus-api-c,event-bus-api-d,event-bus-api-e,event-bus-api-f"


SASL_JAAS_CONFIG=$(echo "org.apache.kafka.common.security.plain.PlainLoginModule required username\=\"${API_KEY}\" password\=\"${API_SECRET}\";" | base64 -w 0 )

# test with dry run .. to make deployment remove that line
helm install \
--dry-run --debug \
--set saslJaasConfig="${SASL_JAAS_CONFIG}" \
--set bootstrapServers=${BROKER_URL} \
--set ingress.hosts[0].host="${DOMAIN_NAME_PREFIX}.${DOMAIN_NAME_SUFFIX}" \
--set ingress.hosts[0].path={"/","/topics/test-01.raw"}
--name rest-proxy-etq \
--namespace dexcom-warrior .


# delete 
helm del --purge rest-proxy;

```


