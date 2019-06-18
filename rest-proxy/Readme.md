
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
CONSUMER_NAME=crm

DOMAIN_NAME_SUFFIX="eu-dev.dexcom-apps.com"
DOMAIN_NAME_PREFIX="event-bus-api-${CONSUMER_NAME}"
SAN_PREFIX_LIST="event-bus-api-a,event-bus-api-b,event-bus-api-c,event-bus-api-d,event-bus-api-e"

MICROSERVICE_NAME="rest-proxy-${CONSUMER_NAME}"
NAMESPACE=kafka-${CONSUMER_NAME}

CONSUMER_BASIC_AUTH_USER="apiuser"
CONSUMER_BASIC_AUTH_PASSWORD="password6"

TOPIC_PATH_WHITELIST={"/\$","/topics\$","/topics/eu.account.crm.raw\$","/topics/test-01.eu-la\$"}
SAN_HOSTNAME_LIST="{$(echo ${SAN_PREFIX_LIST//,/.${DOMAIN_NAME_SUFFIX},}).${DOMAIN_NAME_SUFFIX}}"

CONSUMER_JAAS_CONFIG=$(echo "${CONSUMER_BASIC_AUTH_USER}: ${CONSUMER_BASIC_AUTH_PASSWORD}" | base64 -w 0 )
SASL_JAAS_CONFIG=$(echo "org.apache.kafka.common.security.plain.PlainLoginModule required username\=\"${API_KEY}\" password\=\"${API_SECRET}\";" | base64 -w 0 )

BASE_DIR=..
. ${BASE_DIR}/setenv-crm-eu.sh



echo "Urls that will be whitelisted on the Rest proxy for this customer ${TOPIC_PATH_WHITELIST}"

# test with dry run .. to make deployment remove that line
helm install \
--set consumerBasicAuthRole="${CONSUMER_BASIC_AUTH_USER}" \
--set consumerBasicAuthConfig="${CONSUMER_JAAS_CONFIG}" \
--set saslJaasConfig="${SASL_JAAS_CONFIG}" \
--set bootstrapServers=${BROKER_URL} \
--set ingress.hosts[0].host="${DOMAIN_NAME_PREFIX}.${DOMAIN_NAME_SUFFIX}" \
--set ingress.hosts[0].paths="${TOPIC_PATH_WHITELIST}" \
--set ingress.tls[0].hosts="${SAN_HOSTNAME_LIST}" \
--name ${MICROSERVICE_NAME} \
--namespace ${NAMESPACE} . \
--dry-run --debug 



# delete 
helm del --purge ${MICROSERVICE_NAME} ;

```


